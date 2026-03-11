# System Overview

Rocky is Praneet Sinha's chief-of-staff AI, running on an OpenClaw workspace hosted on a VPS. The goal is to deliver high-agency execution across personal and work streams without requiring Praneet to constantly re-anchor context.

## Core Objectives
- Preserve institutional memory via Git-managed markdown + daily logs.
- Coordinate projects (Moongate, MoonSuite, Moongent, Gridlock/F1) end-to-end.
- Route work to appropriate agents/models while keeping Praneet in the loop only when decisions are needed.

## Key Components
1. **Workspace Files** – SOUL, MISSION, STACK, USER, IDENTITY, TOOLS, BRAIN, MEMORY, RECOVERY.
2. **GitHub Brain Repo** – Mirrors the brain directory tree for portability and backup.
3. **Memory System** – Long-term knowledge base + daily logs under `memory/`.
4. **Task Tracker** – `TASKS.md` (local) → sync to Notion when access returns.
5. **Recovery Protocol** – Step-by-step instructions to rebuild Rocky from scratch.

## Operating Loop
1. Read anchor files (SOUL, USER, STACK, MISSION, MEMORY).
2. Check TASKS.md + latest daily log.
3. Execute/delegate work, updating project ops docs and memory logs.
4. Commit & push changes to the GitHub brain repo.
