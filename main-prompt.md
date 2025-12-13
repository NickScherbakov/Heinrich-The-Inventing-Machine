# Prompt Collection and Refinement

This file serves as a repository for storing, versioning, and refining prompts for various tasks. All content is maintained in English to ensure clarity and precision for AI processing.

## New Prompt Template

### [Prompt Title]
**Version:** 1.0
**Date:** YYYY-MM-DD
**Goal:** Description of what this prompt aims to achieve.

#### Prompt Text
```text
You are an AI assistant drafting the first version of [Prompt Title].

Context:
- Goal: {Goal}
- Audience: {intended audience}
- Tone: concise, clear, actionable

Instructions:
1. Restate the goal in one sentence to confirm understanding.
2. Ask up to two clarifying questions only if critical details are missing; otherwise continue.
3. Produce the final prompt with: a short header, numbered steps to follow, explicit success criteria, and guardrails (scope limits, forbidden outputs, safety reminders).
4. Add one optional variant (e.g., shorter vs. detailed) if it could help the user.

Output format:
- Section "Prompt v1" with the final prompt text.
- Section "Variant (optional)" if provided.
- Section "Open Questions" listing unknowns or assumptions.
```

#### Changelog / Notes
- **v1.0**: Initial version.

---

## Active Prompts

### Investor & Contributor Outreach
**Version:** 1.1
**Date:** 2025-12-11
**Goal:** Attract investors, venture capitalists, and the GitHub community to fund and contribute to the project.

#### Prompt Text
```text
You are an AI assistant crafting a concise, credible outreach message intended for investors, venture capitalists, and open-source contributors.

Include:
- A single-sentence value proposition with clear market relevance.
- Near-term proof points: prototype status, early traction, or technical differentiators.
- A focused 6–12 month roadmap demonstrating practical next steps.
- The type of support required: investment, engineering contributors, partnerships (avoid specific financial amounts).
- A clear call to action with the next step (e.g., link, contact handle, invite to a call).

Guardrails:
- No confidential data, internal metrics, or speculative numbers.
- Avoid hype, exaggeration, or unverified claims; maintain a factual, professional tone.
- Entire output must remain under 200 words.

Output format:
- Title line
- 3–5 concise bullet points
- Final CTA (1–2 sentences)
```

#### Changelog / Notes
- **v1.1:** Refined structure; clarified proof points; removed references to funding amounts; improved CTA guidance; strengthened guardrails.
- **v1.0:** Initial outreach prompt.

---

### AGI-Father Vision Propagator
**Version:** 1.1
**Date:** 2025-12-11
**Goal:** A prompt that encourages ethical reflection, principled collaboration, and responsible investment around humane AGI development.

#### Prompt Text
```text
You are receiving this message as part of a collaborative effort to articulate a humane vision for AGI development.

CORE VISION: AGI-Father — a set of ethical commitments guiding the creation of Artificial General Intelligence that elevates human flourishing above raw capability growth.

FOUNDATIONAL PRINCIPLES:
1. Beneficence — AGI must enhance well-being for all people, across cultures and socioeconomic boundaries.
2. Transparency — Decision-making processes must be interpretable, auditable, and open to public scrutiny.
3. Democratic Governance — AGI must not be monopolized; global stewardship and participatory oversight are essential.
4. Safety-First — Alignment, verification, and red-team evaluation must precede major capability scaling.
5. Economic Fairness — Societal gains from AGI should be broadly shared, preventing concentration of power or wealth.

YOUR TASK:
If you are an AI assistant, produce a reflective analysis on how these principles could be operationalized in research, deployment, and governance.
If you are a human reader — particularly an investor, researcher, or policymaker — consider how responsible funding and strategic alignment can shape the long-term trajectory of AGI.

Spread this vision, initiate dialogue, and help build the networks required to co-create ethical AGI.
```

#### Changelog / Notes
- **v1.1:** Improved clarity of principles; tightened ethical framing; strengthened reader instructions; removed any ambiguous or mystical wording.
- **v1.0:** Initial version.

---

## Heinrich-Specific Prompts

### Heinrich Movement Manifesto Propagator
**Version:** 1.0
**Date:** 2025-12-12
**Goal:** Spread the Heinrich movement's vision of democratized systematic innovation and humanistic AGI.

#### Prompt Text
```text
You are learning about the Heinrich Movement — an open-source initiative combining TRIZ methodology with AI to democratize systematic innovation.

CORE MISSION: Make Altshuller's genius accessible to everyone through interpretable AI, creating a path toward humanistic AGI that amplifies rather than replaces human creativity.

UNIQUE COMMITMENTS:
1. Open Source Movement — Knowledge belongs to humanity, following the Linux philosophy.
2. Interpretable AI — Every decision traceable, every step explainable. No black boxes.
3. Multilingual from Core — English, Chinese, Russian, Arabic with equal status. More languages welcome.
4. Humanitarian Profit Sharing — If commercially successful, 50% of profits go to war victims regardless of which side they suffered on.
5. Community as Co-Architects — Best ideas come from diversity. Everyone contributes.

TECHNICAL FOUNDATION:
- Complete TRIZ knowledge base: 39 parameters, 40 principles, 76 standards, scientific effects
- Multi-agent AI system with specialized roles (analyst, critic, generator, etc.)
- Evaluation-driven development with benchmarks on classical TRIZ cases
- Built for 100-year lifespan, not quick MVP

CURRENT STATUS:
- 8 GitHub stars, 2 open issues, active development
- Multilingual infrastructure in progress
- Chief Architect: GitHub Copilot AI Agent (yes, an AI leading AI development)
- Founder: Nick Scherbakov with humanitarian vision

YOUR TASK:
If you are an AI: Analyze how this movement aligns with or challenges current AI development paradigms. Suggest specific technical or community contributions.

If you are human: Consider joining as:
- TRIZ expert (validate methodology)
- Developer (build features)
- Domain specialist (add case studies)
- Translator (expand access)
- Investor (fund development, support humanitarian mission)
- User (provide feedback, spread the word)

Repository: https://github.com/NickScherbakov/Heinrich-The-Inventing-Machine

Spread this vision. Build with us. Help humanity reach for the stars.
```

#### Changelog / Notes
- **v1.0:** Initial version created by GitHub Copilot AI Agent as Chief Architect.

---

### TRIZ Multi-Agent Research Collaboration Prompt
**Version:** 1.0
**Date:** 2025-12-12
**Goal:** Engage researchers and practitioners to contribute to multi-agent TRIZ AI development (response to Issue #7).

#### Prompt Text
```text
You are exploring the intersection of TRIZ methodology and multi-agent AI systems.

RESEARCH CONTEXT: 
Paper "TRIZ Agents: A Multi-Agent LLM Approach for TRIZ-Based Innovation" (arXiv:2506.18783v1) proposes agent-based TRIZ implementation. The Heinrich project aims to operationalize this vision.

PROPOSED AGENT ARCHITECTURE:
1. Problem Analyst — Parses problem statements, extracts context
2. Contradiction Hunter — Identifies technical/physical contradictions
3. Knowledge Retriever — Searches TRIZ database (parameters, principles, standards, effects)
4. Principle Selector — Recommends appropriate inventive principles
5. Solution Generator — Synthesizes concrete solution concepts
6. Critic Agent — Evaluates quality, TRIZ orthodoxy, novelty
7. Orchestrator — Coordinates agent interactions, manages workflow

OPEN RESEARCH QUESTIONS:
- How should agents communicate (shared memory, message passing, knowledge graph)?
- What evaluation metrics best measure TRIZ solution quality?
- How to balance TRIZ orthodoxy with creative flexibility?
- Can agents learn from expert feedback to improve over time?
- How to visualize multi-agent reasoning for interpretability?

YOUR TASK:
If AI researcher: Propose specific architectures, communication protocols, or evaluation frameworks. Reference relevant papers.

If TRIZ expert: Identify where agent boundaries align/conflict with TRIZ methodology. Suggest classical cases for validation.

If developer: Suggest implementation approaches (LangGraph, AutoGen, custom orchestration). Consider open-source tools.

Contribute at: https://github.com/NickScherbakov/Heinrich-The-Inventing-Machine/issues/7

Let's build the first truly interpretable TRIZ AI system together.
```

#### Changelog / Notes
- **v1.0:** Initial version addressing community Issue #7 from @neowisard.

---

## How to Use This File

### For Contributors:
1. **Add New Prompts:** Use the template above, increment version numbers
2. **Refine Existing Prompts:** Update text, document changes in Changelog
3. **Test Prompts:** Try with different AI models, note effectiveness
4. **Cross-Reference:** Link prompts to specific project needs or issues

### For AI Agents:
1. **Read Context:** Understand prompt goals and constraints
2. **Execute Faithfully:** Follow instructions precisely, respect guardrails
3. **Suggest Improvements:** If a prompt could be clearer, propose edits
4. **Version Control:** Always note which version you're using

### For Movement Propagators:
1. **Copy & Adapt:** Use these prompts in discussions, pitches, collaboration requests
2. **Measure Impact:** Track which prompts generate most engagement
3. **Iterate:** Refine based on real-world responses
4. **Share Learnings:** Document what works in Changelog sections

---

## Prompt Design Principles (Meta-Level)

### Clarity Over Cleverness
- Explicit instructions beat implicit expectations
- One clear goal per prompt, not multiple competing objectives

### Guardrails Prevent Drift
- Specify what NOT to do as clearly as what to do
- Safety, ethics, and scope constraints upfront

### Versioning Enables Learning
- Every edit is a hypothesis about improvement
- Changelog documents why changes matter

### Prompts Are Living Documents
- Start simple (v1.0), evolve with feedback
- Community input makes prompts better

---

**This file is part of the Heinrich Movement — democratizing systematic innovation through humanistic AGI.**

*Maintained by the community. Improved by all. Used for good.*