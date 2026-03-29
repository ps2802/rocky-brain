# Secrets Policy

## Rule

Secrets never live in repo-tracked files.

## Allowed Storage

- environment variables
- external secret managers
- runtime-only local secret files ignored by Git

## Forbidden

- API keys in markdown
- tokens in task files
- credentials in memory logs
- screenshots or copied dumps of sensitive values committed to Git

## Brain Repo Policy

This repo may store:

- secret names
- where the secret is managed
- which compartment owns it

This repo may not store:

- secret values
- full auth dumps
- backup copies of credentials

## Operational Rule

When a task needs secrets, Rocky should reference the required secret and the tool path, not print the secret. The point is to run the system, not audition for an incident report.
