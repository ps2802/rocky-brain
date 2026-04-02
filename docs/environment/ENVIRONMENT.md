# ENVIRONMENT

## Shell & Paths

- Default shell: `/bin/bash -lc`
- Hermes home: `~/.hermes`
- Rocky brain repo: `~/rocky-brain` or equivalent stable clone path

## Runtime

- Hermes provides the agent runtime
- `~/.hermes/SOUL.md` holds Rocky's persona
- this repo provides mounted project context and optional external skills

## Secrets & Env Vars

- Provider keys live in `~/.hermes/.env`
- Google ADC files, when used, live under `~/.config/gcloud/`
- Never commit secret values into this repo

## Tooling Notes

- Store generated artifacts in repo paths and reference them instead of pasting giant blobs
- Exclude large build output when searching unless it is the target of the task
