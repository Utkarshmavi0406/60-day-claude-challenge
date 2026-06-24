# Day 25 — Build an AI Shark Tank Simulator

## Challenge
**Entrepreneurship Applications with Claude** — Build a complete, production-quality AI Shark Tank Simulator as a single self-contained HTML file. Pitch your startup to AI investors, get scored, and receive funding decisions.

---

## What Was Built

A fully functional **AI Shark Tank Simulator** — single HTML file, zero backend, zero dependencies. Open in any browser and start pitching.

**File:** `shark-tank-simulator.html`

---

## App Features

### 4 AI Judge Personas

| Judge | Role | Focus |
|-------|------|-------|
| 🦈 **Vikram Nair** (VC) | Peak Capital | Market Size & Scalability |
| 🦈 **Maya Patel** (Founder) | ex-CEO, EdTech Unicorn | Execution & Team |
| 🦈 **Alex Johnson** (Customer) | Product & UX Expert | Usefulness & Customer Value |
| 🦈 **Priya Sharma** (Angel) | Former Goldman MD | Profitability & ROI |

### App Flow (8 Screens)
1. **Welcome** — Shark Tank intro with judge panel preview
2. **Input Form** — 6 startup fields + "Try Sample: AIcademy India" quick fill
3. **Pitch Stage** — Dramatic startup reveal, judges review the pitch
4. **Q&A Round** — 8 questions total (2 per judge), with judge reactions after each answer
5. **Evaluating** — Animated deliberation screen with pulsing judge avatars
6. **Scorecard** — 5-dimension animated score bars + overall count-up
7. **Verdict** — Investment decision with valuation, judge votes, and reasoning
8. **Leaderboard** — Persistent rankings via localStorage

### Scoring System (5 Dimensions)
- **Market Potential** — Based on market signals in startup description
- **Innovation** — Based on solution uniqueness and answer quality
- **Business Model** — Based on revenue model strength and clarity
- **Execution** — Based on answer quality, length, and depth
- **Investment Worthiness** — Weighted composite of all dimensions

### Investment Decisions
| Score | Decision | Trigger |
|-------|----------|---------|
| ≥ 78 | ✅ INVEST | Confetti + green theme |
| 65-77 | ⏰ COME BACK LATER | Purple theme |
| 52-64 + strong biz model | 🤝 ACQUIRE | Amber theme |
| < 52 | ❌ REJECT | Red theme |

### Bonus Features
- 🎉 **Confetti** on INVEST or ACQUIRE decisions (pure JS particle system)
- 📄 **PDF Download** via window.print() with styled print template
- 🏆 **Leaderboard** with persistent localStorage rankings (top 10)
- 🔗 **Share Result** button (navigator.share API + clipboard fallback)
- ⚡ **Ctrl+Enter** keyboard shortcut for question submission
- 🔄 **Sample startup** quick-fill button (AIcademy India pre-loaded)

---

## My Startup Pitch — AIcademy India

### Input
| Field | Value |
|-------|-------|
| Startup Name | AIcademy India |
| Problem | India's 260M students don't encounter real AI until BTech (21+) — 11 years of compounding learning lost |
| Solution | 12-week online AI program for Class 5-8, Saturdays via Zoom, working AI project guaranteed by Week 12 |
| Revenue Model | ₹1,499/month B2C → ₹300/student/month B2B schools → ₹15-30K teacher certification |
| Target Audience | Parents of Class 5-8 in Bengaluru, Delhi NCR, Mumbai (₹15-60L HHI) |
| Funding Ask | ₹50 Lakh Seed Round |

### Simulation Result
- **Overall Score: 82/100**
- **Decision: ✅ INVEST**
- **Estimated Valuation: ₹4–6 Crore**
- **Equity Offered: 12%**

### Score Breakdown
| Dimension | Score |
|-----------|-------|
| Market Potential | 84/100 |
| Innovation | 79/100 |
| Business Model | 81/100 |
| Execution | 86/100 |
| Investment Worthiness | 80/100 |

### Hardest Question (from Priya, the Angel)
> *"Walk me through your unit economics for AIcademy India. What's your projected LTV, CAC, and payback period — and where could those assumptions break?"*

**My Answer:** CAC is near ₹0 for Batch 1 (pure organic LinkedIn). LTV is ₹8,994 per student (avg 2 batches at ₹4,497 each). Payback period is 0 months on the founder-led model since we're profitable from student 10. Assumptions that could break: if demo class conversion falls below 25% (fixed: rewrite messaging), or if school B2B sales cycle is 24+ months instead of 12 (fixed: start B2C-only revenue, don't depend on B2B for Year 1 survival).

### Judge Votes
- **Vikram (VC):** ✅ IN — "Market timing is right. I see a path to scale."
- **Maya (Founder):** ✅ IN — "You know your unknowns. That's fundable."
- **Alex (Customer):** ✅ IN — "This solves a real pain. Customers will pay."
- **Priya (Angel):** ✅ IN — "The unit economics work. I'll back this."

---

## Key Learnings

### On Shark Tank Simulation
1. **Investor psychology is consistent.** VC asks about market. Founder asks about execution. Customer asks about pain. Angel asks about money. These 4 lenses cover virtually every investor question you'll ever face.

2. **The hardest questions come from the person with the most data.** Priya (ex-Goldman) asking about unit economics is the question that separates founders who know their business from those who just have a deck.

3. **Confetti is a product decision, not a decoration.** The emotional payoff of confetti on "INVEST" makes users want to share the result. It's a retention and virality mechanic disguised as fun.

### On Building the App
4. **Single-file HTML is underrated.** No build step, no server, no npm install, no deployment. Open the file. It works. This is a genuinely useful distribution format for tools that need to be portable.

5. **Scoring algorithms don't need to be AI-powered to feel intelligent.** The simulator uses keyword analysis, text length analysis, and calibrated randomization. It produces realistic, contextual scores without a single API call.

6. **State machines make complex apps simple.** 8 screens, dozens of UI states, no framework — just a `showScreen()` function and careful state management. Clean enough to read, robust enough to ship.

---

## Technical Notes
- **No API calls** — fully self-contained JavaScript logic
- **No external dependencies** — single HTML file, loads Google Fonts from CDN
- **Persistent leaderboard** — localStorage across sessions
- **Print-ready PDF template** — hidden div revealed only on print
- **Mobile responsive** — CSS Grid breakpoints for all screens
- **Keyboard shortcuts** — Ctrl+Enter to submit answers

---

## Deliverables
- `shark-tank-simulator.html` — Complete interactive Shark Tank app
- `shark-tank-card.png` — Cinematic Day 25 card (blue/purple gradient theme)
- `app-welcome.png` — App welcome screen screenshot
- `day-25.md` — This file

---

*Day 25 of 60 · Built with Claude AI · #60DaysOfAI*
