# Phoenix V1 — Metrics & Definitions

**Purpose:** Track compounding progress using a tiny set of signals that actually move deals.

## Core KPIs (report daily during the 10-day sprint)

1) **OwnerVerifiedRate (OVR)**  
   - **Definition:** `owner_verified / total_contacts`  
   - **Target:** ≥ **35%** on first 200-contact batch  
   - **Why:** Without owner verification, nothing compounds.

2) **PillarCapture3of4 (PC34)**  
   - **Definition:** `contacts_with_≥3_pillars / owner_verified`  
   - **Target:** ≥ **60%** (Motivation + Condition are mandatory)  
   - **Why:** Booking quality hinges on M+C captured.

3) **AppointmentSetRate (ASR)**  
   - **Definition:** `appointments / owner_verified`  
   - **Target:** ≥ **7%** initial; improve via micro-moves  
   - **Why:** This is the money stat.

4) **TimeToQualifiedConversation (TTQC)**  
   - **Definition:** Median minutes from first reply to **≥3 pillars** captured  
   - **Target:** Down-trend over the sprint  
   - **Why:** Speed to signal correlates with close probability.

## Secondary Diagnostics (use only if stuck)
- **MisrouteRate** = (agent+buyer+wrong) / total_contacts  
- **NurtureLoopExitRate** = nurture_exits / nurture_entries  
- **ObjectionRedirectSuccess** = returns_to_flow / objections

## Measurement Rules
- Freeze prompts per sprint; measure before changing.  
- Post metrics nightly with **numerator/denominator** and **1-line cause** if off-target.  
- Change one thing at a time; re-measure next day.
