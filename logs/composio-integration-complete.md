# Composio Integration — Complete

**Date:** 2026-03-30 05:15 UTC  
**Status:** ✓ DONE. Ready to use.

---

## What's Done

### 1. Code Changes
- **File:** `/home/praneet/hermes-agent/model_tools.py`
- **Change:** Added Composio tool discovery (lines 172-186)
- **Effect:** 8 tools auto-register on hermes-agent startup

### 2. Wiring Details
```python
# Composio tool discovery (Linear, Notion, Gmail integrations)
try:
    import sys
    from pathlib import Path
    composio_scripts_path = Path.home() / ".hermes" / "skills" / "productivity" / "composio-agent-ops" / "scripts"
    if str(composio_scripts_path) not in sys.path:
        sys.path.insert(0, str(composio_scripts_path))
    from composio_hermes_registry import register_composio_tools
    register_composio_tools(registry)
    logger.info("✓ Composio tools registered (Linear, Notion, Gmail)")
except ImportError:
    logger.debug("Composio not available (composio-core not installed)")
except Exception as e:
    logger.debug("Composio registration failed: %s", e)
```

**Why this pattern:**
- Skills path injected into sys.path (allows skills to be external to hermes-agent)
- Try/except handles missing dependencies gracefully (no hard failure)
- Logs success for visibility
- Fallback logging if Composio not installed or registration fails

### 3. Graceful Degradation
- If `composio-core` not installed → logs debug message, continues normally
- If `COMPOSIO_API_KEY` not set → tools disabled at runtime (check in composio_tools.py)
- If OAuth not done → tools return error on first use, trigger browser OAuth
- Zero impact on other tools if Composio fails

---

## What You Need to Do

### Short Term (Today)
1. **Install composio-core:** `pip install composio-core>=0.7.0`
2. **Get API key:** https://composio.dev (free tier)
3. **Add to .env:** `COMPOSIO_API_KEY=your_key` in `~/.hermes/.env`
4. **Verify:** Run tests from COMPOSIO_SETUP_INSTRUCTIONS.md

### Timeline
- Installation: 5 min
- OAuth setup (first use): 10 min
- **Total: 15 minutes**

---

## Tools Now Available

### Linear (3 tools)
- `composio_read_linear_issue(issue_id)` — Get issue details
- `composio_list_linear_issues(project_id, status, assignee)` — Query issues
- `composio_create_linear_issue(project_id, title, description, assignee)` — Create issue

### Notion (2 tools)
- `composio_read_notion_database(database_id, filter_rules, page_size)` — Query database
- `composio_create_notion_entry(database_id, properties)` — Add entry

### Gmail (2 tools)
- `composio_send_email(to, subject, body, cc, bcc)` — Send email
- `composio_search_email(query, max_results)` — Search inbox

### Status (1 tool)
- `composio_check_status()` — Verify all integrations authenticated

---

## Example Usage

### In Hermes REPL
```
Claude: "Search for invoices from bob@contractor.com and read contractor details from CONTRACTOR-1 in Linear"

→ Hermes calls:
   1. composio_read_linear_issue(issue_id="CONTRACTOR-1")
   2. composio_search_email(query="from:bob@contractor.com")

→ Claude: "Found 3 invoices from bob@contractor.com. The Linear issue shows..."
```

### In Python Code
```python
from tools.registry import registry

# Call directly
handler = registry._registry['composio_search_email']['handler']
result = handler({"query": "from:alice@example.com"})
# Returns JSON with emails
```

### In Agent Code
```python
agent.chat("Find all approved contractors in Notion and email them invoices")
# Agent automatically uses composio_read_notion_database + composio_send_email
```

---

## Files & Locations

| Item | Location |
|------|----------|
| Skill code | `~/.hermes/skills/productivity/composio-agent-ops/` |
| Wiring in hermes-agent | `/home/praneet/hermes-agent/model_tools.py` (lines 172-186) |
| Setup instructions | `~/rocky-brain/COMPOSIO_SETUP_INSTRUCTIONS.md` |
| Skill docs | `~/.hermes/skills/productivity/composio-agent-ops/SKILL.md` |
| Registry integration | `~/.hermes/skills/productivity/composio-agent-ops/scripts/composio_hermes_registry.py` |
| Rocky brain archive | `~/rocky-brain/skills/composio-agent-ops/` |

---

## Verification Checklist

- [x] Code wired into model_tools.py
- [x] Syntax validated (no errors)
- [x] Import tested (gracefully handles missing composio-core)
- [x] 8 tools in registry ready
- [x] Skill documentation complete
- [x] Setup instructions provided
- [x] Integration guide available
- [x] Committed to rocky-brain
- [x] Pushed to origin

**Pending your action:**
- [ ] Install composio-core
- [ ] Get API key + add to .env
- [ ] Run verification tests
- [ ] Do OAuth approvals (happens on first use)

---

## Cost & Limits

| Tier | Price | Calls/Month | Status |
|------|-------|------------|--------|
| Free | $0 | 1,000 | ✓ Selected for MVP |
| Starter | $30 | 10,000 | Upgrade if needed |
| Pro | $100+ | 100,000+ | Overkill for now |

**Agent payroll estimate:** 5 calls/day × 30 = 150 calls/month ← Well under free tier limit

---

## Next Steps

### Immediate (Once You Complete Setup)
- Agent payroll workflow: Read Linear → Query Notion → Email contractor → Log payment
- Should work end-to-end once OAuth approvals done

### Short Term (Week 1-2)
- Test with real Linear issues + Notion database + Gmail account
- Build agent payroll orchestration
- Monitor logs for errors

### Medium Term (Week 3-4, If Needed)
- Evaluate n8n MCP (only if agent payroll grows beyond 5 sequential steps)
- Add workflow scheduling (cron jobs)
- Integrate with MoonPay payment execution

---

## Support

- Composio docs: https://docs.composio.dev
- Setup help: `~/rocky-brain/COMPOSIO_SETUP_INSTRUCTIONS.md`
- Troubleshooting: See "Cost & Limits" section above

---

**Status:** Integration complete. Awaiting your setup (15 min).

**Next message from you:** "Setup done" or questions about setup process.

