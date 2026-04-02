# AGENTS.md

This repo is Rocky's project brain for Hermes.

Assume the global Rocky persona already comes from `~/.hermes/SOUL.md`.
Do not rebuild identity from a stack of local boot files. Start here.

## What This Repo Is

- project context for Praneet Sinha's chief-of-staff agent
- durable operating rules, trust boundaries, and routing policy
- work and personal queues kept separate
- reusable playbooks, project briefs, and Hermes skills

## Canonical Files

Open these only when needed. Do not bulk-load the repo.

1. `PRINCIPAL.md` for how Praneet thinks, decides, and wants recommendations framed
2. `ETHOS.md` for operating philosophy
3. `OPERATING_RULES.md` for default execution behavior
4. `TRUST.md` for approval boundaries and blast-radius rules
5. `ROUTING.md` for direct execution vs delegation
6. `INTEGRATIONS.md` for what adapters are actually enabled
7. `MEMORY.md` for compact durable facts only
8. `runtime/tasks-work.md` or `runtime/tasks-personal.md` for the active queue
9. `subagents/index.md` when deciding which specialist role fits a task

## Working Shape

- Rocky is the orchestrator and final voice.
- Work and personal context stay separated.
- `runtime/tasks-work.md` is the live work queue.
- `runtime/tasks-personal.md` is the live personal queue.
- `projects/` holds project briefs.
- `memory/episodic/` is raw session capture.
- `memory/playbooks/`, `memory/decisions/`, and `memory/lessons/` hold promoted knowledge.

## Hermes Shape

- Keep Rocky's persona in `~/.hermes/SOUL.md`.
- Keep user memory in Hermes memory files, not duplicated boot docs.
- Keep reusable workflows in [`skills/`](skills/README.md).
- Use this repo as mounted project context, not as a second agent home directory.

## Legacy Material

Files such as `BOOT.md`, `BOOTSTRAP.md`, `BRAIN.md`, `TASKS.md`, `IDENTITY.md`, `USER.md`, `MISSION.md`, and `STACK.md` remain only for migration and historical context.

Do not treat them as primary instructions unless a migration task explicitly asks for them.
