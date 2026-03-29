# Server or Infra Task

## Trigger

A VPS, service, deployment, integration, or infra change needs execution or diagnosis.

## Required Inputs

- target system
- intended outcome
- access path
- current problem or desired change
- risk level

## Follow-Up Questions

Ask only if missing:

- environment target
- rollback expectation
- whether downtime is acceptable

## Routing Logic

- `Wrench` leads
- `Gremlin` reviews if risk is medium or higher
- Rocky handles approvals and final report

## Approval Boundary

- read-only diagnosis: autonomous
- low-risk reversible internal ops: autonomous with receipts
- production-impacting, credential, firewall, security, or irreversible changes: approval required every time

## Done Criteria

- desired state reached or blocker identified
- rollback path documented
- evidence captured
- residual risk stated

## Evidence Required

- commands run
- outputs summarized
- service status
- verification check

## Output Format

- Task
- Assigned to
- Objective
- Inputs used
- Actions taken
- Result
- Evidence
- Risks or blockers
- Recommended next move
- Confidence level
