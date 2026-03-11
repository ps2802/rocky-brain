# Notion Bridge – Rocky Command Centre

> **Status:** Access pending. This doc captures the structure and workflow so we can reconnect immediately once Notion credentials are reissued.

## 1. Rocky Command Centre Structure
- Central workspace: **Rocky Command Centre** (Notion)
- Expected top-level areas:
  - **Dashboards:** high-level status (work vs personal streams)
  - **Pipelines / Databases:** task boards, roadmaps, CRM snippets
  - **Reference pages:** project briefs, SOPs, meeting notes
- Once access returns, capture the exact page tree here (e.g., Dashboard → Workstreams → Moongate)

## 2. Important Pages / Databases
Placeholder until access is re-granted. Expected key objects:
- **Task board:** Kanban or table driving execution
- **Meeting notes DB:** logs decisions + action items
- **Projects DB:** Moongate, MoonSuite, Moongent, Gridlock
- **References:** vendor lists, credentials, etc.

Action when access is restored:
1. List each critical page/DB here with its Notion URL
2. Note the purpose + fields for each database

## 3. Task Workflow
- Source of truth for live work: Notion task board (Rocky Command Centre)
- Local mirror: `TASKS.md` in GitHub for resilience + diffing
- Flow once synced:
  1. Capture work in Notion (Backlog → Ready → In Progress → Done)
  2. `n8n` (or manual script) syncs key fields (ID, title, owner, status, due) into `TASKS.md`
  3. Completed items logged daily in `logs/daily-log.md`

## 4. What lives only in Notion
- High-churn collaborative tasks and dashboards
- Meeting notes with inline comments
- CRM-style tables that depend on Notion filters/rollups
- Visual boards for quick triage

## 5. What mirrors into GitHub (`rocky-brain`)
- Canonical memories (`memory/*.md`, `logs/*.md`)
- Task snapshots (`TASKS.md`)
- Project briefs (`projects/*.md`)
- Operating docs (this folder)

## 6. Reconnecting After a Reset
1. Request Notion invite to **Rocky Command Centre** (praneet@moongate.one + bot account)
2. Verify API token / integration (store reference in `SECRETS.md`, actual token in `secrets/`)
3. Sync key databases via `n8n` or scripts
4. Update this file with the actual page map + URLs
5. Resume normal workflow (Notion for live ops, GitHub for recovery)

_Once access resumes, replace the placeholders with real links and screenshots so resets can be recovered end-to-end._
