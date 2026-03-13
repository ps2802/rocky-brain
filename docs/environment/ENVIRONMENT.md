# ENVIRONMENT

## Shell & Paths
- Default shell: `/bin/bash -lc`.
- Workspace root: `/home/praneet/.openclaw/workspace`.
- Key repos: `nightwatch-qa`, `rocky-brain`, plus ops/projects as required.

## Dependencies
- Node + Playwright under `nightwatch-qa/automation/playwright`.
- OpenClaw runtime lives in `/home/praneet/openclaw` (used for tooling + agents).
- Logging/token usage written to `logs/` under the workspace.

## Secrets & Env Vars
- Gemini: `GEMINI_API_KEY` (supply inline before scripts like `./scripts/run-demo-checkout.sh`).
- OpenAI/Anthropic keys managed via `~/.openclaw/agents/rocky/agent/auth-profiles.json`.
- ADC files for Google live under `~/.config/gcloud/` (work vs personal).

## Tooling Notes
- Before running `grep/find`, declare the target directory and exclude `node_modules`, `dist`, `build`, `cache`, `logs` unless explicitly needed.
- Store generated artifacts in `reports/...` and reference their paths in chat instead of pasting verbose content.
