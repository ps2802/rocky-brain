# Moongate Intercom Outbound Message Audit

**Date:** March 29–30, 2026  
**Workspace:** degen@moongate.one  
**Scope:** Banner and survey messages sent last week (March 22–28, 2026)

---

## Status

⚠️ **BLOCKER:** Cannot access Intercom workspace without credentials or API key. This audit requires either:
1. Manual login to https://app.intercom.com (degen@moongate.one) + export of outbound messages
2. Intercom API key (not present in ~/.hermes/.env)

**Next step:** Provide either (1) access to the workspace or (2) an Intercom API token with `messages:read` scope.

---

## Audit Template (To Be Populated)

Once access is available, populate this template for each message:

### Message 1: [Banner/Survey Name]

**Current Version:**

| Field | Value |
|-------|-------|
| Message Type | Banner / Survey |
| Sent Date | [YYYY-MM-DD] |
| Sent Count | [Number] |
| Open Rate | [%] |
| Click Rate | [%] |
| Copy | [Full text] |
| Audience Filters | [List of rules] |

**Diagnosis:**

**Copy Grade:** [ ] A (Clear, specific, earns attention) / [ ] B (Good) / [ ] C (Acceptable) / [ ] D (Weak)

**Copy Feedback:**
- [Strengths]
- [Weaknesses]
- [Suggestions for improvement]

**Audience Targeting Grade:** [ ] A (Precise, no exclusions) / [ ] B (Good) / [ ] C (Acceptable) / [ ] D (Too narrow/broad)

**Audience Targeting Feedback:**
- [Current rules: clear/too restrictive/missing segments]
- [Suggestions for reach optimization]

---

**Improved Version:**

**Rewritten Copy:**
> [Proposed new message]

**Rewritten Audience Rules:**
- [Revised filters to maximize reach without losing relevance]

**Expected Impact:**
- Estimated reach increase: [%]
- Expected engagement lift: [%]

---

## Summary (To Be Completed)

| Message | Current Open Rate | Projected Open Rate | Reach Increase | Status |
|---------|-------------------|-------------------|-----------------|--------|
| [Message 1] | [%] | [%] | [%] | Pending |
| [Message 2] | [%] | [%] | [%] | Pending |

---

## How to Proceed

1. **Access the workspace:** Log in to https://app.intercom.com (degen@moongate.one)
2. **Navigate to:** Messages → Outbound → Filter by sent date last week
3. **For each banner/survey:**
   - Copy the full message text
   - Screenshot or list the audience rules
   - Note the sent count and engagement metrics (if visible in UI)
   - Paste into the template above
4. **Grade and rewrite** using the criteria in the template
5. **Return to Rocky** with completed audit

**Estimated time:** 20–30 minutes depending on message count and complexity of rules.

---

**Prepared by:** Rocky (Praneet's Chief-of-Staff AI)  
**Note:** This audit is designed to maximize engagement on outbound messages by separating copy quality from audience targeting. Often one is strong and the other is weak — fixing both doubles the impact.
