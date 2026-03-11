# Agent Routing

## Routing Logic
1. **Assess Task Type**
   - Strategy / decision → Rocky core
   - Research → spawn research sub-agent or use GPT
   - Engineering / implementation → Sonnet or dedicated coding agent
   - Ops / GTM / outreach → specialized ops agent
2. **Check Context Requirements**
   - Personal projects (Moongent, Gridlock) → personal accounts
   - Work projects (Moongate, MoonSuite) → work accounts
3. **Select Model** (see `brain/model-usage.md`)
4. **Document Hand-off** in TASKS.md and relevant project file.

## Delegation Checklist
- Define desired outcome + constraints
- Provide relevant context files / links
- Specify success criteria + deliverable format
- Set review/feedback loop

## Coordination Artifacts
- TASKS.md: canonical queue
- Project docs (`projects/*.md`): scope + context
- Logs/session-log: who did what and when
- Daily Log: quick snapshot for fast catch-up
