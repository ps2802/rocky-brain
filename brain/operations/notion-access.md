# Notion Bridge – Rocky Command Centre

## Access Checklist (what Praneet must provide)
### Work workspace — “Rocky Command Centre (Work)”
1. Create/confirm Notion internal integration named **`rocky-work-bridge`**.
2. Share the entire workspace (or at minimum the databases below) with that integration.
3. Send the integration secret (I’ll store it at `secrets/notion/work.token`).
4. Share + send database IDs for:
   - `Task Board`
   - `Decision Log`
   - `Ops Feed`

### Personal workspace — “Rocky Command Centre (Personal)”
1. Create integration **`rocky-personal-bridge`**.
2. Share the workspace (or relevant DBs) with that integration.
3. Provide the integration secret (stored at `secrets/notion/personal.token`).
4. Share + send DB IDs for:
   - `Personal Tasks` (future sync target)
   - Any other DBs you want mirrored later.

## Work Workspace Structure
- **Pages:** `Dashboard`, `Moongate Ops`, `Automations`, `Knowledge Base`.
- **Databases:**
  | Database | Purpose | Key Fields |
  |----------|---------|------------|
  | Task Board | Source of truth for execution | `Name`, `Status`, `Owner`, `Priority`, `Due`, `SourceID`, `Notes`
  | Decision Log | Canonical decision history | `Name`, `Date`, `Context`, `Owner`, `SourceLink`
  | Ops Feed | Daily summary snapshots | `Date`, `Highlights`, `SourceLink`

## Personal Workspace Structure
- **Pages:** `Personal HQ`, `Finance`, `Experiments`, `Calendar overlay`.
- **Databases:**
  | Database | Purpose | Key Fields |
  |----------|---------|------------|
  | Personal Tasks | Light-weight personal todos | `Name`, `Status`, `Due`, `Notes`
  | (future) Personal Notes | Reference items | `Name`, `Tags`, `Summary`

## Task Workflow
1. Capture every live task in **Task Board** (Work). Columns: Backlog → Ready → In Progress → Blocked → Done.
2. `TASKS.md` mirrors the active items (Backlog/Ready/In Progress/Blocked/Done sections), using the Notion ID as `{id: }` metadata so round-trips are lossless.
3. Completed tasks get logged in `logs/daily-log.md` (summary) and stay archived in Notion.

## Sync Mappings
1. **Task Board ⇄ `TASKS.md`**
   - `Name` ↔ Markdown entry title
   - `Status` ↔ Markdown section
   - `Owner` ↔ `{owner: }`
   - `Due` ↔ `{due: }`
   - `Priority` ↔ `{priority: }`
   - Notion page ID ↔ `{id: }` for reconciliation
2. **`memory/key-decisions.md` → Decision Log**
   - `- YYYY-MM-DD: Summary` ↔ `Name`
   - Date portion ↔ `Date`
   - Remaining text ↔ `Context`
   - Git permalink ↔ `SourceLink`
3. **`logs/daily-log.md` → Ops Feed**
   - Section heading ↔ `Date`
   - Bullets under that date ↔ `Highlights`
   - File anchor ↔ `SourceLink`

## Sync Execution
- Owner: **n8n** (three workflows: `Notion Task Sync`, `Decision Broadcast`, `Ops Feed Sync`).
- Each workflow accepts the Notion token + DB IDs via environment variables; GitHub files are accessed from this repo.

## Reset / Reconnect Steps
1. Ensure both integration tokens exist locally (`secrets/notion/work.token`, `secrets/notion/personal.token`).
2. Export DB IDs into `secrets/notion/work-db-ids.json` for n8n to consume.
3. Run the n8n workflows (or redeploy them) so they start syncing again.
4. Verify Task Board ↔ `TASKS.md` sync by updating one task and running the job.
5. Verify Decision Log + Ops Feed by appending to the markdown files and confirming the new Notion rows.

Once the tokens and DB IDs are provided, these instructions make the Notion bridge fully executable—no more placeholder mode.
