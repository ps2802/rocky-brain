# rocky-brain

Rocky's project brain for Hermes.

This repo is not the whole agent runtime. It is the mounted context, task system, playbook library, and project memory that Hermes should see while working for Praneet.

## Active Layout

```text
rocky-brain/
├── AGENTS.md                 # canonical project entrypoint for Hermes
├── SOUL.md                   # source-of-truth persona file to install into ~/.hermes/
├── PRINCIPAL.md              # how Praneet thinks and decides
├── ETHOS.md                  # operating philosophy
├── OPERATING_RULES.md        # direct execution rules
├── TRUST.md                  # approval boundaries
├── ROUTING.md                # delegation policy and model defaults
├── INTEGRATIONS.md           # enabled vs draft adapters
├── MEMORY.md                 # compact durable facts only
├── runtime/
│   ├── tasks-work.md         # live work queue
│   └── tasks-personal.md     # live personal queue
├── projects/                 # project briefs
├── memory/
│   ├── episodic/             # raw session capture
│   ├── decisions/            # promoted decisions
│   ├── lessons/              # repeated corrections
│   └── playbooks/            # reusable workflows
├── subagents/                # role definitions and output contract
└── skills/                   # Hermes-native reusable skills
```

## Install Pattern

1. Clone this repo somewhere stable, for example `~/rocky-brain`.
2. Install [`SOUL.md`](SOUL.md) into `~/.hermes/SOUL.md`.
3. Expose [`skills/`](skills/README.md) to Hermes, either by copying each skill directory into `~/.hermes/skills/` or by adding this repo's `skills/` directory as an external skill path.
4. Use this repo as project context so Hermes reads [`AGENTS.md`](AGENTS.md) when working here.

## Operating Rules

- Start from [`AGENTS.md`](AGENTS.md), not from boot scripts.
- Keep Rocky's persona global in `~/.hermes/SOUL.md`.
- Keep `MEMORY.md` compact. If a fact belongs to one project or one day, do not dump it into global memory.
- Keep work and personal compartments separate.
- Treat `runtime/tasks-work.md` and `runtime/tasks-personal.md` as the live queues.

## Skills

Rocky's specialist roles ship as Hermes-native skills in [`skills/`](skills/README.md):

- `rocky-stratt`
- `rocky-wrench`
- `rocky-sputnik`
- `rocky-forge`
- `rocky-velvet-knife`

These are reusable role packets. They do not assume a fake `/spawn` command.

## Legacy Files

Older OpenClaw-era files are still present for migration and historical context.

They are not the active operating path anymore:

- `BOOT.md`
- `BOOTSTRAP.md`
- `BRAIN.md`
- `TASKS.md`
- `IDENTITY.md`
- `USER.md`
- `MISSION.md`
- `STACK.md`

## Public vs Private

Do not assume this repo is public-safe just because it does not contain secrets.

It still contains private operating context, internal task state, and personal/work routing details. Treat the live brain as private.
