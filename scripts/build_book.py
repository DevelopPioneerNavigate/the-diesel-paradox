#!/usr/bin/env python3
"""Create a single dark DPN development-edition PDF; no AI, SaaS or paid API."""
from pathlib import Path
from io import BytesIO
import argparse, html, re, math
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Spacer
from pypdf import PdfReader, PdfWriter

ROOT=Path(__file__).resolve().parents[1]
SIZE=(6.5*inch,9.5*inch)
BG=colors.HexColor("#0b0e16")
RED=colors.HexColor("#d63250")
FG=colors.HexColor("#e5e8ef")

def theme_page(canvas,doc):
    w,h=SIZE
    canvas.saveState()
    canvas.setFillColor(BG);canvas.rect(0,0,w,h,stroke=0,fill=1)
    canvas.setStrokeColor(colors.HexColor("#641c35"))
    canvas.line(49,h-51,w-49,h-51)
    canvas.line(49,46,w-49,46)
    canvas.setFont("Helvetica",7)
    canvas.setFillColor(colors.HexColor("#a5adbc"))
    canvas.drawString(50,h-43,"DPN TECHNOLOGY  /  THE DIESEL PARADOX")
    canvas.drawString(50,33,"DEVELOPMENT EDITION  /  CANON V3.1")
    canvas.drawRightString(w-50,33,str(doc.page+1))
    canvas.restoreState()

def styles():
    regular,bold="Times-Roman","Helvetica-Bold"
    paths=[("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf","DPN-Body"),
           ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf","DPN-Head")]
    if all(Path(p).exists() for p,n in paths):
        for path,name in paths:pdfmetrics.registerFont(TTFont(name,path))
        pdfmetrics.registerFontFamily("DPN-Body", normal="DPN-Body", bold="DPN-Head", italic="DPN-Body", boldItalic="DPN-Head")
        regular,bold="DPN-Body","DPN-Head"
    return {
      "p": ParagraphStyle("p",fontName=regular,fontSize=9.3,leading=15.2,textColor=FG,spaceAfter=8),
      "h1":ParagraphStyle("h1",fontName=bold,fontSize=19,leading=25,textColor=colors.white,spaceBefore=20,spaceAfter=12,keepWithNext=True),
      "h2":ParagraphStyle("h2",fontName=bold,fontSize=14,leading=20,textColor=colors.HexColor("#ffdce3"),spaceBefore=18,spaceAfter=10,keepWithNext=True),
      "h3":ParagraphStyle("h3",fontName=bold,fontSize=11,leading=16,textColor=colors.HexColor("#f7b9c8"),spaceBefore=12,spaceAfter=7,keepWithNext=True),
      "h4":ParagraphStyle("h4",fontName=bold,fontSize=9.6,leading=15,textColor=colors.HexColor("#f7b9c8"),spaceBefore=10,spaceAfter=6,keepWithNext=True),
    }

def markup(text):
    text=html.escape(text)
    text=re.sub(r"\*\*(.+?)\*\*",r"<b>\1</b>",text)
    text=re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)",r"<i>\1</i>",text)
    return text.replace("&quot;","&quot;")

def parse(source, st):
    result=[]; buf=[]
    def flush():
        if buf:
            result.append(Paragraph(markup(" ".join(buf)),st["p"]))
            buf.clear()
    for line in source.splitlines():
        s=line.strip()
        if not s:flush();continue
        match=re.match(r"^(#{1,4})\s+(.+)$",s)
        if match:
            flush()
            result.append(Paragraph(markup(match.group(2)),st["h"+str(len(match.group(1)))]))
        elif s.startswith(">"):
            flush()
            result.append(Paragraph(markup(s[1:].strip()),st["p"]))
        elif re.match(r"^(- |\* |\d+\. )",s):
            flush();s=re.sub(r"^(- |\* |\d+\. )","",s)
            result.append(Paragraph("&bull; "+markup(s),st["p"]))
        elif s.startswith("|"):
            flush()
            if re.fullmatch(r"[\s|:\-]+",s):continue
            result.append(Paragraph(markup(s),st["p"]))
        elif s=="---":
            flush();result.append(Spacer(1,12))
        else:buf.append(s)
    flush()
    return result

def make_cover():
    data=BytesIO()
    c=Canvas(data,pagesize=SIZE)
    w,h=SIZE
    c.setFillColor(BG);c.rect(0,0,w,h,fill=1,stroke=0)
    image=ROOT/"assets/cover/approved-cover.png"
    if image.exists():
        img=ImageReader(str(image));iw,ih=img.getSize()
        scale=max(w/iw,h/ih);dw,dh=iw*scale,ih*scale
        c.drawImage(img,(w-dw)/2,(h-dh)/2,width=dw,height=dh,mask="auto")
    else:
        c.setStrokeColor(RED)
        for radius in (100,125,154):
            c.setLineWidth(3 if radius==154 else 1)
            c.circle(w/2,h*.45,radius,stroke=1,fill=0)
        for i in range(12):
            angle=2*math.pi*i/12
            c.circle(w/2+154*math.cos(angle),h*.45+154*math.sin(angle),2,stroke=1,fill=0)
        c.setFillColor(colors.white);c.setFont("Helvetica-Bold",32)
        c.drawCentredString(w/2,h-125,"THE DIESEL")
        c.drawCentredString(w/2,h-165,"PARADOX")
        c.setFont("Helvetica",10)
        c.drawCentredString(w/2,h-193,"BOOK ONE: THE FIRST IMPOSSIBILITY")
        c.setFillColor(colors.HexColor("#ffa4b7"));c.setFont("Helvetica",8)
        c.drawCentredString(w/2,58,"DEVELOPMENT PLACEHOLDER: APPROVED COVER NOT YET IMPORTED")
    c.showPage();c.save()
    return data.getvalue()

def main():
    cli=argparse.ArgumentParser()
    cli.add_argument("--out",default="dist/The_Diesel_Paradox_Development_Edition.pdf")
    cli.add_argument("--listening",action="store_true",help="Build only written novel chapters for read-aloud PDF apps")
    args=cli.parse_args()
    dest=Path(args.out)
    if not dest.is_absolute():dest=ROOT/dest
    dest.parent.mkdir(parents=True,exist_ok=True)
    st=styles()
    sections=[] if args.listening else [
      ("SERIES BIBLE",ROOT/"docs/series-bible.md"),
      ("BOOK ONE: 42-CHAPTER PLAN",ROOT/"docs/book-one-outline.md"),
    ]
    for p in sorted((ROOT/"manuscript/book-01").glob("chapter-*.md")):
        sections.append((p.stem.upper().replace("-"," "),p))
    story=[
      Paragraph("THE DIESEL PARADOX",st["h1"]),
      Paragraph("Book One: The First Impossibility",st["h2"]),
      Paragraph("Canon V3.1 | DPN Technology | "+("Listening Edition" if args.listening else "Development Edition"),st["p"]),
      Paragraph(("This edition contains only Chapters 1 through "+str(len(sections))+" written in full prose, with selectable text suitable for read-aloud apps. The entire novel is not complete." if args.listening else "This is not a completed novel. It contains the series bible, 42-chapter outline and only chapters currently written in full prose."),st["p"]),
    ]
    for title,path in sections:
        story.extend([PageBreak(),Paragraph(title,st["h2"])])
        story.extend(parse(path.read_text(encoding="utf-8"),st))
    body=BytesIO()
    edition = "Listening Edition" if args.listening else "Development Edition"
    doc=SimpleDocTemplate(body,pagesize=SIZE,leftMargin=50,rightMargin=50,topMargin=67,bottomMargin=65,
                          title="The Diesel Paradox: "+edition,author="DPN Technology")
    doc.build(story,onFirstPage=theme_page,onLaterPages=theme_page)
    pdf=PdfWriter()
    pdf.append(PdfReader(BytesIO(make_cover())))
    pdf.append(PdfReader(BytesIO(body.getvalue())))
    # Bookmarks remain accurate for both the reference and listening editions.
    page_text=[page.extract_text() or "" for page in pdf.pages]
    for section,source in sections:
        source_text=source.read_text(encoding="utf-8")
        if source.name.startswith("chapter-"):
            heading=re.search(r"(?m)^##\\s+(Chapter [^\\n]+)",source_text)
            if not heading:
                raise ValueError(f"Chapter heading not found in {source}")
            label=heading.group(1).strip()
        else:
            label=section
        matches=[i for i,text in enumerate(page_text) if label in text]
        if not matches:
            # Reference-only sections have a separate section label above the source's own heading.
            matches=[i for i,text in enumerate(page_text) if section in text]
        if not matches:
            raise ValueError(f"Unable to bookmark {source.name}: {label}")
        pdf.add_outline_item(label,matches[0])
    pdf.add_metadata({"/Title":"The Diesel Paradox: "+edition,"/Author":"DPN Technology"})
    with dest.open("wb") as handle:pdf.write(handle)
    print("Wrote",dest, "pages",len(pdf.pages))

if __name__=="__main__":main()
