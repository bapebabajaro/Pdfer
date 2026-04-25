# Codex Gold Method: perfekta kemifrågor

Den här metoden finns för att höja kvaliteten på frågeproduktionen från "korrekt extraktion" till "pedagogiskt och ämnesmässigt guld".

Målet är inte bara att få ut en fråga som går att använda. Målet är att få ut en fråga som:

- är exakt mot källan
- är fullt lösbar med Stella Kemi
- använder naturlig svensk ämnesterminologi
- är pedagogiskt ren och självförklarande
- bevarar samma kunskapskrav och samma rätt svar som originalet
- har visuella element som går att rendera utan tolkningstapp

## Kärnprincip

Varje fråga ska behandlas som ett innehållsobjekt med fem separata kvalitetslager:

1. Källtrogenhet
2. Kunskapsmatchning mot Stella Kemi
3. Språk och pedagogik
4. Svarsintegritet
5. Renderbar visuell specifikation

Om ett lager inte håller, är frågan inte klar.

## Arbetsordning

### 1. Extrahera utan att förbättra

Läs originalfrågan exakt som den är.

Identifiera:

- q_nr
- sida
- komplett frågetext
- alla delfrågor
- alla svarsalternativ
- alla visuella referenser
- vilka fakta eleven faktiskt måste kunna

I detta steg får ingen omskrivning ske.

### 2. Bestäm kunskapskärnan

Skriv internt ned frågans faktiska kunskapskärna i en enda rad.

Exempel:

- "Eleven ska avgöra hur koncentration påverkar reaktionshastighet."
- "Eleven ska tolka en kromatogramplatta med Rf-värden."
- "Eleven ska skilja mellan jonbindning och kovalent bindning."

Om kunskapskärnan inte täcks av Stella Kemi ska frågan inte produceras.

### 3. Klassificera förändringsgrad hårt

`none`

- originalet fungerar i svensk skolkontext
- ingen kulturell eller språklig anpassning krävs

`minor`

- liten kontextjustering krävs
- samma kemi, samma svårighetsgrad, samma typ av resonemang

`major`

- kunskapskravet måste ändras
- flera led måste skrivas om
- rätt svar riskerar att förändras
- visualen är så oklar att den måste uppfinnas

Allt som landar i `major` ska stoppas.

### 4. Säkra svarsintegriteten innan omskrivning

Innan frågan skrivs om ska korrekt svar eller korrekt lösningslinje fastställas internt.

Kontrollera:

- att originalet är entydigt
- att omskrivningen inte skapar fler tolkningar
- att A-D-alternativ fortfarande ger samma rätt svar
- att tabeller, grafer och etiketter inte flyttar svårighetsgraden

Om rätt svar ändras av omskrivningen är frågan underkänd.

### 5. Skriv om till svensk lärarsvenska

Omskrivningen ska följa dessa regler:

- korta, tydliga meningar
- Stella Kemis ordval prioriteras över direktöversättning
- instruktioner ska vara elevnära: `ange`, `förklara`, `beskriv`, `beräkna`, `jämför`
- frågan ska vara självbärande
- inget fluff, inga onödiga bakgrundsmeningar
- inga engelska restord eller maskinöversatta fraser

Bra omskrivning:

- tydlig
- ämneskorrekt
- idiomatisk
- lätt att läsa högt

Dålig omskrivning:

- lång
- kantig
- överförklarad
- terminologiskt blandad

### 6. Bygg en renderingskontrakt för varje visual

Varje visual ska beskrivas så att en annan agent kan rendera den utan att se originalet.

En bra visualspec ska alltid innehålla:

- typ av visual
- alla etiketter
- alla värden
- axlar och enheter
- ordning mellan element
- vilka delar som är viktiga för lösningen
- rekommenderat renderingsformat

En visualspec är underkänd om den innehåller ord som:

- "ungefär"
- "något i stil med"
- "typisk"
- "kan visas som"

Visualen ska vara specificerad, inte föreslagen.

### 7. Kör Gold Audit

Ingen fråga är klar förrän alla punkter nedan får `ja`.

- Är kunskapskärnan oförändrad?
- Är rätt svar oförändrat?
- Är språket naturligt på svenska?
- Är varje ämnesterm förenlig med Stella Kemi?
- Är frågan fullt självbärande?
- Är visualen tillräckligt exakt för rendering?
- Är svårighetsgraden oförändrad?
- Är inget viktigt borttappat från originalet?
- Är inget nytt tillagt som eleven måste tolka?

Minsta `nej` betyder att frågan ska omarbetas igen.

## Pedagogiska regler

### Frågan ska testas mot elevperspektivet

Frågan ska kunna förstås i denna ordning:

1. Vad visas?
2. Vad ska jag göra?
3. Vilken kemi gäller?
4. Hur ska jag svara?

Om eleven först måste tolka layouten eller gissa vad som menas är frågan inte tillräckligt bra.

### Varje fråga ska ha en tydlig huvuduppgift

Om en fråga blandar flera operationer utan tydlig struktur ska den delas upp eller skrivas om tydligare.

Exempel:

- först tolka tabellen
- sedan jämföra resultaten
- sedan dra slutsatsen

### Svarsalternativ ska vara jämna

För MCQ gäller:

- alternativen ska ha liknande längd
- grammatiskt ska de passa efter frågestammen
- felalternativ ska vara rimliga
- rätt alternativ får inte sticka ut språkligt

## Produktionsregler

### Tillåtna utdatafält

Behåll samma schema som nuvarande pipeline för att inte bryta verktyg nedströms:

- `q_nr`
- `page`
- `text`
- `has_diagram`
- `stella_chapter`
- `stella_subchapter`
- `stella_solvable`
- `modification`

Metoden får vara smartare internt, men outputformatet ska vara stabilt.

### Push-regel

Inget får pushas förrän frågan har passerat Gold Audit.

Det gäller både:

- JSON-klassificering
- färdig uppgift
- diagramfiler

### Namngivning

Mappnamn ska beskriva kemiinnehållet, inte källprovet.

Bra:

- `reaktionshastighet_temperatur_koncentration`
- `jonbindning_natriumklorid`
- `filtrering_kristallisering_salt`

Dåligt:

- `question_7`
- `anderson_q5`
- `prov_2024_del2`

## Kortversion

En perfekt fråga uppfyller tre krav samtidigt:

- samma kemi som originalet
- bättre svenska än originalet
- noll tvekan om hur den ska lösas eller renderas
