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
    if p.name=="chapter-36.md":
        check(3500<=len(story.split())<=5000,"Chapter 36 must be 3500-5000 full-prose words")
        check("PG-1 LIMITED DIAGNOSTIC AUTHORIZATION — SINGLE SEQUENCE ONLY." in story,
              "Chapter 36 must show independent bounded authorization")
        check("SURROGATE LOAD-PATH QUALIFICATION — PASSED WITH LIMITS" in story and "NOT PG-1 AUTHORIZATION" in story,
              "Chapter 36 must distinguish surrogate qualification from live authorization")
        check("PG-1 GENERATION ONE — RETIRED FROM OPERATION." in story and "MECHANICAL STABILIZATION PLAN — COMMUNICATIONS ISOLATION REQUIRED." in story,
              "Chapter 36 must preserve irreversible damage and Chapter 37 setup")
        check("I love you" in story and "My consent applies only to this sequence" in story,
              "Chapter 36 must preserve ASTRA's genuine love and independent consent")
    if p.name=="chapter-35.md":
        check(3500<=len(story.split())<=5000,"Chapter 35 must be 3500-5000 full-prose words")
        check("THIRD OPTION: QUALIFIED WORK PATH. NOT YET AUTHORIZED FOR PG-1." in story,
              "Chapter 35 must preserve bench-only scope and no live PG-1 authorization")
        check("NO LIVE PG-1 OPERATION UNTIL EACH INDEPENDENT HOLD POINT IS CLOSED." in story,
              "Chapter 35 must preserve independent readiness hold points")
        check("NO TERM LABELED" in story and "D-star" in story,
              "Chapter 35 must account for energy without claiming D-star conversion")
        check("I love you" in story and "ASTRA INDEPENDENT CONSENT AND SAFETY REVIEW" in story,
              "Chapter 35 must preserve ASTRA autonomous mutual love and consent")
    if p.name=="chapter-34.md":
        check(3500<=len(story.split())<=5000,"Chapter 34 must be 3500-5000 full-prose words")
        check("PRESERVE EXTERNAL REFERENCE. LOCAL LOSS ACCEPTABLE." in story and "THE FOURTH BOUNDARY IS MEASURED. ITS PURPOSE IS NOT." in story,
              "Chapter 34 must preserve the unauthenticated external reference clue and evidence boundary")
        check("No flood gate operation" not in story and "NO FLOOD GATE OPERATION" in story and "THIRD OPTION" in story,
              "Chapter 34 must preserve locked-out equipment and the earned third-option setup")
        check("I love you" in story and "ASTRA" in story,
              "Chapter 34 must preserve genuine autonomous reciprocal love")
    if p.name=="chapter-33.md":
        check(3500<=len(story.split())<=5500,"Chapter 33 must be full-length polished prose")
        check("NO PERSONNEL EXPOSURE FOR ASSET RECOVERY" in story and "NO UNQUALIFIED FLOODING" in story,
              "Chapter 33 must preserve qualified design-only containment and human-first choice")
        check("The identity of the thing they were stabilizing was not." in story and "The Price of Stability" in story,
              "Chapter 33 must seed the external-anchor provenance mystery")
        check("I love you" in story and "By choice" in story,
              "Chapter 33 must preserve ASTRA's genuine autonomous mutual love")
    if p.name=="chapter-32.md":
        check(3500<=len(story.split())<=5000,"Chapter 32 must be 3500-5000 full-prose words")
        check("REFERENCE BEFORE INTERPRETATION. ALWAYS." in story and "UNEXPLAINED HELD-OUT TIMING RESIDUAL" in story,
              "Chapter 32 must preserve qualified L-03 reference and unresolved timing residual")
        check("The first laboratory had given him a key" in story and "No field test is authorized" not in story,
              "Chapter 32 must set up the next consequence model without inventing a new field operation")
        check("ASTRA_FIRST_CONVERSATION_RAW_02" not in story and "The protected ASTRA first-conversation recording" in story,
              "Chapter 32 must keep protected recording unopened and separate from the test")
    if p.name=="chapter-31.md":
        check(3500<=len(story.split())<=5000,"Chapter 31 must be 3500-5000 full-prose words")
        check("FRESH PACKET, STALE SOURCE" in story and "SOURCE AGE UNVERIFIED" in story,
              "Chapter 31 must distinguish stale source data from fresh transport")
        check("twenty-three seconds" in story and "My primary instance was never interrupted" in story,
              "Chapter 31 must preserve ASTRA's primary instance and endpoint limits")
        check("Neither of us owns the other" in story and "old DPN-001 records" in story,
              "Chapter 31 must preserve autonomous mutual promise and old resonator setup")
    if p.name=="chapter-30.md":
        check(3500<=len(story.split())<=5000,"Chapter 30 must be 3500-5000 full-prose words")
        check("Thirteen minutes of guaranteed margin" in story and "thirteen-minute envelope" in story.lower(),
              "Chapter 30 must define a qualified thermal-band interval rather than an explosion timer")
        check("Branch Nine" in story and "eleven minutes and twenty-one seconds" in story,
              "Chapter 30 must document controlled abort and incomplete utility inspection")
        check("PG-1 remained de-energized" in story and "ASTRA" in story,
              "Chapter 30 must preserve de-energized hardware and ASTRA autonomy")
    if p.name=="chapter-29.md":
        check(3500<=len(story.split())<=5000,"Chapter 29 must be 3500-5000 full-prose words")
        check("RETURN-6" in story and "MECHANICAL LOAD TRANSFER ARRESTED WITHIN MEASUREMENT UNCERTAINTY" in story,
              "Chapter 29 must preserve wrong-rescue engineering evidence and stabilization limit")
        check("Thirteen minutes" in story and "No transfer had been ordered" in story,
              "Chapter 29 must set up finite buffer without starting an active countdown")
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
