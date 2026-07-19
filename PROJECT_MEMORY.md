# PROJECT_MEMORY — MetaFloor investor deck (deck2/)

A standalone-HTML seed pitch deck. Each slide is its own file in `slides/`, a 1280×720 stage scaled by `deck.js`, themed via `<html data-theme>` (sage · ember · violet), assembled by the `index.html` iframe viewer + `slides.json` manifest. `STORY.md` is the source-of-truth narrative doc; read it before editing copy.

## [P1.S6] Appendix B4 — "The Moat" slide, ported (2026-07-19, done)
- **`slides/B4-moat.html`** — ported the moat slide (**"Short the model. Long the memory."**) from `~/projects/metafloorv2/outreach/mf-supplychain++/deck/slides/04-moat.html` into deck2 as **appendix B4**. Inserted in `slides.json` as the new **last-but-one** slide (after `solution`/B3, before `architecture`/B1). Order tail: …`close` · `solution` (B3) · **`moat-stack` (B4)** · `architecture` (B1) → 16 slides total.
- Same porting method as B3: **Inter / JetBrains Mono** fonts, deck2 slide chrome, full **`--ac*` accent ramp** (theme switcher drives the MEMORY layer + all accents across sage · ember · violet; the ENTERPRISE "where value lands" band + "all ours" bracket stay fixed sage by design). Mapped the four vars deck2 lacks — `--ac-fill2`, `--ac-fill3`, `--ac-ink2`, `--ac-bd2` — onto deck2 tokens; ported the source `.vs` crowd-vs-us component into the slide's local CSS.
- Keeps **both views** + the "Simplify this / Full detail" toggle: detailed = isometric 6-layer "all ours" stack (MEMORY compounds, MODEL is the dashed swappable slab) + trust-primitives card + crowd-vs-us table; simple = flat model-swap-⇄-chain vs compounding-memory-bars contrast.
- Verified via Playwright: both views + all three themes render correctly, fit the 1280×720 stage. Fixed the simple view's far-right "value retained" edge label (was clipping at the viewBox edge) → right-anchored inside the card, dashed rule pulled back to x=1044.
- **PDF regenerated** (`MetaFloor_Deck.pdf`, **16 slides**, 5.33 MB, png @3x) via `export_pdf.py` (needs `img2pdf` — `pip install img2pdf`). B3=#14, B4=#15, architecture=#16.

## [P1.S5] Cover incorporation line + desks footer + GTM spacing (2026-07-19, done)
- **Cover (`01-cover.html`):** added **"Delaware entity · Incorporated Sep 2025"** as a muted mono line under the "Seed Round · 2026" pill (right footer; new `.cv-foot-right` column stacks pill + `.incorp`).
- **Desks (`05-desks.html`):** footer right-side `.diff` was wrapping to two lines (orphan "use.") and misaligned → now a single **flush-right** line (`white-space:nowrap`, dropped `max-width:40ch`).
- **GTM (`10-gtm.html`):** compacted the design-partners block ~20% (padding/chips/note→one line) and reclaimed the space as **center whitespace** (more air under the hero + above the Land/Prove/Expand cards).
- PDF regenerated (15 slides incl. B3).

## [P1.S4] Appendix B3 — "The Loop" slide, ported (2026-07-19, done)
- **`slides/B3-solution.html`** — ported the supply-chain loop slide (capture → govern → let agents act) from `~/projects/metafloorv2/outreach/mf-supplychain++/deck/slides/03-solution.html` into deck2 as **appendix B3**. Inserted in `slides.json` as the **last-but-one** slide (before `B1-architecture`). Order tail: …`close` · **`solution` (B3)** · `architecture` (B1) → 15 slides total.
- Rebuilt on deck2's design system: **Inter / JetBrains Mono** fonts (swapped from Hanken Grotesk / IBM Plex Mono), deck2 slide chrome (`.deck>.slide>.stage>.canvas`, `../theme.css`, `../deck.js`), and the full **`--ac*` accent ramp** so the theme/color switcher drives the entire diagram across **sage · ember · violet**. The **capture plane stays fixed green by design** (source's "human capture" signal). Mapped the three vars deck2 lacks — `--ac-fill2`, `--ac-fill3`, `--ac-ink2` — onto deck2 tokens locally in the slide.
- Keeps **both views** + the **"Simplify this / Full detail"** toggle (rebuilt on deck2's accent pill via `.slide:has(.simplify-input:checked)`): detailed 3-plane loop diagram ↔ live supply-chain message-feed scenario. Dropped the source deck's `deep-dive` link + `.wm` watermark (not part of deck2 vocab).
- Verified via Playwright: both views + all three themes render correctly, fit the 1280×720 stage, switcher present. Placement per founder ("last but one"); offered to relocate if a post-appendix closing slide is intended.

## Publish / deploy (2026-07-09)
- **Git remote:** `origin` → `git@github-org:MetaFloor-AI/metafloor_deck_v2.git` (public org repo, committed as `arun@metafloor.ai`). v1 remote preserved as `origin-v1` (`arunsanthakumar/metafloor-deck`).
- **Hosting:** GitHub Pages off `master` / root. Custom domain **slides.metafloor.ai** via `CNAME` file + `.nojekyll`. DNS: a `CNAME slides → metafloor-ai.github.io` record must exist at the metafloor.ai registrar (owner action).
- The published site is **public** — real champion names/roles + illustrative financials are exposed (founder-approved 2026-07-09).
- **Refinement pass (2026-07-10):** cover reworded to "MetaFloor holds…" + icon-chip blocks; hook numbers up (~$150K/hr · 6–8 systems · dozens of people) + cleaner gap line; tax "the quiet one" accent; **field slide (`B2-field.html`) rebuilt in the dev/field.html scorecard format** — 4 pillars (active capture · governed memory · accountable fleet · vertical depth) × 6 named competitor lanes (o9/Kinaxis/BY, Everstream/Resilinc/Interos, Glean/Copilot/Palantir, Sierra/Agentforce/ServiceNow, Guru/Notion/Starmind, Sentra/Augment/bluefabric), MetaFloor the only full row; **GTM bench → dark block, all 10 as "our champions"** (logos inverted white, no experts/legend/dots).
- **PDF export:** `python3 export_pdf.py [out.pdf]` — Playwright renders each visible slide (`slides.json`) at 3× off the `.stage`, waits for entrance animations, hides the theme switcher, assembles a raster PDF via `img2pdf`. Auto-tunes to a **3–9.5 MB** window (PNG @3x ≈ 4 MB; re-encodes to JPEG if over, bumps scale if under). Interactive slides (ROI, desks) are captured in their **default** state. Output `MetaFloor_Deck.pdf` committed (downloadable at slides.metafloor.ai/MetaFloor_Deck.pdf); `_deck_frames/` gitignored.

## [P1.S3] Anup feedback pass — design partners + Delta Group + fee (2026-07-19, done)

Anup review edits to the live deck (`master`, published at slides.metafloor.ai):

- **GTM (`slides/10-gtm.html`):**
  - **Design partners** now a **highlighted block BELOW the leaders bench** (was a strip above): green-tinted (`--ac-soft`) card with accent left-border, holding **WLS Stamping · Plumage Technologies · ASM Technologies · Digicom** as white chips + a note line: *"Medium-sized companies — our product-discovery testbed. Not our ideal customer size, but they help us design the product."* (Plumage/ASM/Digicom are real entities in the history_bldr live data.)
  - Bench relabeled **"now scaling to large customers"**; **Land/Prove/Expand trimmed ~10%** (padding/font) to reclaim the space.
  - **Removed Microchip / Daniel Jackson; added Shane Nunes / Delta Group Electronics.** Logo is the **real** Delta Group Electronics wordmark: pulled `deltrgroup-logo.png` from deltagroupinc.com, cropped to the "DELTA GROUP" band, made bg transparent, removed a stray icon sliver → `assets/logos/deltagroup.png` (renders white via the bench `grayscale/brightness(0)/invert` filter).
  - **OPEN:** Shane Nunes' exact **title** unverified (web only shows a "Shane Nunes" as COO@Universal Instruments; Delta Group Electronics lists no Shane) — `.rl` shows company only, flagged with a `TODO(anup)` HTML comment. Every other bench entry has a title; drop it in when Anup confirms.

- **ROI (`slides/09-roi.html`):** MetaFloor **medium fee $0.20M → $0.25M** (data `PROFILES.medium.fee` + static defaults). `render("medium")` recomputes: gross $1.77M, net **$1.52M**, **~7×** value, **~7 wks** payback. Large/XL fees unchanged.

- **PDF** regenerated (`MetaFloor_Deck.pdf`, 14 slides, ~3.9 MB). Both changed pages (7 ROI, 11 GTM) visually verified via 3× render.

## [P1.S2] Deck v5 — story rebuild for an UNASSUMING investor (2026-07-09, in progress)

Founder verdict on v4: **too vague AND too specific** for an investor who doesn't even know supply-chain disruptions exist — opens on an insider metric ("8 people scrambling → 2 deciding") and drowns in jargon (allocation/CBAM/expedite/NRR). The PDF `~/Desktop/MetaFloor_SupplyChain_ROI_Deck.pdf` reads clearer (one grammar/slide, huge whitespace, sage restraint) but is **ungrounded** (fabricated ROI as fact) and is a *customer* deck. **Decision: steal the PDF's clarity, keep deck2's honesty, and GROUND the product story in the real `sc_v1` demos.**

**Key grounding source (NEW):** `~/projects/metafloorv2/prototypes/sc_v1` is a real, working, clickable demo — a five-act spine (detect → assemble → decide/crisis → backtest → CM bridge) across **three real desks**: **Solara** (buyer), **Google Pixel** (launch war-room), **Cable** (Supriya Iyer's verbatim incident-ops scenario). See `sc_v1/COOKBOOK.md` + `demos/*/COOKBOOK.md`. These replace deck2's vague "consequential decision events" with concrete, legible flows.

**New story arc (approved + built):** Cover → **Hook: the cable cut** (a legible scene: $50k/hr, 30h to assemble by hand) → **The weekly tax** (4 leak places) → **The model** (Watch/Assemble/Approve + compounding loop) → **3 desks** (buyer/launch/incident from sc_v1) → Value → **Interactive ROI** → Why-now → Moat → **Team+bench** → Ask → Close.

**Built this session (new files, sage pitch template, browser-verified at 1280×720):**
- `01-cover.html` (airy PDF-style, tight headline + 3 "Watches/Assembles/Acts" blocks), `02-hook.html` (cable-cut scene, left=bullets, dark "that gap is the product" callout, right cost column), `03-tax.html` (4 leak **cards**, line+cost-chip, no paragraphs), `04-model.html` (3 step **cards** w/ bullets + dark compounding band), **`05-desks.html` (MERGED 3 desks → ONE slide with a JS desk toggle Buyer/Launch/Incident; 5-beat card flow, line+bullets, key beat accent-tinted, ⚡vs⏳ band — all update on toggle)**, `05-value.html` (3 accent-top cards + dark standing-value band), `09-roi.html` (**interactive M/L/XL toggle — vanilla JS recomputes the whole model live**; medium≈9×/6wks, large≈12×, xl≈14×; all illustrative), `11-team.html` (founder photos+names+roles, 10 champion logos grayscale wall).
- `slides.json` rewired to the new **13-core + 2-appendix** order. Superseded single-desk files `05-desk-buyer/06-desk-launch/07-desk-incident.html` still on disk (out of manifest) — delete once the merge is signed off.
- **Slide-polish doctrine (founder, this pass):** less paragraph, more **line + bullets**; visual blocks/cards for separation; hard-hitting short text; interactive toggles where a comparison exists (desks, ROI). BUT do not over-compress: **slide 5 desks must carry real context** — the event, the systems it reads, the response flow with concrete artifacts (DP-2026-0731, 47-days-stale catch), what it executes into. One-word fragments = "arbitrary/clueless" (founder rejected). Now rebuilt from `sc_v1` with an event bar + system chips + detailed 5-beat flow.
- **Slide 07-moat reframed:** "We own the model and the framework. You own the memory." ownership stack (your agents ⇄ ours [open] · decision memory [yours·moat] · framework [ours] · model [ours⇄]) + tagline "Build your own agents — they talk to ours." Kept the MIT-95%-zero-ROI callout.
- **NEW slide `10-gtm.html` (GTM):** land→prove→expand + the **real 10-leader bench** (names/roles/logos + champion vs expert legend), sourced from `deck_feb26/dev/deck_slides/ask.html`. Champions: Sudarshan Seshadri (Blue Yonder), Prem Jain (AMD), Prakash Seshadri (GE Vernova), Mitch Haynes (Juniper). Experts: Mondher Ben-Hamida (NetApp), Supriya Iyer (Google), Arun Krishnan (AstraZeneca), Sundar Kamath (Sanmina), Cassie Gruber (Jabil), Daniel Jackson (Microchip). Founders live on the **ask** slide (10-ask.html), not here. `slides.json` team→gtm. `11-team.html` now unused.

**Pending (next):** reconcile the REUSED older slides still in the flow — `05-value.html`, `why-now.html`, `07-moat.html`, `10-ask.html` (**strip its team block — now duplicated by 11-team**), `11-close.html` — to the new voice/order; rebuild `11-close`; decide whether Proof/Numbers/Trust/Prize-Path (now displaced) go to appendix. Founder-input still needed: Sridhar's last name, exact founder pedigrees/exit names, real pilot/backtest numbers to replace illustrative ROI.

## [P1.S1] Deck v4 — trust-first restructure + pitch redesign (superseded by S2 story rebuild)

Save-point commit: the deck is restructured to the trust-first spine and the visual "pitch pass" has started (sage palette, chrome removed, Numbers rebuilt as the hero template). Remaining: roll the redesign across the other 8 core slides + build appendix slides for displaced detail. Full plan: `~/.gstack/projects/deck2/arun-master-design-20260707-redesign.md`.

## Done
- **Trust-first restructure** (11 core + 2 backup): Cover · Problem · Product · **Proof** (moved to 4) · Value · Numbers · Moat · **Trust (new)** · **Prize & Path (merged Market+Vision)** · Ask · Close · +B1 Architecture, B2 Field. Headlines read as one story top to bottom.
- **New Proof slide** (backtest-on-your-own-history), **re-scoped Ask** to seed milestones (10 champions → 3–4 paid design partners → validated → Series-A ready, not "$3M ARR/NRR>120%"), **governance "safe to own" strip** on Moat, positioning unified to **"the decision layer for supply chain"** (founder-overridable).
- Global-bleed citations (McKinsey/S&P/Interos), split event/standing-value ledger, four customer-lens overclaim fixes.
- **Visual redesign started (v4 "pitch pass"):** palette switched **green → sage** (muted); **macOS window chrome killed globally** (`.titlebar` hidden in theme.css pitch layer); **Numbers rebuilt as a hero-number slide** (archetype B: giant $3.1M + a readable "the year" support panel). This is the approved template.

## Pending (next)
- Roll the pitch redesign across the other 8 core slides using **CUT vs CONCENTRATE**:
  - CONCENTRATE (keep the one good visual, strip the rest): 02 Problem (drift chart), 03 Product (Assemble decision-package), 04 Proof (replay timeline).
  - CUT (bloated → one idea + support panel): 05 Value (3 tiles), 07 Moat (decision-memory claim as hero), 09 Prize (staircase; rings cut), 10 Ask (**split into two** slides).
- **Create appendix slides (B3–B5)** for displaced density (split ledger + waterfall, both problem charts + citations, the six-value grid) — do NOT delete content, relocate it.
- Apply the hard grid/type/motion/contrast spec from the approved plan (`~/.gstack/projects/deck2/arun-master-design-20260707-redesign.md`).

## Key decisions
- Story/order/copy are settled; the redesign is **visual + density only**.
- One dominant focal point per slide + one subordinate support; generous margins; mono for numbers only; sage accent used sparingly.
- Keep the mac-window motif ONLY where it is literally product UI (cover console, product decision-package); kill it as decoration everywhere else.
- Green-only restraint (no warm secondary); cut TAM rings, keep the land→expand→network staircase.

## Risks / open
- **All dollar figures are illustrative.** The one thing still missing is real pilot data — the standing assignment is a real backtest on a champion's data (Supriya @ Google / Mondher @ NetApp), which converts the Proof/Numbers/Ask from promise to evidence.
- Over-simplification risk in the redesign (founder flagged the first exemplar as "somewhat overly simplified" — keep substance, don't lose valid info).

## Security
- Static HTML/CSS/JS deck, no backend, no secrets, no PII beyond public founder/champion names already used in the pitch.

## Run / view
- `python3 -m http.server 8787` in `deck2/`, open `http://localhost:8787/index.html`. Individual slides also open directly via `file://` (the viewer falls back to an inline slide list when `slides.json` can't be fetched).
