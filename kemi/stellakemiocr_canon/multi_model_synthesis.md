# Multi-model synthesis

Detta ar slutsatserna fran extern modellgranskning av stellakemiocr-canon.
De ska behandlas som kravskarpningar, inte som alternativa ideer.

## Konsensus som ska in i canon

1. Kallforankring maste ske finare an `question -> chapter`.
   Minsta granskningsniva ska vara assessable claim, answer option,
   distractor rationale, diagram region eller table cell.

2. OCR-sidverifiering ska vara fail-closed.
   En fraga far inte ga vidare med varningar om Stella-sidreferensen inte kan
   verifieras mot OCR-sidan.

3. Render QA och Source QA ska ha separata artefakter och statusfalt.
   Render QA far aldrig skriva tillbaka till source evidence, answer key eller
   knowledge links.

4. Dead sins ska vara fatal-koder, inte rad eller varningar.
   Varje fail ska ha kod, target_path, evidence_ref och stoppa produktion.

5. Varje felalternativ maste ha distractor_rationale.
   Gate: antal distractor rationales ska vara antal alternativ minus ett.

## Rekommenderad hybridmodell

Kombinera tre perspektiv:

- Page-first provenance:
  `page_record` ar fysisk sanning for varje Stella-sida.

- Atomar evidence bank:
  `source_atom` och `visual_source_atom` beskriver ateranvandbara
  text-/bildbevis inom en sida.

- Claim-level assessment:
  `claim_table` listar alla bedombara pastaenden i fragan och tvingar varje
  claim att peka till evidence.

Detta ger bade sidintegritet, ateranvandbar kallsanning och mekanisk
tackningskontroll.

## Obligatoriska additions

### page_record

```ts
page_record {
  source_file: "kemi/stella_kemi_OCR.txt";
  printed_page: number;
  page_key: string; // e.g. "stella_kemi_OCR.txt::s.68"
  page_text_hash: string;
  extraction_mode: "ocr" | "native" | "hybrid";
  normalized_text_hash: string;
  chemistry_sensitive_warnings: string[];
  verification_status: "pass" | "fail";
}
```

### evidence_ref

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

### source_atom

```ts
source_atom {
  atom_id: string;
  concept_id: string;
  stella_term_sv: string;
  evidence_refs: evidence_ref[];
  source_grain: "term" | "definition" | "worked_example" | "diagram" | "table";
  allowed_question_roles: [
    "supports_correct_answer",
    "supports_distractor",
    "supports_hidden_reasoning",
    "supports_remediation"
  ];
}
```

### claim_table

```ts
claim_table_entry {
  claim_id: string;
  target_path: string; // e.g. "question.stem", "options.B", "diagram_1.region.atom_label"
  claim_type: "stem_claim" | "correct_answer_claim" | "distractor_claim" | "diagram_semantic_claim" | "solution_claim";
  assessable: boolean;
  required_knowledge_links: string[];
  evidence_refs: evidence_ref[];
  source_status: "same_subchapter" | "earlier_subchapter" | "general_reasoning";
  gate_status: "pass" | "fail";
}
```

### distractor_rationale

```ts
distractor_rationale {
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
```

## OCR verification policy

OCR verification should combine:

- page hash / normalized text hash for page identity.
- anchor/excerpt match for term presence.
- normalized matching before comparison:
  NFC, whitespace collapse, quote normalization, dash normalization.
- fuzzy match only as support, not sole proof, for chemistry-critical terms.
- native-vs-OCR reconciliation where native PDF text exists.
- blocker on chemistry-sensitive divergence:
  charges, subscripts, superscripts, reaction arrows, units, decimal commas,
  element symbols and formula indices.

## New fatal gates

```ts
fatal_gate {
  code: string;
  target_path: string;
  reason: string;
  evidence_refs: evidence_ref[];
  result: "pass" | "fail";
}
```

Required fatal codes:

- `DS_SOURCE_REF_UNVERIFIED`: claimed Stella page lacks OCR support.
- `DS_CLAIM_UNGROUNDED`: assessable claim lacks evidence_ref.
- `DS_ANSWER_UNGROUNDED`: correct answer lacks source evidence.
- `DS_DISTRACTOR_UNRATIONALED`: wrong option lacks rationale/remediation.
- `DS_RENDER_AS_SOURCE`: render QA used as source proof.
- `DS_QA_LAYER_COLLAPSE`: source/render/inference statuses mixed.
- `DS_CHEM_NOTATION_MUTATION`: formula, charge, unit or symbol changed.
- `DS_OPTION_DRIFT`: option meaning changed during rewrite.
- `DS_REMEDIATION_TOO_BROAD`: remediation lacks exact pages/subchapter.
- `DS_NOT_UNIQUE`: more than one defensible answer remains.

## Practical recommendation

Patch the canon toward this sequence:

1. Build `page_record` from OCR page slices.
2. Extract `source_atom` / `visual_source_atom`.
3. Build `claim_table` for every assessable claim in generated item.
4. Link every claim, answer and distractor to `evidence_ref`.
5. Run fatal source gates.
6. Run high-inference gates.
7. Run render QA in a separate artefact.

This preserves the original principle: minimal student text, maximal hidden
cognitive and source-control work.
