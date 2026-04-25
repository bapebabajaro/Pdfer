# Evidence index

## Primara Pdfer-kallor

- `kemi/stella_kemi_OCR.txt`
  - Full OCR-transkription av Stella Kemi.
  - Sidmarkorer: `--- s. NN ---`.
  - Tacker s. 6-309.
  - Ska behandlas som primar kallsanning.

- `INNEHALL.md`
  - Beskriver Pdfer som produktionsbank for Stella-kopplade MCQ.
  - Anger att OCR-filen har 15 244 rader.
  - Beskriver `cambridge_prompts/`, `questions/`, `uppgifter/` och `kalla.txt`.
  - Anger att varje delkapitel mappar till Stella-sidor och output-mapp.

- `kemi/prompts/DODSSYNDLISTA.md`
  - Regel 27: leverera aldrig en fraga med `stella`-sidhansvisning utan att
    amnet faktiskt namns pa de sidorna i `stella_kemi_OCR.txt`.

- `kemi/prompts/perplexity_prompt.md`
  - Kraver att `stella_kemi_OCR.txt` laddas innan solvability klassificeras.
  - Definierar produktionsfalt:
    - `stella_chapter`
    - `stella_subchapter`
    - `stella_solvable`
    - `modification`
  - Innehaller kanonisk lista over chapter- och subchapter-koder.

- `kemi/prompts/perplexity_produktion_prompt.md`
  - Kraver att referensboken laddas i produktionsflodet.
  - Kraver Stella-terminologi och lokal produktion innan en enda slutpush.
  - Producerar till `kemi/uppgifter/{stella_chapter}/{stella_subchapter}/{mappnamn}/`.
  - Sparar kallproveniens i `kalla.txt`.

## Strukturfakta

- `kemi/cambridge_prompts/`
  - Klassificerade Singapore-uppgifter mappade till Stella-delkapitel.

- `kemi/questions/inbox/` och `kemi/questions/processed/`
  - JSON-fragor fran klassificeringssteget.
  - Varje fraga har `q_nr`, `page`, `text`, `has_diagram`,
    `stella_chapter`, `stella_subchapter`, `stella_solvable`, `modification`.

- `kemi/uppgifter/`
  - Slutliga MCQ per Stella-delkapitel.
  - Slutformat per fraga: `id`, `typ`, `niva`, `fraga`, `ratt`,
    `alternativ`, `stella`, `losning` nar obligatoriskt.

## Kanda subchapter-statusar fran `INNEHALL.md`

Klara exempel:

- `1.1_Undersokningar_och_laborativt_arbete`, s. 10-17.
- `1.2_Atomer_och_grundamnen`, s. 18-23.
- `1.3_Molekyler_och_kemiska_foreningar`, s. 24-29.
- `1.4_Forbrannung_med_luft_och_syrgas`, s. 30-35.
- `1.5_Joner`, s. 36-41.
- `1.6_Kemiska_reaktioner`, s. 42-47.
- `1.7_Blandningar`, s. 48-53.
- `1.8_Separationsmetoder`, s. 54-59.
- `2.1_Vattens_egenskaper`, s. 60-67.
- `6.2_Mol_och_molmassa`, s. 270-283.

Kritisk kommande testkandidat:

- `2.2_Vatten_har_unika_egenskaper`, s. 68-73.

## Stellaworkbook-visuell kanon att integrera

- `AtomModel.svelte`
  - Masterkomponent for Bohrmodell.
  - Anvands for atomens uppbyggnad, grundamnen, isotoper, joner.
  - Proton `#E91E63`, neutron `#1565C0`, elektron `#4CAF50`,
    skal `#37474F` streckat.
  - Ren, explicit Chemistry Matters-stil.

- `models/index.ts`
  - Orange `#E8922D`: worked-example/banner.
  - Purple `#7B2D8E`: reasoning.
  - Green `#4CAF50`: particles / Let's Map It / Concept Cartoon.
  - Teal `#00ACC1`: info.
  - Coral `#E53935`: warnings.
  - Kommentar anger att farger/design ar fasta och inte ska andras utan att alla
    instanser uppdateras.
