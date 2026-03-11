# rocky-brain

Reset-resistant knowledge base for Rocky, Praneet Sinha's chief-of-staff AI.

## Structure
- `brain/` – system architecture, routing logic, model usage.
- `memory/` – long-term memory, user profile, decisions, timeline.
- `projects/` – project-specific context (Moongate, Moongent, F1 Gridlock).
- `operations/` – server setup, recovery, deployment playbook.
- `logs/` – daily + session logs for quick catch-up.
- Root files (SOUL, MISSION, STACK, etc.) keep the persona + mission anchored.

## Workflow
1. Pull repo (once published) into the OpenClaw workspace.
2. After each meaningful change, update relevant markdown files.
3. Commit + push so future resets can be restored quickly.

_No secrets or credentials should live in this repo._
