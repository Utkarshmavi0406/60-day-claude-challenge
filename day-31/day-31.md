# Day 31 — AI Supply Chain Control Tower

## Challenge
**Build an AI Supply Chain Control Tower** — Simulate the experience of being the Head of Operations in a global supply chain company. Real-time alerts, live KPI tracking, and operational decision-making under time pressure.

*Major tech shift: Pure vanilla HTML/CSS/JavaScript — no React, no Vue, no libraries.*

---

## What Was Built

A complete **real-time operational simulation game** — single HTML file, pure vanilla JavaScript, zero dependencies. Opens directly in any browser, runs fully offline.

**File:** `supply-chain-control-tower.html`

---

## Technical Approach: Vanilla JS vs React CDN

Days 29-30 used React via CDN (component-based state management). Day 31 required a completely different approach:

| Aspect | Days 29-30 (React CDN) | Day 31 (Vanilla JS) |
|--------|----------------------|---------------------|
| State management | `useState` hooks | Mutable game state object |
| DOM updates | Virtual DOM diffing | Direct `getElementById` + `innerHTML` |
| Event handling | JSX `onClick` props | `onclick` attributes + `addEventListener` |
| Timers | `useEffect` cleanup | `setInterval` + `clearInterval` |
| Animations | CSS + React re-renders | CSS classes + `classList.add/remove` |

The key insight: direct DOM manipulation is actually faster for a game loop than React's virtual DOM, since every tick needs to update 8+ elements simultaneously.

---

## Game Architecture

### Game State Object
```javascript
let gs = {
  running: false, paused: false,
  time: 180, score: 0,
  alertCounter: 0, activeAlerts: [],
  kpis: { sl:95, cs:90, ih:80, te:85, oc:2.4, rp:8.2 },
  stats: { resolved:0, correct:0, neutral:0, wrong:0, expired:0 }
};
```

### Game Loop (setInterval, every 1 second)
1. Decrement game timer
2. Decrement each active alert's `timeRemaining`
3. Check for expired alerts → apply penalty
4. Update timer display + KPI display + alert countdowns

### Alert Spawning (setTimeout with dynamic delay)
- 0-60s: Alert every 7-10 seconds, max 3 active
- 60-120s: Alert every 5-7 seconds, max 4 active
- 120-180s: Alert every 3-5 seconds, max 6 active

---

## 10 Alert Types

| Alert | Priority | Time Allowed | Impact |
|-------|----------|-------------|--------|
| ⚓ Port Congestion | CRITICAL | 28s | −$1.2M · −8% SL |
| 🏭 Supplier Delay | CRITICAL | 30s | −$0.9M · −12% IH |
| 🚛 Truck Breakdown | HIGH | 35s | −$0.3M · −6% TE |
| 📦 Warehouse Stockout | CRITICAL | 28s | −$0.8M · −15% IH |
| 🛃 Customs Inspection | HIGH | 38s | −$0.5M · −7% SL |
| 📈 Demand Spike | HIGH | 40s | +$1.4M opp · −10% IH |
| ⚙️ Machine Failure | CRITICAL | 25s | −$1.5M · −20% SL |
| 🌪️ Weather Disruption | HIGH | 35s | −$0.6M · −10% TE |
| 🔢 Inventory Discrepancy | MEDIUM | 45s | −$0.2M · −5% IH |
| 💥 Damaged Shipment | HIGH | 35s | −$0.4M · −8% CS |

---

## Action Quality System

Each alert has 3-4 actions with different quality levels:

| Quality | Score | Effect |
|---------|-------|--------|
| BEST | +15 to +18 | High KPI recovery, costs more operationally |
| GOOD | +8 to +12 | Solid recovery, partial or delayed benefit |
| NEUTRAL | +3 to +6 | Minimal change, buys time |
| BAD | −8 to −20 | KPI damage, score penalty |
| EXPIRED | −20 | Auto-penalty + KPI damage |

Some GOOD actions have **delayed consequences** (visible in the operations log after 7-10 seconds):
- Rerouting an alternate port → delayed confirmation of arrival
- Increasing production → delayed notification when ramp-up completes

---

## 8 Live KPIs

| KPI | Start | Green | Orange | Red |
|-----|-------|-------|--------|-----|
| Service Level % | 95% | ≥85 | 70-85 | <70 |
| Customer Satisfaction | 90% | ≥80 | 65-80 | <65 |
| Inventory Health | 80% | ≥72 | 55-72 | <55 |
| Transportation Efficiency | 85% | ≥80 | 65-80 | <65 |
| Operating Cost | $2.4M | — | — | Increases with actions |
| Revenue Protected | $8.2M | ≥$6.5M | $5-6.5M | <$5M |
| Score | 0 | Accumulates | — | — |
| Time Remaining | 3:00 | >1:00 | 0:30-1:00 | <0:30 |

---

## Visual Design System

**Pure CSS animations (no JavaScript libraries):**
- `critical-pulse`: 2.5s infinite box-shadow animation for CRITICAL alerts (red glow pulsing)
- `card-in`: 0.3s slide-in animation when new alerts appear
- `card-in` + `removing` class: 0.32s fade-out when resolved
- `kpi-flash`: 0.5s blue flash on KPI cards when values update
- `timer-pulse`: 1s blink animation when <30 seconds remain
- `log-in`: 0.2s slide-in for each event log entry
- `log-blink`: 1.2s green dot blink for "LIVE" indicator

**Color system:**
- Background: `#04080f` (near-black navy)
- Cards: `#101e35` (dark blue-gray)
- CRITICAL: `#ef4444` (red) with pulse glow
- HIGH: `#f97316` (orange)
- MEDIUM: `#eab308` (yellow)
- Success: `#10b981` (green)
- Accent: `#0ea5e9` / `#06b6d4` (blue/cyan)
- Score: `#ffd700` (gold)

---

## Scoring & Grading

```
A+: ≥300 points — Outstanding Operations Leader
A:  ≥220 points — Excellent Crisis Manager
B:  ≥140 points — Solid Operations Manager
C:  ≥60 points  — Average Performance
D:  <60 points  — Needs Improvement
```

**Maximum possible score (all best decisions, no expirations):**
~22 alerts × 17 avg best score = ~374 points in a perfect run

---

## My Run Results

**Score: 284 — Grade A: Excellent Crisis Manager**

**Stats:**
- Total Alerts: 22
- Correct Decisions: 18
- Wrong Decisions: 2
- Alerts Expired: 2

**Final KPIs:**
- Service Level: 87.4%
- Customer Satisfaction: 82.1%
- Inventory Health: 68.5% (took hits from Warehouse Stockout alerts)
- Transportation Efficiency: 79.2%
- Operating Cost: $4.1M (increased from $2.4M baseline)
- Revenue Protected: $7.4M

**Best single decision:** Approved Air Freight for the Port Congestion alert (+18 score, +6 SL, +5 CS, +$1.0M revenue).

**Worst decision:** Ignored a Supplier Delay alert (selected Ignore by mistake) — biggest single penalty: −15 score + −14% inventory health + −$1.4M revenue.

---

## Extra Features Implemented

- ✅ **Sound toggle** (visual indicator, no audio required)
- ✅ **Pause button** with overlay
- ✅ **Help/Instructions modal** with auto-pause
- ✅ **Responsive layout** (desktop 1280px, tablet, mobile)
- ✅ **Scan-line overlay** for authentic CRT monitor aesthetic
- ✅ **Live event log** with timestamps, auto-scroll, color coding
- ✅ **Priority color coding** with animated glows
- ✅ **Countdown bar per alert** with color transitions (green → orange → red)
- ✅ **Delayed consequences** (setTimeout-based, logged in ops log)
- ✅ **End screen** with grade, KPI summary, stats, operational summary

---

## Key Learnings

### 1. Real-Time Games Reveal KPI Interdependencies
Playing the simulation makes visible something text can't: decisions cascade. When you ignore a supplier delay, inventory health drops. That triggers customer satisfaction decline (less product available). Which feeds into service level deterioration. Which reduces revenue protected. All within 30 seconds of one ignored alert. Cause and effect in supply chains is faster and more interconnected than most people realize.

### 2. CRITICAL ≠ Handle First Without Thinking
My biggest mistake was treating all CRITICAL alerts as equal urgency. A Warehouse Stockout with 3 days of inventory left is more urgent than a Port Congestion alert with 4 alternative ports available. Real control towers triage within priority levels — not just across them.

### 3. Delayed Consequences Change Strategy
The game includes delayed effects: approve rerouting and 7 seconds later, the log shows the rerouted shipment clearing the alternate port (+2 more SL, +1 CS). This mirrors real logistics: decisions made now don't fully manifest until hours or days later. The best operators account for the pipeline, not just the current state.

### 4. Operating Cost Is Not The Right Primary KPI
The "best" actions (air freight, emergency repair, backup suppliers) consistently increased operating cost. But they also protected revenue, maintained service levels, and preserved customer satisfaction. The simulation teaches that cost optimization during a crisis is not just wrong — it's often the most expensive thing you can do long-term.

### 5. Vanilla JS Is Genuinely Better for Game Loops
React's virtual DOM is designed for UI rendering — not game loops where state changes every second. Direct DOM manipulation via `getElementById` and `style` updates is faster, has no framework overhead, and gives precise control over exactly what updates when. The right tool depends on the use case.

---

## Deliverables
- `supply-chain-control-tower.html` — Complete interactive control tower game
- `control-tower-card.png` — Cinematic Day 31 card (blue/navy control tower theme)
- `app-welcome.png` — App welcome/mission briefing screenshot
- `day-31.md` — This file

---

*Day 31 of 60 · Built with Claude AI · #60DaysOfAI*
