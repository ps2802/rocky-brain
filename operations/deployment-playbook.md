# Deployment Playbook

1. **Pre-checks**
   - Ensure latest changes committed & pushed.
   - Review TASKS.md for pending blockers.
2. **Update**
   - Pull latest repo state on server.
   - Restart OpenClaw/agent services if configs changed.
3. **Validation**
   - Run smoke tests (agent ping, tool availability, workspace integrity).
   - Confirm Telegram bridge is active.
4. **Post-Deploy**
   - Log deployment details in `logs/session-log.md`.
   - Update MEMORY.md if new capabilities or configs were added.
