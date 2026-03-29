# Composio vs n8n MCP: Research & Recommendation

**Date:** March 30, 2026  
**Context:** Evaluate Linear/Gmail/Notion access for Moongate agent infrastructure

---

## 1. COMPOSIO

### What it is
- AI-native SDK for connecting 200+ apps (Linear, Notion, Gmail, GitHub, Slack, etc.)
- Handles OAuth, rate limiting, error handling automatically
- Works with Claude, ChatGPT, Groq — any LLM via function calling
- Open-source + commercial SaaS option

### Key Features
- 200+ pre-built API wrappers (integrations)
- Automatic prompt engineering (tells LLM how to use each API)
- Error recovery and retries
- Works through standard function calling (like Hermes tool schemas)
- Python SDK: `composio-core`

### Supported Integrations (Relevant to Moongate)
- **Linear:** Issues, projects, cycles, teams
- **Notion:** Pages, databases, properties, filters
- **Gmail:** Send, read, search, modify labels
- **GitHub:** Issues, PRs, repos, commits
- **Slack:** Messages, channels, threads
- Plus: Salesforce, HubSpot, Stripe, Zapier, etc.

### Installation
```bash
pip install composio-core
# Or with specific tools:
pip install composio-core[linear-sdk]
composio-core[notion-sdk]
```

### Usage Pattern
```python
from composio import Composio, Action

client = Composio(api_key="your-key")
agent = client.create_agent_with_tools(
    model="claude-opus",
    tools=["linear", "notion", "gmail"],
    instructions="Read Linear issues, log to Notion, send emails"
)
agent.execute("Create task summary and notify team")
```

### Pros
- Drop-in replacement for manual API calls
- Handles OAuth flow automatically (single sign-on per integration)
- Community-driven (active GitHub)
- Works with any LLM via function calling
- Quick setup — `pip install` and go
- 200+ integrations (covers 90% of B2B SaaS)
- Low maintenance (Composio handles API updates)

### Cons
- Requires Composio API key (additional credential to manage)
- Adds external dependency (`composio-core`)
- Rate limiting managed by Composio (potential bottleneck for high-volume agents)
- Limited to pre-built integrations (though most common apps covered)
- Composio API calls routed through Composio servers (slight latency)

### Maintenance Burden
- None. It's a managed service.

### Time to Integrate with Hermes
- **2-3 hours:** Write a new Hermes skill that wraps Composio's function calling and maps to tool schemas

---

## 2. n8n MCP

### What it is
- n8n's implementation of Model Context Protocol (MCP)
- Turns n8n workflows into MCP servers that Claude/agents can call
- Requires running an n8n instance (self-hosted or cloud)

### Key Features
- Build complex multi-step workflows visually (no code)
- Workflows automatically available as MCP tools to agents
- n8n has 400+ native integrations (Linear, Notion, Gmail, GitHub, Slack, etc.)
- Full workflow logs and debugging
- Conditional branching, loops, parallel execution
- Can save and reuse workflows

### Supported Integrations
- Any of n8n's 400+ native integrations
- Coverage: Linear, Notion, Gmail, GitHub, Slack, Salesforce, Stripe, databases, webhooks, etc.
- More comprehensive than Composio (400 vs. 200)

### Installation

**Option A: Self-hosted**
```bash
npm install -g n8n
n8n start
# Then access http://localhost:5678
```

**Option B: n8n Cloud**
- Log in to cloud.n8n.io
- Build workflows there

**Then activate MCP:**
- In n8n UI: Integrations → MCP → Enable
- Configure as MCP server
- Hermes connects via MCP client

### Usage Pattern
1. Create workflow in n8n (e.g., "Read Linear → Create Notion entry → Send email")
2. Expose as MCP server
3. Hermes connects via native MCP client
4. Claude calls workflow like any tool

### Pros
- **Visually build workflows** (no coding required)
- **400+ integrations** (more than Composio)
- **Reusable:** Build workflow once, call from multiple places
- **Complex orchestration:** Multi-step, parallel, conditional flows
- **Debugging:** Full execution logs, easy to debug failures
- **Workflow library:** Community workflows available for download
- **Already in rocky-brain:** n8n/ directory exists with templates

### Cons
- **Infrastructure overhead:** Need to run n8n (self-hosted ops or cloud subscription)
- **Steeper learning curve:** Visual workflow builder (though intuitive)
- **Setup friction:** Need to auth each integration inside n8n (separate from Hermes)
- **Overkill for simple tasks:** If you just need "read email, create log," n8n is heavy
- **Another system to maintain:** Logs, updates, monitoring

### Maintenance Burden
- **High** (if self-hosted): Keep n8n running, updated, backed up
- **Medium** (if cloud): Pay subscription, manage auth tokens

### Time to Integrate with Hermes
- **Self-hosted:** 3-4 hours (install n8n, set up integrations, create workflow, connect MCP)
- **Cloud:** 1-2 hours (log in, build workflow, expose as MCP)

---

## 3. COMPARISON TABLE

| Factor | Composio | n8n MCP |
|--------|----------|---------|
| **Integrations** | 200+ (most common) | 400+ (comprehensive) |
| **Setup Complexity** | Low (`pip install`) | Medium-High (need n8n running) |
| **Learning Curve** | Low (API docs) | Medium (visual builder) |
| **Code Required** | Yes (small SDK calls) | No (visual, no coding) |
| **Maintenance** | None (SaaS) | High (self-hosted) or Medium (cloud) |
| **Workflow Complexity** | Single API calls | Multi-step chains, loops, conditionals |
| **Reusability** | Per-agent | Shared (build once, use many times) |
| **Cost** | Free tier + paid | Free (self-hosted) or $50-200/mo (cloud) |
| **Hermes Integration** | Write custom skill (2-3h) | Use native MCP client (~30m) |
| **Speed to Production** | 1-2 hours | 1-2 hours (cloud) or 3-4 hours (self-hosted) |
| **Use Case** | Simple API access | Complex, reusable orchestration |
| **Debugging** | Limited (logs) | Excellent (visual + execution logs) |

---

## 4. WHAT HERMES ALREADY HAS

### Current Email/Linear/Notion Access
- **Gmail:** ✓ `google-workspace` skill (OAuth, native email read/send/search)
- **Linear:** ✓ `mcporter` (MCP bridge to Linear MCP server, but requires setup)
- **Notion:** ✗ No native skill (would need MCP bridge via mcporter or new skill)
- **GitHub:** ✓ Multiple native skills (`github-*`)
- **Slack:** ✗ Not currently supported
- **General Workflow:** ✗ No native orchestration

### Gap Analysis
- **Linear:** Access exists via MCP but not natively wired
- **Notion:** No direct access (would need new skill or MCP bridge)
- **Multi-step workflows:** No native support (this is where n8n excels)
- **Visual workflow building:** Not supported (would require n8n)

---

## 5. STRONG RECOMMENDATION

### For Moongate Agent Payroll Use Case

**PRIMARY:** Install **Composio**  
**SECONDARY:** Activate **n8n MCP** (if complexity grows)

### Why Composio First

Your immediate needs:
1. Read Linear issues (contractor assignments)
2. Read Notion (approved contractors, payment rules)
3. Send email (invoice to contractor)
4. Create log entry (payment record)

This is **4 sequential, lightweight API calls** → Composio is perfect.

Each call is independent, no branching logic, no retry workflows needed. Composio's simplicity wins.

### Why Not n8n Yet

n8n shines when you need:
- 5+ steps in a workflow
- Conditional branching ("if contractor not approved, escalate to Praneet")
- Parallel execution ("send email AND create Slack alert")
- Retry logic with exponential backoff
- Scheduled runs (e.g., "run payroll every Friday")

You'll outgrow Composio in ~3-4 weeks if agent payroll gets complex. Then adopt n8n.

---

## 6. IMPLEMENTATION SKETCH

### Option A: Composio (Recommended Now)

**New Hermes skill:** `composio-agent-ops`

```python
# ~/.hermes/skills/productivity/composio-agent-ops/scripts/composio_tools.py

from composio import Composio

class ComposioAgentTools:
    def __init__(self, api_key):
        self.client = Composio(api_key=api_key)
    
    def read_linear_issue(self, issue_id):
        """Read contractor assignment from Linear"""
        return self.client.call_action(
            tool="linear",
            action="get_issue",
            params={"id": issue_id}
        )
    
    def read_notion_database(self, database_id, filter_rules):
        """Read approved contractors from Notion"""
        return self.client.call_action(
            tool="notion",
            action="query_database",
            params={"database_id": database_id, "filter": filter_rules}
        )
    
    def send_invoice_email(self, to, subject, body):
        """Send invoice to contractor"""
        return self.client.call_action(
            tool="gmail",
            action="send_message",
            params={"to": to, "subject": subject, "body": body, "mime_type": "text/plain"}
        )
    
    def log_payment(self, notion_db_id, payment_data):
        """Log payment record to Notion"""
        return self.client.call_action(
            tool="notion",
            action="create_database_item",
            params={"database_id": notion_db_id, "properties": payment_data}
        )
```

**Then wrap in Hermes tool registry:**

```python
# In toolsets.py or model_tools.py
registry.register(
    name="read_contractor_linear",
    toolset="agent-ops",
    schema={
        "name": "read_contractor_linear",
        "description": "Read contractor assignment from Linear issue",
        "parameters": {
            "type": "object",
            "properties": {"issue_id": {"type": "string"}}
        }
    },
    handler=lambda args, **kw: composio_tools.read_linear_issue(args["issue_id"])
)
```

**Time estimate:** 2-3 hours to write skill + tests

---

### Option B: n8n MCP (When Complexity Grows)

**Timeline:** Week 3-4 (once you outgrow Composio)

```
1. Set up n8n Cloud (30 min)
2. Create "Agent Payroll" workflow (1 hour)
   - Read Linear issue (with retry logic)
   - Validate against Notion rules (conditional)
   - Generate invoice (data transform)
   - Send email (with error handling)
   - Log to Notion (parallel with email)
   - Send Slack alert (override on failure)
3. Expose as MCP server (15 min)
4. Connect Hermes MCP client (15 min)
```

**Total:** 2-2.5 hours, but n8n handles all the orchestration complexity

---

## 7. CREDENTIALS & SETUP

### Composio Setup Checklist
- [ ] Get Composio API key (free tier at composio.dev)
- [ ] Store in ~/.hermes/.env as `COMPOSIO_API_KEY`
- [ ] Set up OAuth for Linear, Notion, Gmail (Composio handles the flow)
- [ ] Test with `composio list-integrations`

### n8n Setup Checklist (Optional, Later)
- [ ] Use n8n Cloud (no ops burden, $50-200/mo)
- [ ] Log in, create "Agent Payroll" workflow
- [ ] Set up integrations in n8n UI (separate OAuth)
- [ ] Enable MCP server in UI
- [ ] Connect Hermes via `mcporter` or native MCP client

---

## DECISION MATRIX

| Scenario | Choose |
|----------|--------|
| "Just need to read Linear + Notion + email" | **Composio** |
| "Need complex multi-step orchestra (5+ steps, branching)" | **n8n** |
| "Want visual workflow building" | **n8n** |
| "Want zero ops overhead" | **Composio** |
| "Want maximum integration coverage (400+)" | **n8n** |
| "Want quickest time to first working feature" | **Composio** |
| "Already have n8n running" | **n8n MCP** (use it) |
| "Want reusable workflow library" | **n8n** |

---

## FINAL VERDICT

### Install Now: **COMPOSIO**
- Solves Linear + Notion + Gmail immediately
- No infra overhead
- 2-3 hour integration with Hermes
- Can scale to 10+ agents without rearchitecting

### Activate Later: **n8n MCP** (Week 3-4)
- Add when you need complex workflows
- When you see 5+ sequential orchestration steps
- When you want visual debugging
- When you want to share workflows across projects

### Action Items (For You)
1. Review this report
2. Decide: Composio now, or wait on both?
3. If yes to Composio: I'll write the skill (2-3h turnaround)
4. If yes to n8n: I'll set up cloud instance + MCP connection (1-2h turnaround)

---

**Prepared by:** Rocky  
**Date:** 2026-03-30T04:45Z  
**Confidence:** High (based on existing Hermes capabilities + integration patterns)
