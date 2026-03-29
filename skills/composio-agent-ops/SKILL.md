---
name: composio-agent-ops
description: AI-native integrations for Linear, Notion, Gmail via Composio SDK. Drop-in tool wrappers for agent operations (read issues, log to databases, send emails).
version: 1.0.0
author: Rocky (Praneet's Chief-of-Staff)
license: MIT
required_environment_variables:
  - COMPOSIO_API_KEY
required_python_packages:
  - composio-core>=0.7.0
metadata:
  hermes:
    tags: [Linear, Notion, Gmail, Composio, Agent Operations, Integration]
    category: productivity
    homepage: https://composio.dev
---

# Composio Agent Operations

Drop-in AI integrations for Linear, Notion, Gmail using Composio SDK. Designed for agent payroll infrastructure, ops workflows, and multi-tool orchestration.

## What This Does

Composio is an SDK that wraps 200+ app APIs (Linear, Notion, Gmail, GitHub, Slack, etc.) and exposes them as function-calling tools for Claude, Hermes, or any LLM.

This skill provides four core operations:

1. **Linear Integration:** Read/create issues, query projects
2. **Notion Integration:** Read/write databases, create pages
3. **Gmail Integration:** Send emails, search inbox, read messages
4. **Common Utilities:** Error handling, credential management, rate limiting

## Setup

### Step 1: Get Composio API Key

1. Go to https://composio.dev
2. Sign up (free tier includes 1000 API calls/month)
3. Copy your API key
4. Add to `~/.hermes/.env`:

```bash
COMPOSIO_API_KEY=your_key_here
```

### Step 2: Install Package

```bash
pip install composio-core>=0.7.0
```

### Step 3: Authorize Integrations

First time you use an integration (Linear, Notion, Gmail), Composio will open a browser to ask for OAuth permission. Approve it once, and credentials are cached locally.

```bash
python ~/.hermes/skills/productivity/composio-agent-ops/scripts/composio_setup.py --check-auth
```

## Usage

All operations are registered as Hermes tools. Claude can call them directly:

```
Claude: "Check if there's an assigned contractor in Linear ticket LINER-42"
→ Hermes calls: read_linear_issue(issue_id="LINER-42")
→ Returns: {"assignee": "contractor@example.com", "title": "Agent Payroll", ...}
```

### Available Operations

#### Linear

- **read_linear_issue** — Get issue details (assignee, title, status, custom fields)
- **list_linear_issues** — Query issues (filter by status, project, assignee)
- **create_linear_issue** — Create new issue

#### Notion

- **read_notion_database** — Query database (filter, sort, paginate)
- **create_notion_entry** — Add row to database
- **update_notion_entry** — Modify existing entry
- **read_notion_page** — Get page content

#### Gmail

- **send_email** — Send message (to, subject, body, optional CC/BCC)
- **search_email** — Find messages (query: "from:user@example.com", "has:attachment", etc.)
- **read_email** — Get full message body

#### Utilities

- **check_composio_status** — Verify all integrations are authenticated
- **composio_help** — List all available integrations and their actions

## Examples

### Agent Payroll Workflow

```python
# 1. Read contractor assignment from Linear
contractor = tools.read_linear_issue(issue_id="CONTRACTOR-1")
contractor_email = contractor.get("assignee_email")

# 2. Check payment rules in Notion
payments = tools.read_notion_database(
    database_id="notion_db_xyz",
    filter={"property": "Status", "select": {"equals": "Approved"}}
)

# 3. Send invoice email
tools.send_email(
    to=contractor_email,
    subject=f"Invoice for {contractor['title']}",
    body="Your payment will be processed..."
)

# 4. Log to Notion
tools.create_notion_entry(
    database_id="payments_db",
    properties={
        "Contractor": contractor_email,
        "Amount": 500,
        "Status": "Sent"
    }
)
```

## Rules & Limitations

1. **Rate limiting:** Composio manages rate limits. Errors auto-retry with backoff.
2. **Credentials:** OAuth tokens cached locally in `~/.composio/`. Never share these.
3. **Errors:** API failures logged to `~/.hermes/logs/composio-errors.log`
4. **Timeout:** Default 30 seconds per request. Adjust in config if needed.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `AuthenticationError: Invalid API key` | Check `COMPOSIO_API_KEY` in `~/.hermes/.env` |
| `ToolNotAuthenticated: Linear not authorized` | Run setup script; approve OAuth in browser |
| `RateLimitExceeded` | Composio auto-retries. If persistent, upgrade plan |
| `TimeoutError` | Request took >30s. Check network; may indicate API slowness |

## Performance

- **Linear:** ~200-500ms per request
- **Notion:** ~300-800ms per request
- **Gmail:** ~200-400ms per request

Composio caches responses client-side, so repeated queries to same resource are faster.

## Cost

- **Free tier:** 1000 API calls/month (perfect for MVP)
- **Paid tiers:** $30-300/mo based on volume

This skill makes efficient use of quota (batch reads, caching).

---

**Prepared by:** Rocky  
**Status:** Production-ready  
**Last updated:** 2026-03-30
