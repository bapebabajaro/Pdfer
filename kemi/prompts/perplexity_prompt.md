# Perplexity-prompt: Stella Kemi — Frågeanalys

## Instruktion till Perplexity

Läs först hela `stella_kemi_OCR.txt` som finns i detta GitHub-repo:
`kemi/stella_kemi_OCR.txt`

Det är en komplett transkription av läroboken Stella Kemi (s. 6–309) och är din enda referens för klassificering.

Läs sedan det kemiprov (PDF) som anges, och analysera VARJE fråga.

---

## Prompt att köra

Byt ut FILNAMN.pdf mot det faktiska filnamnet innan du kör.

```
Hämta och läs dessa två filer från GitHub:

1. Stella Kemi OCR (din referens):
https://raw.githubusercontent.com/bapebabajaro/Pdfer/main/kemi/stella_kemi_OCR.txt

2. Kemiprov att analysera:
https://raw.githubusercontent.com/bapebabajaro/Pdfer/main/kemi/pdfs/FILNAMN.pdf

Läs stella_kemi_OCR.txt först — det är en komplett transkription av läroboken
Stella Kemi (s. 6–309) och är din enda referens för klassificering.

Analysera sedan provet (PDF) och för VARJE fråga och delfråga (1, 1a, 1b, 2, 3a ...):

1. q_nr          — frågenumret exakt som det skrivs i provet
2. page          — det tryckta sidnumret synligt i dokumentet
3. text          — FULLSTÄNDIG frågetext ORDAGRANT inkl. ALLA svarsalternativ A/B/C/D
4. has_diagram   — true om frågan refererar till figur, tabell eller diagram
5. stella_chapter    — kapitelkod ur listan nedan
6. stella_subchapter — delkapitelkod ur listan nedan
7. stella_solvable   — true om eleven kan besvara frågan med ENBART Stella Kemi-kunskaper
8. modification      — "none" direkt användbar / "minor" liten anpassning / "major" stort omarbete

REGLER:
- Inkludera ALLA frågor, även stella_solvable=false
- Utelämna ingen fråga — fullständig täckning krävs
- Returnera ENBART valid JSON — ingen annan text, inga förklaringar

JSON-schema:
{
  "filename": "FILNAMN.pdf",
  "processed_at": "ÅÅÅÅ-MM-DD",
  "questions": [
    {
      "q_nr": "1",
      "page": 2,
      "text": "Fullständig frågetext inklusive alla svarsalternativ...",
      "has_diagram": false,
      "stella_chapter": "Kap_2_Vatten_och_pH",
      "stella_subchapter": "2.3_Syror_och_baser",
      "stella_solvable": true,
      "modification": "none"
    }
  ]
}

Tillåtna stella_chapter (exakt stavning):
Kap_1_Kemins_grunder
Kap_2_Vatten_och_pH
Kap_3_Kolets_kemi
Kap_4_Livets_kemi
Kap_5_Periodiska_systemet
Kap_6_Rakna_med_kemi

Tillåtna stella_subchapter (exakt stavning):
1.0_Vad_ar_naturvetenskap
1.1_Undersokningar_och_laborativt_arbete
1.2_Atomer_och_grundamnen
1.3_Molekyler_och_kemiska_foreningar
1.4_Forbrannung_med_luft_och_syrgas
1.5_Joner
1.6_Kemiska_reaktioner
1.7_Blandningar
1.8_Separationsmetoder
2.1_Vattens_egenskaper
2.2_Vatten_har_unika_egenskaper
2.3_Syror_och_baser
2.4_Koncentration_och_pH
2.5_Vatten_ar_livsviktigt
3.1_Kolatomen
3.2_Kolvaten
3.3_Forbrannung_och_fossila_branslen
3.4_Alkoholer
3.5_Organiska_syror_och_estrar
4.1_Cellandning_och_fotosyntes
4.2_Kolhydrater
4.3_Fetter
4.4_Proteiner
4.5_DNA_vitaminer_och_mineraler
4.6_Kvavets_och_fosforns_kretslopp
5.1_Periodiska_systemet
5.2_Kemiska_bindningar
5.3_Elektrokemi_och_batterier
5.4_Spanningsserien
5.5_Korrosion_och_korrosionsskydd
5.6_Elektrolys
6.1_Atommassa_och_isotoper
6.2_Mol_och_molmassa

När du är klar: spara JSON-filen som FILNAMN.json och pusha till:
kemi/questions/inbox/FILNAMN.json
```

---

## Repostruktur

```
kemi/
  stella_kemi_OCR.txt          ← Din referens (läs denna först)
  prompts/
    perplexity_prompt.md       ← Denna fil
  questions/
    inbox/                     ← Pusha JSON hit
    processed/                 ← Pipeline flyttar hit automatiskt
  pipeline/                    ← Lokala klippskript (körs av läraren)
```
