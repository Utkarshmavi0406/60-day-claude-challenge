# Day 30 — Supply Chain Builder

## Challenge
**Build a Supply Chain Optimizer** — Guide a complete beginner through building an enterprise supply chain from scratch. Every decision includes plain-English education on what the concept means, why it matters, and how it affects business performance.

*Day 30 of 60 — Completing the first half of the challenge.*

---

## What Was Built

A complete **Supply Chain Builder** simulation — single HTML file, React 18 via CDN, Babel JSX transpilation in-browser. No npm, no Tailwind, no backend, no external assets. Opens directly in any browser, runs fully offline.

**File:** `supply-chain-builder.html`

---

## Key Design Principle: Education First

Unlike Day 29's crisis response (choose fast under pressure), this app is about **deliberate optimization**. Before every decision, the player reads:

1. **📚 What is [concept]?** — Plain English, with a relatable analogy
2. **🎯 Why does this matter?** — Business impact in concrete terms
3. **Choice cards** — Each shows Pro ✓, Con ⚠, and a mini metric preview
4. **After the choice** — Outcome bullet points explaining what will happen to the business
5. **Updated live metrics** — Animated bars showing what changed and by how much

---

## App Flow (7 Screens)

### Screen 1: Welcome
- Plain English intro to supply chains ("a relay race from raw materials to customer")
- What you'll build (5-step preview)
- Emerald green design theme — distinct from Day 29's blue

### Screen 2: Company Profile
Randomly generated:
- **8 industries** (Electronics, Apparel, Food & Beverage, Automotive, Pharma, Home Furnishings, Industrial Equipment, Sporting Goods)
- **12 name prefixes × 6 suffixes × 5 types** = 360+ unique company names
- **4 demand profiles**: Steady, High Growth, Seasonal, Volatile
- **5 market configurations**: Domestic → Global 50+
- **Starting metrics**: All 5 metrics begin at 50/100

### Screen 3: Supplier Strategy

| Option | Tag | Key Trade-off |
|--------|-----|--------------|
| 1️⃣ Single Supplier | Cheapest · Highest Risk | Best price, zero backup |
| 2️⃣ Dual Sourcing | Balanced · Safer | Backup exists, slightly more expensive |
| 🌐 Multiple (3+) | Resilient · Complex | Competition between suppliers, harder to manage |
| 🛡️ Global Network | Maximum Resilience · Premium | Near-total disruption protection |

**Education:** "Think of it like a restaurant and its food suppliers — without ingredients, nothing gets cooked."

### Screen 4: Factory Location

| Option | Tag | Key Trade-off |
|--------|-----|--------------|
| 🏠 Domestic | Fast · Sustainable · Expensive | 3-5x higher labor cost, but days not weeks |
| 🚂 Near-shore | Balanced · Good Value | Cost savings without full offshore complexity |
| ⚓ Offshore | Cheapest · Slowest · Risky | 50-70% labor saving, 6-12 week lead times |
| 🌍 Multi-region | Most Resilient · Highest Investment | Each market served locally |

**Education:** "Location determines labor cost, how close you are to customers, and how much you spend on shipping."

### Screen 5: Warehouse Strategy

| Option | Tag | Key Trade-off |
|--------|-----|--------------|
| 🏢 Single Central | Cheapest · Slower Delivery | One location, far from some customers |
| 🗺️ Regional Hubs (3-4) | Balanced · Good Coverage | Most common mid-size approach |
| 🌐 Distributed Network | Fastest · Most Expensive | Amazon's model — proximity to every customer |
| ⚡ Just-in-Time Hub | Lean · Requires Precision | Zero buffer, any delay = stockout |

**Education:** "A warehouse is like a network of parking lots for your inventory. Where you park matters."

### Screen 6: Transportation Method

| Option | Tag | Key Trade-off |
|--------|-----|--------------|
| 🚛 Road Freight | Flexible · Medium Impact | Door-to-door, higher emissions |
| 🚂 Rail Freight | Eco-Friendly · Cost-Efficient | 4x lower emissions, needs last-mile truck |
| 🚢 Sea Freight | Cheapest · Slowest | 4-8 week transit, global trade foundation |
| ✈️ Air Freight | Fastest · Most Expensive | 50x more than sea, only for urgent/high-value |

**Education:** "Transportation is 5-15% of total product cost — one of your largest cost levers."

### Screen 7: Inventory Strategy

| Option | Tag | Key Trade-off |
|--------|-----|--------------|
| ⚡ Lean (2-3 weeks) | Low Cost · Stockout Risk | Cash freed, vulnerable to disruptions |
| ⚖️ Balanced Buffer (4-6 weeks) | Safe Middle Ground | Handles typical fluctuations |
| 🛡️ Safety Stock (8-12 weeks) | Always Available · High Cost | Near-zero stockout risk |

**Education:** "Every unit of inventory you hold costs 20-30% of its value per year in carrying costs."

### Screen 8: Final Dashboard
- **Overall Supply Chain Score** (0-100) with animated SVG score ring
- Grade: S (World Class) / A (Excellent) / B (Good) / C (Average) / D (Needs Work)
- **Performance breakdown** — all 5 animated metric bars
- **Strengths** — top metrics above 65
- **Weaknesses** — lowest metrics below 55
- **Biggest Risk** — derived from worst-performing metric
- **3 Practical Improvements** — personalized to your specific weak areas
- **Decisions Summary** — recap of all 5 choices made

---

## Live Metrics System

5 metrics, each starting at 50/100, updated after every decision:

| Metric | Icon | Color | What it measures |
|--------|------|-------|-----------------|
| Cost Efficiency | 💰 | Emerald | How well you control supply chain costs |
| Delivery Speed | ⚡ | Blue | How fast products reach customers |
| Risk Resilience | 🛡️ | Purple | How well your chain handles disruptions |
| Customer Satisfaction | ⭐ | Amber | Customer experience quality |
| Sustainability | 🌱 | Cyan | Environmental impact rating |

**Note displayed in app:** "Higher is always better for all metrics"

After each choice, the app shows:
- Previous value → New value
- Delta (+X or -X) colored green/red
- Animated bar transition (0.9s cubic-bezier)

---

## My Run

**Company:** Sterling Goods Corp · Automotive Parts · $2,400M revenue · High & Growing demand · North America + Europe

**Decisions Made:**
1. 🌐 **Multiple Suppliers** (+15 Risk Resilience, +12 Customer Satisfaction)
2. 🚂 **Near-shore Manufacturing** (+8 Cost, +12 Speed, +5 Risk)
3. 🗺️ **Regional Hubs** (+10 Speed, +10 Customer Satisfaction)
4. 🚂 **Rail Freight** (+12 Cost, +22 Sustainability)
5. ⚖️ **Balanced Buffer** (+10 Cost, +8 Speed, +5 Risk)

**Final Scores:**
| Metric | Score |
|--------|-------|
| Cost Efficiency | 72 |
| Delivery Speed | 68 |
| Risk Resilience | 82 |
| Customer Satisfaction | 76 |
| Sustainability | 88 |
| **OVERALL** | **78 — Grade A: Excellent** |

**Strength:** Sustainability (88) and Risk Resilience (82)
**Weakness:** Delivery Speed (68) — regional hubs helped but near-shore adds transit time
**Improvement 1:** Add 1-2 distribution hubs near largest customer clusters
**Improvement 2:** Demand forecasting software to right-size inventory
**Improvement 3:** Long-term preferred supplier agreements for price stability

---

## Key Learnings

### 1. Rail Freight Is the Hidden Sustainability Win
Rail transport produces 4x lower carbon emissions than road freight — with minimal delivery speed impact on land routes. Yet most supply chain discussions jump straight to ocean vs air. For domestic and continental shipping, rail is the most underutilized green lever. The sustainability metric moved from 55 to 88 from this single decision.

### 2. The Single Supplier Trap Is Seductive
Single sourcing gives you the best unit price and the simplest supplier relationship. But it's the most common cause of catastrophic supply chain failures. The app makes this explicit: "If this one supplier has any problem, your production stops completely." Moving to dual sourcing costs more per unit but dramatically changes your risk profile.

### 3. Warehouse Location Is a Customer Satisfaction Problem
Most people think of warehousing as a cost-management decision. It's actually a customer experience decision. Where you store products determines delivery speed, and delivery speed directly drives satisfaction and repeat purchase rates. The metrics make this connection visible in real time.

### 4. Offshore Manufacturing Saves Money — Until It Doesn't
The lure of 50-70% labor cost savings is real. But the app makes visible what the P&L often obscures: 6-12 week lead times require expensive demand forecasting capability, inventory buffers eat back the cost savings, and one tariff change or port disruption can make the economics collapse. The sustainability score also takes a significant hit.

### 5. Just-in-Time Is a Strategy for Perfect Conditions
Just-in-time inventory is beloved in business school case studies. The app shows why: it minimizes carrying cost and looks great on balance sheets. But the Risk Resilience score tells the truth — any supply disruption creates immediate stockouts. JIT is a strategy for stable, predictable supply chains with very reliable suppliers. Most businesses don't qualify.

---

## Technical Notes
- React 18 (CDN) + Babel Standalone (JSX transpilation in-browser)
- Single HTML file, fully offline
- All state managed with `useState` — no Redux, no Context
- Metric bar animations use `useEffect` with 80ms timeout for CSS transition to fire
- Educational content embedded in DECISIONS data structure with `getOutcome()` functions per choice
- Final score: simple average of all 5 metrics (each 0-95 after clamping)
- Grade thresholds: S≥85, A≥75, B≥65, C≥55, D<55
- ~1,800 lines of clean JSX

---

## Deliverables
- `supply-chain-builder.html` — Complete interactive supply chain optimizer
- `supply-chain-card.png` — Cinematic Day 30 card (emerald green theme)
- `day-30.md` — This file

---

*Day 30 of 60 — Completing the first half of the challenge. Built with Claude AI · #60DaysOfAI*
