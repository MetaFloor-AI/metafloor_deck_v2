# MetaFloor Deck v3 (`deck2/`) — Story, Thought Process & Handoff

> **Purpose of this doc.** This is the single source of truth for *why the new deck says what it says*.
> Read it before touching any slide so the narrative stays consistent across agents and edits.
> Last updated: 2026-07-06 (v3.1 story/drama pass). Companion design doc: `~/.gstack/projects/deck2/arun-main-design-20260706-150641.md` (supersedes `-130600`).
>
> **v3.1 pass (2026-07-06):** crisis reframed to *consequential decision events* (crisis kept as a proof feature, not scrubbed); added global-bleed citations, a new **07 Where This Goes** long-term/breadth slide, two appendix backups (**B1 Architecture**, **B2 The Field**), dry-wit annotation clouds, a split event/standing-value ledger, a funnel line on the ask, and four customer-lens overclaim fixes. Deck is now **10 core + 2 backup = 12 slides.**
>
> **v3.2 (story/impact pass):** slide 3 rebuilt as a one-hour story (timestamps + payoff); slide 5 made hard-hitting ("$3.1M protected" + "the rest is margin"); slide 7 rebuilt with concrete horizons; B1 rebuilt with 3 worked flows.
>
> **v3.3 (proof/coherence pass — from a two-persona cold-read: YC investor + Apple/Google SC head):** added a new Proof slide (backtest-on-your-own-history — the fix for "no proof"); killed the self-undermining "founder input/assumption" badges on the ask funnel; added a **"safe to own" governance strip** on Moat (enterprise litigation-fear fix); resolved the exec/support wobble → category is now **"The decision layer for supply chain"** (founder-overridable).
>
> **v3.4 (trust-first restructure — the coherence/flow fix):** the deck was internally polished but had **no spine**. Rebuilt around one logline and a trust-first order. **New order (11 core):** 01 Cover · 02 Problem · 03 Product · **04 Proof** (moved up — proof = trust, comes early for enterprise) · 05 Value · 06 Numbers · 07 Moat (Why Us) · **08 Why Trust Us (NEW)** · **09 The Prize & The Path** (merged old Market + Where-This-Goes) · 10 Ask · 11 Close · +B1/B2. **New Trust slide (08):** three de-risking pillars (it proves itself / champions vouch / we were the buyer) mapped to the three questions enterprise-seed investors actually ask, + advisor→design-partner ladder. **Ask (10) re-scoped** off Series-A metrics (was "$3M ARR, NRR>120%") onto **seed milestones** (10 champions → 3–4 paid design partners → validated backtest → Series-A ready) — right-sizing builds trust. Headlines now read as one story top to bottom. Deck is **11 core + 2 backup = 13 slides.** The one thing still missing is real pilot data — see The Assignment.

---

## 0. Hard consistency rules (do not break these)

These come straight from the founder and the Supriya Iyer (Google Supply Chain) repositioning. Every edit must pass this scrub:

- **One product: MetaFloor.** Never mention **CXO** or **Compass** — both are dead pivots.
- **We are decision SUPPORT, not a decision-MAKER.** MetaFloor watches, assembles, recommends, readies, and executes *only what a human approves*. Your people make the call. Never write copy that implies the system decides autonomously (banned: "the layer every decision runs on", "has made your decisions before"). Use "you decide", "backs every call", "assembled — you decide", "your people keep making the call".
- **Category (resolved v3.3): "The decision layer for supply chain."** Replaced "Decision execution for supply chain" — the exec/support wobble (cover said "execution", vision/close said "decision-support layer") was flagged by the investor cold-read. "The decision layer" is the deck's own phrase (market slide: "the decision layer on top is empty"), sidesteps both the autonomy read of "execution" and the sleepy-DSS read of "support", and stays differentiated. Used on cover, product titlebar, vision (08), close (11). **Founder-overridable** — one word flips it to "Decision support" (their stated identity) or back to "Decision execution".
- **Never use records/memory framing as the headline.** Banned as category words: *system of information*, *system of records*, *organizational memory*, *knowledge platform*. Buyers file these under "good to have." The decision-trace/memory layer appears **only** as a mechanism, in one sentence: *"it gets smarter with every decision you make."*
- **Value is the headline; crisis is one of the features (the proof moment).** The recurring unit is **consequential decision events** — supplier cuts, price runs, lane closures, allocation reviews, renewals, ramps. The tax is paid on every event. Crisis is the day the tax becomes *visible* AND the moment the product proves itself. Do **not** reframe the deck as "crisis software"; do **not** scrub crisis either.
- **Frequency formula (say it the same way on slides 02 and 05):** *"dozens of consequential decisions a year; 12–20 put $0.5M+ on the line."* Never contradict this (no "every week" ≈ 50/yr claims).
- **The global bleed (real cited numbers, not founder estimates — always show the source):** McKinsey — a single ≤30-day disruption puts 3–5% of EBITDA at stake, ~45% of a year's EBITDA erased per decade; S&P Global — ~$1.2T incremental supply-chain cost / lost profit in 2025; Interos — average Fortune 1000 firm loses ~$182M/yr; Xeneta 2026 — 96% of orgs hit by disruption in 2025. On-slide: **02 carries McKinsey 45% + S&P $1.2T**; **08 echoes S&P $1.2T + McKinsey 45% + Interos $182M**. Xeneta is talk-track only.
- **Numbers discipline.** Operational deltas (8→2 people, 3 days→40 min) are defensible and repeat across slides. Dollar/market figures are **illustrative, founder-input**, and must stay labeled as such. **No single figure wears two costumes:** the one-event *precedent* on slide 03 is **~$2.4M** (illustrative); the one-event *protected value* on slide 05 is **$3.1M** — they must stay distinct. The watchtower **standing value (~$0.7M/yr, illustrative)** appears on slides 04 and 05 but is NOT the ~2,000 event hours (anti-double-count). The knowledge repo and the old deck are both partially outdated — treat with a handful of salt.
- **Four customer-lens overclaim fixes (keep them fixed):** (1) "0 people watching" → **"0 connecting the three"**; (2) contract amendments **"drafted for legal"** (not executed); (3) trust perimeter → **"deployed in your VPC · scoped read-only in pilot · reviewed once, expanded with trust"** (not "passes your security review once"); (4) the **"78% of simulated futures"** row is **cut** → "allocation risk rising · 3 independent signals agree."
- **Ask/team/champions stay consistent with the recent deck** (dev): $2M seed → $3M+ ARR in 18 months, same 3 founders, same 10-person expert/champion wall, same 60/25/15 use of funds. The ask headline is **"Raising $2M to convert champion pilots into $3M+ ARR"** with a visible funnel line (10 champions → 6–8 pilots → ~40% convert → $3M+ ARR; pilots + conversion are founder-input placeholders).
- **Category label on slide 1:** "The decision layer for supply chain." (was "Decision execution" — see the category-resolved rule above.)
- **Deprecated:** `dev/docs/investor/investor_story.md` is the OLD Compass/QMS (quality-management, CAPA, defect) story. **Do not use it as a source.** It survives only as history of a prior pivot.

---

## 1. The core thesis (the one-paragraph version)

Every consequential supply-chain decision — a supplier cutting allocation, a commodity price running, a lane closing, a contract manufacturer going dark — is treated as a from-scratch project: ~8 senior people, 2–3 days, five systems, and whoever happens to remember what worked last time. The information to decide **already exists inside the company**; reassembling it every time is the tax. MetaFloor watches the signals continuously, assembles the decision package *before you ask* (options, costs, risks, precedent, evidence) in ~40 minutes, and executes with human approval in the tools the team already uses — and it compounds, because every decision trains the next one.

## 2. Audience & job of the deck

- **Two decision-maker audiences:** investors, and senior leaders at large orgs (the buyer/champion).
- **Emotional arc:** recognition ("this is my Tuesday") → relief ("there's a way out") → conviction ("the math and the moat hold") → action ("I want the pilot").
- **The slide a customer screenshots** is Slide 4 (Value). **The slide that closes an investor** is Slide 6 (Moat) into Slide 8 (Ask).

## 3. Narrative arc — why the slides are ordered this way

**Order reworked in v3.4 (trust-first spine) — see the v3.4 note at the top for the authoritative 11-slide order.** The numbered beats below are the pre-v3.4 sequence; the logline the whole deck now hangs on is: *"Supply-chain decisions are 3-day, 8-person scrambles that cost millions. MetaFloor makes them 40-minute, evidence-backed calls your people still own — and proves it on your own history before you commit."* Every headline is a beat in that sentence, in this order: Problem → Product → **Proof** → Value → Numbers → Moat → **Trust** → Prize&Path → Ask → Close.

Pre-v3.4 sequence (kept for reference):

1. **Hook** (01) → establish the transformation (8/days → 2/minutes) and the cold-open proof (memory prices doubled).
2. **Problem** (02) → the global bleed → your share is a weekly tax; both reactive (the scramble) and proactive (the drift nobody connects).
3. **Product** (03) → show *how* the answer gets assembled and executed — concretely, as a product, not a concept.
4. **Value** (04) → six pillars a customer can repeat, plus the watchtower's *standing* value (a number, not four icons).
5. **Numbers** (05) → a CFO-legible equation split into **event value + standing value**.
6. **Proof** (06, NEW v3.3) → "don't trust it forward, prove it backward." The 6-week pilot's week 1 = replay your last 12 months, show the events you scrambled on and what MetaFloor would have flagged and how early. Answers the #1 investor + customer objection (no proof) honestly — you grade it on outcomes you already lived. Callbacks the cover's memory-price hook.
7. **Moat** (07) → "why can't we / an LLM just build this?" answered by outcome-labeled decision data that compounds — plus a **"safe to own" governance strip** (VPC · access-scoped · retention you set · deletable on exit) that flips the enterprise buyer's litigation-risk read.
8. **Where This Goes** (08) → the long-term arc + multifaceted breadth: wedge → surface → the enterprise's decision layer. Answers "how big can this get?" (your people keep making the call).
9. **Market & motion** (09) → size the prize (grounded in the bleed numbers) and show the low-risk land→expand path.
10. **Ask & team** (10) → the raise as a funnel (10 named champions → pilots → ARR), the plan, and the people/champions who de-risk it.
11. **Close** (11) → recap the four numbers, echo the endgame, and the pilot CTA.

**Backups (appendix, after Close):**
- **B1 — Architecture** → the vertical stack (signals → capture → decision core → agents → execution, outcomes loop back); the model is the only swappable layer, everything else compounds. Rebuilt from `dev/deck_slides` visuals in the deck2 theme.
- **B2 — The Field** → supply-chain competitive matrix (planning suites plan / risk tools alert / horizontal AI has no vertical workflow / MetaFloor runs the whole decision) + advisor highlight band (the 5 category-leader champions).

---

## 4. Slide-by-slide: what it says, why, and the visual intent

Each slide is a standalone file in `slides/`, 1280×720 fixed stage, scaled by `deck.js`. Theme is set by `data-theme` on `<html>` and the floating switcher (green | ember | violet). All motion respects `prefers-reduced-motion`.

### 01 — Cover (`01-cover.html`)
- **Says:** "Decision execution for supply chain." Headline: *From 8 people scrambling for days to 2 people deciding in minutes.* Lede: watches signals → assembles the answer before you ask → executes with approval → gets smarter every decision. Three chips (your cloud / human-approved / backed by veterans). Cold-open hook: memory prices doubled.
- **Why:** lead with the transformation and the one stat that makes the pain visceral. The "gets smarter" line is the only memory reference — deliberately one sentence.
- **Visual:** split layout. Left = brand + headline. Right = animated **signal-convergence diagram** (ERP, suppliers, market, email, CMs → the mark → a "decision / 40 min" node) above a **live "watching" console** whose feed rows type in and end at "decision package ready." The **real MetaFloor logo** (`assets/logo_only_transparent.png`) sits next to the wordmark. *(Logo added 2026-07-06 at founder request.)*

### 02 — The Decision Tax (`02-problem.html`)
- **Says:** every consequential decision is a project you pay for weekly. **Global-bleed band** up top (McKinsey 45% EBITDA/decade + S&P $1.2T in 2025 → your share is a weekly tax). Two lanes. Left "the scramble": cost-of-delay curve — cheap-options window closes in hours, 8 seniors pulled in, decision lands day 3 after the window closed. Right "the drift": three signals (commodity price, lead-time 8→11wk, supplier stress) rise for ~6 months before the crisis flare, each first-visible months early, **nobody connecting the three**. Takeaway band: *a crisis isn't rare — it's the day the daily tax becomes visible; dozens a year, 12–20 put $0.5M+ on the line.*
- **Why:** proves the problem is both reactive (expensive scramble) *and* proactive (missed early warnings) — sets up product's "watch + assemble." The bleed band scales it to the world so the tax reads as inevitable, not niche.
- **Visual:** two self-drawing SVG charts + stat strips (8 / 5+ / 2–3 days / window closed ; T−5mo / 3 warnings / **0 connecting the three** / 2× price). Two **dry-wit clouds**: "day 3: the cheap options left yesterday" · "three warnings. zero people connecting them."
- **v3.1:** added the global-bleed band; relabelled "0 watching"→"0 connecting the three"; frequency formula in the takeaway; two wit clouds. Densest slide — verify no overflow at 1280×720.

### 03 — The Product (`03-product.html`)
- **Says:** the decision, assembled. Three steps: **Watch** (live signal feed across ERP/market/finance/email/simulation) → **Assemble** (the decision package: 3 ranked options with fit scores, costs, precedent, evidence, ready in ~40 min) → **Execute** (human approves, then drafts POs, notifies owners, tracks to close, records the why). Feedback loop underneath: every decision trains the next. Deployment chips: your cloud / predictable cost / lives in Slack·email·Teams.
- **Why:** the middle "Assemble" window is the hero — it makes the abstract concrete. Precedent line ("2024 panel squeeze, saved ~$2.4M") ties memory to money without making memory the pitch — and stays distinct from slide 05's $3.1M.
- **Visual:** three-column engine with animated connectors; the Assemble card is an elevated product window with animated fit-score meters. Subtle **breadth line** under the memory loop: "beyond the event · runs the low-level ops · readies production · standing decision support."
- **v3.1:** cut the "78% of simulated futures" watch row → "allocation risk rising · 3 independent signals agree"; contract amendments "drafted **for legal**"; precedent figure $3.1M→**~$2.4M (illustrative)**; added the subtle multifaceted-breadth line.
- **v3.2 (story pass):** rebuilt as a **one-hour story** — hook ("8:41am, a supplier goes quiet"), timestamps on each stage (Watch 8:41 → Assemble ready 9:22 → You decide 9:41), payoff ("the work that used to take 3 days and 8 people"). Headline now "assembled — **you decide**" (decision-support). Eyebrow: "one hour, one decision."

### 04 — The Value (`04-value.html`)
- **Says:** six ways it pays for itself from day one — **Time** (3 days→40 min), **People** (8→2), **Consistency** (same playbook every time), **Objectivity** (evidence-ranked options), **Low-risk automation** (approval-gated), **Friction** (zero new tabs). Watchtower band: before anything breaks — live risk scores, drift alerts, renewal windows, supplier stress.
- **Why:** this is the customer-repeatable summary. Each pillar maps to a founder value word. The watchtower answers "crises are rare — what do we get day one?" — now with a **standing-value number**, not four icons.
- **Visual:** six tiles, each with a purpose-built **micro-visualization** (not text): timeline compression, 8→2 dots, jagged-vs-aligned playbooks, ranked bars, human-gate flow, Slack "Approve" button. Watchtower band leads with **≈$0.7M/yr standing value (illustrative)**. One **wit cloud** on the friction tile: "no new tab. your team already lives here."
- **v3.1:** watchtower gets a standing-value figure (≈$0.7M/yr, illustrative, distinct from the ~2,000 event hours on slide 05); 8→2 reframed to "the other six are consulted, not conscripted"; friction wit cloud added.

### 05 — The Numbers (`05-numbers.html`)
- **Says:** one event pays for the year; you get **12–20 a year**. Left waterfall for one allocation-cut event: **$12M revenue exposed → −$4.9M** deciding day 3 → **−$1.8M** deciding in the window → **$3.1M protected** by one decision. Right ledger now **split into two groups**: *event value* (12–20 events/yr, $0.5–3M protected/event, ~2,000 senior hours returned) + *standing value* (the watchtower, ≈$0.7M/yr illustrative) vs. "low 6 figures" predictable cost → shape of return **≫10×**.
- **Why:** CFO-legible — protected margin, not soft ROI. The split makes the money story **event + recurring**, not event-only insurance economics. Explicitly the TCO defense.
- **Visual:** animated bar waterfall + two-group ledger + dark total band. One **wit cloud**: "you'll pay this one again next quarter — with or without us." **All figures labeled illustrative**, "calibrated with your data in a 6-week pilot." Baseline: mid-size electronics OEM ~$2B revenue.
- **v3.1:** header frequency aligned to 12–20/yr; ledger split into event value + standing value (no figure appears in both columns — the ~2,000 hours live only here, the watchtower $0.7M is the standing line); recurrence wit cloud added. $3.1M kept here (now unique — slide 03 precedent is $2.4M).
- **v3.2 (impact pass):** made hard-hitting for a bored observer — headline leads with the gut-punch (**"One 40-minute decision. $3.1M protected."**), sub adds "the first one covers our fee; the rest is margin," total band reframed to **"the other 11–19 are pure margin,"** $3.1M enlarged in the waterfall.

> **Numbering note (v3.3):** a new **Proof** slide was inserted at position 06, shifting Moat→07, Where-This-Goes→08, Market→09, Ask→10, Close→11. The `### NN —` headings below still show pre-v3.3 numbers/filenames from 06 onward; **`slides.json` is the authoritative order + paths.** Titlebar counters and files on disk are correct (01–11 / 11).

### 06 — The Proof (`06-proof.html`) — NEW v3.3
- **Says:** don't trust it forward, prove it backward. Week 1 of the pilot replays your last 12 months. A "replay" timeline shows 3 event types (allocation cut, **memory-price run** — the cover-hook callback, lane closure), each with **MetaFloor's signal (green) firing months before your team scrambled (red)** + the $ that was on the table. A scorecard (events caught, avg head start, $ protectable) marked "your pilot fills this in." Trust band: *"you grade it on outcomes you already lived — no forward bet, no integration risk."*
- **Why:** the #1 gap from BOTH cold-reads (YC investor + Apple/Google SC head) was **no proof** — every figure illustrative. This answers it honestly without fabricating results: the mechanism is real, the numbers are what the pilot produces on their data. It de-risks the pilot to near-zero and turns the cover's memory-price hook into a payoff.
- **Visual:** left replay-timeline card (3 lanes, signal-vs-scramble lead brackets, memory-run highlighted) + right accent scorecard + dark trust band. Placeholders honestly marked ("your pilot" / "illustrative").
- **The Assignment still stands:** the real backtest on a champion's data replaces the illustrative scorecard numbers — that's what converts this slide from promise to evidence.

### 06 — Why Us / Moat (`06-moat.html` → now `07-moat.html`)
- **v3.3:** headline now "This one has **sat in** every decision you've made" (was "made your decisions" — decision-support fix). Added the **"safe to own" governance strip** (your VPC · data never leaves · access-scoped by role · retention you set · read-only in pilot · deletable on exit) to flip the enterprise buyer's "recording every decision = discoverable liability" fear.
- **Says:** generic AI answers questions; this one has *made your decisions before*. Core claim sharpened to **outcome-labeled decision data**: *"Your ERP records what you ordered. Only MetaFloor records what you considered, what you chose, and how it turned out."* Left: value-per-decision **compounding curve** vs flat generic AI — the gap is the moat. Right: four switching-cost layers — Integration surface → Trust perimeter → Workflow habit → **Decision memory** (the flywheel). Bench band: 2 exits / 30+ yrs ops / PhD AI / 10 experts & champions.
- **Why:** the "why not build it ourselves / why won't OpenAI eat this" defense. Decision memory is the only durable moat, so it's the deepest layer.
- **Visual:** self-drawing compounding chart with "THE MOAT" gap bracket; four layer rows with depth meters. One **wit cloud**: "the generic model forgets. yours doesn't."
- **v3.1:** headline sub re-anchored on the outcome-data claim; **cut the unfounded "~40 decisions kept" milestone** → "precedent accrues"; trust-perimeter overclaim fixed → "deployed in your VPC · scoped read-only in pilot · reviewed once, expanded with trust"; decision-memory layer reworded (it's the customer's data; the moat is it exists *only because MetaFloor structures it* — dropped the sloppy "unexportable"); wit cloud added.

### 07 — Where This Goes (`07-where-this-goes.html`) — NEW
- **Says:** today one team's decisions; tomorrow the enterprise's decision-**support** layer. Three horizons, each a concrete card with a *reach* line + 4 real capabilities + a value payoff: **Year 1 · the wedge** (one BU / one champion — allocation & sourcing calls, price-run timing, the watchtower; "paid pilot, measured on the champion's own data") → **Year 3 · the surface** (every BU/category/site — + production readiness, S&OP & supplier/sustainability reviews, low-level ops handled; *multifaceted breadth lives here*; "the decision-support standard the enterprise runs on") → **Year 5+ · the layer** (OEM + its CMs — shared signals, joint capacity/allocation calls, the CM black hole lit up; "the coordination layer ERP never delivered"). Mechanism band: *"it gets smarter with every decision your people make."*
- **Why:** answers "how big can this get?" with concrete scope growth, not abstraction. Carries long-term value + multifaceted breadth, decision-**support** framed throughout (your people keep making the call).
- **Visual (v3.2 redesign):** three content-rich horizon cards — reach line, 4-item capability list that fills the card edge-to-edge, tinted value marker at the bottom — + a dark mechanism band. Earlier abstract node-glyphs were cut (they read as meaningless / wasted space and implied autonomous decision-making).

### 08 — Market & Motion (`08-market.html`)
- **Says:** a huge market entered through one sharp wedge. Rings: **$150–250B** supply-chain software+services / **$40–70B** decision support & orchestration / **$1–3B** our wedge (mid-size OEMs, electronics/hardware, $0.5–5B revenue). Why now: AI can finally read the unstructured half (emails, calls, earnings, contracts). Motion: **land** (paid 6-week watchtower pilot) → **convert** (low 6-fig ACV) → **expand** (NRR>120%, execution + more BUs) → **network** (invite the CMs).
- **Why:** shows a big prize but a low-risk, champion-led entry that sits on ERP rather than fighting it. CM visibility is the expansion wedge Supriya lit up on.
- **Visual:** concentric market rings (animated) + why-now band; right = 4-step motion staircase with ACV progression. **Market figures = founder estimate / directional.**
- **v3.1:** added a **"why the spend is real"** grounding band echoing the global bleed ($1.2T / 45% EBITDA / $182M Fortune-1000, cited) so TAM reads as demand-backed, not a pure founder estimate; rings stay labeled directional; staircase unchanged.

### 09 — The Ask & Team (`09-ask.html`)
- **Says:** raising **$2M** to convert champion pilots into **$3M+ ARR** in 18 months, NRR>120%, Series-A ready. **Funnel line:** 10 champions → 6–8 pilots in motion (founder input) → ~40% convert (assumption) → $3M+ ARR. Three gates: clear IT/security (0–3mo) → convert pilots (3–9mo) → scale the vertical (9–18mo). Use of funds 60/25/15 (Engineering/GTM/Ops). Three founders (Anup CEO, Sridhar COO, Arun Head AI) with photos + pedigree. Full experts & champions wall (10 names) with expert/champion legend.
- **Why:** consistency requirement — mirrors the recent dev deck's ask/team/champions exactly. The champion bench is the primary de-risker. The funnel makes the ask math survive 60-second arithmetic.
- **Visual:** ask header + funnel line + gates timeline + use-of-funds bar; founders list with real photos; 5×2 champion grid with logos.
- **v3.1:** headline reworded (killed the "oldest B2B playbook" filler); added the visible funnel line; Arun's line answers the agent-race objection ("ships agentic LLM systems in production"). **Open:** exact conversion/pilot numbers and Anup's 2 exit names are founder-input.

### 10 — Close (`10-close.html`)
- **Says:** *your next decision is already assembling itself.* Endgame echo: "Start with the watchtower. End as **the layer every decision runs on.**" Recap strip: 3 days→40 min / 8→2 people / ≫10× / $2M seed open. CTA: see it on your data — 6-week pilot; or 20-min walkthrough → hello@metafloor.com.
- **Why:** end on the transformation + the four numbers + a low-friction next step (the pilot, not "invest").
- **Visual:** centered brand, ambient constellation background, endgame echo line, recap strip, CTA button.
- **v3.1:** added the endgame echo line from slide 07.

### B1 — Architecture (`B1-architecture.html`) — APPENDIX / BACKUP
- **Says:** five stages, signal to action — read any row left to right. Top row = the 5 stages with the systems in play (**Signal sources → Capture plane → Decision core → Agents that act → Execution**, chevrons show direction, decision core tinted). Below = **3 worked flows** aligned to those 5 columns, 2–3 words per cell, key elements bolded: **Allocation cut** (PO slips 8→11wk · earnings call read · risk + precedent · draft dual-source · Slack→ERP), **Price run** (DRAM +18% · matched to exposure · 3 options priced · recommend hedge · PO→procurement), **Production readiness** (drift on line 4 · tickets + emails · readiness score · qualify alternate · work order→MES). Footer: *"Short the model. Long the memory."* — the model is the only swappable layer.
- **Why:** the technical-credibility backup + the "won't the model companies eat this?" answer. The 3 worked flows make the abstract pipeline concrete and double as use cases.
- **Visual (v3.2 redesign):** one aligned grid — a 5-stage header row + 3 highlighted flow rows (dark title tiles, tinted decision-core column) filling the space; slim footer with the stack point. Replaced the earlier tall flow-cards + separate stack strip, which read as "complex, no flow, wasted space." **Source:** concepts from `dev/deck_slides` (moat.html stack strip + wave.html capture→govern→act), rebuilt in the deck2 theme. `dev/` is the approved *visual* source for B1 only; deprecated for story/copy.

### B2 — The Field (`B2-field.html`) — APPENDIX / BACKUP
- **Says:** everyone owns one slice; the decision layer is empty. Capability matrix (Watch / Assemble / Execute / Compounds) across **Planning suites** (o9 · Kinaxis · Blue Yonder · SAP IBP — plan, don't execute the decision), **Risk visibility** (Everstream · Resilinc · Interos · Prewave — alert, don't decide), **Horizontal AI** (Copilot · Palantir · generic agents — no vertical workflow, no precedent corpus), and **MetaFloor** (all four; sits on the ERP, doesn't fight it). Advisor highlight band: the 5 category-leader champions — *"the people who run these categories sit on our bench."*
- **Why:** answers "what's the competitive landscape?" (the investor cold-read flagged its absence, with a Blue Yonder VP on the champion wall). Nothing borrowed from `dev/` — a fresh supply-chain frame.
- **Visual:** 4×4 capability matrix (MetaFloor row highlighted, filled dots) + dark advisor band with 5 logos+names (Blue Yonder, Google, Jabil, Sanmina, AMD).

---

## 5. The reusable proof points (keep these identical everywhere)

| Fact | Value | Status |
|---|---|---|
| People per decision | 8 → 2 | defensible operational delta |
| Time to decide | 2–3 days → ~40 min | defensible operational delta |
| Systems reassembled by hand | 5+ | defensible |
| First signal visible before crisis | ~T−5 months | illustrative (memory-price event) |
| Frequency formula | dozens/yr; 12–20 put $0.5M+ at stake | illustrative — say it identically on 02 & 05 |
| One-event **precedent** (slide 03) | ~$2.4M | illustrative — MUST differ from slide 05 |
| One-event **protected value** (slide 05) | $3.1M | illustrative, founder-input |
| Watchtower standing value (slides 04/05) | ≈$0.7M/yr | illustrative — NOT the ~2,000 event hours |
| Senior hours returned (event value, slide 05 only) | ~2,000 hrs/yr | defensible delta |
| Annual return shape | ≫10× | illustrative |
| Global bleed — S&P Global | ~$1.2T disruption cost, 2025 | **cited** (on 02 + 08) |
| Global bleed — McKinsey | ~45% of a year's EBITDA / decade | **cited** (on 02 + 08) |
| Global bleed — Interos | ~$182M/yr, avg Fortune 1000 | **cited** (on 08) |
| Global bleed — Xeneta 2026 | 96% of orgs hit in 2025 | **cited** (talk-track) |
| Ask funnel | 10 champions → 6–8 pilots → ~40% → $3M+ ARR | pilots + conversion founder-input |
| TAM / SAM / SOM | $150–250B / $40–70B / $1–3B | founder estimate |
| Raise | $2M seed → $3M+ ARR / 18 mo | consistent with dev deck |
| Use of funds | 60 / 25 / 15 | consistent with dev deck |
| Champion bench | 10 named experts/champions | consistent with dev deck |

The cold-open script, discovery questions, and the three rehearsed defenses ("why not build it", "TCO", "crises are rare") live in `context/positioning-and-tagline.md` — pull verbatim from there, don't paraphrase.

---

## 6. Design system & architecture (so edits stay on-theme)

- **macOS-dense, white background, NO translucency.** No `backdrop-filter`, no `color-mix` plate fills, no grain. Solid surfaces only (`#FFFFFF` / `#F5F5F7`), 1px hairlines, 10–12px radii, layered subtle shadows.
- **Type:** Inter (display/body) + JetBrains Mono (labels/data). Tight tracking.
- **Themes:** green | ember | violet, swapped via `<html data-theme>`. Full accent ramp per theme in `theme.css`. Switcher pill is injected by `deck.js` (bottom-right, low opacity).
- **Architecture:** standalone slide files + iframe viewer (`index.html`) + `slides.json` manifest. Stage is 1280×720, uniform-scaled. Same pattern as `dev/`.
- **Motion:** entrance stagger via `.r` rows; a few purposeful SVG animations (signal pulses, self-drawing charts, counters). No decorative motion. Everything degrades under `prefers-reduced-motion`.
- **Assets:** `assets/logo_only_transparent.png` (brand mark), `assets/team/*` (founder photos + pedigree), `assets/logos/*` (champion company logos).

### Reviewing changes
Serve locally and screenshot with the **playwright** MCP (real Chromium), not the IDE browser — the IDE browser's screenshot pipeline mis-renders some SVGs. Command: `cd deck2 && python3 -m http.server 8787`, then open `http://localhost:8787/index.html` or individual `slides/NN-*.html?theme=ember|violet`.

---

## 7. Status & open items for the next agent

**Done (v3):** original 9 slides built and browser-verified across green/ember/violet; no CXO/Compass references; value-first arc; logo added to cover; no overflow at 1280×720.

**Done (v3.1, this pass):** crisis→events language pass (crisis kept as a proof feature); global-bleed band on 02 + echo on 08 with cited sources; new **07 Where This Goes** (long-term value + multifaceted breadth); appendix **B1 Architecture** (from dev/deck_slides, deck2 theme) + **B2 The Field** (competitive matrix + advisor band); dry-wit annotation clouds (02×2, 04, 05, 06) via a new additive `.witcloud` component in `theme.css`; split event/standing-value ledger on 05; watchtower standing-value number on 04; four customer-lens overclaim fixes; distinct precedent ($2.4M) vs protected ($3.1M); funnel line + reworded headline on 09; endgame echo on 10. Deck is now **10 core + 2 backup**; `slides.json` and per-slide titlebar counters updated to `/10` (backups labelled APPENDIX · B1/B2).

**Open / suggested next (founder-input placeholders labelled illustrative in-slide until supplied):**
- Watchtower standing value (≈$0.7M/yr), slide-03 precedent (~$2.4M), ask funnel (6–8 pilots, ~40% convert) — swap placeholders for real numbers.
- Arun's exact agentic/LLM production claim + Anup's 2 exit names (currently generic).
- **The backtest artifact** (The Assignment): replay the 2025–26 memory-price run through a champion's data — converts the deck from fiction to forecast. Nothing moves second-meeting probability more.
- Replace remaining illustrative dollar figures with real pilot/model numbers once available.
- PDF export not yet wired for `deck2/` (dev has `export_pdf.py` — adapt, don't rebuild).
- Confirm founder titles/pedigree logos are current before any external send.
- If publishing, `deck2/` follows the same static-host path as the existing deck.

**The assignment (founder's own test):** present to one champion from the wall (not a friendly) and time how long before they ask about price or pilot — that's the slide that's working.
