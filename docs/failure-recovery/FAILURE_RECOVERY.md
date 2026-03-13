# FAILURE RECOVERY

## Lost Context / Reset
1. Clone `ps2802/rocky-brain` and read `docs/identity/` + `docs/operations/` first.
2. Load workspace bootstrap files (`SOUL.md`, `USER.md`, etc.) to sync persona + owner prefs.

## Missing API Keys
1. Verify env with `env | grep -i GEMINI` (or provider-specific).
2. If missing, request the key or load from the documented secret location; never assume previous runs.
3. Only rerun scripts once the key is confirmed in the active shell.

## Script Failures
1. Capture the exact command + working dir + error snippet.
2. Check prerequisites (deps installed, env vars, network).
3. Re-run with scoped logging; if a tool is unavailable, report immediately instead of looping.

## Status Loops / Cost Spikes
- Disable proactive status blocks; send updates only when something changes.
- Summarize large outputs to file and share the path to avoid token blowups.
