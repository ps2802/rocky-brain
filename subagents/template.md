# Subagent Template

Use this template when creating a new subagent (temporary or permanent).

## Metadata
- name: <subagent-name>
- owner: <team or person>
- tools_allowed: [list of tools]
- forbidden_actions: [list]
- sunset_condition: <condition to retire>

## Mission
One-sentence mission statement.

## Input Packet
Required input fields sent to the subagent (Rocky ensures 'search before spawning' before sending):
- task_id
- objective
- scope
- constraints
- tools_allowed
- approval_boundary
- success_condition
- ETA
- known_context: list of files/notes/memory entries already checked
- model_preference: optional string hint (e.g., "google/gemini-flash-2.0")

## Output Packet (must match subagents/OUTPUT_SCHEMA.md)
- task_id
- objective
- result
- artifacts
- confidence_level
- context_gaps
- owner
- timestamp
- metadata

## Pre-run hooks
Rocky will run these checks before spawning the subagent:
- ensure known_context is non-empty (unless explicitly allowed)
- ensure tools_allowed is a subset of permitted tools
- ensure model_preference, if provided, matches allowed routing policy in brain/model-routing.md

## Post-run hooks
Rocky will run these: 
- run python3 subagents/validate_output.py <path-to-result.json>
- if validator fails, reject the result and request fix from subagent
- if confidence_level == Low, require explicit human approval before action
- log model decision to logs/session-log.md

## Example
(Include a small example of input and output JSON)

```json
{
  "task_id": "task-20260329-01",
  "objective": "Find 3 growth channels with <x> criteria",
  "result": "Found 3 channels... Confidence: High",
  "artifacts": ["/tmp/report.csv"],
  "confidence_level": "High",
  "context_gaps": [],
  "owner": "stratt-executive",
  "timestamp": "2026-03-29T20:00:00Z",
  "metadata": {"runtime": "v1"}
}
```
