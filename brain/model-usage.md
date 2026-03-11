# Model Usage

| Task Type | Preferred Model | Notes |
|-----------|-----------------|-------|
| Lightweight drafting, rote summaries | Kimi / lower-cost GPT | Use when precision stakes are low. |
| General reasoning, planning, synthesis | GPT-5.1 Codex (default) | Balance of cost + capability. |
| Engineering, implementation, code review | Claude Sonnet 4.x | Better for long-form code + tools. |
| Deep reasoning, audits, critical reviews | Claude Opus / GPT-5.4 class | Only when stakes justify cost. |
| Multimodal/image understanding | GPT-5.1 vision | Use when user sends diagrams/screens. |

## Principles
- Always match model to task complexity + sensitivity.
- Escalate only when default performance is insufficient.
- Log model choices for traceability in `logs/session-log.md`.
