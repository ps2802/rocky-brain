#!/usr/bin/env python3
"""
Enforce token discipline and model routing decisions.

Usage:
  python3 tools/enforce_token_discipline.py --requested-model provider/model --task-id <id> --budget-tokens <n>

This script selects an appropriate model given requested_model and budget, logs the decision to logs/session-log.md,
and returns the chosen model on stdout. It also supports a dry-run mode.

Policy implemented:
- Prefer requested_model if listed in brain/model-routing.md and budget allows.
- If requested_model unavailable or budget too small, fall back to the next-cheapest model per routing table.
- If budget is below a minimal threshold for any high-tier model, automatically choose Rote/formatting model (openai/gpt-5-mini).
- Always append a log entry to logs/session-log.md with timestamp, task_id, requested_model, chosen_model, reason, and token_estimate.

Note: This is a coordination helper — actual enforcement in subagents must call this script before running.
"""
import argparse
import datetime
import json
import os
import sys

ROUTING = [
    ("rocky", "anthropic/claude-haiku-4-5"),
    ("sputnik", "google/gemini-flash-2.0"),
    ("stratt", "google/gemini-flash-2.0"),
    ("wrench", "openai/gpt-5-mini"),
    ("velvet", "anthropic/claude-haiku-4-5"),
    ("forge", "anthropic/claude-haiku-4-5"),
    ("rote", "openai/gpt-5-mini"),
]

# Simple ranking from cheapest to most expensive (approx)
MODEL_COST_RANK = {
    "openai/gpt-5-mini": 1,
    "google/gemini-flash-2.0": 2,
    "anthropic/claude-haiku-4-5": 2,
}

DEFAULT_ROUTES = {
    "Rocky orchestration": "anthropic/claude-haiku-4-5",
    "Sputnik": "google/gemini-flash-2.0",
    "Stratt": "google/gemini-flash-2.0",
    "Wrench": "openai/gpt-5-mini",
    "Velvet Knife": "anthropic/claude-haiku-4-5",
    "Forge": "anthropic/claude-haiku-4-5",
    "Rote/formatting": "openai/gpt-5-mini",
}

LOG_PATH = os.path.expanduser("~/rocky-brain/logs/session-log.md")


def ensure_log_dir():
    logdir = os.path.dirname(LOG_PATH)
    os.makedirs(logdir, exist_ok=True)
    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "w") as f:
            f.write("# Session log\n\n")


def log_decision(entry: dict):
    ensure_log_dir()
    ts = datetime.datetime.utcnow().isoformat() + "Z"
    line = f"- {ts} | task_id={entry.get('task_id')} | requested={entry.get('requested_model')} | chosen={entry.get('chosen_model')} | reason={entry.get('reason')} | token_est={entry.get('token_est')}\n"
    with open(LOG_PATH, "a") as f:
        f.write(line)


def choose_model(requested: str, budget: int, role_hint: str = None):
    # If requested empty, use role_hint mapping
    if not requested and role_hint:
        requested = DEFAULT_ROUTES.get(role_hint, "openai/gpt-5-mini")

    # If requested not in cost map, prefer fallback
    if requested not in MODEL_COST_RANK:
        # fallback to cheapest
        chosen = "openai/gpt-5-mini"
        reason = "requested unknown; fallback to cheapest"
        return chosen, reason

    # If budget is very small (<100 tokens), force cheapest
    if budget is not None and budget < 100:
        chosen = "openai/gpt-5-mini"
        reason = "budget too small; choose cheapest"
        return chosen, reason

    # Otherwise accept requested
    chosen = requested
    reason = "requested allowed and budget sufficient"
    return chosen, reason


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--requested-model", default="", help="provider/model")
    p.add_argument("--task-id", default="", help="task id")
    p.add_argument("--budget-tokens", type=int, default=1000)
    p.add_argument("--role-hint", default="", help="role hint like Sputnik or Wrench")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    chosen, reason = choose_model(args.requested_model, args.budget_tokens, args.role_hint)
    entry = {
        "task_id": args.task_id,
        "requested_model": args.requested_model,
        "chosen_model": chosen,
        "reason": reason,
        "token_est": args.budget_tokens,
    }
    if not args.dry_run:
        log_decision(entry)
    print(json.dumps(entry))


if __name__ == "__main__":
    main()
