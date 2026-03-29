# Composio Setup Instructions

**Status:** ✓ Composio skill wired into hermes-agent/model_tools.py

Now complete these steps to activate it.

---

## Step 1: Install composio-core

```bash
pip install composio-core>=0.7.0
```

Verify:
```bash
python3 -c "import composio; print(f'✓ composio-core {composio.__version__}')"
```

---

## Step 2: Get Composio API Key

1. Go to https://composio.dev
2. Sign up (free tier included)
3. Copy your API key

---

## Step 3: Add to ~/.hermes/.env

```bash
echo "COMPOSIO_API_KEY=your_key_here" >> ~/.hermes/.env
```

Replace `your_key_here` with the actual key from Step 2.

**Verify:**
```bash
grep COMPOSIO ~/.hermes/.env
```

---

## Step 4: Verify Registration

```bash
cd ~/hermes-agent
source venv/bin/activate
python3 << 'EOF'
import model_tools
from tools.registry import registry

# Check if Composio tools are registered
composio_tools = [name for name in registry._registry.keys() if 'composio' in name]
print(f"✓ {len(composio_tools)} Composio tools registered:")
for tool in sorted(composio_tools):
    print(f"  - {tool}")
EOF
```

**Expected output:**
```
✓ 8 Composio tools registered:
  - composio_check_status
  - composio_create_linear_issue
  - composio_create_notion_entry
  - composio_read_linear_issue
  - composio_list_linear_issues
  - composio_read_notion_database
  - composio_search_email
  - composio_send_email
```

---

## Step 5: Test OAuth Setup

```bash
cd ~/hermes-agent
python3 << 'EOF'
from tools.registry import registry
import json

# Call the check_status tool
handler = registry._registry['composio_check_status']['handler']
result = handler({})
print(json.dumps(json.loads(result), indent=2))
EOF
```

**Expected output (first run):**
```json
{
  "composio": "connected",
  "linear": "not_authenticated",
  "notion": "not_authenticated",
  "gmail": "not_authenticated"
}
```

**If integrations not authenticated:**
- First use of each integration (Linear, Notion, Gmail) will open a browser for OAuth
- Approve the permission request
- Credentials cached locally in `~/.composio/`
- Subsequent uses are instant (no auth needed)

---

## Step 6: Test a Real Operation

```bash
hermes
> composio_check_status
```

Then try a search:

```bash
> composio_search_email query="from:example@gmail.com"
```

**Note:** This will fail if Gmail isn't authenticated. If it fails:
1. Run `composio_check_status` (opens browser for Gmail OAuth)
2. Approve
3. Try again

---

## Complete Workflow Test

Once all integrations are authenticated, test the full agent payroll workflow:

```bash
hermes
> 
> Linear issue CONTRACTOR-1 says the contractor is assigned to alice@example.com.
> Search for invoices from alice@example.com in Gmail.
> Then log a payment of 500 USDC to the Notion payments database.
```

Claude should:
1. Read Linear issue
2. Extract contractor email
3. Search Gmail for invoices
4. Create Notion entry
5. Report results

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: No module named 'composio'` | Install: `pip install composio-core>=0.7.0` |
| `AuthenticationError: Invalid API key` | Check COMPOSIO_API_KEY in ~/.hermes/.env is correct |
| `ToolNotAuthenticated: Linear not authorized` | Run composio_check_status to trigger OAuth |
| Tools not showing in `hermes tools --list` | Verify COMPOSIO_API_KEY set. Restart hermes. Check logs. |
| `TimeoutError` | Check network. Composio timeout is 30s by default. |

---

## What's Installed

**Hermes-Agent Side:**
- ✓ model_tools.py patched to register Composio tools
- ✓ 8 tools ready (Linear 3, Notion 2, Gmail 2, Status 1)

**Your Side:**
- [ ] composio-core package
- [ ] COMPOSIO_API_KEY in ~/.hermes/.env
- [ ] OAuth approvals (happens on first use)

---

## Next Steps

Once complete, agents can:
- Read Linear issues (contractor assignments)
- Query Notion databases (payment rules, approved contractors)
- Send Gmail (invoices, reports, notifications)
- Search Gmail (find invoices, track communications)

Perfect for agent payroll infrastructure.

---

**Timeline:**
- Step 1-3: 5 minutes
- Step 4-6: 10 minutes (includes OAuth browser approvals)
- Total: ~15 minutes

Ready to go?
