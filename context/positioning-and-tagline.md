# Positioning & Tagline — Post-Supriya Repositioning (Execution Version)

## 1. The tagline (pinned in session)

> **"Don't just respond to crises faster. Predict which failures are coming and get ahead of them."**

Variants to A/B in outreach and decks:
- "Problem solver, not record holder."
- "Your supply chain's nervous system — it knows the answer before you know there's a problem."
- "From 8 people scrambling for days to 2 people deciding in minutes."
- "The crisis playbook that writes itself from every decision you've ever made."

## 2. Category label (the words that go on slide 1 and the website)

Banned: *system of information*, *system of records*, *organizational memory*, *knowledge platform*. (Per Supriya: buyers file these under "good to have.")
Use: **Supply Chain Crisis Management & Decision Execution System.** Short form: *decision execution for supply chain*. The memory/decision-trace layer is described only as the mechanism: "it gets smarter with every decision you make" — one sentence, never the headline.

## 3. The 90-second cold open (verbatim script — rehearse this)

> "Last quarter, memory prices doubled and suppliers cut allocations with two weeks' notice. Companies that saw it coming locked contracts months earlier and saved millions. Companies that didn't paid spot prices or shipped worse specs.
>
> When something breaks in your supply chain — a supplier cuts you, a cable gets cut, a contract manufacturer goes dark — your best people spend the next two days on calls reassembling information that already exists somewhere in your company. MetaFloor is the system that already has it assembled. When a crisis hits, it hands your team a decision package in forty minutes — options, costs, risks, and what you did last time it happened. And before the crisis, it's watching the signals — supplier earnings, price moves, your own lead-time slippage — and tells you which failure is coming next, months out.
>
> It runs in your cloud, on our models, so nothing leaves your walls. Want to see the memory-price event replayed?"

Then run the UC2 backtest demo. Tech stack discussion only if they pull it out of you.

## 4. Discovery question bank (make *them* pitch the pain — Supriya's "focus on their problems" operationalized)

1. "Walk me through your last supply crisis. How many people, how many days, before someone could put three options in front of a decision-maker?"
2. "When a supplier confirms a PO at 11 weeks instead of 8 — who notices, and when?"
3. "How much visibility do you actually have inside your contract manufacturers between quarterly reviews?"
4. "Where do the reasons behind your big allocation decisions live today? Could someone new find them during an incident?"
5. "What did the memory price run-up cost you, and when did you first see it coming?"
6. "How current is your FMEA, honestly?"

Each question maps to a demo beat: Q1→UC1, Q2/5/6→UC2, Q3→CM bridge, Q4→precedent view.

## 5. Messaging matrix (before → after, use to scrub every asset)

| Old (tech-led) | New (problem-led) |
|---|---|
| "Typed causal graph captures the why behind decisions" | "During your next crisis, the system already knows what you did last time — and why" |
| "Agent layer integrates with your systems" | "Your team stops spending day one of every incident collecting data from five systems" |
| "We capture organizational memory" | "Every decision your team makes trains the response to the next one" |
| "Multi-agent simulation environment" | "We replay your supply chain against thousands of futures and tell you which failure shows up in most of them" |
| "Privacy-aware deployment architecture" | "Runs inside your AWS account. Your data never leaves." |

## 6. The three rehearsed defenses (30 seconds each, from the meeting)

**"Why not build it ourselves?"** — "You can build the integrations; any good team can. What you can't shortcut: supply-chain-tuned models running privately in your VPC, a simulation engine calibrated on real enterprise failure history, and a decision-trace graph that compounds with every incident. That's a multi-year build competing with your roadmap — and it still wouldn't have seen the memory squeeze coming, because that calibration is our whole company."

**"What's your TCO?"** — Never answer with architecture. Answer: "Deployment runs about $X/month in your cloud plus subscription — call it $Y annually all-in. Against that: [pull the UC1/UC2 value math — decision-window cost, FTEs, avoided spend]. We'll build the model on your incident history in the pilot, so the ROI number is yours, not ours." (Customer-facing TCO doc: numbers and tables only, per established rule.)

**"Crises are rare — what do we get on day one?"** — "Day one you get the watchtower: live risk scores on your top failure modes, lead-time drift alerts, contract-renewal windows flagged, CM visibility. The crisis is when it proves itself; the readiness is what you're subscribed to. Same argument as insurance, except this one works for you every day."

## 7. One-pager skeleton (build next, numbers-and-tables style)

1. Header: category label + tagline
2. Three problem rows (crisis scramble / silent risk drift / CM opacity), each: cost of status quo → outcome with MetaFloor → the metric
3. Value table: decision window, FTEs, warning lead time, avoided cost — with pilot-measurable definitions (pull targets from UC1 §8 and UC2 §6)
4. Deployment strip: your VPC, our models, no data egress, ~$X/mo infra
5. Pilot offer: read-only, 6 weeks, backtest on your history, exit metrics pre-agreed

## 8. Supriya follow-up plan

1. Thank-you note (short, lowercase-Arun voice, one specific reference to her cable-cut example).
2. Attach the reworked one-pager (§7) once built — *not* the internal use-case docs.
3. The ask, sequenced: feedback on the one-pager first → then the advisory conversation → then (if warm) intro-level design-partner discussion. Don't stack all three in one email.
4. Offer to show the backtest demo when built — it directly answers her reactive-vs-proactive challenge, closing the loop on her own question.
