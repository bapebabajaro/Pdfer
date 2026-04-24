"""
Läser JSON-filer från kemi/questions/inbox/ och skapar för varje fråga:

  pastpapers_klippta/
    {stella_chapter}/
      {stella_subchapter}/
        {prov_kortnamn}_q{q_nr}/
          question.md

question.md innehåller frågetexten (svensk, med diagrambeskrivningar) + metadata.
Körs med: python3 build_question_folders.py
"""

import json
import os
import re
import shutil
from pathlib import Path
from datetime import datetime

INBOX    = "/Users/Admin/Desktop/Pdfer/kemi/questions/inbox"
PROCESSED = "/Users/Admin/Desktop/Pdfer/kemi/questions/processed"
OUT_BASE = "/Users/Admin/Desktop/pastpapers_klippta"

VALID_CHAPTERS = {
    "Kap_1_Kemins_grunder", "Kap_2_Vatten_och_pH", "Kap_3_Kolets_kemi",
    "Kap_4_Livets_kemi", "Kap_5_Periodiska_systemet", "Kap_6_Rakna_med_kemi",
}


def short_name(filename: str) -> str:
    """
    'Olevel_PureChemistry_2024_SA2_Anderson.pdf' → 'Anderson2024'
    'Sec4_2022_Chemistry_Prelims_broadrick.pdf'  → 'Broadrick2022'
    'Sec_4_Science_Chemistry_SA2_2018_Bedok_Green.pdf' → 'BedokGreen2018'
    """
    stem = Path(filename).stem
    # Extrahera år
    year = re.search(r'(20\d{2})', stem)
    year = year.group(1) if year else ""
    # Ta bort vanliga brus-tokens
    noise = re.compile(
        r'(?i)(olevel|sec_?[0-9]|science|chemistry|pure|prelim[s]?|sa[12]|'
        r'p[12]|paper|exam|test|_|-)'
    )
    clean = noise.sub(' ', stem)
    words = [w for w in clean.split() if w and w != year and not w.isdigit()]
    base = ''.join(w.capitalize() for w in words[:3])
    return f"{base}{year}" if year else base


def safe_folder(name: str) -> str:
    """Gör strängen säker som mappnamn."""
    return re.sub(r'[^\w\-]', '_', str(name)).strip('_')


def make_question_md(q: dict, source_file: str, prov_name: str) -> str:
    q_nr      = q.get("q_nr", "?")
    page      = q.get("page", "?")
    text      = q.get("text", "").strip()
    chapter   = q.get("stella_chapter", "")
    subchapter= q.get("stella_subchapter", "")
    mod       = q.get("modification", "")
    has_diag  = q.get("has_diagram", False)

    lines = [
        f"# Fråga {q_nr} — {prov_name}",
        "",
        f"> **Källa:** {source_file}  |  **Sida:** {page}  |  "
        f"**Kapitel:** {chapter}  |  **Delkapitel:** {subchapter}",
        f"> **Modifikation:** {mod}  |  **Diagram:** {'ja' if has_diag else 'nej'}",
        "",
        "---",
        "",
        text,
        "",
    ]
    return "\n".join(lines)


def process_json(json_path: str):
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    filename  = data.get("filename", Path(json_path).stem + ".pdf")
    questions = data.get("questions", [])
    prov_name = short_name(filename)

    saved = 0
    skipped = 0
    for q in questions:
        # Filtrera: endast stella_solvable=true + modification none/minor
        if not q.get("stella_solvable", False):
            skipped += 1
            continue
        if q.get("modification", "major") == "major":
            skipped += 1
            continue

        chapter    = q.get("stella_chapter", "")
        subchapter = q.get("stella_subchapter", "")
        q_nr       = str(q.get("q_nr", "?"))

        if chapter not in VALID_CHAPTERS:
            chapter = "_oklassificerat"
            subchapter = ""

        # Bygg mappstig
        folder_name = safe_folder(f"{prov_name}_q{q_nr}")
        dest = Path(OUT_BASE) / chapter / subchapter / folder_name
        dest.mkdir(parents=True, exist_ok=True)

        # Skriv question.md
        md_path = dest / "question.md"
        md_path.write_text(
            make_question_md(q, filename, prov_name),
            encoding="utf-8"
        )
        saved += 1

    print(f"  {filename}: {saved} frågemappar skapade  ({skipped} hoppades över)")

    # Flytta till processed
    dest_processed = Path(PROCESSED) / Path(json_path).name
    shutil.move(json_path, dest_processed)


def run():
    Path(PROCESSED).mkdir(parents=True, exist_ok=True)
    json_files = sorted(Path(INBOX).glob("*.json"))

    if not json_files:
        print("Inga JSON-filer i inbox.")
        return

    print(f"Processar {len(json_files)} fil(er)...\n")
    for jf in json_files:
        process_json(str(jf))

    print("\nKlart.")


if __name__ == "__main__":
    run()
