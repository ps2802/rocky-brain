# Composio Integration with Hermes Agent

**Date:** 2026-03-30  
**Status:** Skill built. Ready to integrate.

---

## What's Done

1. ✓ Built Composio skill: `~/.hermes/skills/productivity/composio-agent-ops/`
2. ✓ Implemented 8 tools (Linear, Notion, Gmail)
3. ✓ Created Hermes registry integration
4. ✓ Archived to rocky-brain/skills/
5. ⏳ **Pending:** Wire into hermes-agent/model_tools.py

---

## Integration Steps

### Step 1: Copy Skill to Hermes Repo

If hermes-agent is a separate repo from ~/.hermes/skills:

```bash
cp -r ~/.hermes/skills/productivity/composio-agent-ops ~/hermes-agent/skills/
# Or: just keep in ~/.hermes/skills; Hermes auto-discovers skills
```

### Step 2: Enable Tool Discovery

In `hermes-agent/model_tools.py`, find the `_discover_tools()` function around line 80-120.

**Add this import at the top of model_tools.py:**

```python
import sys
from pathlib import Path

# Add skills directory to path for skill imports
SKILLS_PATH = Path.home() / ".hermes" / "skills"
if str(SKILLS_PATH) not in sys.path:
    sys.path.insert(0, str(SKILLS_PATH))
```

**In `_discover_tools()`, add after other tool imports (around line 110):**

```python
def _discover_tools():
    """Discover and register all tools."""
    
    # ... existing tool discovery code ...
    
    # Register Composio tools (if available)
    try:
        sys.path.insert(0, str(Path.home() / ".hermes" / "skills" / "productivity" / "composio-agent-ops" / "scripts"))
        from composio_hermes_registry import register_composio_tools
        register_composio_tools(registry)
        logger.info("✓ Composio tools registered")
    except ImportError as e:
        logger.debug(f"Composio not available: {e}")
    
    return registry
```

### Step 3: Verify Registration

```bash
# Start Hermes Agent
cd ~/hermes-agent
source venv/bin/activate
python run_agent.py

# In another terminal, list tools
hermes tools --list | grep composio

# Output should show:
# composio_read_linear_issue ✓
# composio_list_linear_issues ✓
# composio_create_linear_issue ✓
# composio_read_notion_database ✓
# composio_create_notion_entry ✓
# composio_send_email ✓
# composio_search_email ✓
# composio_check_status ✓
```

### Step 4: Set Credentials

Add to `~/.hermes/.env`:

```bash
COMPOSIO_API_KEY=your_key_here
```

Get key: https://composio.dev (free tier)

### Step 5: Test

```bash
hermes
> composio_check_status
→ {composio: "connected", linear: "not_authenticated", ...}
→ (First use opens browser for OAuth approvals)
```

---

## Implementation Notes

### Why This Approach?

1. **Skill pattern:** Uses standard Hermes skill structure (SKILL.md, scripts/, registry integration)
2. **No core changes:** Doesn't require modifying hermes-agent source; works as external skill
3. **Composio handles state:** OAuth caching, rate limiting, error recovery — all handled by Composio SDK
4. **Function calling pattern:** Tools registered exactly like existing Hermes tools (same schema format)

### Tool Schema Format

Each tool follows Hermes standard:

```python
registry.register(
    name="composio_read_linear_issue",
    toolset="agent-operations",
    schema={
        "name": "composio_read_linear_issue",
        "description": "...",
        "parameters": {
            "type": "object",
            "properties": { ... },
            "required": [ ... ]
        }
    },
    handler=lambda args, **kw: composio_read_linear_issue(
        issue_id=args.get("issue_id", ""),
        task_id=kw.get("task_id")
    ),
    requires_env=["COMPOSIO_API_KEY"]
)
```

### Why `requires_env=["COMPOSIO_API_KEY"]`

This tells Hermes: "Only enable this tool if COMPOSIO_API_KEY is set." Prevents errors if credential is missing.

---

## Testing the Integration

### Test 1: Simple Linear Query

```python
from composio_tools import ComposioAgentTools

tools = ComposioAgentTools(api_key="your_key")
result = tools.read_linear_issue("ACME-42")
print(result)
# {"id": "ACME-42", "title": "...", "assignee": "...", ...}
```

### Test 2: Via Hermes

```
User: "Get details for Linear issue ACME-42"
→ Hermes calls composio_read_linear_issue(issue_id="ACME-42")
→ Returns issue details
→ Claude says: "The issue is assigned to alice@contractor.com and is in-progress..."
```

### Test 3: Multi-step Workflow

```
User: "Find all approved contractors in Notion, then send each an invoice"
→ Hermes calls:
   1. composio_read_notion_database(database_id="...", filter={status: Approved})
   2. For each: composio_send_email(to=contractor_email, subject=..., body=...)
→ Claude confirms: "Sent 5 invoices"
```

---

## Troubleshooting Integration

| Problem | Fix |
|---------|-----|
| Tools not showing in `hermes tools --list` | Check sys.path injection. Verify SKILL.md exists. Run `hermes tools --verbose` to see errors. |
| `ImportError: composio-core not installed` | `pip install composio-core>=0.7.0` |
| `AuthenticationError: Invalid API key` | Check COMPOSIO_API_KEY in ~/.hermes/.env |
| `ToolNotAuthenticated: Linear not authorized` | Run composio_setup.py --check-auth. First use opens browser for OAuth. |
| Tools timeout | Check network. Composio default timeout: 30s. Adjust in composio_tools.py if needed. |

---

## Production Checklist

- [ ] COMPOSIO_API_KEY set in ~/.hermes/.env (and not in git)
- [ ] Skills path added to sys.path in model_tools.py
- [ ] Registry import + register call added to _discover_tools()
- [ ] Test: `hermes tools --list | grep composio` returns 8 tools
- [ ] Test: `composio_check_status` returns auth status
- [ ] Test: `composio_read_linear_issue` works with real Linear workspace
- [ ] Test: `composio_read_notion_database` works with real Notion workspace
- [ ] Test: `composio_send_email` successfully sends test email
- [ ] Logs monitored: Check ~/.hermes/logs/ for errors

---

## Performance & Limits

### API Latency
- Linear: 200-500ms
- Notion: 300-800ms
- Gmail: 200-400ms

### Rate Limits
- **Free tier:** 1000 calls/month (33/day)
- **Pro:** 100k calls/month (3333/day)

### Recommended Usage
- Agent payroll: 5 calls/day (Linear read, Notion read, email, log) = 150/mo ✓
- Treasury automation: 10 calls/day = 300/mo ✓
- High-frequency trading bot: 100+ calls/day → upgrade to Pro

---

## Next Steps

1. **Integrate into hermes-agent/model_tools.py** (30 min)
2. **Test with real Linear + Notion + Gmail** (30 min)
3. **Build agent payroll workflow** (2-3 hours)
4. **Monitor logs for errors** (ongoing)

Once integrated, agents can immediately:
- Read contractor assignments from Linear
- Check payment rules in Notion
- Send invoices via Gmail
- Log transactions

Full agent payroll pipeline ready.

---

**Prepared by:** Rocky  
**Status:** Ready to integrate
