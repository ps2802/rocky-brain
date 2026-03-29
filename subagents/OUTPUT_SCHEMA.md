# Subagent Output Schema

All subagents must return a result packet matching this schema.

Required fields:
- task_id: string
- objective: string
- result: string (or structured JSON)
- artifacts: list of file paths or URLs
- confidence_level: one of [High, Medium, Low]
- context_gaps: list of strings (explicit missing context Rocky should surface to Praneet)
- owner: string (subagent name)
- timestamp: ISO 8601 UTC
- metadata: optional key-value map

Notes:
- confidence_level must be justified in the result body (one short sentence).
- context_gaps must be explicit and actionable.
