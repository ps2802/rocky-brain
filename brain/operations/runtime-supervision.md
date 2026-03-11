# Runtime Supervision — Gateway

## Supervisor
- **Controller:** PM2 (process `rocky` → `node dist/index.js gateway --port 18789`)
- **Startup:** `pm2 startup systemd -u praneet --hp /home/praneet` (installed as `pm2-praneet.service`, enabled)
- **Process list:** stored via `pm2 save`

## Check Commands
```bash
pm2 list                       # should show only the "rocky" gateway entry
systemctl status pm2-praneet    # confirms systemd unit is enabled
lsof -i :18789                 # verify single listener (PID from pm2)
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:18789/__openclaw__/health
openclaw status                # confirm gateway reachable
```

## Restart Procedure
```bash
pm2 restart rocky
pm2 save                      # if the process definition changes
```

## Notes
- Systemd user services weren’t available before; persistence now depends on the root-level `pm2-praneet` unit. If the machine reboots, systemd launches PM2 which resurrects the saved process list.
- Manual `openclaw gateway` invocations are no longer needed. Use PM2 only.
