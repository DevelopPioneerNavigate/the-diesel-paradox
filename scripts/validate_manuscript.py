#!/usr/bin/env python3
"""Fast canon/manuscript validation, with no paid tokens or remote APIs."""
from pathlib import Path
import re
import sys

root=Path(__file__).resolve().parents[1]
bible=(root/"docs/series-bible.md").read_text(encoding="utf-8")
outline=(root/"docs/book-one-outline.md").read_text(encoding="utf-8")
drafts=sorted((root/"manuscript/book-01").glob("chapter-*.md"))
errors=[]
def check(test,message):
    if not test: errors.append(message)
for token in ("Aaron Diesel","ASTRA","Boundary-Response Manifold"):
    check(token in bible, "Series bible missing "+token)
check("love" in bible.lower(), "Series bible missing emotional canon")
found=re.findall(r"(?m)^\*\*(\d{2})\. ",outline)
check(found==[f"{n:02}" for n in range(1,43)],"Expected ordered outline of chapters 01–42")
check(len(drafts)>0, "No written chapters")
nums=[int(p.stem.split("-")[-1]) for p in drafts]
check(nums==list(range(1,len(nums)+1)),"Written chapters are not consecutively numbered")
for p in drafts:
    story=p.read_text(encoding="utf-8")
    check(len(story.split())>500, p.name+" is not full prose")
    check("Diesel" in story and "ASTRA" in story,p.name+" is missing a main character")
    if p.name=="chapter-28.md":
        check(3500<=len(story.split())<=5000,"Chapter 28 must be 3500-5000 full-prose words")
        check("DAI-01" in story and "NO DEMONSTRATED EXTERNAL BRM COUPLING" in story,
              "Chapter 28 must preserve residual-state safety and evidence boundaries")
        check("The next emergency" in story and "CONTINGENCY EQUIPMENT CUSTODY" in story,
              "Chapter 28 must preserve the setup for Chapter 29")
    if p.name=="chapter-27.md":
        check(3500<=len(story.split())<=5000,"Chapter 27 must be 3500-5000 full-prose words")
        check("BELLWETHER INCIDENT" in story and "NO VERIFIED BRM SIGNATURE" in story,
              "Chapter 27 must preserve municipal and evidence boundaries")
opening=(root/"manuscript/book-01/chapter-01.md").read_text(encoding="utf-8")
check("LANTERN" in opening and "THANK YOU FOR NOT TURNING IT OFF" in opening,"Opening technical clues missing")
print(f"Checked 42 planned chapters; {len(drafts)} complete manuscript chapters.")
for chapter in drafts:print(f"  {chapter.name}: {len(chapter.read_text(encoding='utf-8').split())} words")
if errors:
    for err in errors:print("FAIL:",err,file=sys.stderr)
    raise SystemExit(1)
print("PASS: core canon and manuscript checks")
