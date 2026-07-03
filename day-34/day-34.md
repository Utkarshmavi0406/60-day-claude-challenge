# Day 34 — Marketing Detective

## Challenge
**Build a Marketing Detective Game** — Solve marketing mysteries through interactive investigation. Analyze campaign evidence, identify the fatal mistake, and close the case. Detective game aesthetic with corkboard, sticky notes, push pins, and folder-style case files.

---

## What Was Built

A complete **Marketing Detective Game** — single HTML file, pure vanilla JavaScript and CSS. 10 fully detailed fictional marketing cases, randomized each replay. Detective aesthetic with draggable evidence cards, animated metric bars, clue reveal system, Case Closed animation, and Learning Report.

**File:** `marketing-detective.html`

---

## 5 Detective Themes
- 🟠 **Claude Orange** — Signature
- 🟡 **Detective Gold** — Classic
- 🔵 **Midnight Blue** — Forensic
- 🟢 **Field Agent** — Covert
- 🔴 **Crime Scene** — Intense

---

## Game Flow (6 Screens)

### 1. Theme Selection
Colorful theme cards with gradient preview swatches. Click to select and immediately proceed to the case.

### 2. Case Assignment
Manila folder-style case file reveal with:
- "CONFIDENTIAL" stamp (rotated, red border)
- Case ID in detective style
- Company name in Georgia serif
- Objective, Target Audience, Channels, Budget

### 3. Investigation Board (Core Screen)
**Corkboard aesthetic** with dark brown background and subtle radial gradient texture.

**4 Evidence Cards** (draggable, cream/paper colored, push-pinned):
- 📊 Campaign Metrics (animated progress bars, color-coded by performance)
- 💬 Customer Feedback (3 direct quotes from real-sounding customers)
- 💰 Budget Allocation (animated bar chart visualization)
- 📱 Social Performance (platform-by-platform breakdown)

**Key Evidence Pin Board** — drag any evidence card here to "pin" it with a push pin animation.

**3 Clue Cards** — Locked initially (grey, with lock icons). Reveal one at a time by clicking "Reveal Next Clue." Each reveals with a card-in animation. Once all 3 revealed, "Solve the Case" button unlocks.

### 4. Solve the Case
Four shuffled options (one correct, three distractors). Options styled as detective note cards. Submit activates after selection.

### 5. Case Closed Animation
- Stamp animation (scales from 2x to 1x with rotation) — green for correct, red for incorrect
- "CASE CLOSED" or "CASE REOPENED"
- Verdict text explaining correct answer

### 6. Learning Report
- Primary mistake identified
- Full explanation of why it happened
- 3 numbered improvement suggestions
- Marketing lesson quote
- Full clue evidence summary
- "Next Case" → new random case

---

## 10 Marketing Cases

| Case | Company | Industry | Primary Mistake |
|------|---------|----------|----------------|
| MKT-001 | FreshBrew Coffee | Food & Beverage | Platform-Audience Mismatch (TikTok for professionals) |
| MKT-002 | TechLeap Pro | B2B SaaS | B2B Brand on Consumer Social Channels |
| MKT-003 | StyleHaven Fashion | E-commerce | Over-Investment in Acquisition vs Retention |
| MKT-004 | GreenLeaf Organics | Health & Wellness | Influencer-Audience Mismatch |
| MKT-005 | PulseCity Gym | Fitness | Campaign Launched After Purchase Decision Already Made |
| MKT-006 | LuxeNest Interiors | Luxury Services | Wrong Platform for High-Trust Purchase |
| MKT-007 | CloudSuite Analytics | Data SaaS | Acquisition Marketing for Retention Problem |
| MKT-008 | ArtisanBite Restaurant | Food Service | Local Business in Non-Local Channels |
| MKT-009 | VoyageVault Travel | Travel Agency | Wrong Product Advertised to Wrong Segment |
| MKT-010 | QuickHire Staffing | HR Tech | Marketing to Non-Paying Users Instead of Buyers |

---

## Case Data Structure (Per Case)
Each case includes:
- Company Name, Industry, Tagline
- Campaign Objective, Target Audience, Channels, Budget
- **5 Campaign Metrics** with animated bar visualization (poor/warning/good status)
- **3 Customer Comment Quotes** (realistic, revealing)
- **2-Platform Social Stats** (with key revealing numbers)
- **3 Investigation Clues** (locked, revealed sequentially)
- **1 Primary Mistake** (the correct answer)
- **4 Options** (shuffled each game — 1 correct, 3 plausible distractors)
- **Full Explanation** of why the mistake happened
- **3 Specific Improvements** with actionable detail
- **1 Marketing Lesson** (the core principle)

---

## Design System: Detective Aesthetic
- **Background:** #08090e (near-black)
- **Corkboard:** #2c1a06 with radial gradient texture
- **Evidence cards:** #f5f0e8 (cream/paper) with 2px rotate and dark drop shadow
- **Push pins:** CSS radial-gradient circles with glow effect
- **Folder:** Linear-gradient from #c8954a to #a57328 (manila)
- **Clue cards:** #fef3c7 (yellow sticky note) with rotation variations
- **Stamps:** Border + color + rotation CSS
- **Typography:** Georgia serif for case content, Courier New for evidence

---

## My Investigation: Case MKT-001

**FreshBrew Coffee Co.** — Premium cold brew launch

**Evidence found:**
- TikTok campaign: 1.4M views, average viewer age: 17 (target was 25-35 professionals)
- CTR: 0.3% vs industry average 0.9%
- 2.1M reach → 189 conversions → $254 per conversion
- Competitor achieved 2.4% conversion on LinkedIn with 1/5 the budget

**Clue that cracked the case:** Competitor Intelligence — LinkedIn achieved 15x better results at 1/5 the cost. This made the platform mismatch undeniable.

**Verdict:** CASE CLOSED ✅

**Primary Mistake:** Platform-Audience Mismatch

**Marketing Lesson:** Platform selection must follow where YOUR specific audience spends their attention — not where the largest total audience exists. Platform popularity and platform fit are completely different things.

---

## Key Learnings

### 1. The Gap Between Reach and Conversion Is the Most Revealing Metric
Every single case in the simulator showed that high reach + low conversion = wrong audience. The FreshBrew case had 2.1M reach and 0.09% conversion. The LuxeNest case had 4.2M views and zero clients. When reach is high and conversion is near-zero, you're reaching the wrong people — not making bad creative.

### 2. The Leaky Bucket Problem Is More Common Than Anyone Admits
The CloudSuite Analytics case was the most counterintuitive: they tried to fix an 8% monthly churn rate by running $95K in new customer acquisition campaigns. They added 420 customers while 391 churned. Net gain: 29 customers at $3,276 each. The right fix was onboarding completion — users who completed onboarding had 1.2% churn; those who didn't had 11.4%. This is a principle most SaaS companies ignore: marketing cannot fix product problems.

### 3. Timing Is as Important as Channel
The PulseCity Gym case revealed something critical: consumers make gym membership decisions in November-December, not January. By launching the entire campaign on January 1st, PulseCity missed 67% of their audience's decision window. Their competitors who started in December captured memberships before PulseCity even started advertising. The "New Year gym surge" is actually a pre-New Year decision pattern.

### 4. The Side of the Marketplace That Pays Determines Your Marketing Strategy
The QuickHire case was the clearest example of audience confusion: they marketed to job seekers (free users) instead of HR managers (paying customers). Their 3 unpaid LinkedIn posts targeting HR ROI metrics generated 5 of their 7 employer clients, while $54K in paid job seeker campaigns generated 2. If you have a two-sided marketplace, always market to the side that writes the check.

### 5. Your Own Data Always Knows the Answer
The VoyageVault Travel case had all the evidence: 71% of their database booked family vacations, 68% of site visitors searched family packages, family ROAS was 4.1x vs adventure ROAS of 0.6x. Yet they allocated 75% of their budget to adventure travel. The data was never the problem — the problem was marketing what they wanted to sell rather than what their data proved customers wanted to buy.

---

## Deliverables
- `marketing-detective.html` — Complete interactive marketing game
- `detective-card.png` — Cinematic Day 34 card (amber detective theme)
- `day-34.md` — This file

---

*Day 34 of 60 · Built with Claude AI · #60DaysOfAI*
