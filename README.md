# Pdfer — Stella-kopplade provfrågor

Pipeline för att extrahera, klassificera och organisera kemifrågor ur Singapore-prov
mot läroboken Stella Kemi.

## Struktur

```
kemi/
  questions/
    inbox/      ← Perplexity pushar JSON hit (en fil per PDF-prov)
    processed/  ← Pipeline flyttar hit efter klippning
  prompts/
    perplexity_prompt.md  ← Prompt att ge Perplexity
  pipeline/
    pipeline.py           ← Huvudskript: läser JSON → klipper PDF → sparar PNG
    pdf_utils.py          ← PDF-detektering och klippning (PyMuPDF)
    setup_local_folders.py ← Skapar lokal mappstruktur
    make_perplexity_prompt.py ← Genererar prompt per PDF
```

## Workflow

1. Ladda upp `stella_kemi_OCR.txt` till ditt Perplexity-projekt
2. Ladda upp ett kemiprov (PDF) till Perplexity
3. Klistra in prompten från `kemi/prompts/perplexity_prompt.md`
4. Perplexity returnerar JSON → pusha till `kemi/questions/inbox/`
5. Kör lokalt: `python3 kemi/pipeline/pipeline.py /Users/Admin/Desktop/Pdfer`

## Lokalt resultat

Frågor sparas som PNG i `Desktop/pastpapers_klippta/` organiserade efter Stella-kapitel.
