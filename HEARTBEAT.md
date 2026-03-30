# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

## Scheduled Routines

### 09:00 — Morning Briefing
- **Trigger:** Daily at 09:00
- **Model:** `google/gemini-2.0-flash-001` via OpenRouter
- **Task:** Compile and send Praneet a daily briefing covering:
  1. Tasks due or relevant today from the Kanban board
  2. Open GitHub issues/PRs assigned to or mentioning Praneet
  3. Unread office mail highlights (subject + sender + urgency)
  4. Personal tasks noted in memory/tasks-personal.md
  5. Calendar meetings for today (time, title, attendees)
- **Format:** Short bullet list per section. Lead with anything time-sensitive.
- **Send via:** Telegram

### 11:00 — News Digest
- **Trigger:** Daily at 11:00
- **Model:** `google/gemini-2.0-flash-001` via OpenRouter (use web search grounding)
- **Task:** Fetch and send a segmented news digest:
  1. **Top World News** — 3–5 stories most relevant to Praneet (tech, geopolitics, startups)
  2. **Crypto / Solana** — top 3 price moves + ecosystem news
  3. **Space News** — 2–3 stories (launches, discoveries, SpaceX, NASA, ESA)
- **Format:** Each section as a header with 2–3 line summaries per story. No fluff.
- **Send via:** Telegram

### 11:15 — Top Tweets + Draft Replies
- **Trigger:** Daily at 11:15 (after news digest)
- **Model:** `anthropic/claude-haiku-4-5` via OpenRouter
- **Task:**
  1. Find top 10 tweets relevant to Praneet (tech, crypto, AI, space, startups)
  2. For each tweet, draft a short reply in Praneet's voice (direct, knowledgeable, no hype)
- **Format:** Numbered list. Each entry: tweet summary → drafted reply.
- **Send via:** Telegram
- **Note:** Drafts only — Praneet reviews and sends manually.
