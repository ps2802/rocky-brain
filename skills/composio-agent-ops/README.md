# Composio Agent Operations Skill

AI-native integrations for Linear, Notion, and Gmail via Composio SDK.

## Quick Start

### 1. Get Composio API Key

Go to https://composio.dev, sign up (free tier), and copy your API key.

### 2. Add to `.env`

```bash
echo "COMPOSIO_API_KEY=your_key_here" >> ~/.hermes/.env
```

### 3. Verify Setup

```bash
python ~/.hermes/skills/productivity/composio-agent-ops/scripts/composio_setup.py --check-auth
```

### 4. Use in Hermes

Once registered with Hermes, tools are available:

```
Claude: "Search for invoices from bob@contractor.com"
→ Hermes uses composio_search_email to find messages
→ Returns: [email1, email2, ...]
```

## Tools Available

### Linear
- `composio_read_linear_issue` — Read issue details
- `composio_list_linear_issues` — Query issues with filters
- `composio_create_linear_issue` — Create new issue

### Notion
- `composio_read_notion_database` — Query database
- `composio_create_notion_entry` — Add entry to database

### Gmail
- `composio_send_email` — Send email
- `composio_search_email` — Search inbox

### Status
- `composio_check_status` — Verify all integrations authenticated

## Integration with Hermes

To enable these tools in Hermes Agent:

1. **Add import to `hermes-agent/model_tools.py`:**

```python
# In _discover_tools() function, add:
from composio_hermes_registry import register_composio_tools
register_composio_tools(registry)
```

2. **Verify tools registered:**

```bash
hermes tools --list | grep composio
```

## Examples

### Read contractor from Linear

```
Claude: "What's the status of CONTRACTOR-1?"
Tool call: composio_read_linear_issue(issue_id="CONTRACTOR-1")
Response: {
  "id": "CONTRACTOR-1",
  "title": "Q1 Agent Payroll",
  "assignee": "alice@contractor.com",
  "status": "In Progress",
  ...
}
```

### Log payment to Notion

```
Claude: "Log payment of 500 USDC to bob@contractor.com in the payments database"
Tool call: composio_create_notion_entry(
  database_id="xyz123",
  properties={
    "Contractor": "bob@contractor.com",
    "Amount": 500,
    "Status": "Paid"
  }
)
Response: {
  "page_id": "abc456",
  "status": "created"
}
```

### Send invoice email

```
Claude: "Send an invoice to carol@contractor.com for contract CONTRACTOR-3"
Tool call: composio_send_email(
  to="carol@contractor.com",
  subject="Invoice for Q1 Work",
  body="Your invoice is attached..."
)
Response: {
  "status": "sent",
  "message_id": "msg123"
}
```

## Troubleshooting

**Error: `COMPOSIO_API_KEY not set`**
- Add to `~/.hermes/.env`: `COMPOSIO_API_KEY=your_key`

**Error: `Tool not authenticated (Linear)`**
- Run a Linear operation. Browser will open for OAuth. Approve it once.
- Credentials cached locally in `~/.composio/`

**Error: `RateLimitExceeded`**
- Free tier: 1000 calls/month
- If hitting limits, upgrade plan at https://composio.dev

**Error: `TimeoutError`**
- Request took >30 seconds. Check network and API status.

## Cost

- **Free tier:** 1000 API calls/month (perfect for MVP)
- **Paid:** $30-300/mo based on volume

## Support

- Composio docs: https://docs.composio.dev
- GitHub: https://github.com/ComposioHQ/composio
- Discord: https://discord.gg/composio
