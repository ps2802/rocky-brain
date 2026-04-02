# FAILURE RECOVERY

## Lost Context / Reset

1. Confirm Hermes is healthy.
2. Confirm `~/.hermes/SOUL.md` is present.
3. Start from this repo's `AGENTS.md`, not from the legacy boot docs.
4. Open only the files relevant to the active task.

## Missing API Keys

1. Check `~/.hermes/.env` for the required provider variables.
2. Request missing values or load them from the documented secret store.
3. Do not print secret values into chat or logs.

## Script Failures

1. Capture the exact command, working directory, and error.
2. Check prerequisites first.
3. Re-run with scoped logging.

## Status Loops / Cost Spikes

- keep updates concise
- avoid re-reading large files without reason
- write large evidence to files and reference the path
