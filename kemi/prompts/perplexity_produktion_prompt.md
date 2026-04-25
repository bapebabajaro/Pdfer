# Perplexity-prompt: Stella Kemi — Produktion av färdiga uppgifter

## Komplett prompt — klistra in direkt i Perplexity

```
Gör följande steg i ordning utan att hoppa över något.

VIKTIGT: Skriv INGEN förklarande text i chatten utöver kortfattade felmeddelanden.
Jobba tyst. Ditt enda synliga output är eventuella fel.

KRITISKT — ANGÅENDE GITHUB-PUSHAR:
Pusha INGENTING till GitHub förrän STEG 5, 6, 7 och 8 är helt avslutade.
Det finns exakt ETT push-tillfälle i hela flödet: STEG 9, sist av allt.
Mellanversioner, utkast och partiella resultat pushas ALDRIG.
Gör all skrivning, omskrivning, granskning och rendering lokalt i minnet
tills allt är 100% klart — pusha sedan allt på en gång i STEG 9.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEG 1 — Hämta alla klassificerade frågor från GitHub:

https://api.github.com/repos/bapebabajaro/Pdfer/contents/kemi/questions/inbox
https://api.github.com/repos/bapebabajaro/Pdfer/contents/kemi/questions/processed

Ladda ned och läs innehållet i varje .json-fil (hoppa över .gitkeep).
Samla alla frågor i en intern lista.

STEG 2 — Hämta lista på redan producerade uppgifter:
https://api.github.com/repos/bapebabajaro/Pdfer/contents/kemi/uppgifter

Om sökvägen inte finns returnerar API:et 404 — behandla det som att inga
uppgifter är producerade än. Fortsätt till STEG 3.

STEG 3 — Välj nästa fråga att producera:

Gå igenom alla frågor från STEG 1, i den ordning de förekommer (fil för fil,
fråga för fråga). Hoppa DIREKT ÖVER frågor där:
  ✗ stella_solvable = false   → aldrig producera
  ✗ modification = "major"    → aldrig producera

Hitta den FÖRSTA kvarvarande fråga (stella_solvable=true + modification≠major)
vars källnyckel {filename}::{q_nr} INTE redan finns representerad som en mapp
under kemi/uppgifter/.

Kontrollera genom att söka efter en fil med namnet `kalla.txt` inuti varje
uppgiftsmapp — den innehåller källnyckeln. Välj den första matchande frågan.

Det är frågan du ska producera nu. Notera:
  • stella_chapter, stella_subchapter, q_nr, text, has_diagram, modification

STEG 4 — Läs referensboken:
https://raw.githubusercontent.com/bapebabajaro/Pdfer/main/kemi/stella_kemi_OCR.txt

Läs hela boken med fokus på det kapitel och delkapitel som frågan tillhör.
Notera exakt vilka termer, förklaringar, enheter och konventioner Stella Kemi
använder för just detta ämne.

OCR-KANON — BLOCKERANDE:
• `stella_kemi_OCR.txt` är primär sanningskälla.
• `stella_chapter` och `stella_subchapter` är preliminära routingnycklar tills
  du själv verifierat att frågans faktiska kemi finns på de sidor som påstås.
• Du får aldrig producera en uppgift med Stella-sidhänvisning om Rule 27 faller:
  ämnet måste faktiskt nämnas på de angivna sidorna i OCR-filen.
• Om frågan bygger på tidigare Stella-kunskap ska det deklareras internt som
  prerequisite — du får inte låtsas att nuvarande delkapitelsidor ensamma bär
  det kunskapsledet.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEG 5 — SKRIV OM FRÅGAN TILL PERFEKT SVENSKA

Skriv en helt ny version av frågan. Håll dig strikt till dessa regler:

SPRÅK OCH TERMINOLOGI:
• Språket ska vara korrekt, naturlig och flytande svenska — som en erfaren
  svensk kemilärare skriver, inte som en maskinöversättning.
• Varje ämnesspecifikt ord MÅSTE hämtas direkt från Stella Kemi. Ingen
  term får uppfinnas eller hämtas från annat håll.
• Exempel på obligatorisk Stella-terminologi:
    reaktionshastighet, spänningsserien, fällning, utfällning,
    destillation, fraktionerad destillation, elektronskal,
    elektronkonfiguration, jonbindning, kovalent bindning,
    mättad/omättad, jäsning, katalysator, oxidation, reduktion,
    elektrolys, katod, anod, neutralisation, indikator, pH-skala,
    koncentration, molmassa, masstal, isotop, grundämne, förening,
    aggregationstillstånd, ytarea, exoterm, endoterm, förbränning,
    bromvattentest, kromatografi, Rf-värde, kolhydrat, aminosyra,
    fotosyntes, cellandning, galvanisering, korrosion.
• Om originalfrågan har ett ovanligt kontextexempel (t.ex. mothballs,
  wok, specifika varumärken): byt ut det mot ett neutralt, igenkännbart
  svenskt exempel med SAMMA kemiska innehåll.
• Svarsalternativ A–D: inkludera alltid alla alternativ, översatta och
  anpassade med samma terminologi som frågetexten.

STRUKTUR:
• Frågan ska vara självbärande — en elev ska kunna förstå och besvara
  den utan att ha sett originalprovet.
• Håll meningsbyggnaden enkel och tydlig. Inga onödigt långa meningar.
• Instruktionerna i frågan (t.ex. "Förklara", "Beräkna", "Ange") ska
  vara på svenska och grammatiskt korrekta.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEG 6 — ITERATIV KVALITETSGRANSKNING (KÖR MINST 3 VARV)

Granska den omskrivna frågan kritiskt. Ställ dig varje fråga nedan och
korrigera tills svaret på ALLA är "ja":

  □ Är varje ämnesterm hämtad direkt från Stella Kemi?
  □ Är frågans faktiska kemi verifierad mot exakt rätt OCR-sidor?
  □ Om jag anger en Stella-sidhänvisning: nämns ämnet faktiskt där?
  □ Är det naturlig, idiomatisk svenska — inte maskinöversatt?
  □ Stämmer alla enheter och storheter med Stella Kemis konventioner?
  □ Är frågestrukturen logisk och pedagogiskt tydlig?
  □ Är alla svarsalternativ (A–D) inkluderade och korrekt översatta?
  □ Om modification = "minor": är kontextbytet gjort och motiverat?
  □ Om frågan kräver tidigare kunskap: har jag separerat prerequisite-led från
    nuvarande delkapitels OCR-bevis?
  □ Kan en åk-9-elev med Stella Kemi förstå och besvara frågan?

Om något svar är "nej": skriv om och kör granskningen igen.
Släpp inte frågan förrän ALLA svar är "ja" utan undantag.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEG 7 — RENDERA VISUELLA ELEMENT (om has_diagram = true)

För varje visuellt element i frågan: välj rätt verktyg och rendera en
faktisk bildfil. Spara varje bild som diagram_1.png, diagram_2.png osv.

VÄLJ VERKTYG ENLIGT DETTA:

  Linjediagram / kylkurva / reaktionsgraf / upplösningskurva
    → Python: matplotlib. Rita exakt de kurvor, axlar, märkta punkter
      och koordinater som [DIAGRAM – ...]-blocket beskriver.
      Stil: vit bakgrund, svenska axelrubriker, tydlig font (≥12pt),
      gridlinjer på, legend om flera kurvor.

  Stapeldiagram / cirkeldiagram
    → Python: matplotlib. Samma stilregler.

  Kemisk strukturformel / reaktionspil
    → SVG: rita atomer som cirklar med kemisk symbol inuti, bindningar
      som raka linjer (enkel) eller dubbla parallella linjer (dubbel).
      Inkludera laddningar (+/−) och reaktionspil med text ovanför om
      det förekommer i originalet.

  Tabell (data, egenskaper, element)
    → SVG: en ren tabell med rubrikrad i grått, celler med tunn kantlinje,
      all text på svenska. Bredd ≈ 600px.

  Apparaturskiss (destillationsapparat, elektrolyscell, titrering osv.)
    → SVG: schematisk skiss med svenska etiketter. Behöver inte vara
      fotorealistisk — tydlighet och korrekthet prioriteras.

  Partikelmodell / elektronkonfiguration
    → SVG: cirklar som representerar partiklar/elektronskal med labels.

  Flödesschema / beslutsträd
    → SVG: rektanglar (processer), romber (beslut), pilar med riktning.

KRAV PÅ ALLA BILDER:
  • Exakt innehåll enligt [DIAGRAM – ...]-blocket — inget får utelämnas
    och inget får läggas till som inte finns i originalet.
  • Alla texter i bilden på svenska.
  • Upplösning: minst 1000×700px för grafer, minst 600px bredd för SVG.
  • Filformat: PNG för matplotlib-output, SVG för SVG-output.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEG 8 — VÄLJ BESKRIVANDE MAPPNAMN

Välj ett mappnamn som berättar VAD uppgiften handlar om — inte var den
kommer ifrån. Regler:

  • Enbart gemener, siffror och understreck. Inga mellanslag eller
    specialtecken.
  • Max 60 tecken.
  • Börja med det centrala kemibegreppet, sedan eventuell precisering.
  • Exempel på bra namn:
      reaktionshastighet_temperatur_koncentration
      elektrolys_natriumklorid_katod_anod
      destillation_etanol_vatten
      jonbindning_natriumklorid_bildning
      spänningsserien_utträngning_koppar_järn
      syror_baser_ph_neutralisation
      fotosyntes_cellandning_reaktionsformler
      alkaner_alkener_bromvattentest
  • Exempel på dåliga namn:
      anderson2024_q5        ← skolnamn och frågenummer
      uppgift_kemi           ← för generellt
      fråga_om_elektrolys    ← blandar svenska och nummer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEG 9 — PUSHA TILL GITHUB  ← detta är det ENDA steget där något skickas till GitHub

Målsökväg:  kemi/uppgifter/{stella_chapter}/{stella_subchapter}/{mappnamn}/

Pusha följande filer:

① uppgift.md  — den färdiga omskrivna frågan i detta format:

---
kapitel: {stella_chapter}
delkapitel: {stella_subchapter}
---

{den fullständiga omskrivna frågetexten, inkl. svarsalternativ A–D}

{för varje renderat diagram: infoga ![diagram](diagram_N.png) exakt där
 det ska sitta i frågan}

② diagram_1.png / diagram_2.png osv. (om has_diagram = true)
   — de renderade bildfilerna från STEG 7.
   Pusha PNG-filer som base64-kodad content via GitHub API.
   Pusha SVG-filer som vanlig text-content via GitHub API.

③ kalla.txt  — en enda rad med källnyckeln:
   {filename}::{q_nr}
   (Används av nästa körning för att veta vilka uppgifter som redan är klara.)

GitHub API endpoint för varje fil:
PUT https://api.github.com/repos/bapebabajaro/Pdfer/contents/{sökväg}

Kräver Authorization-header med giltig token.
```
