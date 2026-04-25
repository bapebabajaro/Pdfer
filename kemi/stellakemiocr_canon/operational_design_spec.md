# Operational design spec: stellakemiocr canon

## A. Vad stellakemiocr canon betyder operativt

`stellakemiocr canon` betyder att `kemi/stella_kemi_OCR.txt` ar primar
sanningskalla for all Stella Kemi-kopplad kemiuppgiftsgenerering.

Det ar inte en stilkansla, ett pedagogiskt lager eller en efterhandsreferens.
Det ar ett sidnycklat kallkontrakt:

1. OCR-filen laddas fore klassificering, solvability-beslut, generering och QA.
2. Sidmarkorerna `--- s. NN ---` definierar auktoritativa sidgransar.
3. `stella_chapter` och `stella_subchapter` ar routingnycklar, inte bevis.
4. `stella: "s. NN"` ar giltigt endast om det testade amnet faktiskt namns pa
   de sidorna i OCR.
5. `stella_solvable = true` far endast satts efter OCR-stodd tackningskontroll.
6. `modification = "minor"` ar endast tillatet om kemin ar samma och fortfarande
   ligger inom verifierad Stella-tackning.
7. Elevtexten ska vara minimal. All tung kontroll ligger dolt i
   source-certifiering, knowledge-link-map och remediation-map.
8. Kallforankring sker pa claim/option/diagram-region-niva, inte bara pa
   frag- eller kapitel-niva.

## B. Obligatorisk kanonisk datamodell

### OCR source manifest

```ts
ocr_source_manifest {
  source_file: "kemi/stella_kemi_OCR.txt";
  source_role: "primary_truth";
  page_marker_pattern: "--- s. NN ---";
  page_range: { start: 6, end: 309 };
  expected_line_count: 15244;
  loaded_before_classification: boolean;
  loaded_before_generation: boolean;
}
```

Stoppa om OCR saknas, inte kan sidparsa, eller bara ersatts av en
sammanfattning.

### Page record

```ts
page_record {
  source_file: "kemi/stella_kemi_OCR.txt";
  printed_page: number;
  page_key: string;
  page_text_hash: string;
  extraction_mode: "ocr" | "native" | "hybrid";
  normalized_text_hash: string;
  chemistry_sensitive_warnings: string[];
  verification_status: "pass" | "fail";
}
```

`page_record` ar fysisk sanning for varje Stella-sida. Alla senare evidence refs
pekar in i en page record.

### Subchapter registry entry

```ts
stella_subchapter_registry_entry {
  stella_chapter: string;
  stella_subchapter: string;
  title_sv: string;
  page_span: { start: number; end: number };
  output_folder: string;
  ocr_slice_pages: number[];
  production_status: "ready" | "remaining" | "legacy" | "blocked";
}
```

Chapter-span racker inte. Systemet maste losa en exakt delkapitelnyckel och
sidspann innan produktion.

### Evidence ref

```ts
evidence_ref {
  page_key: string;
  printed_page: number;
  locator_type: "text_span" | "bbox" | "table_cell" | "diagram_region";
  locator: string;
  excerpt_hash?: string;
  normalized_excerpt?: string;
  confidence: "high" | "medium" | "low";
}
```

Alla answer keys, knowledge links, distractor rationales och remediation targets
maste ha evidence refs. Sidnummer utan locator ar inte tillrackligt for komplexa
fragor med tabeller, diagram eller flera pastaenden.

### Source atom

```ts
source_atom {
  atom_id: string;
  concept_id: string;
  stella_term_sv: string;
  evidence_refs: evidence_ref[];
  source_grain: "term" | "definition" | "worked_example" | "diagram" | "table";
  allowed_question_roles: string[];
}
```

`source_atom` ar ateranvandbart OCR-bevis. Det ska inte blandas ihop med
student-facing text.

### Claim table

```ts
claim_table_entry {
  claim_id: string;
  target_path: string;
  claim_type: "stem_claim" | "correct_answer_claim" | "distractor_claim" | "diagram_semantic_claim" | "solution_claim";
  assessable: boolean;
  required_knowledge_links: string[];
  evidence_refs: evidence_ref[];
  source_status: "same_subchapter" | "earlier_subchapter" | "general_reasoning";
  gate_status: "pass" | "fail";
}
```

`claim_table` ar blockerande coverage-kontroll: varje assessable claim i stam,
alternativ, diagramsemantik eller losning maste ha knowledge links och
evidence refs.

### Question source certification

```ts
question_source_certification {
  id: string;
  source_key: string; // kalla.txt, e.g. filename::q_nr
  stella_chapter: string;
  stella_subchapter: string;
  claimed_stella_pages: string;
  page_records: page_record[];
  claim_table: claim_table_entry[];

  ocr_verification: {
    ocr_file: "kemi/stella_kemi_OCR.txt";
    verified_pages: number[];
    topic_mentions: [
      {
        concept_id: string;
        stella_term_sv: string;
        pages_found: number[];
        evidence_refs: evidence_ref[];
        evidence_type: "direct_term" | "stella_synonym" | "worked_example" | "diagram_label";
        sufficient_for_question: boolean;
      }
    ];
    missing_terms: string[];
    verification_result: "pass" | "fail";
  };

  knowledge_link_map: [
    {
      link_id: string;
      hidden_reasoning_step: string;
      required_concept: string;
      source_status: "same_subchapter" | "earlier_subchapter" | "general_reasoning";
      stella_pages: number[];
      evidence_refs: evidence_ref[];
      must_not_be_revealed_in_text: boolean;
    }
  ];

  distractor_rationales: [
    {
      option_key: "A" | "B" | "C" | "D";
      misconception: string;
      why_plausible: string;
      why_wrong: string;
      evidence_refs: evidence_ref[];
      remediation_target: {
        stella_subchapter: string;
        pages: number[];
        concept: string;
      };
    }
  ];

  remediation_map: [
    {
      failure_mode: string;
      send_student_to: {
        stella_subchapter: string;
        pages: number[];
        concept: string;
      };
    }
  ];

  shortcut_check: {
    solvable_from_text_alone: boolean;
    solvable_from_single_fact: boolean;
    answer_length_leak: boolean;
    grammar_parallel: boolean;
    result: "pass" | "fail";
  };
}
```

## C. Gating pipeline

### Gate 1: OCR truth load

Ladda `kemi/stella_kemi_OCR.txt` och dela upp texten med sidmarkorer.
Skapa en `page_record` per sida med page hash och normalized text hash.

Fail om:

- OCR inte laddas.
- sidmarkorer inte kan parsas.
- angivet sidspann inte kan extraheras.
- systemet anvander promptens coverage-lista som ersattning for OCR.
- native-vs-OCR reconciliation flaggar kemi-kanslig konflikt som inte ar lost.

### Gate 2: Subchapter resolution

Lasa `stella_chapter` och `stella_subchapter` mot den kanoniska listan fran
`kemi/prompts/perplexity_prompt.md`.

Fail om:

- delkapitelnyckeln inte ar kanonisk.
- output folder inte matchar delkapitelnyckeln.
- sidspann saknas.
- solvability pastaes utan OCR-evidens.

### Gate 3: OCR page verification

For varje testat koncept, kontrollera forst endast delkapitlets sidspann.
Verifiering ska ske med `evidence_ref`, inte bara sidnummer.

Godkand evidens:

- direkt term pa sidan.
- tydlig Stella-synonym pa sidan.
- worked example pa sidan.
- diagrametikett eller tabell pa sidan.

Normalisera text fore matchning: NFC, whitespace, citationstecken och bindestreck.
Fuzzy match far bara stotta, inte ensamt bevisa, kemi-kritiska tecken som
laddningar, index, reaktionspilar, enheter och decimaltecken.

Om konceptet bara finns i tidigare delkapitel far det anvandas som
prerequisite, men maste markeras som `earlier_subchapter`.

Fail om det testade amnet inte finns pa de sidor som `stella` anger.

### Gate 3b: Claim coverage

Bygg `claim_table` for varje assessable claim i:

- stem.
- korrekt svar.
- varje distraktor.
- diagramsemantik.
- tabellceller.
- losning.

Fail om en assessable claim saknar evidence_ref eller knowledge link.

### Gate 4: Stella solvability

Acceptera klassificering endast efter Gate 3.

Beslut:

- `stella_solvable = true` och `modification = "none"`: producera.
- `stella_solvable = true` och `modification = "minor"`: producera endast om
  kemin ar oforandrad.
- `stella_solvable = false`: producera aldrig.
- `modification = "major"`: producera aldrig.

### Gate 5: High-inference doctrine

Applicera efter OCR-verifiering:

- Text far definiera uppgiften.
- Text far inte utfora uppgiften.
- Inga helper links i synlig text.
- Inga forklarande ord i alternativen.
- Ingen kopierad Stella-mening i stammen.
- Gold-fragor kraver minst 5 oberoende knowledge links.
- Varje knowledge link maste peka till OCR-sidor eller klassas som
  prerequisite/general reasoning.
- Varje felalternativ maste ha distractor rationale. Gate:
  `len(distractor_rationales) == len(options) - 1`.

### Gate 6: Generation

Generera student-facing fraga endast efter Gates 1-5.

Synligt slutformat:

```ts
id
typ
niva
fraga
ratt
alternativ
stella
losning // obligatoriskt vid berakning
```

Dolt produktionsformat:

```ts
ocr_verification
knowledge_link_map
remediation_map
shortcut_check
source_key
modification_rationale
claim_table
distractor_rationales
```

### Gate 7: Rule 27 audit

Fore leverans, kontrollera final rewritten question mot final `stella` pages:

Fraga: "Namns det faktiska testade amnet pa exakt dessa OCR-sidor?"

Om nej: underkant.

### Gate 8: Render QA

Render QA kontrollerar bara implementering:

- diagram renderar.
- labels syns dar de ska.
- dolda refs syns inte for eleven.
- visuell kanon foljs.

Render QA certifierar inte Stella-validitet.
Render QA far inte skriva tillbaka till source evidence, answer key,
knowledge_link_map eller claim_table.

## D. Skillnad mellan canon-lagren

- Source canon: OCR-sanning. Avgor vad Stella faktiskt tacker pa vilka sidor.
- Subchapter canon: routing. Mappar `stella_chapter` + `stella_subchapter` till
  sidspann och output folder.
- Visual canon: presentation. Styr AtomModel, farger, diagramstil och komponenter.
- Inference doctrine: kognitiv lag. Styr hur lite texten far hjalpa eleven.
- Render QA: implementation. Kontrollerar rendering, inte kallsanning.

Skriv aldrig bara "verified". Skriv vilket gate som ar verifierat:
`OCR-verified`, `inference-audited`, `render-checked`.

## E. Hard failure conditions

Direkt stopp om nagot av detta hander:

1. Generering sker innan OCR laddats.
2. Coverage-listan anvands som bevis istallet for OCR.
3. `stella: "s. NN"` anges utan kontroll av exakt OCR-sida.
4. `stella_solvable = true` bygger pa allman kemi, inte Stella OCR.
5. Chapter-span anvands nar subchapter-span kravs.
6. Fragan hamnar i ratt kapitel men fel delkapitel.
7. Ett koncept finns nagon annanstans i Stella men inte pa angivna sidor.
8. Prerequisite-kunskap blandas ihop med same-subchapter-kunskap.
9. Remediation ar bredare an exakt delkapitel/sidspann.
10. Stella-formulering kopieras sa textsokning loser fragan.
11. `modification = "minor"` andrar den testade kemin.
12. Final rewritten question glider bort fran den ursprungligt verifierade
    source-mappen.
13. `kalla.txt` behandlas som Stella-bevis.
14. Renderad bild behandlas som pedagogisk/source QA.
15. Leverans saknar dold `ocr_verification`.
16. `missing_terms` ar olosta.
17. Systemet sager "Stella-aligned" utan sidnycklad evidens.

## F. Minimal patchplan for skill/docs

1. Skapa `references/stellakemiocr-canon.md` i relevanta skills.
2. Patcha `references/high-inference-doctrine.md` sa OCR-verifiering sker fore
   inference doctrine.
3. Patcha `singaporempc` och format-skills med pre-generation gates:
   - load Stella OCR
   - resolve subchapter key
   - verify topic on claimed pages
   - build OCR-backed knowledge_link_map
   - generate only after pass
4. Patcha `perplexity_prompt.md` och `perplexity_produktion_prompt.md`:
   - chapter/subchapter ar preliminar routing
   - `stella_solvable = true` kraver page-level OCR evidence
   - final `stella` kraver Rule 27 audit efter omskrivning
5. Skapa ett canonical audit example for `2.2_Vatten_har_unika_egenskaper`,
   s. 68-73.

Karnregel: OCR truth ar upstream of everything.
