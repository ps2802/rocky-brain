# Recovery Procedure (Ops View)

1. Restore VPS snapshot or deploy fresh server (see `server-setup.md`).
2. Install OpenClaw + dependencies.
3. Clone/pull the `rocky-brain` repo.
4. Copy workspace files into `~/.openclaw/workspace` (or symlink repo directly).
5. Launch Rocky; follow RECOVERY.md for in-agent rehydration steps.
6. Verify TASKS.md, memory logs, and project files are present.
7. Resume operations and log the recovery in `logs/daily-log.md` + `logs/session-log.md`.
