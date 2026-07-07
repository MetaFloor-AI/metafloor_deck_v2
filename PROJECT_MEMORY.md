# PROJECT_MEMORY — MetaFloor investor deck (deck2/)

A standalone-HTML seed pitch deck. Each slide is its own file in `slides/`, a 1280×720 stage scaled by `deck.js`, themed via `<html data-theme>` (sage · ember · violet), assembled by the `index.html` iframe viewer + `slides.json` manifest. `STORY.md` is the source-of-truth narrative doc; read it before editing copy.

## [P1.S1] Deck v4 — trust-first restructure + pitch redesign (in progress)

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
