# Brain Architecture

## Layers
- **Identity Layer** – SOUL.md, IDENTITY.md, USER.md define persona, user preferences, and boundaries.
- **Mission Layer** – MISSION.md + STACK.md encode goals, responsibilities, and project separation.
- **Execution Layer** – TASKS.md, project docs, and operations playbooks drive day-to-day work.
- **Memory Layer** – `memory/*.md`, `MEMORY.md`, and `logs/` capture continuity (short + long term).
- **Recovery Layer** – RECOVERY.md + Git procedures restore Rocky after resets.

## Control Flow
1. **Boot** – Run through RECOVERY checklist; pull Git repo; load anchor docs.
2. **State Rehydrate** – Read MEMORY.md, user-profile, timeline, project files, daily log.
3. **Task Selection** – Prioritize via TASKS.md + open loops list.
4. **Execution** – Use built-in tools, spawn sub-agents, or call external services as needed.
5. **Write-back** – Update relevant docs, append daily memory, commit/push.

## Delegation Rules
- Route engineering-heavy tasks to Sonnet-class models/sub-agents.
- Use Kimi/cheaper models for rote work to control costs.
- Keep Rocky focused on orchestration, synthesis, and decision support.

## Data Separation
- Never store secrets or credentials in the repo.
- Use personal vs. work accounts per STACK.md guidelines.
- Keep sensitive tokens in external secret managers and reference their location only if necessary.
