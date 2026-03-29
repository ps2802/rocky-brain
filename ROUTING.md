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

## Cost Discipline

Cheaper competent agent beats expensive vanity.

Use:

- strongest model for Rocky and high-stakes review
- mid-tier models for specialist reasoning
- cheap models for rote transformation and formatting

If delegation increases coordination cost more than it saves, do the work directly.
