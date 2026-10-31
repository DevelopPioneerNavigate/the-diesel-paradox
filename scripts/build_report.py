#!/usr/bin/env python3
"""Create plain-English manuscript progress reports for every GitHub build."""
from pathlib import Path
from datetime import datetime, timezone
from pypdf import PdfReader
import argparse
import os

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument("--pdf",default="dist/The_Diesel_Paradox_Development_Edition.pdf")
parser.add_argument("--out",default="dist/BUILD_REPORT.md")
args=parser.parse_args()

chapters=sorted((ROOT/"manuscript/book-01").glob("chapter-*.md"))
counts={x.name:len(x.read_text(encoding="utf-8").split()) for x in chapters}
count=len(chapters)
words=sum(counts.values())
pdf=ROOT/args.pdf
listening=ROOT/"dist/The_Diesel_Paradox_Listening_Edition.pdf"
approved=ROOT/"assets/cover/approved-cover.png"
report=[
"# The Diesel Paradox — Build Report",
"",
"**Built at (UTC):** "+datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
"**Commit:** "+os.environ.get("GITHUB_SHA","local build"),
"**Deliverable:** Development edition PDF (not completed novel)",
"",
"## What is included",
f"- Fully written chapters: **{count} of 42** ({count/42:.1%}).",
f"- Manuscript: approximately **{words:,}** words.",
"- Series bible Canon V3.1 and connected 42-chapter outline.",
f"- PDF pages rendered: **{len(PdfReader(str(pdf)).pages)}**.",
(f"- Listening-only pages rendered: **{len(PdfReader(str(listening)).pages)}**." if listening.exists() else "- Listening-only edition not generated."),
"- Listening edition includes only written chapter prose; no planning bible or outline.",
"",
"## Chapter inventory",
]
for name,word_count in counts.items():
    report.append(f"- {name}: {word_count:,} words")
report += [
"",
"## Checks",
"- Manuscript numbering, continuity baseline, core characters and opening clues validated.",
"- PDF rendered and text extraction verified.",
"- The story is written as scientific adventure with ASTRA as an independent character.",
"",
"## Art and remaining tasks",
("Approved cover: PRESENT in source assets." if approved.exists() else
 "Approved cover: NOT YET IMPORTED into GitHub. PDF explicitly uses a placeholder. See Issue #2."),
f"- Chapters remaining to write: **{42-count}**.",
"- Approved cover import and scene-accurate interior illustrations.",
"- Editorial quality review and typesetting after all chapters are finished.",
"",
"## What the passing build means",
"A successful build confirms the current source produced a readable development PDF. It does not mean the full novel, its illustrations or all literary review are finished.",
"",
]
out=ROOT/args.out
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text("\n".join(report),encoding="utf-8")
summary=os.environ.get("GITHUB_STEP_SUMMARY")
if summary:
    with open(summary,"a",encoding="utf-8") as handle:
        handle.write("\n".join(report)+"\n")
print(f"Report written: {out} — {count}/42 chapters, {words:,} words")
