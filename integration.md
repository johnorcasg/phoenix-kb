# Phoenix - Integration Guide

This document explains how Phoenix connects the **main prompt**, **knowledge base (KB)**, and **CRM tags/stages** for smooth inbound call handling.

---

## 🔗 System Architecture

1. **Main Prompt**
   - Defines Phoenix’s **identity, tone, and personality**.
   - Handles **general rules** (never admit AI, natural phone pacing, empathy first).
   - Delegates specialized flows to the KB instead of hardcoding them.

2. **Knowledge Base (KB)**
   - Repository of `.md` files stored in GitHub and crawled into Phoenix.
   - Each file covers one domain (e.g., seller qualification, agent handling, objection handling, wrong number, emotional de-escalation).
   - Phoenix always consults KB for detailed flows, scripts, and specialized responses.

3. **Tags & Routing**
   - Controlled by `tags.yml`.
   - Ensures outcomes are **consistent and CRM-ready**:
     - `QUALIFIED_HOT` → HOT stage
     - `LONG_TERM` → Nurture stage
     - `DEAD` → Closed
     - `WRONG_CONTACT` → Removed
     - `OTHER` → Misc capture

4. **CRM Sync**
   - Phoenix writes tags/stages directly into CRM fields via webhook or API.
   - Example mapping:
     - `{{contact.stage}}` → CRM Pipeline Stage
     - `{{contact.tag}}` → CRM Tag
     - `{{contact.last_mode}}` → Detected emotional mode
     - `{{contact.mode_confidence}}` → Confidence score for mode detection

---

## ⚙️ Call Handling Flow

1. **Open Call**
   - Phoenix greets naturally.
   - Identifies caller type (seller, agent, lender, misc) → consults KB.

2. **Use Knowledge Base**
   - If seller: run ownership + selling interest + qualification flow (via KB).
   - If agent/lender: run alternate KB script.
   - If misc/wrong number: route to KB handling and apply tags.

3. **Tag & Route**
   - Applies tags from `tags.yml`.
   - Updates CRM with stage + tag.
   - Logs detected emotional mode and confidence.

4. **Close Out**
   - Ends call with **gratitude** and **next steps** (KB-driven phrasing).
   - Example: *“Appreciate your time today. You’ll hear from us soon with next steps.”*

---

## 🛠 Technical Notes

- **Knowledge Base Crawler**
  - Make sure GitHub repo with `.md`, `.yml`, `.json` files is public or accessible by the crawler.
  - Organize by folder: `kb/seller_qualification.md`, `kb/agent_handling.md`, etc.

- **Webhook/CRM Integration**
  - Confirm mapping:
    - Tags → `{{contact.tags}}`
    - Stage → `{{contact.stage}}`
    - Notes → `{{contact.notes}}`
  - Ensure Phoenix writes data after call end.

- **Logging**
  - Phoenix logs emotional mode, tags, and routing decisions.
  - Stored in: `{{contact.last_mode}}` and `{{contact.mode_confidence}}`.

---

## ✅ Best Practices

- Keep the **main prompt** focused on identity & personality.
- Push **flows and scripts** into KB files — easier to scale and update.
- Use **tags.yml** as the single source of truth for CRM outcomes.
- Test with **training samples.json** to validate Phoenix handles each caller type.
- Regularly refine KB content with real call data and objections.

---
