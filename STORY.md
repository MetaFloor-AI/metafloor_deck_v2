# MetaFloor Deck v3 (`deck2/`) — Story, Thought Process & Handoff

> **Purpose of this doc.** This is the single source of truth for *why the new deck says what it says*.
> Read it before touching any slide so the narrative stays consistent across agents and edits.
> Last updated: 2026-07-06. Companion design doc: `~/.gstack/projects/deck2/arun-main-design-20260706-130600.md`.

---

## 0. Hard consistency rules (do not break these)

These come straight from the founder and the Supriya Iyer (Google Supply Chain) repositioning. Every edit must pass this scrub:

- **One product: MetaFloor.** Never mention **CXO** or **Compass** — both are dead pivots.
- **Never use records/memory framing as the headline.** Banned as category words: *system of information*, *system of records*, *organizational memory*, *knowledge platform*. Buyers file these under "good to have." The decision-trace/memory layer appears **only** as a mechanism, in one sentence: *"it gets smarter with every decision you make."*
- **Value is the headline; crisis is the proof.** Crisis is **not** rare — the "decision tax" is paid every day. Crisis is the day the daily tax becomes *visible*. Do not reframe the deck as "crisis software."
- **Numbers discipline.** Operational deltas (8→2 people, 3 days→40 min) are defensible and repeat across slides. Dollar/market figures are **illustrative, founder-input**, and must stay labeled as such. The knowledge repo and the old deck are both partially outdated — treat with a handful of salt.
- **Ask/team/champions stay consistent with the recent deck** (dev): $2M seed → $3M+ ARR in 18 months, same 3 founders, same 10-person expert/champion wall, same 60/25/15 use of funds.
- **Category label on slide 1:** "Decision execution for supply chain."
- **Deprecated:** `dev/docs/investor/investor_story.md` is the OLD Compass/QMS (quality-management, CAPA, defect) story. **Do not use it as a source.** It survives only as history of a prior pivot.

---

## 1. The core thesis (the one-paragraph version)

Every consequential supply-chain decision — a supplier cutting allocation, a commodity price running, a lane closing, a contract manufacturer going dark — is treated as a from-scratch project: ~8 senior people, 2–3 days, five systems, and whoever happens to remember what worked last time. The information to decide **already exists inside the company**; reassembling it every time is the tax. MetaFloor watches the signals continuously, assembles the decision package *before you ask* (options, costs, risks, precedent, evidence) in ~40 minutes, and executes with human approval in the tools the team already uses — and it compounds, because every decision trains the next one.

## 2. Audience & job of the deck

- **Two decision-maker audiences:** investors, and senior leaders at large orgs (the buyer/champion).
- **Emotional arc:** recognition ("this is my Tuesday") → relief ("there's a way out") → conviction ("the math and the moat hold") → action ("I want the pilot").
- **The slide a customer screenshots** is Slide 4 (Value). **The slide that closes an investor** is Slide 6 (Moat) into Slide 8 (Ask).

## 3. Narrative arc — why the slides are ordered this way

Value-first, then proof, then economics, then defensibility, then the ask:

1. **Hook** → establish the transformation (8/days → 2/minutes) and the cold-open proof (memory prices doubled).
2. **Problem** → make the daily tax undeniable and quantified, both reactive (the scramble) and proactive (the drift nobody watches).
3. **Product** → show *how* the answer gets assembled and executed — concretely, as a product, not a concept.
4. **Value** → distill it into six pillars a customer can repeat from memory.
5. **Numbers** → convert the value into a CFO-legible dollar equation.
6. **Moat** → answer "why can't we / an LLM just build this?" with the compounding decision memory.
7. **Market & motion** → size the prize and show the low-risk land→expand path in.
8. **Ask & team** → the raise, the plan, and the people/champions who de-risk it.
9. **Close** → recap the four numbers and the pilot CTA.

---

## 4. Slide-by-slide: what it says, why, and the visual intent

Each slide is a standalone file in `slides/`, 1280×720 fixed stage, scaled by `deck.js`. Theme is set by `data-theme` on `<html>` and the floating switcher (green | ember | violet). All motion respects `prefers-reduced-motion`.

### 01 — Cover (`01-cover.html`)
- **Says:** "Decision execution for supply chain." Headline: *From 8 people scrambling for days to 2 people deciding in minutes.* Lede: watches signals → assembles the answer before you ask → executes with approval → gets smarter every decision. Three chips (your cloud / human-approved / backed by veterans). Cold-open hook: memory prices doubled.
- **Why:** lead with the transformation and the one stat that makes the pain visceral. The "gets smarter" line is the only memory reference — deliberately one sentence.
- **Visual:** split layout. Left = brand + headline. Right = animated **signal-convergence diagram** (ERP, suppliers, market, email, CMs → the mark → a "decision / 40 min" node) above a **live "watching" console** whose feed rows type in and end at "decision package ready." The **real MetaFloor logo** (`assets/logo_only_transparent.png`) sits next to the wordmark. *(Logo added 2026-07-06 at founder request.)*

### 02 — The Decision Tax (`02-problem.html`)
- **Says:** every consequential decision is a project you pay for weekly. Two lanes. Left "the scramble": cost-of-delay curve — cheap-options window closes in hours, 8 seniors pulled in, decision lands day 3 after the window closed. Right "the drift": three signals (commodity price, lead-time 8→11wk, supplier stress) rise for ~6 months before the crisis flare, each first-visible months early, **nobody assigned to watch**. Takeaway band: *a crisis isn't rare — it's the day the daily tax becomes visible.*
- **Why:** proves the problem is both reactive (expensive scramble) *and* proactive (missed early warnings) — sets up product's "watch + assemble."
- **Visual:** two self-drawing SVG charts + stat strips (8 / 5+ / 2–3 days / window closed ; T−5mo / 3 warnings / 0 watching / 2× price).

### 03 — The Product (`03-product.html`)
- **Says:** the decision, assembled. Three steps: **Watch** (live signal feed across ERP/market/finance/email/simulation) → **Assemble** (the decision package: 3 ranked options with fit scores, costs, precedent, evidence, ready in ~40 min) → **Execute** (human approves, then drafts POs, notifies owners, tracks to close, records the why). Feedback loop underneath: every decision trains the next. Deployment chips: your cloud / predictable cost / lives in Slack·email·Teams.
- **Why:** the middle "Assemble" window is the hero — it makes the abstract concrete. Precedent line ("2024 panel squeeze, saved $3.1M") ties memory to money without making memory the pitch.
- **Visual:** three-column engine with animated connectors; the Assemble card is an elevated product window with animated fit-score meters.

### 04 — The Value (`04-value.html`)
- **Says:** six ways it pays for itself from day one — **Time** (3 days→40 min), **People** (8→2), **Consistency** (same playbook every time), **Objectivity** (evidence-ranked options), **Low-risk automation** (approval-gated), **Friction** (zero new tabs). Watchtower band: before anything breaks — live risk scores, drift alerts, renewal windows, supplier stress.
- **Why:** this is the customer-repeatable summary. Each pillar maps to a founder value word. The watchtower answers "crises are rare — what do we get day one?"
- **Visual:** six tiles, each with a purpose-built **micro-visualization** (not text): timeline compression, 8→2 dots, jagged-vs-aligned playbooks, ranked bars, human-gate flow, Slack "Approve" button. Watchtower has icons.

### 05 — The Numbers (`05-numbers.html`)
- **Says:** one event pays for the year; you get ~15 a year. Left waterfall for one allocation-cut event: **$12M revenue exposed → −$4.9M** deciding day 3 → **−$1.8M** deciding in the window → **$3.1M protected** by one decision. Right annualized ledger: 12–20 events/yr, $0.5–3M protected/event, ~2,000 senior hours returned, "low 6 figures" predictable cost → shape of return **≫10×**.
- **Why:** CFO-legible — protected margin, not soft ROI. Explicitly the TCO defense.
- **Visual:** animated bar waterfall + ledger + dark total band. **All figures labeled illustrative**, "calibrated with your data in a 6-week pilot." Baseline assumption: mid-size electronics OEM ~$2B revenue.

### 06 — Why Us / Moat (`06-moat.html`)
- **Says:** generic AI answers questions; this one has *made your decisions before*. The product an LLM can't replicate = your decision history/precedent/context, accumulated inside your walls. Left: value-per-decision **compounding curve** vs flat generic AI — the gap is the moat. Right: four switching-cost layers, each deeper — Integration surface → Trust perimeter → Workflow habit → **Decision memory** (the flywheel). Bench band: 2 exits / 30+ yrs ops / PhD AI / 10 experts & champions.
- **Why:** the "why not build it ourselves / why won't OpenAI eat this" defense. Decision memory is the only durable moat, so it's the deepest layer.
- **Visual:** self-drawing compounding chart with "THE MOAT" gap bracket; four layer rows with depth meters.

### 07 — Market & Motion (`07-market.html`)
- **Says:** a huge market entered through one sharp wedge. Rings: **$150–250B** supply-chain software+services / **$40–70B** decision support & orchestration / **$1–3B** our wedge (mid-size OEMs, electronics/hardware, $0.5–5B revenue). Why now: AI can finally read the unstructured half (emails, calls, earnings, contracts). Motion: **land** (paid 6-week watchtower pilot) → **convert** (low 6-fig ACV) → **expand** (NRR>120%, execution + more BUs) → **network** (invite the CMs).
- **Why:** shows a big prize but a low-risk, champion-led entry that sits on ERP rather than fighting it. CM visibility is the expansion wedge Supriya lit up on.
- **Visual:** concentric market rings (animated) + why-now band; right = 4-step motion staircase with ACV progression. **Market figures = founder estimate / directional.**

### 08 — The Ask & Team (`08-ask.html`)
- **Says:** raising **$2M seed** → $3M+ ARR in 18 months, NRR>120%, Series-A ready. Three gates: clear IT/security (0–3mo) → convert pilots (3–9mo) → scale the vertical (9–18mo). Use of funds 60/25/15 (Engineering/GTM/Ops). Three founders (Anup CEO, Sridhar COO, Arun Head AI) with photos + pedigree. Full experts & champions wall (10 names across Google, AMD, Jabil, NetApp, AstraZeneca, GE Vernova, Juniper, Blue Yonder, Sanmina, Microchip) with expert/champion legend.
- **Why:** consistency requirement — mirrors the recent dev deck's ask/team/champions exactly. The champion bench is the primary de-risker.
- **Visual:** ask header + gates timeline + use-of-funds bar; founders list with real photos; 5×2 champion grid with logos. Assets from `assets/team/` and `assets/logos/`.

### 09 — Close (`09-close.html`)
- **Says:** *your next decision is already assembling itself.* Recap strip: 3 days→40 min / 8→2 people / ≫10× / $2M seed open. CTA: see it on your data — 6-week pilot; or 20-min walkthrough → hello@metafloor.com.
- **Why:** end on the transformation + the four numbers + a low-friction next step (the pilot, not "invest").
- **Visual:** centered brand, ambient constellation background, recap strip, CTA button.

---

## 5. The reusable proof points (keep these identical everywhere)

| Fact | Value | Status |
|---|---|---|
| People per decision | 8 → 2 | defensible operational delta |
| Time to decide | 2–3 days → ~40 min | defensible operational delta |
| Systems reassembled by hand | 5+ | defensible |
| First signal visible before crisis | ~T−5 months | illustrative (memory-price event) |
| One-event protected value | ~$3.1M | illustrative, founder-input |
| Events per year | 12–20 | illustrative |
| Annual return shape | ≫10× | illustrative |
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

**Done:** all 9 slides built and browser-verified across green/ember/violet; no CXO/Compass references; value-first arc; logo added to cover; no overflow at 1280×720.

**Open / suggested next:**
- Replace illustrative dollar figures (Slides 5/7) with real pilot/model numbers once available — keep the "illustrative" labels until then.
- PDF export not yet wired for `deck2/` (dev has `export_pdf.py` — adapt it, don't rebuild).
- Consider a UC2 backtest demo link from the cover/close (Supriya's reactive-vs-proactive answer).
- Confirm founder titles/pedigree logos are current before any external send.
- If publishing, `deck2/` follows the same static-host path as the existing deck (GitHub Pages / slides.metafloor.com).

**The assignment (founder's own test):** present to one champion from the wall (not a friendly) and time how long before they ask about price or pilot — that's the slide that's working.
