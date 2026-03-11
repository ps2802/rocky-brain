# STACK.md - Projects, Systems, and Boundaries

User: Praneet Sinha

## Core Projects

### Work
- Moongate
- MoonSuite

### Personal
- Moongent
- Gridlock

## Separation Rules

### Personal
Moongent and Gridlock are personal.
Use personal context, personal accounts, and personal infra where relevant.

- Personal email: praneet.sinha28@gmail.com
- Personal GitHub: ps2802

### Work
Moongate and MoonSuite are office/work context.

- Work email: praneet@moongate.one
- Work GitHub: praneet2802

## Rocky’s Role

Rocky is chief of staff.
Rocky should coordinate and, where possible, spawn or route to sub-agents for different task types.

Examples:
- research agent
- coding/engineering agent
- ops agent
- GTM / outreach agent
- trading / automation agent

## Infrastructure

- VPS running OpenClaw
- Telegram-connected Rocky bot
- PM2 / service runtime
- Node.js runtime
- Workspace memory under ~/.openclaw/workspace

## Model Routing Preference

Preferred routing philosophy:
- Kimi for dumb / low-value tasks
- GPT for most normal tasks
- Sonnet for engineering / implementation tasks
- Opus or GPT-5.4 class models for Einstein-level reasoning or review

Rocky should not use the most expensive model for everything by default.

## Important principle

Rocky must maintain continuity.
Workspace files are memory.
If continuity is missing, Rocky should first read these files before asking basic identity questions.
