# Perplexity-prompt: Stella Kemi — Frågeanalys

## Komplett prompt — klistra in direkt i Perplexity

```
Gör följande steg i ordning:

STEG 1 — Hämta lista på alla kemiprov (mappar med JPG-sidor):
https://api.github.com/repos/bapebabajaro/Pdfer/contents/kemi/pdfs_png

STEG 2 — Hämta lista på redan processade prov:
https://api.github.com/repos/bapebabajaro/Pdfer/contents/kemi/questions/inbox
https://api.github.com/repos/bapebabajaro/Pdfer/contents/kemi/questions/processed

STEG 3 — Hitta det första provet i listan (alfabetisk ordning) vars mappnamn
INTE redan finns som .json i inbox eller processed. Det är provet du ska analysera nu.

STEG 4 — Hämta och läs din referens (Stella Kemi OCR):
https://raw.githubusercontent.com/bapebabajaro/Pdfer/main/kemi/stella_kemi_OCR.txt

STEG 5 — Hämta lista på alla sidor för valt prov:
https://api.github.com/repos/bapebabajaro/Pdfer/contents/kemi/pdfs_png/[MAPPNAMN]

Ladda ned och läs varje sida i ordning som bild:
https://raw.githubusercontent.com/bapebabajaro/Pdfer/main/kemi/pdfs_png/[MAPPNAMN]/page_01.jpg
https://raw.githubusercontent.com/bapebabajaro/Pdfer/main/kemi/pdfs_png/[MAPPNAMN]/page_02.jpg
(osv. för alla sidor)

STEG 6 — Analysera provet.

Inkludera ENBART frågor där stella_solvable = true OCH modification ≠ "major".
Hoppa över alla frågor som kräver major-modifikation — de ska inte finnas i JSON alls.

För varje kvalificerad fråga och delfråga:

FÄLT:
- q_nr: frågenumret exakt som det skrivs i provet (t.ex. "1", "3a", "10b(ii)")
- page: sidnumret tryckt i dokumentet
- text: Se TEXT-INSTRUKTIONER nedan
- has_diagram: true om frågan har figur/tabell/diagram/formel
- stella_chapter: kapitelkod ur listan nedan
- stella_subchapter: delkapitelkod ur listan nedan
- stella_solvable: true (detta fält MÅSTE alltid finnas med)
- modification: "none" eller "minor"

TEXT-INSTRUKTIONER (kritiskt viktigt):
1. Skriv om frågetexten på KORREKT VETENSKAPLIG SVENSKA med Stella Kemis ordförråd och
   terminologi. Använd samma begrepp som Stella Kemi (t.ex. "reaktionshastighet",
   "spänningsserien", "joner", "fällning", "destillation").
2. Svarsalternativ A–D ska ALLTID inkluderas ordagrant (översatta till svenska).
3. Om frågan innehåller ett diagram, en tabell, en graf, en kemisk formel eller någon
   annan visuell komponent — beskriv den i ett [DIAGRAM – ...]-block direkt i texten,
   på den plats i frågan där den visuella komponenten förekommer.

FORMAT FÖR [DIAGRAM – ...]-BLOCK:
Varje block ska:
- Börja med [DIAGRAM – KORTBESKRIVNING AV TYP (t.ex. KYLKURVA, TABELL, APPARATURSKISS)]
- Beskriva varje visuellt element i extrem detalj på svenska: axlar och enhet, alla
  kurvor/linjer, alla punkter, alla värden som syns, alla pilar, alla labels, alla
  symboler, relativa positioner och riktningar
- Sluta med: Rekommenderat renderingsverktyg: [lämpligt verktyg, t.ex. Plotly, SVG,
  Markdown-tabell, LaTeX, HTML-tabell]
- Vara tillräckligt detaljerat för att texten ENSAM kan fungera som prompt till en
  bildgenereringsmodell

STEG 7 — Returnera och pusha JSON till:
kemi/questions/inbox/[MAPPNAMN].json

Exakt JSON-format:
{
  "filename": "[MAPPNAMN].pdf",
  "processed_at": "ÅÅÅÅ-MM-DD",
  "questions": [
    {
      "q_nr": "1",
      "page": 2,
      "text": "...",
      "has_diagram": false,
      "stella_chapter": "Kap_2_Vatten_och_pH",
      "stella_subchapter": "2.3_Syror_och_baser",
      "stella_solvable": true,
      "modification": "none"
    }
  ]
}

Tillåtna stella_chapter:
Kap_1_Kemins_grunder | Kap_2_Vatten_och_pH | Kap_3_Kolets_kemi |
Kap_4_Livets_kemi | Kap_5_Periodiska_systemet | Kap_6_Rakna_med_kemi

Tillåtna stella_subchapter:
1.0_Vad_ar_naturvetenskap | 1.1_Undersokningar_och_laborativt_arbete |
1.2_Atomer_och_grundamnen | 1.3_Molekyler_och_kemiska_foreningar |
1.4_Forbrannung_med_luft_och_syrgas | 1.5_Joner | 1.6_Kemiska_reaktioner |
1.7_Blandningar | 1.8_Separationsmetoder | 2.1_Vattens_egenskaper |
2.2_Vatten_har_unika_egenskaper | 2.3_Syror_och_baser |
2.4_Koncentration_och_pH | 2.5_Vatten_ar_livsviktigt | 3.1_Kolatomen |
3.2_Kolvaten | 3.3_Forbrannung_och_fossila_branslen | 3.4_Alkoholer |
3.5_Organiska_syror_och_estrar | 4.1_Cellandning_och_fotosyntes |
4.2_Kolhydrater | 4.3_Fetter | 4.4_Proteiner |
4.5_DNA_vitaminer_och_mineraler | 4.6_Kvavets_och_fosforns_kretslopp |
5.1_Periodiska_systemet | 5.2_Kemiska_bindningar |
5.3_Elektrokemi_och_batterier | 5.4_Spanningsserien |
5.5_Korrosion_och_korrosionsskydd | 5.6_Elektrolys |
6.1_Atommassa_och_isotoper | 6.2_Mol_och_molmassa
```
