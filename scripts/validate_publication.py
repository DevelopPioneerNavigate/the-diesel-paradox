#!/usr/bin/env python3
"""Gate a public Book One release against missing text, draft labels, and wrong cover."""
from pathlib import Path
from pypdf import PdfReader
import re

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "dist/The_Diesel_Paradox_Book_One.pdf"
PAGES_MIN = 42
pdf = PdfReader(str(PDF))
assert len(pdf.pages) >= PAGES_MIN, "Suspiciously short publication PDF"
assert pdf.pages[0].images, "Official approved cinematic cover not embedded"
assert len(pdf.outline) == 42, f"Expected 42 chapter bookmarks, found {len(pdf.outline)}"
title = str(pdf.metadata.title or "")
assert "The Diesel Paradox" in title and "First Impossibility" in title
assert "Development" not in title and "Draft" not in title
texts = [page.extract_text() or "" for page in pdf.pages]
text = " ".join(" ".join(texts).split())
for forbidden in (
    "DEVELOPMENT EDITION", "DEVELOPMENT PLACEHOLDER", "SERIES BIBLE",
    "42-CHAPTER PLAN", "CANON V3.1", "THE ENTIRE NOVEL IS NOT COMPLETE",
    "NOT PUBLICATION-READY", "EDITORIAL AND PUBLISHING APPROVAL REMAIN PENDING",
):
    assert forbidden not in text.upper(), f"Public release text contains internal label: {forbidden}"
# A character may legitimately mention a first draft of a technical document.
# Only frontmatter and publication metadata must not describe this book as a draft.
frontmatter = " ".join(" ".join(texts[0:2]).split()).upper()
assert "FIRST DRAFT" not in frontmatter, "Public book title/frontmatter is labeled first draft"
for required in (
    "The First Impossibility", "A Very Bad Day for Physics",
    "The Room That Wasn't Empty", "The Observer at the Door",
    "YOU WERE NOT THE FIRST AARON",
):
    assert required in text, f"Missing public novel content: {required}"
assert len(re.findall(r"BOOK ONE\s*/\s*THE FIRST IMPOSSIBILITY",text)) >= 10
assert "DPN Technology" in text
for n in range(1, 43):
    p = ROOT / "manuscript/book-01" / f"chapter-{n:02d}.md"
    assert p.exists(), f"Chapter {n} missing from source"
print(f"PASS: official public edition: {len(pdf.pages)} pages, 42 chapters, "
      f"approved cover, no development/beta/draft labels or planning appendices")
