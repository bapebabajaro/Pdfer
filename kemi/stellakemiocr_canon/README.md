# Stellakemiocr canon

Detta paket samlar den operativa designen for hur Stella Kemi OCR ska vara
primar sanningskalla vid kemiuppgiftsgenerering.

Syftet ar att lata flera modeller granska samma underlag och foresla ett
skarpt, hermetiskt system for:

- OCR-baserad kallsanning fran `kemi/stella_kemi_OCR.txt`
- subchapter- och sidnycklad Stella-tackning
- minimal elevtext och maximal dold kognitiv kontroll
- obligatorisk bakatkartlaggning till exakta Stella-sidor
- harda stoppvillkor mot falska eller overdrivna QA-pastaenden

Las i denna ordning:

1. `operational_design_spec.md`
2. `evidence_index.md`
3. `model_review_prompt.md`

Primar regel: en fraga ar inte Stella-valid for att den later ratt, matchar ett
kapitel eller renderar korrekt. Den ar Stella-valid endast nar det slutliga
testade amnet ar verifierat mot de exakta OCR-sidor fragan anger.
