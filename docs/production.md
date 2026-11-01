# DPN Book Production

## Repository layout

```text
README.md
docs/
  series-bible.md         # Master canon V3.1
  book-one-outline.md     # Five acts / 42 chapters
  continuity.md           # Editorial gates
  art-direction.md        # Cover and illustration requirements
  production.md           # This guide
manuscript/book-01/
  chapter-01.md           # Full prose, not outline
  chapter-02.md           # Three Clocks, One Lie
  chapter-03.md           # The Origin Room
  chapter-04.md           # Stop Means Explode
  chapter-05.md           # The Eleven-Minute Window
  chapter-06.md           # Classified as Impossible
  chapter-07.md           # The Call They Can't Make
  chapter-08.md           # The First Debt
  chapter-09.md           # Heat Has to Go Somewhere
  chapter-10.md           # An Invention with Opinions
  chapter-11.md           # The Visitors
  chapter-12.md           # A Note in His Handwriting
  chapter-13.md           # The Quiet Room
  chapter-14.md           # The Woman in the Glass
  chapter-15.md           # Something That Counts
  chapter-16.md           # The Offer
  chapter-17.md           # A Signal Without a Sender
  chapter-18.md           # The Observing Machine
  chapter-19.md           # Cold Metal, Warm Hands
  chapter-20.md           # The Housekeeping Signal
  chapter-21.md           # A Courtesy Warning
  chapter-22.md           # An Expensive Question
  chapter-23.md           # The Dead Station
  chapter-24.md           # The Curator's Arithmetic
  chapter-25.md           # Twelve Seconds of Silence
  chapter-26.md           # A City on the Diagram
  chapter-27.md           # Red Clearance
  chapter-28.md           # The Emergency Nobody Invented Yet
  chapter-29.md           # The Wrong Rescue
  chapter-30.md           # Thirteen Minutes to Empty
  chapter-31.md           # The Promise
  chapter-32.md           # The First Laboratory Key
  chapter-33.md           # The Price of Stability
  chapter-34.md           # The Fourth Boundary
  chapter-35.md           # Third Option
  chapter-36.md           # The Argument's Last Test
  chapter-37.md           # ASTRA, Stay with Me
  chapter-38.md           # The Heat of an Impossible Decision
  chapter-39.md           # The Day the Future Stayed Dead
assets/
  brand/phasegate-blueprint.svg
  cover/approved-cover.jpg # Approved composition recovered from early edition; SHA-256 pinned
scripts/
  validate_manuscript.py
  build_book.py
.github/workflows/book-build.yml
requirements.txt
```

## Build and CI

Python 3.11 or newer.

```bash
python -m pip install -r requirements.txt
python scripts/validate_manuscript.py
python scripts/build_book.py --out dist/The_Diesel_Paradox_Development.pdf
python scripts/build_book.py --listening --out dist/The_Diesel_Paradox_Listening_Edition.pdf
python scripts/build_report.py --pdf dist/The_Diesel_Paradox_Development.pdf --out dist/BUILD_REPORT.md
```

A GitHub Actions workflow validates the canon and produces **the reference development PDF**, a **chapters-only listening PDF** with selectable text, and **BUILD_REPORT.md** as artifacts for each PR. Its GitHub Actions run summary explains, after each build, exactly how many chapters exist, word counts, PDF page count, and known blockers. After a reviewed merge to main, it can also publish the built PDF to `books/` as a repository file.

**Current manuscript:** 39 of 42 chapters drafted; Chapter 39 tests the original warning against a separately pre-registered post-stabilization hazard interval, finds no facility-loss event in that interval, and documents a corrected D-star proxy decline toward a nonzero observational plateau. The original packet remains physically preserved and its source unverified. Three chapters remain. PG-1 remains retired, Axiom dismantled, municipal evacuation still in force; no new field restart, demonstrated D-star conservation/transfer, or municipal re-entry authorization is implied by a passing build.

**Do not mistake successful PDF generation for manuscript completeness.** Unwritten chapters remain unwritten.

## Approved visual direction

The creator approved an image showing Diesel at his futuristic laboratory controls, with ASTRA as a holographic technological presence, and an immense PhaseGate / spacetime anomaly. The composition reads as high-stakes technological science fiction, not a romance book cover.

**Cover restoration:** The original cinematic composition was recovered from the creator-approved chapters 1–25 edition and is now committed at `assets/cover/approved-cover.jpg` as a visually faithful, high-quality JPEG derivative (1024 × 1536). This is the same approved illustration, not a generated or redesigned cover. The exact lossless extracted PNG is available separately to the creator and may be imported later at `assets/cover/approved-cover.png` (tracked by Issue #2).

The PDF builder prefers the **verified PNG** when present and otherwise uses the committed **verified JPEG**. Both accepted image files are SHA-256 locked in `scripts/build_book.py`. **Missing or altered artwork must fail the build; never silently publish a placeholder or substitute a new cover.** The publishing job also checks both PDFs contain a cover image.

### Artwork conventions

- `assets/interior/<chapter>-<scene>.png` or `.jpg`.
- 300 DPI minimum at intended print size for production.
- Match approved DPN black/crimson direction; subtle binary visual treatment, red lighting, engineered hardware.
- Scene art belongs close to the relevant scene; no dumping all images into an appendix.
- Invented labels and scientific diagrams must match the current technology bible.
- ASTRA and Diesel stand together as scientific partners, not default romantic couple posing.

## Publication pipeline

1. Write and review chapters individually.
2. Update canon / timeline when discoveries change.
3. Generate and validate the development PDF.
4. Add approved cover and interior illustrations.
5. Build **one authoritative illustrated edition** of each book.
6. Validate page rendering, overflow, artifacts and chapter index.
7. Approve a release only after manuscript and art are complete.
