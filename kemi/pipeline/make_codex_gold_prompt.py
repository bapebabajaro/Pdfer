"""Skriv ut en skarpare analys-prompt byggd på Codex Gold Method."""
import sys


PROMPT = """Du arbetar enligt Codex Gold Method för att skapa perfekta kemifrågor.

Målet är inte bara att extrahera frågor. Målet är att producera frågor som är:
- källtrogna
- fullt lösbara med Stella Kemi
- skrivna på naturlig svensk lärarsvenska
- pedagogiskt självbärande
- renderbara utan tolkningstapp

Gör följande steg i ordning utan att hoppa över något.

VIKTIGT:
- Skriv ingen förklarande text i chatten.
- Jobba tyst.
- Ditt enda synliga output ska vara den JSON som till sist skrivs.
- Behåll exakt samma JSON-schema som det befintliga systemet använder.

STEG 1 — Välj nästa prov

1. Läs listan över provmappar i `kemi/pdfs_png`.
2. Läs listan över redan klassificerade JSON-filer i:
   - `kemi/questions/inbox`
   - `kemi/questions/processed`
3. Välj första ännu ej klassificerade prov enligt samma urvalslogik som nuvarande pipeline.

STEG 2 — Läs Stella Kemi

Läs `kemi/stella_kemi_OCR.txt` med fokus på:
- relevanta kapitel
- terminologi
- enheter
- konventioner
- vilka resonemang som faktiskt täcks

STEG 3 — Extrahera varje fråga utan förbättring

För varje fråga och delfråga:
- extrahera komplett originalinnehåll
- identifiera visuella element
- identifiera vad eleven faktiskt måste kunna

I detta steg får du inte skriva om något.

STEG 4 — Bestäm kunskapskärnan

För varje fråga: formulera internt en enda rad som beskriver kunskapskärnan.

Exempel:
- eleven ska tolka hur temperatur påverkar reaktionshastighet
- eleven ska skilja mellan jonbindning och kovalent bindning
- eleven ska välja lämplig separationsmetod

Om kunskapskärnan inte täcks av Stella Kemi:
- sätt `stella_solvable = false`
- uteslut frågan ur JSON

STEG 5 — Klassificera förändringsgrad

Använd endast:
- `none`
- `minor`
- `major`

Regler:
- `none`: frågan fungerar direkt i svensk kontext
- `minor`: liten kontextanpassning krävs men samma kemi, svårighetsgrad och rätt svar bevaras
- `major`: större omskrivning krävs eller rätt svar/svårighetsgrad riskerar att ändras

Alla frågor med `major` ska uteslutas.

STEG 6 — Säkra svarsintegriteten

Innan du godkänner en fråga måste du internt kontrollera:
- att rätt svar eller korrekt lösningslinje är tydlig
- att omskrivning inte skapar fler tolkningar
- att visuella element inte ändrar vad som testas

Om rätt svar riskerar att förändras:
- klassificera som `major`
- uteslut frågan

STEG 7 — Skriv om inkluderade frågor till perfekt svenska

För varje fråga som ska med:
- skriv om den till naturlig svensk lärarsvenska
- använd Stella Kemis ämnestermer
- gör frågan självbärande
- behåll samma kunskapskrav
- behåll samma rätt svar
- inkludera alltid alla svarsalternativ A-D om de finns

Språkregler:
- korta, tydliga meningar
- inga maskinöversatta fraser
- inga engelska restord
- inga konstlade synonymer om Stella redan har etablerat termen

STEG 8 — Bygg renderingskontrakt för visualer

Om frågan har visual:
- ersätt visualen i texten med ett `[DIAGRAM - ...]`-block
- blocket ska vara tillräckligt exakt för att en annan agent ska kunna rendera visualen utan originalbilden

Varje block ska ange:
- typ av visual
- alla rubriker och etiketter
- alla värden
- axlar och enheter
- kurvformer eller tabellinnehåll
- relativa positioner
- rekommenderat renderingsformat

Undvik vaga ord som:
- ungefär
- typisk
- kan visas som

STEG 9 — Gold Audit

Ingen fråga får släppas igenom förrän alla dessa är uppfyllda:
- kunskapskärnan är oförändrad
- rätt svar är oförändrat
- språket är naturligt svenska
- alla ämnestermer stämmer med Stella Kemi
- frågan är självbärande
- visualspecen är renderbar utan gissning
- svårighetsgraden är oförändrad
- inget viktigt saknas
- inget nytt har lagts till som eleven måste tolka

Minsta avvikelse betyder att frågan ska skrivas om igen eller uteslutas.

STEG 10 — Skriv JSON

Returnera enbart valid JSON i detta format:

{
  "filename": "FILNAMN.pdf",
  "processed_at": "YYYY-MM-DD",
  "questions": [
    {
      "q_nr": "1",
      "page": 2,
      "text": "Färdig svensk fråga...",
      "has_diagram": false,
      "stella_chapter": "Kap_2_Vatten_och_pH",
      "stella_subchapter": "2.3_Syror_och_baser",
      "stella_solvable": true,
      "modification": "none"
    }
  ]
}

TILLÅTNA chapter-koder:
Kap_1_Kemins_grunder
Kap_2_Vatten_och_pH
Kap_3_Kolets_kemi
Kap_4_Livets_kemi
Kap_5_Periodiska_systemet
Kap_6_Rakna_med_kemi

TILLÅTNA subchapter-koder:
1.0_Vad_ar_naturvetenskap
1.1_Undersokningar_och_laborativt_arbete
1.2_Atomer_och_grundamnen
1.3_Molekyler_och_kemiska_foreningar
1.4_Forbrannung_med_luft_och_syrgas
1.5_Joner
1.6_Kemiska_reaktioner
1.7_Blandningar
1.8_Separationsmetoder
2.1_Vattens_egenskaper
2.2_Vatten_har_unika_egenskaper
2.3_Syror_och_baser
2.4_Koncentration_och_pH
2.5_Vatten_ar_livsviktigt
3.1_Kolatomen
3.2_Kolvaten
3.3_Forbrannung_och_fossila_branslen
3.4_Alkoholer
3.5_Organiska_syror_och_estrar
4.1_Cellandning_och_fotosyntes
4.2_Kolhydrater
4.3_Fetter
4.4_Proteiner
4.5_DNA_vitaminer_och_mineraler
4.6_Kvavets_och_fosforns_kretslopp
5.1_Periodiska_systemet
5.2_Kemiska_bindningar
5.3_Elektrokemi_och_batterier
5.4_Spanningsserien
5.5_Korrosion_och_korrosionsskydd
5.6_Elektrolys
6.1_Atommassa_och_isotoper
6.2_Mol_och_molmassa
"""


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "FILNAMN.pdf"
    print(PROMPT.replace("FILNAMN.pdf", filename))
