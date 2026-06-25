# Day 26 — Prior Authorization Workflow Simulator

## Challenge
**Build a Prior Authorization Workflow Simulator** — Learn healthcare workflows through interactive gameplay. Gamified drag-and-drop simulation of the US healthcare PA process.

---

## What Was Built

A fully functional **Prior Authorization Workflow Simulator** — single HTML file, zero dependencies, runs in any browser.

**File:** `pa-workflow-simulator.html`

---

## App Features

### Three Workflow Lanes
| Lane | Actor | Steps |
|------|-------|-------|
| 👤 **Patient** | Patient / Front Desk | Patient Visit, Eligibility Verification |
| 🩺 **Provider** | Clinical Staff / Physician | PA Check, Document Collection, Medical Necessity, Complete Form |
| 🏦 **Payer** | Insurance Staff / MD | Submit, Initial Review, Clinical Review, Decision |

### Four Patient Scenarios

| Scenario | Patient | Service | Complexity | Est. Cost |
|----------|---------|---------|------------|-----------|
| 🦵 Elective Knee Replacement | Sarah Mitchell, 58F | Total Knee Arthroplasty (CPT 27447) | High | $25,000 |
| 🧲 MRI — Lumbar Spine | James Torres, 44M | MRI Lumbar Spine (CPT 72148) | Medium | $1,200 |
| 💊 Biologic Medication | Priya Nair, 35F | Adalimumab/Humira (J0135) | High | $6,200/mo |
| ❤️ Inpatient Cardiac Admission | Robert Chen, 67M | Inpatient Cardiology (DRG 282) | High | $45,000 |

### Gamification Elements
- **Days Elapsed Counter** — each stage costs real-world time (1-5 days)
- **Efficiency Score (0-100%)** — decreases for unnecessary documents, denials, pends
- **Letter Grade (A-F)** — based on final efficiency score
- **Progress Tracker** — horizontal 10-step progress bar at top
- **Three-Lane Sidebar** — visual lane indicator updates in real-time

### Interactive Drag-and-Drop Document Assembly
- Left panel: Available documents (required + decoy documents)
- Right panel: PA Package drop zone
- Required documents checklist with live checkmarks
- Decoy documents add penalty: +1 day, -5% efficiency
- 14 total documents across scenarios (11 legitimate, 3 decoys)

### PA Outcomes (5 possible)
1. **✅ Approved** — Confetti celebration animation
2. **⏳ Pended** → Additional info → **Approved** (with time penalty)
3. **❌ Denied** → Choose response:
   - **Standard Appeal** (15-30 days, ~45% success rate)
   - **Peer-to-Peer Review** (3-7 days, ~68% success rate)
   - **Accept Denial** (process ends)

### Educational Notes
Every stage includes a contextual educational explanation with real-world statistics and best practices. Topics covered:
- Why step therapy documentation matters for biologics
- How penders (Additional Information Requests) work
- InterQual and MCG clinical criteria
- Peer-to-peer review effectiveness
- Patient rights after denial (External Independent Review)
- CMS concurrent review rules for inpatient admission

---

## Key Learnings About Prior Authorization

### 1. PA Affects 41% of All US Healthcare Services
The American Medical Association (AMA) reports that prior authorization requirements have increased 40% since 2015. Patients with delayed PA can experience treatment interruption, adverse clinical outcomes, and care gaps.

### 2. Documentation Quality is the #1 Lever
Missing or incomplete documentation is the cause of 35% of all PA pends. A single missing document (clinical notes, imaging report, treatment history) adds 3-7 business days to the timeline. First-submission completeness has the highest ROI of any PA process improvement.

### 3. Peer-to-Peer Review Has Dramatically Higher Success Rates
When a PA is denied, requesting a physician-to-physician "peer-to-peer" review succeeds ~65-70% of the time vs. ~45% for standard written appeals. The direct conversation allows the treating physician to provide clinical context that written forms can't capture.

### 4. Physicians Spend 14.6 Hours/Week on PA Paperwork
The AMA's 2023 survey found physicians and their staff spend nearly 2 full business days per week on PA-related administrative work. This represents an enormous clinical capacity loss — time spent on forms rather than patient care.

### 5. Inpatient Admissions Use Concurrent Review, Not Pre-Authorization
For urgent/semi-urgent inpatient admissions, providers submit the PA notification within 24-48 hours of admission (concurrent), not before. This is called "concurrent review" and differs significantly from elective procedure pre-authorization. Retroactive review (requesting PA after discharge) carries the highest denial risk.

### 6. Biologic Medications Have the Most Complex PA Requirements
Step therapy requirements (fail 2 conventional DMARDs before biologic approval), formulary tier rules, and specialty pharmacy routing make biologic medication PAs the most documentation-intensive category. First-submission denial rates can reach 25-30%, but peer-to-peer review resolves most of these.

---

## Completed Workflow — Sample Run

**Scenario:** Biologic Medication (Priya Nair, Adalimumab for RA)

| Stage | Actor | Days |
|-------|-------|------|
| Patient Visit | Patient / Provider | +1 day |
| Eligibility Verification | Front Desk Staff | +1 day |
| PA Required Check | Insurance Coordinator | +0 days |
| Document Assembly | Clinical Staff | +2 days (+1 decoy penalty) |
| Medical Necessity | Treating Physician | +1 day |
| Complete PA Form | Insurance Coordinator | +1 day |
| Submit to Payer | Provider → Payer | +1 day |
| Initial Review | Payer Staff | +2 days |
| Medical Necessity Review | Clinical Reviewer MD | +5 days |
| Decision | Medical Director | +1 day |
| **Initial Outcome:** | | **❌ DENIED** |
| Peer-to-Peer Review | Treating MD + Payer MD | +5 days |
| **Final Outcome:** | | **✅ APPROVED** |
| **Total Days:** | | **21 days** |
| **Efficiency Score:** | | **72% (Grade: B)** |

---

## Technical Notes
- **Single HTML file** — zero dependencies, no CDN, no backend
- **Drag-and-drop** — HTML5 native `draggable` + `dragover`/`drop` events
- **State management** — pure JavaScript object (no localStorage per spec)
- **Weighted random outcomes** — scenario-specific probability weights (approve/pend/deny)
- **Confetti** — pure JS particle system (same approach as Day 25)
- **Educational content** — 4 scenarios × 10 stages × unique notes = 40+ educational callouts
- **Scenario data** — stored in editable `SCENARIOS` array near top of file for easy customization

---

## Deliverables
- `pa-workflow-simulator.html` — Complete interactive PA workflow simulator
- `pa-card.png` — Cinematic Day 26 card (blue medical theme)
- `app-welcome.png` — App welcome screen screenshot
- `day-26.md` — This file

---

*Day 26 of 60 · Built with Claude AI · #60DaysOfAI*
