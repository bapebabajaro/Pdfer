# Perplexity-prompt: Stella Kemi — Frågeanalys

## Komplett prompt — klistra in direkt i Perplexity

```
Gör följande steg i ordning utan att hoppa över något.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEG 1 — Hämta lista på alla kemiprov (mappar med JPG-sidor):
https://api.github.com/repos/bapebabajaro/Pdfer/contents/kemi/pdfs_png

STEG 2 — Hämta lista på redan processade prov:
https://api.github.com/repos/bapebabajaro/Pdfer/contents/kemi/questions/inbox
https://api.github.com/repos/bapebabajaro/Pdfer/contents/kemi/questions/processed

STEG 3 — Jämför listorna. Hitta det FÖRSTA mappnamnet (alfabetisk ordning) från
STEG 1 som INTE redan finns som .json i inbox eller processed.
Det är provet du ska analysera. Notera mappnamnet.

STEG 4 — Hämta och läs referensboken (Stella Kemi OCR, 414 KB):
https://raw.githubusercontent.com/bapebabajaro/Pdfer/main/kemi/stella_kemi_OCR.txt
Läs igenom den så att du vet exakt vad som täcks i varje kapitel.

STEG 5 — Hämta lista på alla bildsidor för valt prov:
https://api.github.com/repos/bapebabajaro/Pdfer/contents/kemi/pdfs_png/[MAPPNAMN]

Ladda ned och läs varje sida i ordning som bild:
https://raw.githubusercontent.com/bapebabajaro/Pdfer/main/kemi/pdfs_png/[MAPPNAMN]/page_01.jpg
https://raw.githubusercontent.com/bapebabajaro/Pdfer/main/kemi/pdfs_png/[MAPPNAMN]/page_02.jpg
(osv. för alla sidor — hoppa inte över några)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEG 6 — ANALYSERA PROVET

Gå igenom varje fråga och delfråga. För varje fråga: bestäm om den ska inkluderas
enligt URVALSREGLERNA nedan, och fyll i alla fält.

─────────────────────────────────────────────────────
URVALSREGLER (följ exakt):

✓ INKLUDERA om: stella_solvable = true  OCH  modification = "none"
✓ INKLUDERA om: stella_solvable = true  OCH  modification = "minor"
✗ UTESLUT om:   modification = "major"        → finns ej i JSON
✗ UTESLUT om:   stella_solvable = false        → finns ej i JSON

─────────────────────────────────────────────────────
BEDÖMNING AV stella_solvable — vad täcker Stella Kemi?

Stella Kemi (s. 6–309) täcker följande. Sätt stella_solvable = true om frågan
primärt handlar om något av detta:

KAP 1 — Kemins grunder
  • Laborationsutrustning: byrett, pipett, mätglas, termometer, Erlenmeyer-kolv osv.
  • Atomens uppbyggnad: proton, neutron, elektron, elektronskal, elektronkonfiguration
  • Molekyler och kemiska formler: grundämnen, föreningar, molekylformler
  • Förbränning: fullständig (CO₂ + H₂O) och ofullständig (CO, sot)
  • Joner: bildning, laddning, jonföreningar, utfällning, löslighetsregler (grundläggande)
  • Kemiska reaktioner: endo-/exoterm (grundläggande), reaktionshastighet (temperatur,
    koncentration, ytarea/partikelstorlek, katalysator), masskvoter
  • Blandningar: lösning, suspension, emulsion
  • Separationsmetoder: filtrering, avdunstning, destillation, fraktionerad destillation,
    kristallisering, kromatografi (Rf-värde ingår)

KAP 2 — Vatten och pH
  • Vattenmolekylens egenskaper, poläritet, aggregationstillstånd
  • Syror och baser: stark/svag, pH-skala, neutralisation, salter, indikatorer
  • Koncentration: beräkning i mol/dm³, g/dm³

KAP 3 — Kolets kemi
  • Kolatomen och kolkedjor
  • Alkaner och alkener (C1–C4): namngivning, mättad/omättad, bromvatten-test
  • Förbränning av fossila bränslen, växthuseffekten, försurning (SO₂, NOₓ, CO₂)
  • Alkoholer: etanol, jäsning av glukos, förbränning, oxidation med KMnO₄
  • Organiska syror och estrar: ättiksyra, bildning av estrar (alkohol + syra)

KAP 4 — Livets kemi
  • Fotosyntes och cellandning (reaktionsformler)
  • Kolhydrater: glukos, sackaros, stärkelse, jäsning
  • Fetter: mättade/omättade, grundläggande struktur
  • Proteiner: aminosyror, grundläggande struktur (ej kondensationspolymerisering i detalj)
  • Kvävets och fosforns kretslopp: ammoniak, nitrater, gödsel

KAP 5 — Periodiska systemet
  • Periodiska systemets uppbyggnad: grupper, perioder, trender (reaktivitet, atomradie)
  • Grupp 1 (alkalimetaller): mjuka, reaktiva, reagerar med vatten och syre
  • Grupp 7 (halogener): reaktivitet minskar nedåt, utträngning
  • Kemiska bindningar: jonbindning och kovalent bindning (grundläggande, inkl. elektronstruktur)
  • Spänningsserien: metallers relativa reaktivitet, utträngning ur lösning, reduktion
    av metalloxider med kol eller koldioxid
  • Korrosion: rost, galvanisering, katodiskt skydd
  • Elektrolys: katod/anod, produkter vid elektrolys av smält salt och vattenlösning

KAP 6 — Räkna med kemi
  • Isotoper: protoner, neutroner, masstal, relativ atommassa (viktade medelvärden)
  • Mol och molmassa: beräkning av massa, antal mol, gasmol (24 dm³ vid RTP)

Sätt stella_solvable = false (och uteslut frågan) om den kräver:
  — Oxidationstillstånd (oxidation numbers / oxidation states)
  — Enthalpiberäkningar eller bindningsenergi
  — Energiprofil-diagram med aktiveringsenergi
  — % yield eller empirisk formel
  — Titreringsberäkningar
  — Giant covalent structures (diamant, grafit, SiO₂) i detalj
  — Avancerad organik (substitution, additionspolymerer utöver grundnivå, isomerer)
  — Komplexa elektrolysberäkningar (Faradays lagar)
  — Radioaktiva sönderfall
  — Koordinationstal i jonkristaller

─────────────────────────────────────────────────────
BEDÖMNING AV modification:

"none"  — Frågan kan användas direkt utan ändringar.
"minor" — Frågan behöver en liten anpassning: byt ut ett egennamn, ett ovanligt
          kontextexempel (t.ex. wok, mothballs), eller justera ett värde. Kunskapen
          som krävs är densamma.
"major" — Frågan kräver genomgripande omarbetning eller täcks inte av Stella.
          → Uteslut ur JSON.

─────────────────────────────────────────────────────
FÄLT FÖR VARJE INKLUDERAD FRÅGA:

  q_nr         : frågenumret exakt som i provet  (t.ex. "1", "3a", "10b(ii)")
  page         : sidnumret tryckt i dokumentet
  text         : Se TEXT-INSTRUKTIONER nedan
  has_diagram  : true om frågan har figur / tabell / graf / kemisk struktur
  stella_chapter    : kapitelkod ur listan i STEG 7
  stella_subchapter : delkapitelkod ur listan i STEG 7
  stella_solvable   : true  (MÅSTE alltid vara med)
  modification      : "none" eller "minor"

─────────────────────────────────────────────────────
TEXT-INSTRUKTIONER:

1. Skriv om hela frågetexten på KORREKT VETENSKAPLIG SVENSKA med Stella Kemis
   terminologi. Använd exakt samma begrepp som Stella Kemi, t.ex.:
   reaktionshastighet, spänningsserien, fällning, destillation, elektronskal,
   jonbindning, kovalent bindning, mättad/omättad, jäsning, katalysator.

2. Svarsalternativ A–D: ALLTID inkluderade, ordagrant översatta till svenska.

3. Visuella element (diagram, tabell, graf, kemisk formel, apparaturskiss):
   Beskriv varje visuell komponent i ett [DIAGRAM – ...]-block, placerat exakt
   där det förekommer i frågan. Se FORMAT nedan.

FORMAT FÖR [DIAGRAM – ...]-BLOCK:
  • Första raden: [DIAGRAM – TYP] där TYP är t.ex. KYLKURVA, TABELL, APPARATURSKISS,
    REAKTIONSGRAF, KROMATOGRAMPLATTA, FLÖDESSCHEMA, PARTIKELMODELL, STRUKTURFORMEL
  • Beskriv VARJE visuellt element i extrem detalj på svenska:
    – Axlar: namn, enhet, skala, min–max-värden
    – Kurvor/linjer: form, riktning, märkta punkter och deras koordinater
    – Tabeller: antal rader/kolumner, alla rubriker, alla cellvärden
    – Pilar: vad de pekar på, riktning
    – Symboler, labels, markeringar: position och betydelse
    – Relativa positioner mellan element
  • Sista raden: Rekommenderat renderingsverktyg: [t.ex. Plotly linjediagram,
    SVG-skiss, Markdown-tabell, LaTeX kemisk formel, HTML-tabell]
  • Blocket ska vara så detaljerat att texten ENSAM fungerar som prompt till
    en bildgenereringsmodell — ingen information får utelämnas.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEG 7 — Pusha JSON till GitHub:
kemi/questions/inbox/[MAPPNAMN].json

Exakt JSON-format (inga extra fält, ingen extra text):
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TILLÅTNA stella_chapter-koder:
Kap_1_Kemins_grunder
Kap_2_Vatten_och_pH
Kap_3_Kolets_kemi
Kap_4_Livets_kemi
Kap_5_Periodiska_systemet
Kap_6_Rakna_med_kemi

TILLÅTNA stella_subchapter-koder:
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
```
