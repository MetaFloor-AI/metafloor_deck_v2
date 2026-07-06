# Meeting Notes — Supriya Iyer (Google Supply Chain)

**Date:** July 2026
**Who:** Supriya Iyer — Director, Supply Chain & Commercial Operations at Google. 20+ years in supply chain; runs materials supply and network operations at Google scale. Based in Menlo Park.
**Purpose:** Explore a potential advisory role; get her read on MetaFloor's product and pitch; look for network effects.
**Outcome:** Went well. She found the idea and capabilities interesting, validated the problem space, and gave hard, useful feedback on positioning. Advisory conversation stays open.

---

## Glossary first (every term she used, in plain English)

- **TCO — Total Cost of Ownership.** The full cost of buying and running a solution, not just the sticker price. The first number every enterprise buyer demands.
- **FTE — Full-Time Equivalent.** One person's full workload. "Saves 6 FTEs" = frees up six people's worth of time.
- **FMEA — Failure Mode and Effects Analysis.** A structured exercise: list everything that could go wrong in your operation, then rank the risks.
- **RPN — Risk Priority Number.** The score FMEA produces. Severity × likelihood × how hard it is to see coming. High score = deal with it first.
- **Decision documents.** Google's internal practice of writing down major decisions and the reasoning behind them. Relevant because it's their existing answer to "we already record why we did things."
- **Contract manufacturer (CM).** An outside factory that builds your product for you (e.g., Foxconn assembling phones). You depend on them but can't see inside their operations.
- **Crisis ops.** The scramble mode a company enters when something breaks — a cable cut, a supplier failure — and people drop everything to coordinate a fix.

---

## How the conversation ran

### 1. Opening critique: we pitched technology, not problems
We walked her through the product. Her first major pushback: the idea is interesting, but **there's no customer pitch**. We were selling architecture and capabilities when supply chain leaders buy solved problems. Simpler is better: name the problem, show the fix, show the dollar value.

### 2. "We already record everything" — the decision-documents objection
She noted Google already documents decisions and the reasoning behind them. Translation of the objection: *recording* the why is not the value — they have that. The value has to be **surfacing the right answer faster and better than their current process**. This reframes our organizational-memory story: the memory is the engine, not the pitch.

### 3. The crisis scenario she threw at us: submarine cable cut
Her concrete test case. An undersea internet cable gets cut. Suddenly: who has spare parts, in which warehouse? Which repair crews are free? How do you physically get people and parts there? Parts take days to source but are needed now. Today this runs on phone calls and whoever remembers things — expensive, slow, chaotic. She was asking: *can your product own this?* → Worked into **Use Case 1** (separate doc).

### 4. "Why can't we build this ourselves?"
Standard enterprise challenge: Google (or any Fortune 500) has engineers; models are available; why buy? Our defense, which held:
- We're a **full-stack AI company** — our own models specialized for supply chain, not a wrapper around a general model.
- **Privacy-aware** — customer data doesn't get shipped to an outside AI cloud provider.
- **Predictable costs** — no surprise usage bills.

Her immediate counter: "then what's your TCO?" — meaning prove the total cost and the payback.

### 5. TCO and the day-one value bar
Her point: big companies have run their supply chains for decades and manage billions with existing processes. A tool that's "useful when there's a crisis" doesn't justify itself — crises are occasional. The pitch must show **dollar value from day one**: e.g., "crisis coordination takes 2 people instead of 8," "decision in 40 minutes instead of 3 days," with money attached. We answered that we provide estimates by company size and usage; she accepted it, but the lesson is to make these numbers front-and-center.

### 6. Contract manufacturer visibility — the use case *she* brought us
Google supplies parts to contract manufacturers who build products. Problem: **no visibility inside them**. The CM says everything's fine until it isn't. Her question: what can you see, and do you have plans here?

Our answer: it's on the roadmap — integrations that let a customer invite their CMs into the platform, have them update status live, and enforce the customer's policies on them **without replacing the CM's existing systems**. Forced transparency via a data bridge, not a software migration.

**This was the high point.** She responded to the *possibility* more than any technical detail — called these the real decision problems and "information black holes" they actually live with.

### 7. Reactive vs. proactive challenge
Her test: do you show up after something breaks, or do you see it coming? Our answer: proactive by design — the pipeline picks up early signals, forms hypotheses, and watches for confirmation. Differentiator: **multi-agent simulation** — model the supply chain as a game, let AI agents play out thousands of scenarios (as suppliers, buyers, competitors), and the failures that keep emerging are the ones to prepare for.

Proof point used: the current **memory chip price spike** (AI data centers absorbing chip supply, phone/device makers getting squeezed). A simulation run beforehand would have flagged it and recommended locking contracts early. She was impressed by this.

Honest caveat we gave (and she respected): calibrating this needs a big company's real data — it's why we need enterprise design partners. She agreed these problems don't even exist at small-company scale. → Worked into **Use Case 2** (separate doc).

### 8. Closing feedback: fix the label
Don't call it a "system of information" or lead with record-keeping. Portray it as a **crisis management / execution system — a problem solver, not a record holder**. Talk possibilities and outcomes, not good-to-haves. → Worked into **Positioning doc**.

---

## Action items

1. **Rebuild the pitch deck** problem-first: crisis scenario → cost of status quo → MetaFloor outcome → day-one dollar value. Tech only in appendix/deep-dive.
2. **Build the TCO one-pager**: FTEs saved, decision-time reduction, risk (RPN) reduction, cost per incident — numbers and tables, no narrative.
3. **Promote CM visibility** from roadmap item to headline enterprise wedge — it's the thing she lit up at.
4. **Prepare the 30-second "why not build it yourself" answer** as a rehearsed unit.
5. **Follow up with Supriya**: thank-you note + the reworked one-pager; keep the advisory question alive.
6. **Design partner ask**: use her sympathy for the calibration constraint as the explicit ask if the relationship progresses — a real enterprise problem to simulate against.

---

## Companion documents

- `use-case-1-crisis-ops.md` — submarine cable cut scenario, full write-up
- `use-case-2-fmea-predictive.md` — proactive failure prediction + Pixel worked example
- `positioning-and-tagline.md` — repositioning summary + tagline variants
