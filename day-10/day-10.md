# Day 10 — Build Your Personal Portfolio Website

**Challenge:** Use Claude to generate a complete personal portfolio website — a modern, single-file HTML application that showcases skills, projects, experience, and professional profile without writing a single line of code manually.

**Deliverable:** A fully self-contained `portfolio.html` — no backend, no build step, no external dependencies. Open it locally or visit it live.

🌐 **Live Portfolio:** [utkarshmavi-portfolio.netlify.app](https://utkarshmavi-portfolio.netlify.app/)

---

## What I Built

A personal portfolio website built entirely through a structured prompt to Claude. The site covers every section a recruiter or hiring manager would want to see, written with recruiter-friendly copy, and styled as a premium dark-theme SaaS interface.

**Sections built:**
- Hero with typing animation (cycles through 4 role descriptors), initials avatar, and a Quick Stats card
- About Me with domain-specific copy and a four-quadrant skills summary
- Skills with animated proficiency bars and a full tech-stack tag cloud
- Three project cards with descriptions, tech stacks, and GitHub links
- Experience timeline and education section with achievement badges
- Contact section with direct links and a contact form
- Dark/Light mode toggle
- Smooth scroll animations on every section reveal
- Active nav highlighting as you scroll
- Footer with social links

---

## Screenshots

### Hero
![Portfolio Hero](portfolio-hero.png)

### Skills
![Skills Section](portfolio-skills.png)

### Projects
![Projects Section](portfolio-projects.png)

### Experience & Education
![Experience Section](portfolio-experience.png)

### Full Page
![Full Portfolio](portfolio-full.png)

---

## Projects Featured

**Business Loan Credit Risk Model** — End-to-end PD scorecard deployed at Bajaj Finance. 7,000+ features, SHAP explainability, live lending decisions. Professional project (confidential codebase). Badges: Python, XGBoost, LightGBM, SHAP, PySpark, Azure Databricks.

**BERT Bank Statement Analyzer** — Fine-tuned BERT pipeline replacing manual underwriting steps, 98%+ classification accuracy on Azure Databricks. Professional project (confidential codebase). Badges: BERT, Transformers, Python, NLP, Databricks.

**60 Days of AI Challenge** — Daily AI-powered applications built in public using Claude. Live on GitHub with daily commits. Badges: Claude AI, JavaScript, HTML, Chart.js, Python.

---

## Deployment

Deployed as a static site on **Netlify** via drag-and-drop — no CLI, no build config, no backend.

🔗 [https://utkarshmavi-portfolio.netlify.app/](https://utkarshmavi-portfolio.netlify.app/)

---

## Key Learnings

**1. Personal branding is a positioning problem, not a design problem.** The first and hardest decision was not the colour scheme — it was figuring out the single sentence that captures who you are to a recruiter in under five seconds. "Data Scientist & Credit Risk Analyst | AI/ML Engineer | MS Business Analytics & AI" is the distillation of a three-year career into one line. Everything else on the site exists to support that claim.

**2. A prompt with real content beats a prompt with placeholders.** The challenge template says to replace `[Your Name]` with your name. That is a starting point, not the actual prompt. The portfolio got dramatically better when I gave Claude full context — exact job titles, real achievement numbers (7,000+ features, 98%+ accuracy), specific tech stacks, and honest descriptions of what the projects actually do. Real content in means real content out.

**3. No-CDN, no-build is a deliberate design choice, not a limitation.** Building the site as a single, self-contained HTML file with no external dependencies means it opens instantly, works offline, deploys in one drag-and-drop to Netlify, and never breaks because a CDN goes down. The constraint that seemed limiting became the most practical feature.

**4. A portfolio is a conversation-starter, not a CV substitute.** The goal is not to tell the whole story — it is to make a recruiter curious enough to reach out. Every project description ends at the most interesting claim (production deployment, 98%+ accuracy) and stops. The conversation fills in the rest.

**5. Deploying takes two minutes.** Netlify Drop — drag the file, get a live URL. No account, no config, no CLI. The barrier to having a live public portfolio is effectively zero.

---

## Files in This Folder

- `portfolio.html` — the complete portfolio website (also live at the Netlify URL above)
- `portfolio-hero.png` — hero section screenshot
- `portfolio-skills.png` — skills section with animated bars and tech tags
- `portfolio-projects.png` — three project cards
- `portfolio-experience.png` — experience timeline, education, and achievements
- `portfolio-full.png` — full-page capture
