# RECOVERY.md

Use this when Hermes or the VPS comes back cold and needs the Rocky brain re-mounted cleanly.

## Recovery Steps

1. Confirm Hermes is installed and the gateway/service is healthy.
2. Confirm `~/.hermes/SOUL.md` exists and matches this repo's `SOUL.md` if you are using Rocky's persona.
3. Pull the latest `rocky-brain` repo state.
4. Re-expose this repo's `skills/` directory to Hermes if skill paths were lost.
5. Start from `AGENTS.md`, then open only the files relevant to the current task.
6. Check `runtime/tasks-work.md` and `runtime/tasks-personal.md` for active queues.
7. Check the latest relevant `memory/episodic/` note if recent continuity matters.

## What Not To Do

- Do not rebuild identity from `BOOT.md` or `BOOTSTRAP.md`.
- Do not treat `TASKS.md` as the live queue.
- Do not assume OpenClaw paths still exist.

## Evidence

After recovery, record what was reconnected and what still needs verification in `logs/session-log.md` or the relevant episodic note.
