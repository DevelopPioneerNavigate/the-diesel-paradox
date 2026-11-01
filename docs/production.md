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
  chapter-40.md           # A Bill from the Universe
  chapter-41.md           # The Room That Wasn't Empty
  chapter-42.md           # The Observer at the Door
assets/
  brand/phasegate-blueprint.svg
  cover/approved-cover.jpg  # Preview only: approved artwork
  cover/source/           # Eight binary shards of the exact original approved PNG; SHA-256 pinned
scripts/
  validate_manuscript.py
  build_book.py
  build_accessible.py      # Reflowable EPUB & continuous TXT
  validate_accessible.py   # Exact 42-chapter paragraph check
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
python scripts/build_accessible.py
python scripts/validate_accessible.py
python scripts/build_report.py --pdf dist/The_Diesel_Paradox_Development.pdf --out dist/BUILD_REPORT.md
```

A GitHub Actions workflow validates the canon and produces **the official novel PDF**, a **reflowable audiobook-friendly EPUB**, **continuous TXT**, improved chapters-only listening PDF, and **BUILD_REPORT.md** as artifacts for each PR. Its GitHub Actions run summary explains, after each build, exactly how many chapters exist, word counts, PDF page count, and known blockers. An author-approved merge with the release marker publishes versioned PDF/EPUB/TXT assets to GitHub Releases; ordinary pushes cannot republish v1.0.0.

**Current manuscript:** Book One has all 42 chapters and is approved for official v1.0.0 publication. Chapter 42 re-examines the anchored optical packet with the 1984 R-7 Observer Reference clue, finds an uncertain second message in a private notation shared by Aaron and ASTRA, and preserves explicit alternative decodings and source ambiguity. **Creator-approved v1.0.0 public edition.** Full editorial/canon verification, proofreading, interior illustration approval, final pagination and creator release approval remain open. PG-1 stays retired, Axiom dismantled, Bellwether's four-block evacuation in force, and the Directorate's wider safety framework unsigned.

**Publication decision:** The author has approved the official release after extensive listening checks; CI also verifies full chapter and cover integrity. Further literary revisions, independent line edits and interior art can be added in later versions. See [the draft audit](book-one-draft-audit.md) for historical technical and editorial notes.

## Approved visual direction

The creator approved an image showing Diesel at his futuristic laboratory controls, with ASTRA as a holographic technological presence, and an immense PhaseGate / spacetime anomaly. The composition reads as high-stakes technological science fiction, not a romance book cover.

**Original approved cover restored without redesign:** The exact 1024 × 1536 lossless PNG artwork was extracted from the creator-approved chapters 1–25 edition. Because the GitHub connector limits the size of an individual upload, the 3,443,010 original PNG bytes are stored, in order, in **eight binary parts** at `assets/cover/source/approved-cover.png.part-01.bin` through `part-08.bin`. The PDF builder combines those bytes in memory, verifies SHA-256 `5ba1bd629ff9b7b86bbcc4e1a2f956f4965078989fe46e66d508d6f6cf976e06`, and renders that exact approved artwork. This is **not** a regenerated cover.

A high-quality JPEG at `assets/cover/approved-cover.jpg` exists for GitHub preview **only**, and is never used to generate the book's cover. If the creator later imports the standalone lossless PNG at `assets/cover/approved-cover.png`, the builder uses it after the same checksum verification (Issue #2 tracks this optional consolidation).

**Missing, incomplete or altered approved artwork must fail the build; never silently publish a placeholder or substitute a new cover.** The publishing job additionally checks both PDFs contain an embedded image on their cover pages.

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
5. Build **one authoritative official PDF edition** of each book, preserving the approved cover.
6. Validate page rendering, overflow, artifacts and chapter index.
7. Publish the versioned release with the creator-approved artwork and verified complete manuscript.


## Text-to-speech and accessibility compatibility

The original 1,032-page fixed-layout listening PDF repeated headers/footers on 1,031 pages, had approximately 29,248 extracted layout line breaks, and contained at least 121 page transitions interrupting sentences. Some speech-reading apps treated those layout markers as natural stopping points.

**Preferred listening file:** `dist/The_Diesel_Paradox_Book_One_Audio_Friendly.epub` (EPUB3 with EPUB2-compatible NCX; semantic, continuous paragraphs; 42-chapter nav; original checksum-pinned cover). **Fallback:** `dist/The_Diesel_Paradox_Book_One_Continuous_Text.txt` (plain UTF-8, no page furniture). Fixed-layout PDF is not the recommended audio source.

The PDF listening build removes repeated running text and duplicate chapter production headers, keeps typical paragraphs together where layout allows, and identifies the book accurately as a complete first draft rather than an unfinished manuscript. Do not claim this can force a particular third-party audiobook app to handle PDF reading correctly. CI compares every EPUB source paragraph against the original Markdown and rejects missing/altered content, bad book navigation, unverified cover, repeated PDF headers or missing finale.

Avoid hand-modifying any generated file. Run the source validators, then regenerate all editions in CI. Do not change or merge the original cover.


## Official v1.0.0 publication

Run `python scripts/build_book.py --out dist/The_Diesel_Paradox_Book_One.pdf` for the novel-only publication PDF. This book excludes research bibles and chapter plans and contains no development-status notices. Verify `python scripts/validate_publication.py` after building the PDF. The `--listening` option remains for a PDF with no running text; reflowable EPUB is preferred for TTS.

Version **v1.0.0** is created by GitHub Actions after the owner-approved merge, gated by full manuscript, PDF, accessible EPUB/TXT and cover integrity checks. The release artifact is `The_Diesel_Paradox_Book_One.pdf`; EPUB/TXT and optional listening PDF are attached alongside it. The exact creator-approved cinematic cover remains immutable.
