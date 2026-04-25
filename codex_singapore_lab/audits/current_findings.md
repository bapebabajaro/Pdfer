# Current Findings

## Repository roles

- `Pdfer` is the source and production bank. It contains Singapore source classifications, Stella OCR, and finished simple MCQ material.
- `stellaworkbook` is the workbook app and visual rendering environment. Its extension point for Singapore questions is `src/lib/models/QuestionBlock.svelte`.
- `SOLO-FORALDRAR/app` is the learner and feedback layer. Its chemistry quiz data is simpler than stellaworkbook's Singapore formats and is used for student practice and misconception follow-up.

## Main failure pattern

The recurrent failure is format drift. A model sees "Singapore" and forces everything into one shape, usually Format 1. This breaks the source task.

Examples of failure classes found in existing material and skills:

- Format 3 source transformed into Format 1.
- Whole molecule split into fragments.
- `which is NOT correct` changed into `which are correct`.
- Swedish or explanatory text inside SVG.
- `construction_note` written in Swedish instead of `construction_note_en`.
- Handwritten SVG instead of generator scripts.
- Visual verification skipped.

## Practical implication

Every new question needs a work order before generation. The work order is the guardrail that prevents the model from "helpfully" changing the task.

