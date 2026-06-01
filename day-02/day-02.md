# Day 2 — Lazy Prompt vs. Engineered Prompt

## Overview

Today's challenge compared two ways of asking Claude the same underlying question — a quick, casual "lazy" prompt versus a detailed, structured "engineered" prompt — to see how prompt quality shapes the output. I framed both around my own field, Credit Risk Analytics.

## Prompt 1 — The Lazy Prompt

> What is prompt Engineering and how can I use that in Credit Risk Analytics?

**Output summary:** Claude returned a brief, accurate definition followed by a simple 6-item list (Data Analysis, Model Validation, Documentation, Feature Engineering, Scenario Analysis, Regulatory Compliance) and a single example prompt. Useful, but surface-level and short.

## Prompt 2 — The Engineered Prompt

> You are an experienced prompt engineer and data analytics consultant. Explain prompt engineering in clear, practical terms and demonstrate how to apply it to credit risk analytics. Include:
> 1) A concise definition of prompt engineering and why it matters in analytics projects.
> 2) A step-by-step workflow for applying prompts to credit risk tasks (data exploration, model selection, feature engineering, model evaluation, deployment).
> 3) Concrete use cases with example prompts:
>    - Data profiling and quality checks
>    - Feature engineering for credit scoring (e.g., handling imbalanced data, segment-specific features)
>    - Model explanation and auditability prompts (SHAP/feature importance)
>    - Risk reporting and regulatory-compliant explainability prompts
> 4) Best practices for prompt design in this domain (data privacy, reproducibility, versioning, prompt templates).
> 5) A minimal example: provide one ready-to-use prompt template for building a credit risk model and one for generating a model explainability report.
> Optionally, tailor recommendations for common tools (e.g., SQL, Python with pandas/sklearn, LLM-assisted data labeling) and note potential pitfalls (data leakage, overfitting prompts, misinterpretation of outputs).

**Output summary:** Claude produced a full structured guide — "Prompt Engineering for Credit Risk Analytics: A Practical Guide" — delivered as a formatted document (artifact) with an Executive Summary, numbered sections, defined principles (Clarity, Context, Constraints, Reproducibility, Auditability), and supporting tables.

## Key Differences Observed

| Dimension | Lazy Prompt | Engineered Prompt |
|-----------|-------------|-------------------|
| **Depth** | Short, high-level overview | Comprehensive, in-depth guide |
| **Structure** | Single flat list | Executive summary, numbered sections, sub-headings, tables |
| **Examples** | One generic example prompt | Multiple targeted, domain-specific prompt templates |
| **Specificity** | Generic credit-risk mentions | Tailored to real tasks (SHAP, imbalanced data, auditability) |
| **Format/Design** | Plain chat response | Polished, document-style artifact, ready to reuse |
| **Reusability** | Limited | High — usable as a reference document |

## Key Learnings

- The same question can yield wildly different value depending on how it's framed. Specificity in the prompt directly drives specificity in the output.
- Assigning a **role** ("experienced prompt engineer and data analytics consultant") and giving **explicit structure** (numbered deliverables) pushes Claude toward a more rigorous, organized response.
- Asking for concrete artifacts — templates, examples, tables — turns a generic explanation into something genuinely reusable in my workflow.
- For analytical and regulated domains like credit risk, engineered prompts that demand reproducibility and auditability produce outputs that are far closer to production-ready.

## What I Worked On

Ran both prompts in separate Claude chats, captured screenshots of each output, and compared them side by side across explanation quality, structure, examples, and overall design.