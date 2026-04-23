import json
import os
import re
import shutil
from datetime import datetime
from pathlib import Path

from pdf_utils import detect_pdf_type, clip_text_question, render_page

PDF_DIR = "/Users/Admin/Desktop/pastpapers"
OUT_BASE = "/Users/Admin/Desktop/pastpapers_klippta"
LOG_FILE = os.path.join(OUT_BASE, "_log.txt")

VALID_CHAPTERS = {
    "Kap_1_Kemins_grunder", "Kap_2_Vatten_och_pH", "Kap_3_Kolets_kemi",
    "Kap_4_Livets_kemi", "Kap_5_Periodiska_systemet", "Kap_6_Rakna_med_kemi",
}


def sanitize(s: str) -> str:
    return re.sub(r"[^\w\-.]", "_", s)


def resolve_dest(chapter: str, subchapter: str) -> str:
    if chapter in VALID_CHAPTERS:
        path = os.path.join(OUT_BASE, chapter, subchapter)
        os.makedirs(path, exist_ok=True)
        return path
    return os.path.join(OUT_BASE, "_oklassificerat")


def log(msg: str):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    print(msg)


def process_json(json_path: str, inbox_dir: str, processed_dir: str):
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    filename = data.get("filename", "")
    pdf_path = os.path.join(PDF_DIR, filename)

    if not os.path.exists(pdf_path):
        log(f"  [FEL] PDF hittades inte: {pdf_path}")
        return

    pdf_type = detect_pdf_type(pdf_path)
    questions = data.get("questions", [])
    stem = sanitize(Path(filename).stem)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")

    log(f"\n[{ts}] {filename} | {pdf_type}-PDF | {len(questions)} frågor")

    saved = skipped = 0

    for q in questions:
        solvable = q.get("stella_solvable", False)
        mod = q.get("modification", "major")
        q_nr = str(q.get("q_nr", "?"))
        page = int(q.get("page", 1))
        chapter = q.get("stella_chapter", "")
        subchapter = q.get("stella_subchapter", "")

        if not solvable or mod == "major":
            log(f"  q{q_nr} → hoppas (solvable={solvable} mod={mod})")
            skipped += 1
            continue

        try:
            if pdf_type == "text":
                img_bytes = clip_text_question(pdf_path, page, q_nr)
            else:
                img_bytes = render_page(pdf_path, page)

            dest_dir = resolve_dest(chapter, subchapter)
            out_name = f"{stem}_q{sanitize(q_nr)}.png"
            out_path = os.path.join(dest_dir, out_name)

            # Avoid overwriting — append suffix if collision
            suffix = 1
            while os.path.exists(out_path):
                out_path = os.path.join(dest_dir, f"{stem}_q{sanitize(q_nr)}_{suffix}.png")
                suffix += 1

            with open(out_path, "wb") as f:
                f.write(img_bytes)

            log(f"  q{q_nr} → {chapter}/{subchapter} | mod={mod} → ✓ {out_name}")
            saved += 1

        except Exception as e:
            log(f"  q{q_nr} → FEL: {e}")
            skipped += 1

    log(f"  Resultat: {saved} sparade, {skipped} hoppades")

    # Move JSON to processed
    dest = os.path.join(processed_dir, os.path.basename(json_path))
    shutil.move(json_path, dest)


def run(repo_dir: str):
    inbox = os.path.join(repo_dir, "questions", "inbox")
    processed = os.path.join(repo_dir, "questions", "processed")
    os.makedirs(processed, exist_ok=True)
    os.makedirs(inbox, exist_ok=True)

    json_files = sorted(Path(inbox).glob("*.json"))
    if not json_files:
        print("Inga JSON-filer i inbox. Kör efter att Perplexity pushat.")
        return

    for jf in json_files:
        process_json(str(jf), inbox, processed)

    print(f"\nKlart. {len(json_files)} filer processade.")


if __name__ == "__main__":
    import sys
    repo = sys.argv[1] if len(sys.argv) > 1 else "."
    run(repo)
