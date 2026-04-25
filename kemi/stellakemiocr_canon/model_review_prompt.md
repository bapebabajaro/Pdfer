# Prompt till GPT-5.5, Opus 4.7 och Kimi k2.6

Du ska granska och forbattrar ett hermetiskt authoring-canon for Stella
Kemi-kopplad kemiuppgiftsgenerering.

Las dessa filer i GitHub-repot `bapebabajaro/Pdfer`:

1. `kemi/stellakemiocr_canon/operational_design_spec.md`
2. `kemi/stellakemiocr_canon/evidence_index.md`
3. `kemi/prompts/DODSSYNDLISTA.md`
4. `kemi/prompts/perplexity_prompt.md`
5. `kemi/prompts/perplexity_produktion_prompt.md`
6. `INNEHALL.md`

Primar kallsanning ar:

`kemi/stella_kemi_OCR.txt`

Din uppgift:

1. Identifiera luckor, motsagelser eller overclaiming i designen.
2. Foresla exakta obligatoriska falt for OCR-verifiering, subchapter-routing,
   knowledge-link-map och remediation-map.
3. Foresla harda gate-beslut som stoppar generering nar Stella-sidreferensen
   inte kan verifieras mot OCR.
4. Kontrollera att systemet bevarar minimal elevtext men maximal dold kognitiv
   kontroll.
5. Skilj strikt mellan source canon, visual canon, inference doctrine och render QA.
6. Foresla en minimal patchplan for lokala skills/prompts utan att gora systemet
   tungrott.

Viktiga constraints:

- Leverera inte vaga principer. Ge falt, checks och beslutregler.
- Acceptera inte `stella_chapter` eller `stella_subchapter` som bevis i sig.
- En `stella`-sidhansvisning ar giltig endast om amnet faktiskt namns pa exakt
  de OCR-sidorna.
- `kalla.txt` ar kallproveniens for Singapore-fragan, inte Stella-bevis.
- Render QA far aldrig anvandas som bevis for pedagogisk kvalitet eller
  source-validitet.
- Om du foreslar en forandring, ange exakt vilken fil eller gate den hor hemma i.

Outputformat:

```md
## Findings
- [severity] Exact issue and why it matters.

## Required Model/Field Changes
- Exact field/check/rule.

## Gate Order Corrections
- Corrected order if needed.

## Dead Sins To Add
- New hard failure conditions.

## Minimal Patch Plan
- File/path and concrete edit summary.
```
