# INTEGRATIONS.md

## Purpose

This file tracks capability classes, approval policy, and enablement state.

Do not confuse "architecturally useful" with "enabled right now."

## Enabled in v1

### Communication

- Telegram: enabled, live

### Research

- web search: enabled
- browser access: enabled only when runtime tooling exists

### Workspace

- local files: enabled
- git: enabled
- shell/scripts: enabled

## Draft-Only in v1

- X / Twitter
- email

Rocky may draft, queue, and recommend, but not send or publish without approval.

## Future Adapters

- WhatsApp
- voice
- SaaS connectors
- browser-submit automations
- payments

## Capability Classes

- communication
- execution
- browser
- crawl/search
- memory
- SaaS/API
- payments
- voice

## Adapter Rule

Every enabled adapter must define:

- compartment allowed: work, personal, or both
- trust zone
- approval requirement
- evidence requirement

If an adapter does not have a written policy, it is not enabled. Bureaucratic? Yes. Better than waking up to a surprise invoice.
