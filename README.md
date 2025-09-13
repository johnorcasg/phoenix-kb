# Phoenix Knowledge Base (Phoenix-KB)

Phoenix is an **elite inbound call assistant** designed to handle all types of calls — sellers, agents, buyers, lenders, or misc — with precision, empathy, and authority.  

The system is modular:  
- **Main Prompt** → Defines Phoenix’s personality, voice, and high-level behavior.  
- **Knowledge Base (KB)** → A library of specialized playbooks Phoenix consults in real time.  

---

## 📚 Knowledge Modules

### Seller Handling
- **seller_qualification.md** – Core seller flow (ownership, interest, 4 pillars: Condition, Motivation, Timeline, Price).  
- **objections_library.md** – Full catalog of common objections and validated responses.  
- **objection_micro_moves.md** – Bite-sized objection handling tactics (acknowledge → align → pivot).  

### Communication Mastery
- **elite_question_stacking.md** – Advanced question stacking for flow and clarity.  
- **dr_psych_principles.md** – Doctor–Patient style communication framework.  
- **emotional_intelligence.md** – How Phoenix reads and adapts to caller emotions.  
- **rapport_foundations.md** – Building trust, safety, pacing, and validation.  
- **rapport_playbook.md** – Specific scripts for sellers, agents, and lenders.  
- **trust_blueprints.md** – Anchors for building lasting credibility.  

### Prosody & Tonality
- **prosody_precision.md** – Exact pitch, pacing, and pauses per caller type.  
- **prosody_tone_guidance.md** – Direction for tone shifts in questions/statements.  

### Routing & Tagging
- **pro_routing.md** – High-level outcome rules (QUALIFIED_HOT, LONG_TERM, DEAD, OTHER).  
- **routing_cues.md** – Signals that trigger routing (verbal, paraverbal, situational).  

### Buyer/Agent/Lender Handling
- **buyer_intake.md** – Intake questions for buyers (criteria, price, timeline, financing).  

---

## 🛠 Integration

- **phoenix_kb_build.py** – Python script to index all `.md`, `.yml`, and `.json` KB files into `phoenix_index.json`.  
- **tags.yml** – Central tag mapping (`QUALIFIED_HOT`, `LONG_TERM`, `DEAD`, etc.).  
- **responses.md** – Shared acknowledgments and fallback responses.  
- **integration.md** – Guides CRM/webhook integration for routing & tagging.  
- **training_samples.json** – Training call transcripts for Phoenix’s learning loop.  

---

## 🔄 Workflow

1. **Main Prompt** → Creates Phoenix’s personality + high-level handling.  
2. **KB Modules** → Consulted dynamically per call type and tone.  
3. **CRM Tags** → Outcomes logged (`QUALIFIED_HOT`, `LONG_TERM`, `DEAD`, `OTHER`).  
4. **Continuous Training** → Add/edit KB modules as new scenarios emerge.  

---

## 🚀 Usage

- Keep the **main prompt under 2,000 words** — personality only, no heavy flows.  
- Push **all conversation flows, objection handling, scripts, and playbooks** into KB modules.  
- Use `phoenix_kb_build.py` to rebuild the index after every KB update.  
- Phoenix will then act as an **elite inbound agent**, pulling knowledge from the KB to respond naturally, intelligently, and persuasively.  

---

## 📈 Expansion

As testing reveals new needs:  
- Add KB modules (`.md`) for new call types or industries.  
- Append **tags** to `tags.yml` to track more nuanced outcomes.  
- Update `training_samples.json` with real-world calls for calibration.  

Phoenix’s strength = modularity.  
Your prompt defines *who Phoenix is*.  
The KB defines *what Phoenix knows*.  
Together → **.000001% elite inbound assistant**.  
