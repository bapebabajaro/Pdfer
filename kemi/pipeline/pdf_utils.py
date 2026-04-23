import fitz
import re

PDF_DIR = "/Users/Admin/Desktop/pastpapers"
DPI = 200
SCALE = DPI / 72
PAD = 20  # px padding around clipped region


def detect_pdf_type(path: str) -> str:
    doc = fitz.open(path)
    page_idx = min(1, len(doc) - 1)
    text = doc[page_idx].get_text().strip()
    doc.close()
    return "text" if len(text) > 50 else "image"


def render_page(path: str, page_nr: int) -> bytes:
    doc = fitz.open(path)
    page = doc[page_nr - 1]
    mat = fitz.Matrix(SCALE, SCALE)
    pix = page.get_pixmap(matrix=mat)
    data = pix.tobytes("png")
    doc.close()
    return data


def clip_text_question(path: str, page_nr: int, q_nr: str) -> bytes:
    doc = fitz.open(path)
    page = doc[page_nr - 1]

    # Collect all text blocks sorted by Y position
    blocks = sorted(
        [b for b in page.get_text("blocks") if b[6] == 0],
        key=lambda b: b[1]
    )

    # Find which block starts our question
    q_pattern = re.compile(r"^\s*" + re.escape(str(q_nr)) + r"[\s\(\.]")
    start_y = None
    end_y = None

    for i, b in enumerate(blocks):
        text = b[4].strip()
        if q_pattern.match(text) and start_y is None:
            start_y = b[1]
        elif start_y is not None:
            # Look for next question number to find end boundary
            next_q = _next_q_nr(q_nr)
            if next_q and re.match(r"^\s*" + re.escape(next_q) + r"[\s\(\.]", text):
                end_y = b[1]
                break

    if start_y is None:
        # Fallback: render full page if question not found
        return render_page(path, page_nr)

    if end_y is None:
        end_y = page.rect.height

    page_w = page.rect.width
    clip = fitz.Rect(0, start_y - PAD, page_w, end_y + PAD)
    clip = clip & page.rect  # clamp to page bounds

    mat = fitz.Matrix(SCALE, SCALE)
    pix = page.get_pixmap(matrix=mat, clip=clip)
    data = pix.tobytes("png")
    doc.close()
    return data


def _next_q_nr(q_nr: str) -> str | None:
    """Guess the next question number given current one (e.g. '3' → '4', '3a' → '3b')."""
    m = re.match(r"^(\d+)([a-z]?)$", str(q_nr))
    if not m:
        return None
    num, letter = m.group(1), m.group(2)
    if letter:
        next_letter = chr(ord(letter) + 1)
        return f"{num}{next_letter}"
    return str(int(num) + 1)
