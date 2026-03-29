#!/usr/bin/env python3
"""
Validate subagent result packets against OUTPUT_SCHEMA.md
Usage:
  validate_output.py path/to/result.json
  cat result.json | validate_output.py -

Exits 0 on success, 2 on validation errors.
"""
import sys
import json
from typing import Any, Dict, List
from datetime import datetime

REQUIRED_FIELDS = [
    "task_id",
    "objective",
    "result",
    "artifacts",
    "confidence_level",
    "context_gaps",
    "owner",
    "timestamp",
]

CONFIDENCE_VALUES = {"High", "Medium", "Low"}


def load_input(path: str) -> Dict[str, Any]:
    if path == "-":
        data = sys.stdin.read()
    else:
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
    try:
        return json.loads(data)
    except Exception as e:
        print(f"ERROR: failed to parse JSON: {e}")
        sys.exit(2)


def is_iso8601_utc(ts: str) -> bool:
    # Accepts formats like 2026-03-29T19:59:00Z or with offset
    try:
        if ts.endswith("Z"):
            ts2 = ts[:-1] + "+00:00"
        else:
            ts2 = ts
        # datetime.fromisoformat handles offsets like +00:00
        datetime.fromisoformat(ts2)
        return True
    except Exception:
        return False


def validate(packet: Dict[str, Any]) -> List[str]:
    errors = []
    for k in REQUIRED_FIELDS:
        if k not in packet:
            errors.append(f"missing required field: {k}")
    # check confidence
    if "confidence_level" in packet:
        if packet["confidence_level"] not in CONFIDENCE_VALUES:
            errors.append(
                f"confidence_level must be one of {sorted(list(CONFIDENCE_VALUES))}; got: {packet.get('confidence_level')!r}"
            )
    # context_gaps should be a list (can be empty unless confidence is Low)
    if "context_gaps" in packet and not isinstance(packet["context_gaps"], list):
        errors.append("context_gaps must be a list of strings (can be empty)")
    # artifacts should be a list
    if "artifacts" in packet and not isinstance(packet["artifacts"], list):
        errors.append("artifacts must be a list of file paths or URLs (can be empty)")
    else:
        # ensure artifacts items are strings
        if isinstance(packet.get("artifacts"), list):
            for a in packet.get("artifacts", []):
                if not isinstance(a, str):
                    errors.append("artifact list must contain strings only (file paths or URLs)")
                    break
    # simple owner and task_id checks
    if "task_id" in packet and not isinstance(packet["task_id"], str):
        errors.append("task_id must be a string")
    if "owner" in packet and not isinstance(packet["owner"], str):
        errors.append("owner must be a string (subagent name)")
    # timestamp ISO8601 check
    ts = packet.get("timestamp")
    if ts and isinstance(ts, str):
        if not is_iso8601_utc(ts):
            errors.append("timestamp must be ISO 8601 (e.g., 2026-03-29T19:59:00Z or with offset)")
    else:
        errors.append("timestamp must be an ISO 8601 string")
    # If confidence is Low, require non-empty context_gaps
    if packet.get("confidence_level") == "Low":
        if not packet.get("context_gaps"):
            errors.append("context_gaps must be non-empty when confidence_level is Low")

    return errors


def main(argv):
    if len(argv) != 2:
        print("Usage: validate_output.py <path|->")
        sys.exit(2)
    path = argv[1]
    packet = load_input(path)
    errors = validate(packet)
    if errors:
        print("Validation failed:")
        for e in errors:
            print(" - ", e)
        sys.exit(2)
    # Print short justification requirement check: confidence justification present in result
    conf = packet.get("confidence_level")
    res = packet.get("result", "")
    if conf and isinstance(res, str):
        # require at least one sentence referencing confidence word
        if conf.lower() not in res.lower():
            print(
                "Warning: confidence_level not explicitly justified in result body. It's recommended to include a short sentence justifying the confidence."
            )
    print("OK: result packet valid")
    sys.exit(0)


if __name__ == "__main__":
    main(sys.argv)
