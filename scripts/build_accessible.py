#!/usr/bin/env python3
"""Build an actual reflowable, chapter-native text ebook for speech readers.

No hard page breaks, running headers, PDF layout lines or research appendices.
Only source-controlled manuscript prose. No third-party packages required.
"""
from __future__ import annotations
import argparse
import hashlib
import html
import re
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_STORED, ZIP_DEFLATED
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript/book-01"
COVER_SHA256 = "5ba1bd629ff9b7b86bbcc4e1a2f956f4965078989fe46e66d508d6f6cf976e06"
XHTML_NS = "http://www.w3.org/1999/xhtml"
TITLE = "The Diesel Paradox — Book One: The First Impossibility"

def source_files() -> list[Path]:
    paths = sorted(MANUSCRIPT.glob("chapter-[0-9][0-9].md"))
    expected = [MANUSCRIPT / f"chapter-{n:02d}.md" for n in range(1, 43)]
    if paths != expected:
        raise ValueError("Expected exactly 42 consecutively named manuscript files")
    return paths

def approved_cover() -> bytes:
    single = ROOT / "assets/cover/approved-cover.png"
    parts = [ROOT / "assets/cover/source" / f"approved-cover.png.part-{n:02d}.bin" for n in range(1, 9)]
    if single.is_file():
        data = single.read_bytes()
    elif all(p.is_file() for p in parts):
        data = b"".join(p.read_bytes() for p in parts)
    else:
        raise FileNotFoundError("Checksum-pinned original cover parts missing; never substitute a preview")
    if hashlib.sha256(data).hexdigest() != COVER_SHA256:
        raise ValueError("Approved original cover checksum mismatch")
    return data

def prose_blocks(source: str):
    """Yield exact paragraph/scene boundaries; join source hard wraps within paragraphs."""
    buf = []
    def drain():
        nonlocal buf
        if buf:
            yield ("paragraph", " ".join(buf))
            buf = []
    for line in source.splitlines():
        s = line.strip()
        if not s:
            yield from drain()
        elif s in ("***", "* * *", "---"):
            yield from drain()
            yield ("scene", "")
        elif re.match(r"^#{1,4}\s+", s):
            yield from drain()
            # Source often repeats book/series banners before its real chapter heading.
            if re.search(r"Chapter (?:[A-Z]|\d)", s, re.I):
                continue
            if re.search(r"^(?:#{1,4}\s+)?(?:THE DIESEL PARADOX|BOOK ONE:)", s, re.I):
                continue
            # Other headings retain their content as a short spoken paragraph.
            yield ("paragraph", re.sub(r"^#{1,4}\s+", "", s))
        elif s.startswith(">"):
            yield from drain()
            yield ("paragraph", s.lstrip("> ").strip())
        elif re.fullmatch(r"\|?[\s|:\-]+\|?", s):
            yield from drain()
        else:
            buf.append(s)
    yield from drain()

def title_of(source: str) -> str:
    match = re.search(r"^#{1,3}\s+(Chapter [^\n]+)", source, re.M)
    if not match:
        raise ValueError("Chapter title not found")
    return match.group(1).strip()

def strip_md(s: str) -> str:
    """Strip paired Markdown emphasis only, preserving literal D-star notation."""
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"\1", s)
    return s.replace("`", "").replace("\\_", "_")

def rich(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", s)
    return s.replace("`", "")

def document(inner: str, title: str) -> str:
    return ('<?xml version="1.0" encoding="utf-8"?>\n'
            '<!DOCTYPE html>\n'
            '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">'
            '<head><meta charset="utf-8"/><title>' + html.escape(title) +
            '</title><link rel="stylesheet" type="text/css" href="style.css"/></head>'
            '<body>' + inner + '</body></html>')

def zip_write(z: ZipFile, name: str, data: str | bytes, store: bool = False):
    info = ZipInfo(name)
    info.compress_type = ZIP_STORED if store else ZIP_DEFLATED
    info.date_time = (2020, 1, 1, 0, 0, 0)
    z.writestr(info, data.encode("utf-8") if isinstance(data, str) else data)

def build(epub: Path, txt: Path):
    paths = source_files()
    chapters = []
    for index, path in enumerate(paths, 1):
        source = path.read_text(encoding="utf-8")
        title = title_of(source)
        blocks = list(prose_blocks(source))
        if sum(1 for k, _ in blocks if k == "paragraph") < 30:
            raise ValueError(f"{path.name}: suspiciously few prose paragraphs")
        chapters.append((index, title, blocks))
    # Speech content begins with the novel, not manufacturing notes or instructions.
    ebook_text = [TITLE, "", ""]
    for n, title, blocks in chapters:
        ebook_text.extend([title, ""])
        for kind, item in blocks:
            if kind == "scene":
                ebook_text.append("")
            else:
                ebook_text.extend([strip_md(item), ""])
        ebook_text.append("")
    txt.parent.mkdir(parents=True, exist_ok=True)
    txt.write_text("\n".join(ebook_text).rstrip() + "\n", encoding="utf-8")
    cover = approved_cover()
    toc_items = "".join(f'<li><a href="chapter-{n:02d}.xhtml">{html.escape(t)}</a></li>'
                        for n, t, _ in chapters)
    nav = document('<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>' +
                   toc_items + '</ol></nav>', "Contents")
    # Required epub namespace must be present where epub:type is used.
    nav = nav.replace('xmlns="http://www.w3.org/1999/xhtml"',
                      'xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops"', 1)
    css = ("html{font-size:100%}body{font-family:serif;line-height:1.55;margin:5%}"
           "h1{font-size:1.45em;line-height:1.3;margin:0 0 1.4em}p{margin:0 0 .85em}"
           "hr.scene{border:0;border-top:1px solid #999;width:24%;margin:1.9em auto}"
           "img.cover{display:block;width:100%;height:auto}a{color:inherit}")
    manifest = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="cover-image" href="images/approved-cover.png" media-type="image/png" properties="cover-image"/>',
        '<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>',
        '<item id="style" href="style.css" media-type="text/css"/>'
    ] + [f'<item id="c{n:02d}" href="chapter-{n:02d}.xhtml" media-type="application/xhtml+xml"/>'
         for n, _, _ in chapters]
    spine = ['<itemref idref="cover"/>'] + [f'<itemref idref="c{n:02d}"/>'
                                                for n, _, _ in chapters]
    opf = ('<?xml version="1.0" encoding="utf-8"?>'
           '<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="pub-id" version="3.0">'
           '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">'
           '<dc:identifier id="pub-id">urn:dpn:diesel-paradox:first-impossibility:book-one</dc:identifier>'
           '<dc:title>' + html.escape(TITLE) + '</dc:title>'
           '<dc:creator>DPN Technology</dc:creator><dc:language>en</dc:language>'
           '<meta property="dcterms:modified">2026-11-01T00:00:00Z</meta>'
           '<meta name="cover" content="cover-image"/>'
           '<dc:description>Complete first draft of Book One; reflowable chapters for accessible reading and speech.</dc:description>'
           '</metadata><manifest>' + "".join(manifest) + '</manifest><spine>' +
           "".join(spine) + '</spine></package>')
    ncx = ('<?xml version="1.0" encoding="UTF-8"?>'
           '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">'
           '<head><meta name="dtb:uid" content="urn:dpn:diesel-paradox:first-impossibility:book-one"/></head>'
           '<docTitle><text>' + html.escape(TITLE) + '</text></docTitle><navMap>' +
           "".join(f'<navPoint id="nav{n}" playOrder="{n}"><navLabel><text>{html.escape(t)}</text></navLabel>'
                   f'<content src="chapter-{n:02d}.xhtml"/></navPoint>'
                   for n, t, _ in chapters) + '</navMap></ncx>')
    # Include NCX for older audio-reading software, while retaining EPUB3 nav.
    opf = opf.replace('<item id="style"', '<item id="toc-ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/><item id="style"')
    opf = opf.replace('<spine>', '<spine toc="toc-ncx">')
    epub.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(epub, "w") as z:
        zip_write(z, "mimetype", "application/epub+zip", store=True)
        zip_write(z, "META-INF/container.xml",
                  '<?xml version="1.0" encoding="UTF-8"?>'
                  '<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
                  '<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>'
                  '</rootfiles></container>')
        zip_write(z, "OEBPS/content.opf", opf)
        zip_write(z, "OEBPS/nav.xhtml", nav)
        zip_write(z, "OEBPS/toc.ncx", ncx)
        zip_write(z, "OEBPS/cover.xhtml", document(
                  '<div><img class="cover" src="images/approved-cover.png" alt="The Diesel Paradox approved cinematic cover"/></div>', TITLE))
        zip_write(z, "OEBPS/images/approved-cover.png", cover)
        zip_write(z, "OEBPS/style.css", css)
        for n, title, blocks in chapters:
            body = [f'<section id="chapter-{n:02d}" epub:type="chapter"><h1>{html.escape(title)}</h1>']
            for kind, item in blocks:
                body.append('<hr class="scene"/>' if kind == "scene" else '<p>' + rich(item) + '</p>')
            body.append('</section>')
            xhtml = document("".join(body), title)
            xhtml = xhtml.replace('xmlns="http://www.w3.org/1999/xhtml"',
                                  'xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops"', 1)
            zip_write(z, f"OEBPS/chapter-{n:02d}.xhtml", xhtml)
    # Verify every XHTML document parses and we have exact page-free file count.
    with ZipFile(epub) as z:
        for n in range(1, 43):
            ET.fromstring(z.read(f"OEBPS/chapter-{n:02d}.xhtml"))
        ET.fromstring(z.read("OEBPS/nav.xhtml"))
        ET.fromstring(z.read("OEBPS/content.opf"))
    print(f"Built {epub} and {txt} with {len(chapters)} reflowable chapters")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--epub", default="dist/The_Diesel_Paradox_Book_One_Audio_Friendly.epub")
    parser.add_argument("--txt", default="dist/The_Diesel_Paradox_Book_One_Continuous_Text.txt")
    args = parser.parse_args()
    build(ROOT / args.epub, ROOT / args.txt)
