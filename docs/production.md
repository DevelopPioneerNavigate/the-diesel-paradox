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
  chapter-02.md           # Subsequent chapter if drafted
assets/
  brand/phasegate-blueprint.svg
  cover/                  # Approved full-resolution cover goes here
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
```

A GitHub Actions workflow validates the canon and produces the **development PDF** as a workflow artifact for each PR. After a reviewed merge to main, it can also publish the built PDF to `books/` as a repository file.

**Do not mistake successful PDF generation for manuscript completeness.** Unwritten chapters remain unwritten.

## Approved visual direction

The creator approved an image showing Diesel at his futuristic laboratory controls, with ASTRA as a holographic technological presence, and an immense PhaseGate / spacetime anomaly. The composition reads as high-stakes technological science fiction, not a romance book cover.

The approved artwork currently exists in the creator's ChatGPT development edition. Place its full-resolution source at:

```text
assets/cover/approved-cover.png
```

The PDF builder automatically uses this exact file when present. Until it is in the repo, the builder uses an explicit **development placeholder** cover rather than falsely claiming the real asset is embedded.

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
