# Pdfer — Innehållsförteckning

Repo för att producera **Stella Kemi**-kopplade MCQ-frågor i samma format som Stella Fysik-bibban (`SOLO-FORALDRAR/app/src/lib/data/np/kap2-rorelse-kraft.json`). Källa: 80+ Singapore-prov i kemi (Sec 3, Sec 4, O-level), klassificerade mot Stella Kemis kapitelstruktur.

Senast uppdaterad: 2026-04-25.

---

## Topp-nivå

| Fil/mapp | Innehåll | Status |
|---|---|---|
| `README.md` | Pipeline-översikt: PDF → Perplexity → JSON → klippning till PNG | Stabil |
| `INNEHALL.md` | Den här filen | Aktuell |
| `kemi/` | Hela kemi-arbetsflödet | Aktivt |

---

## `kemi/` — strukturen

### `kemi/stella_kemi_OCR.txt`
- **Vad:** OCR-extraherad lärobokstext från Stella Kemi, 15 244 rader, sidorna indexerade med `--- s. NN ---`-markörer.
- **Status:** Färdig referens. Används i steg 4 av `perplexity_produktion_prompt.md` (Perplexity läser hela boken).
- **Språk:** Svenska.

### `kemi/pdfs/` — Singapore-prov (källmaterial)
- **Vad:** ~80 PDF-filer med kemi-prov från Singapore.
- **Spridning:** O-level Pure Chemistry SA2 2024 (18 st), Sec 3 Pure Chemistry SA1/SA2 2019 (12 st), Sec 4 Chemistry Prelims 2022 (8 st), Sec 4 Chemistry SA1 2018 (5 st), Sec 4 Chemistry SA2 2016/2017/2018 (28 st), Sec 4 Science Chemistry SA2 2018 (10 st).
- **Status:** Råmaterial. Inläst, oförändrat.
- **Språk:** Engelska (källa).

### `kemi/pdfs_png/` — sidvisa PNG-utdrag
- **Vad:** ~80 mappar (en per PDF) med sidvisa PNG-bilder för OCR och klippning.
- **Status:** Färdiga, genererade av `pipeline/pipeline.py`.

### `kemi/cambridge_prompts/` — klassificerade Singapore-uppgifter
- **Vad:** 50 `.txt`-filer. Varje fil = en isolerad uppgift från Singapore-proven, klassificerad mot Stella-delkapitel, med [DIAGRAM]-block som beskriver eventuella diagram/tabeller på svenska.
- **Format:** Header (källa, kapitel, sidor, typ, poäng, modifiering) + frågetext + [DIAGRAM]-block.
- **Status:** Färdiga 50 st. Översatta till svenska och anpassade.
- **Språk:** Svenska (text), engelska kvar i tabellrubriker undantagsvis.

### `kemi/EFTERLBLIVEN/`
- **Vad:** 4 `.txt`-filer som ser ut att vara dubletter/förkastade kopior av cambridge_prompts.
- **Status:** Skräp. Bör granskas och tas bort eller flyttas tillbaka.
- **Språk:** Svenska.

### `kemi/pipeline/` — Python-skript
| Fil | Funktion |
|---|---|
| `pipeline.py` | Huvudskript: läser JSON från `questions/inbox/` → klipper PDF-sidor → sparar PNG. |
| `pdf_utils.py` | PyMuPDF-hjälpare för PDF-detektering och klippning. |
| `setup_local_folders.py` | Skapar lokal mappstruktur. |
| `make_perplexity_prompt.py` | Genererar Perplexity-prompt per PDF. |
| `build_question_folders.py` | Bygger uppgiftsmappar. |
- **Status:** Kärnpipeline fungerande. Beroenden: PyMuPDF.

### `kemi/prompts/` — Perplexity-prompter och regler
| Fil | Funktion | Status |
|---|---|---|
| `perplexity_prompt.md` | Klassificerar Singapore-prov mot Stella-delkapitel. Definierar kapitelkoder och delkapitelkoder (kanonisk lista). | Stabil |
| `perplexity_produktion_prompt.md` | 9-stegs produktionsprompt: hämtar inbox/processed → väljer fråga → läser Stella → genererar uppgift → renderar diagram → pushar 1 gång till slut. | Stabil |
| `DODSSYNDLISTA.md` | 27-punkts bön för exakt uppgiftskapande (rev 3, verifierad mot fysik-bibban). | Aktuell |
- **Språk:** Svenska.

### `kemi/questions/` — JSON-frågor från Perplexity
| Mapp | Vad | Antal |
|---|---|---|
| `inbox/` | JSON-filer som Perplexity skickat in, ej klippta än | 3 (broadrick, christchurch, chuachukang — Sec4 2022 Prelims) |
| `processed/` | JSON-filer som pipeline:n redan klippt till PNG | 3 (Anderson, Payalebarmethodist, cahtolichigh — O-level 2024 SA2) |
- **Format:** En JSON per PDF-prov, varje `questions[i]` har `q_nr`, `page`, `text`, `has_diagram`, `stella_chapter`, `stella_subchapter`, `stella_solvable`, `modification`.
- **Status:** Aktiv pipeline. Endast ett fåtal prov genomgångna än så länge.

### `kemi/uppgifter/` — färdiga MCQ-frågor (Stella-formaterade)

**Vad:** Resultatet av frågegenereringen — Stella Kemi MCQ-frågor i samma format som Stella Fysik. Varje delkapitel = en mapp med `uppgifter.md` (50 frågor) + `kalla.txt`.

**JSON-fältnamn (per fråga):** `id`, `typ`, `nivå`, `fråga`, `rätt`, `alternativ`, `stella`, `lösning` (sistnämnda obligatoriskt vid `typ: "beräkning"`).

#### Status per delkapitel

**Klara (rev 2 — parallella alternativ, fördelning 13/13/12/12, 50 frågor):**

| Delkapitel | Stella-sidor | Mapp |
|---|---|---|
| 1.1 Undersökningar och laborativt arbete | s. 10–17 | `Kap_1_Kemins_grunder/1.1_Undersokningar_och_laborativt_arbete/` |
| 1.2 Atomer och grundämnen | s. 18–23 | `Kap_1_Kemins_grunder/1.2_Atomer_och_grundamnen/` |
| 1.3 Molekyler och kemiska föreningar | s. 24–29 | `Kap_1_Kemins_grunder/1.3_Molekyler_och_kemiska_foreningar/` |
| 1.4 Förbränning med luft och syrgas | s. 30–35 | `Kap_1_Kemins_grunder/1.4_Forbrannung_med_luft_och_syrgas/` |
| 1.5 Joner | s. 36–41 | `Kap_1_Kemins_grunder/1.5_Joner/` |
| 1.6 Kemiska reaktioner | s. 42–47 | `Kap_1_Kemins_grunder/1.6_Kemiska_reaktioner/` |
| 1.7 Blandningar | s. 48–53 | `Kap_1_Kemins_grunder/1.7_Blandningar/` |
| 1.8 Separationsmetoder | s. 54–59 | `Kap_1_Kemins_grunder/1.8_Separationsmetoder/` |
| 2.1 Vattens egenskaper | s. 60–67 | `Kap_2_Vatten_och_pH/2.1_Vattens_egenskaper/` |
| 6.2 Mol och molmassa | s. 270–283 | `Kap_6_Rakna_med_kemi/6.2_Mol_och_molmassa/` |

**Återstår att producera (22 delkapitel):**

| Kapitel | Återstående delkapitel |
|---|---|
| Kap 2 — Vatten och pH | 2.2 Vatten har unika egenskaper · 2.3 Syror och baser · 2.4 Koncentration och pH · 2.5 Vatten är livsviktigt |
| Kap 3 — Kolets kemi | 3.1 Kolatomen · 3.2 Kolväten · 3.3 Förbränning och fossila bränslen · 3.4 Alkoholer · 3.5 Organiska syror och estrar |
| Kap 4 — Livets kemi | 4.1 Cellandning och fotosyntes · 4.2 Kolhydrater · 4.3 Fetter · 4.4 Proteiner · 4.5 DNA, vitaminer och mineraler · 4.6 Kvävets och fosforns kretslopp |
| Kap 5 — Periodiska systemet | 5.1 Periodiska systemet · 5.2 Kemiska bindningar · 5.3 Elektrokemi och batterier · 5.4 Spänningsserien · 5.5 Korrosion och korrosionsskydd · 5.6 Elektrolys |
| Kap 6 — Räkna med kemi | 6.1 Atommassa och isotoper |

**Filer att granska/städa:**

- `kemi/uppgifter/Kap_2/` — verkar vara ett legacy-skal (bara cambridge-prompt-namnade undermappar utan `uppgifter.md`). Riktigt innehåll ligger i `Kap_2_Vatten_och_pH/`. Kontrollera om `Kap_2/` ska tas bort eller migreras.
- `kemi/uppgifter/Kap_1_Kemins_grunder/1.1_Undersokningar_och_laborativt_arbete/forbrannung_magnesium_*` och `titrering_matinstrument_*` — undermappar inom delkapitel-mappen som verkar vara cambridge-prompt-extraktioner. Granska om de hör hemma här eller flyttas till `cambridge_prompts/`.
- `kemi/uppgifter/DODSSYNDLISTA.md` — kopia av `prompts/DODSSYNDLISTA.md` som referens vid granskning.

---

## Arbetsflöde — sammanfattning

1. **Insamling:** Singapore-PDF läggs i `kemi/pdfs/`.
2. **Klippning:** `pipeline.py` extraherar sidvisa PNG till `kemi/pdfs_png/`.
3. **Klassificering (Perplexity):** Använd `prompts/perplexity_prompt.md`. Output → JSON i `kemi/questions/inbox/`.
4. **Bearbetning:** `pipeline.py` flyttar JSON till `kemi/questions/processed/` efter klippning.
5. **Produktion (Perplexity):** Använd `prompts/perplexity_produktion_prompt.md`. Output → uppgiftsmappar under `kemi/uppgifter/{stella_chapter}/{stella_subchapter}/`.
6. **Granskning:** Varje fråga måste klara `prompts/DODSSYNDLISTA.md` (27 regler).

---

## Språk

- Allt slutproducerat material: **svenska**.
- Källmaterial (`pdfs/`): engelska — översätts under produktionsfasen.
- Kod (`pipeline/`): kommentarer på engelska, prints på svenska.
