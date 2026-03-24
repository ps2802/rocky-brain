# Model Usage

| Tier | Task Type | Preferred Model | Notes |
|------|-----------|-----------------|-------|
| Trivial | Admin, rote summaries, formatting, quick lookups | `gemini-2.0-flash` | Near-free, fast, 1M token context. Default for low-stakes ops. |
| Default | General reasoning, planning, synthesis, most messages | `gemini-2.5-pro` (default) | Best reasoning per dollar. Use this unless task is clearly trivial or engineering. |
| Engineering | Code implementation, code review, integrations, debugging | `claude-sonnet-4-6` | Best-in-class for code and tool use. Anthropic provider. |
| Einstein | Deep audits, critical decisions, complex architecture, security review | `claude-opus-4-6` | Only when stakes truly justify it. Watch TPM counter. |
| Multimodal | Image/diagram/screenshot understanding | `gemini-2.5-pro` | Native vision; no extra cost vs default. |

## Principles
- Always match model to task complexity + sensitivity.
- **Default is gemini-2.5-pro** — not Codex, not Opus.
- Escalate only when default performance is genuinely insufficient.
- Log model choices for traceability in `logs/session-log.md`.
- If rate limits hit: downshift to `gemini-2.0-flash` immediately; re-escalate only when needed.

## Provider Notes
| Model | Provider | API Key Needed |
|-------|----------|----------------|
| `gemini-2.0-flash` | Google | `GEMINI_API_KEY` |
| `gemini-2.5-pro` | Google | `GEMINI_API_KEY` |
| `claude-sonnet-4-6` | Anthropic | `ANTHROPIC_API_KEY` |
| `claude-opus-4-6` | Anthropic | `ANTHROPIC_API_KEY` |

## Deprecated
- `openai/gpt-5.1-codex` — removed as default. Do not use unless Praneet explicitly requests OpenAI for a specific task.
- `openai/gpt-4o-mini` — replaced by `gemini-2.0-flash` for trivial tasks.
