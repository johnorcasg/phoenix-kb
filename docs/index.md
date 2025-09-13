---
title: Phoenix Knowledge Base
description: Public index for Phoenix-KB (crawler-friendly)
---

# Phoenix-KB

This site lists public KB documents for the Phoenix call agent.  
Each link points to an HTML-renderable page (recommended for web crawlers).

## Core
- [README](./README.md)
- [Agent Handling](./agent_handling.md)
- [Responses](./responses.md)
- [Seller Qualification](./seller_qualification.md)
- [Routing Cues](./routing_cues.md)
- [Pro Routing](./pro_routing.md)

## Communication & Psychology
- [Rapport Foundations](./rapport_foundations.md)
- [Rapport Playbook](./rapport_playbook.md)
- [Trust Blueprints](./trust_blueprints.md)
- [Prosody Precision](./prosody_precision.md)
- [Prosody Tone Guidance](./prosody_tone_guidance.md)
- [Emotional Intelligence](./emotional_intelligence.md)
- [Objection Micro-Moves](./objection_micro_moves.md)
- [Objections Library](./objections_library.md)
- [Elite Question Stacking](./elite_question_stacking.md)
- [Buyer Intake (DR Psych Principles)](./buyer_intake_dr_psych_principles.md)

## Data & Config (human-readable mirrors)
- [Tags (mirror of tags.yml)](./tags.md)
- [Training Samples (mirror of training_samples.json)](./training_samples.md)

---

**Notes**
- `.yml` and `.json` often aren’t “HTML” so some crawlers refuse them. That’s why we also include human-readable **mirrors** (`tags.md`, `training_samples.md`). Keep mirrors in sync when you update the source files.
- For raw programmatic access you can still use:  
  - `https://raw.githubusercontent.com/johnorcasg/phoenix-kb/main/docs/tags.yml`  
  - `https://raw.githubusercontent.com/johnorcasg/phoenix-kb/main/docs/training_samples.json`
