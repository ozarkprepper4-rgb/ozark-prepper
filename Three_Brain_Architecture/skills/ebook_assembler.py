#!/usr/bin/env python3

from pathlib import Path
import argparse
import html
import re

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageBreak,
    Table,
    TableStyle,
    ListFlowable,
    ListItem,
    KeepTogether,
)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")

pdfmetrics.registerFont(TTFont("OzarkSerif", str(FONT_DIR / "DejaVuSerif.ttf")))
pdfmetrics.registerFont(TTFont("OzarkSerifBold", str(FONT_DIR / "DejaVuSerif-Bold.ttf")))
pdfmetrics.registerFont(TTFont("OzarkSerifItalic", str(FONT_DIR / "DejaVuSerif-Italic.ttf")))
pdfmetrics.registerFont(TTFont("OzarkSerifBoldItalic", str(FONT_DIR / "DejaVuSerif-BoldItalic.ttf")))

pdfmetrics.registerFontFamily(
    "OzarkSerif",
    normal="OzarkSerif",
    bold="OzarkSerifBold",
    italic="OzarkSerifItalic",
    boldItalic="OzarkSerifBoldItalic",
)


def inline_markup(text):
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    text = re.sub(r"`(.+?)`", r"<font name='Courier'>\1</font>", text)
    return text


def fit_image(path, max_width=6.4 * inch, max_height=7.7 * inch):
    with PILImage.open(path) as im:
        w, h = im.size

    scale = min(max_width / w, max_height / h)
    return Image(str(path), width=w * scale, height=h * scale)


def resolve_image(source_dir, image_ref, assets_dir=None):
    p = Path(image_ref)

    candidates = [
        source_dir / p,
    ]

    if assets_dir:
        candidates.append(Path(assets_dir) / p.name)

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return None


def make_styles():
    styles = getSampleStyleSheet()

    body = ParagraphStyle(
        "OzarkBody",
        parent=styles["BodyText"],
        fontName="OzarkSerif",
        fontSize=11,
        leading=16,
        spaceAfter=9,
        textColor=colors.HexColor("#222222"),
    )

    h1 = ParagraphStyle(
        "OzarkH1",
        parent=styles["Heading1"],
        fontName="OzarkSerifBold",
        fontSize=24,
        leading=29,
        spaceBefore=10,
        spaceAfter=16,
        textColor=colors.HexColor("#26352B"),
    )

    h2 = ParagraphStyle(
        "OzarkH2",
        parent=styles["Heading2"],
        fontName="OzarkSerifBold",
        fontSize=17,
        leading=21,
        spaceBefore=15,
        spaceAfter=9,
        textColor=colors.HexColor("#354E3D"),
    )

    h3 = ParagraphStyle(
        "OzarkH3",
        parent=styles["Heading3"],
        fontName="OzarkSerifBold",
        fontSize=13,
        leading=17,
        spaceBefore=10,
        spaceAfter=6,
        textColor=colors.HexColor("#536B57"),
    )

    caption = ParagraphStyle(
        "OzarkCaption",
        parent=body,
        fontName="OzarkSerifItalic",
        fontSize=8.5,
        leading=11,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#666666"),
    )

    return body, h1, h2, h3, caption


def parse_markdown(md_text, source_dir, assets_dir=None):
    body, h1, h2, h3, caption = make_styles()
    story = []

    lines = md_text.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()

        if not line.strip():
            story.append(Spacer(1, 5))
            i += 1
            continue

        if line.strip() == "<!-- PAGEBREAK -->":
            story.append(PageBreak())
            i += 1
            continue

        image_match = re.match(r"!\[(.*?)\]\((.*?)\)", line.strip())
        if image_match:
            alt, image_ref = image_match.groups()
            image_path = resolve_image(source_dir, image_ref, assets_dir)

            if image_path:
                story.append(Spacer(1, 8))
                story.append(fit_image(image_path))
                if alt:
                    story.append(Spacer(1, 4))
                    story.append(Paragraph(inline_markup(alt), caption))
                story.append(Spacer(1, 10))
            else:
                story.append(
                    Paragraph(
                        "<i>Image not found: " + html.escape(image_ref) + "</i>",
                        caption,
                    )
                )

            i += 1
            continue

        if line.startswith("# "):
            story.append(Paragraph(inline_markup(line[2:].strip()), h1))
            i += 1
            continue

        if line.startswith("## "):
            story.append(Paragraph(inline_markup(line[3:].strip()), h2))
            i += 1
            continue

        if line.startswith("### "):
            story.append(Paragraph(inline_markup(line[4:].strip()), h3))
            i += 1
            continue

        if "|" in line and i + 1 < len(lines):
            next_line = lines[i + 1].strip()

            if re.match(r"^\|?[\s\-:|]+\|?$", next_line):
                rows = []

                while i < len(lines) and "|" in lines[i]:
                    row = [
                        cell.strip()
                        for cell in lines[i].strip().strip("|").split("|")
                    ]

                    if not all(re.fullmatch(r"[-:\s]+", cell or "") for cell in row):
                        rows.append([
                            Paragraph(inline_markup(cell), body)
                            for cell in row
                        ])

                    i += 1

                if rows:
                    table = Table(rows, repeatRows=1, hAlign="LEFT")
                    table.setStyle(TableStyle([
                        ("FONTNAME", (0, 0), (-1, -1), "OzarkSerif"),
                        ("FONTNAME", (0, 0), (-1, 0), "OzarkSerifBold"),
                        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E7ECE8")),
                        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#999999")),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 6),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                        ("TOPPADDING", (0, 0), (-1, -1), 5),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                    ]))
                    story.append(KeepTogether([table, Spacer(1, 10)]))

                continue

        if re.match(r"^\s*[-*]\s+", line):
            items = []

            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                item_text = re.sub(r"^\s*[-*]\s+", "", lines[i]).strip()
                items.append(ListItem(Paragraph(inline_markup(item_text), body)))
                i += 1

            story.append(
                ListFlowable(
                    items,
                    bulletType="bullet",
                    leftIndent=20,
                    bulletFontName="OzarkSerif",
                )
            )
            story.append(Spacer(1, 7))
            continue

        paragraph_lines = [line.strip()]
        i += 1

        while i < len(lines):
            nxt = lines[i].strip()

            if (
                not nxt
                or nxt.startswith("#")
                or nxt.startswith("![")
                or nxt == "<!-- PAGEBREAK -->"
                or re.match(r"^[-*]\s+", nxt)
            ):
                break

            paragraph_lines.append(nxt)
            i += 1

        paragraph_text = " ".join(paragraph_lines)
        story.append(Paragraph(inline_markup(paragraph_text), body))

    return story


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("OzarkSerif", 8)
    canvas.setFillColor(colors.HexColor("#777777"))

    if doc.page > 1:
        canvas.drawCentredString(
            A4[0] / 2,
            0.42 * inch,
            f"Ozark Prepper  •  Page {doc.page}"
        )

    canvas.restoreState()


def build_pdf(source_md, output_pdf, cover=None, assets_dir=None):
    source_md = Path(source_md)
    output_pdf = Path(output_pdf)

    if not source_md.exists():
        raise FileNotFoundError(source_md)

    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(output_pdf),
        pagesize=A4,
        rightMargin=0.72 * inch,
        leftMargin=0.72 * inch,
        topMargin=0.72 * inch,
        bottomMargin=0.68 * inch,
        title="Ozark Prepper Ebook",
        author="Ozark Prepper",
    )

    story = []

    if cover:
        cover_path = Path(cover)

        if cover_path.exists():
            story.append(Spacer(1, 0.15 * inch))
            story.append(
                fit_image(
                    cover_path,
                    max_width=7.0 * inch,
                    max_height=10.0 * inch,
                )
            )
            story.append(PageBreak())

    md_text = source_md.read_text(encoding="utf-8")
    story.extend(parse_markdown(md_text, source_md.parent, assets_dir))

    doc.build(story, onFirstPage=footer, onLaterPages=footer)

    return output_pdf


def main():
    parser = argparse.ArgumentParser(
        description="Build a professional Ozark Prepper PDF from Markdown and Canva assets."
    )

    parser.add_argument("source", help="Markdown source ebook")
    parser.add_argument("output", help="Finished PDF path")
    parser.add_argument("--cover", help="Canva-exported cover image")
    parser.add_argument(
        "--assets-dir",
        help="Folder containing Canva-exported interior images",
    )

    args = parser.parse_args()

    finished = build_pdf(
        args.source,
        args.output,
        cover=args.cover,
        assets_dir=args.assets_dir,
    )

    print("EBOOK PDF CREATED:", finished)


if __name__ == "__main__":
    main()
