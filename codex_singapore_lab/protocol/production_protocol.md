# Production Protocol

Detta ar den korta, operativa versionen jag ska folja nar jag skapar Singapore/Stella-fragor.

## 1. Las kallan

Las faktisk kallfil eller bild. Skriv ner:

- source path
- original question type
- Stella chapter/subchapter
- Stella page range
- source visual count
- exact concept tested

Ingen produktion innan detta ar gjort.

## 2. Klassificera format

Rakna visualer innan fragan byggs.

| Format | Villkor | Output |
|---|---|---|
| 1 Combination | 4 separata visual-items A-D | `singapore-combo` |
| 2 Table | 1 tabell med A-D-rader | `singapore-table` |
| 3 Single visual | 1 central graf/diagram/struktur/apparat | `singapore-single-visual` |
| 4 Pure text | 0 visualer | `singapore-pure-text` |

Om osaker: defaulta till Format 3, inte Format 1.

## 3. Las tva raexempel

Innan generering ska minst tva exempel av samma format lasas. Anteckna:

- vad originalet testar
- hur korrekt svar verifieras
- hur varje distraktor fungerar
- vilken visuell operation eleven maste gora

## 4. Bevara pedagogisk karna

Skriv forst:

```text
Original tests: ...
```

Detta ar kontraktet. Om output testar nagot annat ar uppgiften fel, aven om den ser snygg ut.

## 5. Bygg visual deterministiskt

Anvand scripts i `stellaworkbook/scripts/` nar formatet ar graf, dot-cross eller strukturformel.

Forbjudet:

- handskriva lang SVG direkt i JSON
- textetiketter i SVG som forklarar svaret
- grafer utan numeriska ticks
- olika skalor mellan jamforda items

## 6. Bygg distraktorer

Varje felalternativ ska motsvara en elevmissuppfattning:

- fel tolkning av visual
- korrekt visualtolkning men fel kemi
- ratt metod men fel siffra/enhet
- overgeneralisering fran ett annat fall

Alternativ ska vara parallella: samma typ, liknande langd, samma grammatiska form.

## 7. Skriv `construction_note_en`

Engelska. Fyra delar ar obligatoriska:

1. Correct answer and independent verification.
2. Distractor type per incorrect option/item.
3. At least four cognitive dimensions.
4. Specific-knowledge vs general-ability classification.

## 8. Stop gates

Stoppa om nagot av detta galler:

- formatet ar inte klassificerat
- inga tva raexempel ar lasta
- Stella-sidreferens ar inte verifierad
- visualen kravde forklarande text for att forstas
- korrekt svar ar langst/kortast eller spraket sticker ut
- construction note saknar verifiering
- fragan kan losas med textmatchning snarare an resonemang

## 9. Leveranspaket

En labbfraga ar inte klar utan:

- work order
- formatbeslut
- visual spec
- genererad SVG/preview
- JSON-forslag
- verifieringsnot
- kvarvarande risk

