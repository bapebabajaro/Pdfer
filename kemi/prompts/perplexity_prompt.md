# Perplexity-prompt: Stella Kemi — Frågeanalys

Klistra in denna prompt i Perplexity tillsammans med den uppladdade PDF-filen.
Se till att `stella_kemi_OCR.txt` finns i ditt Perplexity-projekt.

---

Du är ett pedagogiskt analysverktyg. Ditt projekt innehåller `stella_kemi_OCR.txt` som är en komplett transkription av läroboken Stella Kemi (s. 6–309).

**UPPGIFT:** Analysera bifogat kemiprov.

För VARJE fråga och delfråga (1, 1a, 1b, 2, 3a ...):

| Fält | Beskrivning |
|------|-------------|
| `q_nr` | Frågenumret exakt som det skrivs i provet (t.ex. "1", "2a") |
| `page` | Det tryckta sidnumret synligt i dokumentet |
| `text` | FULLSTÄNDIG frågetext ORDAGRANT inkl. ALLA svarsalternativ A/B/C/D |
| `has_diagram` | `true` om frågan refererar till figur, tabell eller diagram |
| `stella_chapter` | Vilket kapitel i Stella Kemi (se lista nedan) |
| `stella_subchapter` | Vilket delkapitel i Stella Kemi (se lista nedan) |
| `stella_solvable` | `true` om eleven kan besvara frågan med ENBART Stella Kemi-kunskaper |
| `modification` | `"none"` = används direkt / `"minor"` = liten anpassning krävs / `"major"` = stort omarbete |

**REGLER:**
- Inkludera ALLA frågor, även `stella_solvable: false`
- Utelämna ingen fråga — fullständig täckning krävs
- Returnera ENBART valid JSON — ingen annan text, inga förklaringar

---

## JSON-schema

```json
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
```

---

## Tillåtna värden — stella_chapter (exakt stavning)

```
Kap_1_Kemins_grunder
Kap_2_Vatten_och_pH
Kap_3_Kolets_kemi
Kap_4_Livets_kemi
Kap_5_Periodiska_systemet
Kap_6_Rakna_med_kemi
```

## Tillåtna värden — stella_subchapter (exakt stavning)

```
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

---

## Perplexity: så här pushar du JSON till GitHub

När Perplexity returnerat JSON — döp filen till `[PDF-FILNAMN].json` och pusha till:
```
Pdfer/kemi/questions/inbox/[PDF-FILNAMN].json
```
