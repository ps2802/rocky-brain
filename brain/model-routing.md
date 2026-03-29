# Model Routing

Apply this mapping for subagent/model selection:

- Rocky orchestration -> anthropic/claude-haiku-4-5
- Sputnik, Stratt -> google/gemini-flash-2.0
- Wrench (ops/code tasks) -> openai/gpt-5-mini
- Velvet Knife, Forge -> anthropic/claude-haiku-4-5
- Rote/formatting -> openai/gpt-5-mini

Implementation notes:
- Include a model_preference field in Standard Subagent Packet and enforce it in subagents/template.md.
- The delegate_task context should include model hint: {"model": "provider/model-name"} and orchestration should honor it if available and permitted by cost/rate limits.
- Log every model decision to logs/session-log.md with timestamp, task_id, chosen_model, reason.

Safety:
- Any attempt to override Rocky orchestration for high-risk tasks must require Principal approval.
