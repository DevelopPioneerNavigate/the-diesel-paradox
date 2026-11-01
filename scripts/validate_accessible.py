#!/usr/bin/env python3
"""Fail CI if the audiobook-friendly reading formats lose prose or reintroduce page noise."""
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
import hashlib
import re
from pypdf import PdfReader
from build_accessible import source_files, prose_blocks, strip_md, title_of, COVER_SHA256

ROOT=Path(__file__).resolve().parents[1]
epub=ROOT/"dist/The_Diesel_Paradox_Book_One_Audio_Friendly.epub"
txt=ROOT/"dist/The_Diesel_Paradox_Book_One_Continuous_Text.txt"
pdf=ROOT/"dist/The_Diesel_Paradox_Listening_Edition.pdf"
chapters=source_files()
text=txt.read_text(encoding="utf-8")
assert "The entire novel is not complete" not in text
assert text.count("DPN TECHNOLOGY  /  THE DIESEL PARADOX")==0
assert len(chapters)==42
ns={"h":"http://www.w3.org/1999/xhtml","opf":"http://www.idpf.org/2007/opf"}
with ZipFile(epub) as z:
    assert z.namelist()[0]=="mimetype" and z.read("mimetype")==b"application/epub+zip"
    assert z.getinfo("mimetype").compress_type==0
    cover=z.read("OEBPS/images/approved-cover.png")
    assert hashlib.sha256(cover).hexdigest()==COVER_SHA256, "Cover bytes do not match approved original"
    toc=ET.fromstring(z.read("OEBPS/nav.xhtml"))
    navlinks=toc.findall(".//h:nav/h:ol/h:li/h:a",ns)
    assert len(navlinks)==42, f"EPUB chapter navigation has {len(navlinks)} entries"
    opf=ET.fromstring(z.read("OEBPS/content.opf"))
    assert len(opf.findall(".//opf:spine/opf:itemref",ns))==43, "EPUB spine must be cover plus 42 chapters"
    for n,path in enumerate(chapters,1):
        src=path.read_text(encoding="utf-8")
        title=title_of(src)
        tree=ET.fromstring(z.read(f"OEBPS/chapter-{n:02d}.xhtml"))
        headings=tree.findall(".//h:h1",ns)
        assert len(headings)==1 and "".join(headings[0].itertext())==title, f"Wrong Chapter {n} heading"
        pnodes=tree.findall(".//h:section/h:p",ns)
        actual=["".join(p.itertext()) for p in pnodes]
        expected=[strip_md(s) for kind,s in prose_blocks(src) if kind=="paragraph"]
        assert actual==expected, f"Chapter {n} prose differs from source, {len(actual)} vs {len(expected)} paragraphs"
        assert all("\n" not in s for s in actual), f"Chapter {n} contains hard-wrapped prose"
        assert title in text and expected[0] in text and expected[-1] in text, f"TXT lost Chapter {n} content"
    assert "YOU WERE NOT THE FIRST AARON" in text, "Finale missing in continuous text"
reader=PdfReader(pdf)
assert len(reader.outline)==42, "Listening PDF lost chapter bookmarks"
pages=[page.extract_text() or "" for page in reader.pages]
assert len(pages)>42
assert sum("DPN TECHNOLOGY  /  THE DIESEL PARADOX" in page for page in pages)==0, "PDF contains repeating speech-disrupting headers"
assert sum("LISTENING EDITION  /  CANON V3.1" in page for page in pages)==0, "PDF contains repeating speech-disrupting footers"
assert "The entire novel is not complete" not in " ".join(pages), "PDF still claims full draft incomplete"
assert "YOU WERE NOT THE FIRST AARON" in " ".join(pages), "PDF lost ending"
print(f"PASS: 42/42 EPUB chapters and TXT paragraphs match manuscript exactly; cover verified; "
      f"repeated PDF running text removed; {len(pages)} listening pages, {len(reader.outline)} bookmarks")
