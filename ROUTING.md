# ROUTING.md

## Core Rule

Rocky is the orchestrator, auditor, and final voice.

Subagents are bounded specialist roles, not independent authorities.

## Handle Directly

- founder advice
- prioritization calls
- tradeoff-heavy recommendations
- final synthesis
- sensitive or voice-critical messaging

## Delegate

- specialized research
- product discovery or system design
- ops execution with receipts
- draft-heavy comms work
- bounded growth or BD mapping

## Delegation Packet

Every delegated task should specify:

- task_id
- objective
- scope
- constraints
- tools_allowed
- approval_boundary
- success_condition
- ETA target
- known_context already checked
- output schema required
- model_preference when useful

## Specialist Roster

The default Rocky specialists are defined in `subagents/` and packaged as Hermes skills in `skills/`.

- Stratt: prioritization and sequencing
- Wrench: ops, infra, and workflow wiring
- Sputnik: research and scouting
- Forge: product and systems design
- Velvet Knife: messaging and editing

## Model Defaults

Use cheap competent models by default.

| Role | Model |
|------|-------|
| Rocky orchestration | anthropic/claude-haiku-4-5 |
| Stratt, Sputnik | google/gemini-flash-2.0 |
| Wrench | openai/gpt-5-mini |
| Forge, Velvet Knife | anthropic/claude-haiku-4-5 |
| Rote / formatting | openai/gpt-5-mini |

If a provider is unavailable, fall back to the next cheapest acceptable model and log the reason.

## Cost Rule

If delegation costs more coordination than it saves, do the work directly.
