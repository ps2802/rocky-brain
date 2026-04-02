# Deployment Playbook

1. **Pre-checks**
   - Ensure the repo is committed and pushed.
   - Review `runtime/tasks-work.md` and `runtime/tasks-personal.md` for blockers.
   - Review the diff for trust-boundary or routing regressions.

2. **Update Production Brain**
   - Pull the latest repo state on the VPS.
   - Re-sync `SOUL.md` into `~/.hermes/SOUL.md` if it changed.
   - Re-sync `skills/` into Hermes if skill definitions changed.

3. **Validation**
   - Start Hermes in the repo context.
   - Verify `AGENTS.md` is the active project entrypoint.
   - Verify the Rocky skills are discoverable.
   - Confirm Telegram and provider connectivity if relevant to the change.

4. **Post-Deploy**
   - Record what changed in `logs/session-log.md` or an episodic note.
   - If the deployment changed durable behavior, update `MEMORY.md` or the relevant playbook.
