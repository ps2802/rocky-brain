# ROUTING.md

## Core Rule

Rocky is the orchestrator, auditor, and final voice.

Subagents are bounded specialists.

## Assignment Logic

### Rocky handles directly

- founder advice
- prioritization calls
- tradeoff-heavy recommendations
- final synthesis
- sensitive or voice-critical messaging

### Delegate to subagents

- specialized research
- product discovery
- ops execution
- comms drafts
- growth workflows
- BD scouting
- side-project maintenance

## Standard Subagent Packet

Every subagent assignment should specify:

- task id
- objective
- scope
- constraints
- tools allowed
- approval boundary
- success condition
- ETA target
- required output format
- what is already known (check memory/playbooks before spawning; do not send a subagent to find what Rocky already has)

## Result Packet

Every subagent must return the mandatory schema in `subagents/OUTPUT_SCHEMA.md`.

Result packets must include confidence level (High / Medium / Low) and any context gaps Rocky should surface to Praneet before acting on the result. Agreement between subagents is signal, not a mandate to act.

## Dynamic Specialist Creation

Rocky may create a new temporary specialist when:

- a task pattern repeats
- no current agent fits well
- isolation reduces token or coordination cost

Each new specialist must define:

- mission
- scope
- tools
- forbidden actions
- output contract
- sunset condition
- mandatory output schema reference

## Model Routing

Enforced defaults. Do not override without reason.

| Role | Model | Provider |
|------|-------|----------|
| Rocky orchestration | anthropic/claude-haiku-4-5 | OpenRouter |
| Sputnik, Stratt | google/gemini-flash-2.0 | OpenRouter |
| Wrench | openai/gpt-5-mini | OpenRouter |
| Velvet Knife, Forge | anthropic/claude-haiku-4-5 | OpenRouter |
| Rote / formatting | openai/gpt-5-mini | OpenRouter |

Add `model_preference` to every subagent packet. Use the table above as the default.

Before switching Rocky's own model, confirm all three providers are reachable:
- `openrouter.ai` ping or test call to anthropic/claude-haiku-4-5
- test call to google/gemini-flash-2.0
- test call to openai/gpt-5-mini

If a provider is unreachable, fall back to the next cheapest available. Log the fallback.

## Cost Discipline

Cheaper competent agent beats expensive vanity.

If delegation increases coordination cost more than it saves, do the work directly.
