# OCR-verifierade renderade Stella-frågor

Batchen ersätter tidigare render-only-bilder med fulla MCQ-produkter som har:

- OCR-verifierad Stella-koppling.
- Dödsyndskontroll enligt `DODSSYNDLISTA.md`.
- Minimal synlig text och separata renderprompter.
- En renderad PNG per fråga.

Filer:

- `questions.json` - färdiga frågor i schema med `id`, `typ`, `nivå`, `fråga`, `rätt`, `alternativ`, `stella`, `lösning`.
- `render_prompts.md` - renderkontrakt/prompt per bild utan facitfraser.
- `source_certification.json` - OCR- och dödsyndsgrindar.
- `assets/` - renderade PNG-bilder.

Medvetna ersättningar:

- Originalidén `endoterm/exoterm` ersattes med kalciumoxid + vatten, eftersom `endoterm` och `exoterm` inte finns som stöd i Stella OCR på angivna sidor.
- Originalidén `jod/tellur/protontal` ersattes med grupp 17/halogen, eftersom `tellur` och `protontal` saknade OCR-stöd.
- Originalidén `väteperoxidkurva` ersattes med lösningshastighet för fast ämne, eftersom Stella OCR inte stödjer katalytisk sönderdelning av väteperoxid på angivna sidor.
