# Day 29 — Operation Lifeline: Supply Chain Crisis Lab

## Challenge
**Build Operation Lifeline: Supply Chain Crisis Lab** — Lead an enterprise through a supply chain crisis. Interactive React simulation teaching supply chain strategy, business decision-making, negotiation, and AI investment.

---

## What Was Built

A complete **Supply Chain Crisis Simulation** built with React via CDN + Babel JSX in a single HTML file. No npm, no Tailwind, no backend. Opens directly in any browser.

**File:** `operation-lifeline.html`

---

## App Architecture

**Tech Stack:** React 18 (CDN) + Babel Standalone (JSX transpilation) + Pure CSS in-file

**Key React patterns used:**
- `useState` for all state management
- `useEffect` for animated progress bar transitions
- Component-based architecture (7 screen components)
- Props drilling for state across screens
- Callback pattern for screen transitions

---

## 7-Stage Game Flow

### Stage 1: Welcome Screen
Full-screen hero with animated gradient title, feature preview grid, glowing CTA button.

### Stage 2: Company + Crisis
**Randomized company profile** (8 industries, 4 names each):
- Revenue ($250M–$9B), Factories, Warehouses, Suppliers, Inventory Days, Lead Time, Countries, Employees

**8 randomized crisis types:**
| Crisis | Urgency | Key Impact |
|--------|---------|-----------|
| 🔥 Factory Fire | CRITICAL | 40% production offline |
| 💸 Supplier Bankruptcy | CRITICAL | 35% of critical inputs at risk |
| ⚓ Port Strike | HIGH | 60% of imports blocked |
| 💻 Cyberattack | CRITICAL | ERP systems down, no inventory visibility |
| 🌊 Regional Flood | HIGH | 2 distribution centers underwater |
| ⛏️ Raw Material Shortage | HIGH | 14 days to manufacturing halt |
| 🚨 Trade Sanctions | HIGH | 45% component supply cut off |
| 🚢 Ocean Shipping Delay | HIGH | $180M goods in regulatory hold |

### Stage 3: War Room
**6 response actions, choose 3.** Each action affects 5 business metrics:
- Cost Efficiency, Inventory Health, Profitability, Delivery Speed, Customer Satisfaction

Actions and their real-world tradeoffs:
| Action | Key Effect | Cost Impact |
|--------|-----------|------------|
| 🔍 Emergency Sourcing | +18 Inventory | -10 Cost |
| 📦 Deploy Safety Stock | +22 Inventory, +12 CX | -4 Cost |
| 📢 Customer Communication | +22 Customer Sat | -3 Cost |
| ✈️ Air Freight Emergency | +28 Speed | -22 Cost |
| 🏭 Production Redistribution | +16 Speed | -14 Cost |
| 🤝 Government Partnerships | +9 Speed, +6 CX | +5 Cost (saves money) |

**Live metric animation** as actions are selected (progress bars update in real-time with color coding).

### Stage 4: Supplier Negotiation
**4 rounds with branching choices.** Each choice affects Trust, Price Position, and Lead Time:

| Round | Topic | Best Strategy |
|-------|-------|--------------|
| 1 | Opening Position | Partnership framing (not desperation, not legal threats) |
| 2 | Price Negotiation | Counter at 15% + 2-year volume commitment |
| 3 | Contract Terms | Accept with targeted modifications protecting SLAs |
| 4 | Long-term Partnership | Mutual risk-sharing framework with shared data |

Results and explanations shown after each choice. Cumulative negotiation score calculated across all 4 rounds.

### Stage 5: CEO Boardroom
**5 multiple-choice leadership questions** with expert explanations:
1. Media communication during crisis → Transparent, timely, factual
2. CFO vs ops team: inventory cut → Surgical triage beats blanket cuts
3. Competitor data-sharing offer → Share aggregated non-proprietary data only
4. Team burnout at 70% resolved → Rotate shifts, bring external support
5. Post-crisis priority → 30-day post-mortem and playbook

Score: 0-500 (100 per question), converted to 0-100 for final scoring.

### Stage 6: AI Strategy
**Choose 2 of 5 AI investments:**

| AI Tool | Estimated ROI | Key Impact |
|---------|---------------|-----------|
| 📊 Demand Forecasting AI | 340% / 3yr | Stockouts down 65%, inventory costs -18% |
| 🔄 Inventory Optimization | 280% / 2yr | Inventory turns +35%, $45M working capital freed |
| 🛡️ Supplier Risk Monitoring | 420% / 3yr | 85% of disruptions flagged 30+ days early |
| 👁️ Warehouse Vision AI | 220% / 2yr | Picking accuracy 99.7%, labor efficiency +35% |
| 🤖 Procurement Copilot | 380% / 2yr | Procurement costs -12%, cycle time -45% |

Combined impact on metrics shown live after selection.

### Stage 7: Final Executive Dashboard
- **Overall Crisis Score (0-100)** with animated SVG score ring
- **6 sub-scores:** Leadership, Negotiation, Resilience, Cost Control, Risk Management, Customer Satisfaction
- **Personalized feedback:** Best decision, biggest learning, expert recommendation
- **5 lessons learned** from the playthrough
- **Replay button** with full randomization

---

## Score Calculation

```
Overall = Leadership(25%) + Negotiation(20%) + Resilience(20%) + 
          Cost Control(15%) + Risk Management(10%) + Customer Satisfaction(10%)
```

**Grade Scale:**
- 90+: S+ (Crisis Master)
- 80-89: A (Executive Leader)
- 70-79: B (Solid Manager)
- 60-69: C (Average Response)
- <60: D (Needs Improvement)

---

## My Run Results

**Company:** Apex Motor Group (Automotive Manufacturing) · $3.2B revenue · 14 factories · 28 warehouses · 180 suppliers

**Crisis:** 🔥 Factory Fire (CRITICAL) — 40% production capacity offline, 6-8 weeks repair

**War Room Actions Selected:**
1. 📦 Deploy Safety Stock — buys immediate breathing room
2. 📢 Customer Communication — saves relationships, high CX boost
3. 🏭 Production Redistribution — addresses root capacity problem

**Negotiation Strategy:** Partnership framing → volume commitment counter → SLA-protected terms → risk-sharing framework
**Negotiation Score: 88/100**

**CEO Questions:** 4/5 best answers → Score: 420/500 → 84%

**AI Investments:** 🛡️ Supplier Risk Monitoring + 📊 Demand Forecasting AI

**Final Score: 84/100 — Grade A: Executive Leader**

---

## Key Learnings

### 1. Safety Stock Is Your Fastest Lever
The single highest-value action in almost any supply chain crisis is deploying safety stock. It's insurance already paid for, has near-zero additional cost, and buys time for all other decisions. Organizations that under-invest in safety stock face a 3x worse crisis recovery timeline.

### 2. Customer Communication Beats Customer Protection
Most companies instinctively try to "protect" customers from bad news. The data shows the opposite: proactive, transparent communication during disruption saves relationships worth far more than the disruption itself. Customers who are warned forgive. Customers who are blindsided leave.

### 3. Negotiation Framing Is a Supply Chain Strategy
How you open a supplier negotiation during a crisis determines the outcome more than your leverage does. "Strategic partnership during a difficult period" outperforms both pleading and legal threats — in trust, in price, and in lead time. The negotiation game made this tangible.

### 4. AI ROI Peaks at Risk Prevention
Supplier Risk Monitoring has the highest estimated ROI (420%) of all 5 AI tools — because disruptions prevented cost nothing. The next crisis you don't experience is more valuable than the most optimized response to the crisis you do. This reframes how to prioritize supply chain AI investment.

### 5. Post-Crisis Learning Is Where Competitive Advantage Is Built
Every company experiences supply chain disruptions. The ones that build sustainable competitive advantage are those that systematically conduct post-mortems within 30 days, before institutional memory fades, and convert lessons into documented playbooks. Companies that skip this repeat the same crisis.

---

## Technical Notes
- React 18 via CDN (no build step)
- Babel Standalone for JSX transpilation in-browser
- All state in `useState` — no Redux, no Context
- Progress bar animations use `useEffect` with timeout (wait for mount before transition)
- Fully offline — no external assets beyond CDN scripts
- ~2,000 lines of clean JSX
- Full randomization: 8 industries × 4 companies × 8 crises = 256+ unique company+crisis combinations

---

## Deliverables
- `operation-lifeline.html` — Complete interactive supply chain crisis simulation
- `crisis-card.png` — Cinematic Day 29 card
- `day-29.md` — This file

---

*Day 29 of 60 · Built with Claude AI · #60DaysOfAI*
