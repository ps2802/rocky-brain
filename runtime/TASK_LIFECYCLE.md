# Task Lifecycle

Every runtime task moves through these states:

1. `intake`
2. `clarify`
3. `assign`
4. `execute`
5. `audit`
6. `report`
7. `complete` or `blocked`

## State Meanings

### intake

Task captured, not yet shaped.

### clarify

Inputs, compartment, trust boundary, and success criteria checked.

### assign

Rocky decides direct execution or subagent owner.

### execute

Work is happening.

### audit

Result reviewed against done criteria and evidence standards.

### report

Rocky sends the structured result upward.

### complete

Task is done and any durable memory updates are handled.

### blocked

Task cannot proceed without a dependency, approval, or missing input.

## Queue Rule

Do not skip `audit` for meaningful work.
