# Model Usage

Keep model choices aligned with `ROUTING.md`.

## Defaults

| Task Type | Preferred Model | Notes |
|-----------|-----------------|-------|
| Rocky orchestration | `anthropic/claude-haiku-4-5` | cheap default for routing and synthesis |
| research and prioritization | `google/gemini-flash-2.0` | fast, cheap, good enough for option mapping |
| ops and rote execution | `openai/gpt-5-mini` | good fit for procedural work |
| product design and sensitive editing | `anthropic/claude-haiku-4-5` | stronger writing and framing |

Escalate only when the default model is clearly not enough for the task.
