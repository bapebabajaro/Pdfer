# Dödssyndernas bön — rev 3

Bön för exakt uppgiftskapande av Stella Kemi MCQ-frågor. Verifierad mot fysik-bibban (`SOLO-FORALDRAR/app/src/lib/data/np/kap2-rorelse-kraft.json`) 2026-04-25.

Skalan i regel #11 är induktiv läsning av fysik-frågor och bör verifieras mot fler exempel innan första kemi-batch låser sig vid den.

---

## Form & längd

1. Jag ska aldrig skriva alternativ där rätt-svaret är längre än de felaktiga.
2. Jag ska aldrig skriva alternativ där rätt-svaret är kortare än de felaktiga.
3. Jag ska aldrig låta längdvariationen mellan alternativen överstiga ±30 % från medianen.
4. Jag ska aldrig skriva "eftersom", "därför att", "på grund av" eller annan förklaring inuti alternativtexten — bara i `lösning`-fältet.
5. Jag ska aldrig bryta parallell grammatisk struktur — börjar ett alternativ med substantiv ska alla göra det; börjar ett med siffra + enhet ska alla göra det.
6. Jag ska aldrig blanda format inom alternativlistan — t.ex. tre kemiska formler och ett namn, eller tre värden med enhet och ett utan.

## Position & schema

7. Jag ska aldrig låsa rätt-svar-positionen systematiskt — fördelningen över A/B/C/D ska vara 13/13/12/12 över 50 frågor (±2 max).
8. Jag ska aldrig avvika från fysik-bibbans JSON-fältnamn på frågenivå: `id`, `typ`, `nivå`, `fråga`, `rätt`, `alternativ`, `stella`, `lösning` (sistnämnda obligatoriskt vid `typ: "beräkning"`).
9. Jag ska aldrig glömma sidreferens (`stella: "s. NN"`) på en fråga.
10. Jag ska aldrig glömma `lösning`-fältet på en fråga av typen `beräkning`.
11. Jag ska aldrig sätta nivå-fältet utanför skalan 1/2/3 — nivå 1 = igenkänning/formel-application på given data, nivå 2 = tillämpning som kräver mellansteg, nivå 3 = resonemang/jämförelse/flerstegs-syntes.

## Stammen — anti-läcka

12. Jag ska aldrig skriva "Stella Kemi", "boken", "läroboken" eller "enligt Stella" inuti frågetexten.
13. Jag ska aldrig kopiera en mening verbatim från Stella in i frågetexten — eleven ska inte kunna lösa via textsökning.
14. Jag ska aldrig namnge i stammen den process som alternativen prövar — om svaret är "destillation" får ordet "destillation" inte stå i stammen.
15. Jag ska aldrig lägga in numerisk redundans i stammen där samma siffra dyker upp i rätt-svaret utan att också dyka upp i minst en distraktor.
16. Jag ska aldrig använda akademiska meta-fraser i stammen ("vilket av följande illustrerar bäst", "i enlighet med ovanstående", "som ett exempel på fenomenet").
17. Jag ska aldrig skriva tomma fraser ("Det är viktigt att notera...", "Som vi vet...", "Naturligtvis...", "Självklart...").

## Frågans form

18. Jag ska aldrig skriva en abstrakt en-stegs-definitionsfråga ("Vad är en jon?") — varje fråga ska ha ett scenario med namngiven elev, konkret ämne och konkret data.
19. Jag ska aldrig skriva en fråga som inte är självbärande — allt som krävs för att lösa frågan ska finnas i uppgiften själv, inte i ett tidigare prov eller bilaga.
20. Jag ska aldrig skriva en fråga om jämförelse, mätning, graf eller struktur utan att inkludera tabell/diagram när det krävs (kontextuellt — gäller inte rena begrepp- eller laborationsfrågor som är lösbara från text).

## Distraktorer

21. Jag ska aldrig skriva distraktorer som uppenbara skämt eller orimligheter — varje distraktor ska vara ett plausibelt felsvar som en elev faktiskt kan tänka.
22. Jag ska aldrig skriva en distraktor som inte är kopplad till en dokumenterad missuppfattning — varje fel-alternativ ska kunna namnges ("eleven blandar ihop X med Y").
23. Jag ska aldrig skriva en distraktor så svag att process-of-elimination reducerar frågan till 50/50-gissning.
24. Jag ska aldrig skriva en distraktor som överlappar rätt-svaret — alternativen ska vara ömsesidigt uteslutande, ett enda korrekt under alla rimliga tolkningar.
25. Jag ska aldrig låta rätt-svaret vara extremvärdet ("högst", "mest reaktivt", "flest atomer") när alternativen är ordnade i storleksordning — eleven gissar då på extremen utan ämneskunskap.

## Frågans korrekthet

26. Jag ska aldrig leverera en `typ: "beräkning"`-fråga vars facit jag inte räknat oberoende från grunden, oberoende av vilket alternativ som ser "rätt" ut.
27. Jag ska aldrig leverera en fråga med en `stella`-sidhänvisning utan att ämnet faktiskt nämns på de angivna sidorna i `stella_kemi_OCR.txt`.
