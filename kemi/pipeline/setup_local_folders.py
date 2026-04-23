import os

BASE = "/Users/Admin/Desktop/pastpapers_klippta"

STRUCTURE = {
    "Kap_1_Kemins_grunder": [
        "1.0_Vad_ar_naturvetenskap",
        "1.1_Undersokningar_och_laborativt_arbete",
        "1.2_Atomer_och_grundamnen",
        "1.3_Molekyler_och_kemiska_foreningar",
        "1.4_Forbrannung_med_luft_och_syrgas",
        "1.5_Joner",
        "1.6_Kemiska_reaktioner",
        "1.7_Blandningar",
        "1.8_Separationsmetoder",
    ],
    "Kap_2_Vatten_och_pH": [
        "2.1_Vattens_egenskaper",
        "2.2_Vatten_har_unika_egenskaper",
        "2.3_Syror_och_baser",
        "2.4_Koncentration_och_pH",
        "2.5_Vatten_ar_livsviktigt",
    ],
    "Kap_3_Kolets_kemi": [
        "3.1_Kolatomen",
        "3.2_Kolvaten",
        "3.3_Forbrannung_och_fossila_branslen",
        "3.4_Alkoholer",
        "3.5_Organiska_syror_och_estrar",
    ],
    "Kap_4_Livets_kemi": [
        "4.1_Cellandning_och_fotosyntes",
        "4.2_Kolhydrater",
        "4.3_Fetter",
        "4.4_Proteiner",
        "4.5_DNA_vitaminer_och_mineraler",
        "4.6_Kvavets_och_fosforns_kretslopp",
    ],
    "Kap_5_Periodiska_systemet": [
        "5.1_Periodiska_systemet",
        "5.2_Kemiska_bindningar",
        "5.3_Elektrokemi_och_batterier",
        "5.4_Spanningsserien",
        "5.5_Korrosion_och_korrosionsskydd",
        "5.6_Elektrolys",
    ],
    "Kap_6_Rakna_med_kemi": [
        "6.1_Atommassa_och_isotoper",
        "6.2_Mol_och_molmassa",
    ],
}

created = 0
for chapter, subchapters in STRUCTURE.items():
    for sub in subchapters:
        path = os.path.join(BASE, chapter, sub)
        os.makedirs(path, exist_ok=True)
        created += 1

os.makedirs(os.path.join(BASE, "_oklassificerat"), exist_ok=True)
print(f"Skapade {created} delkapitelmappar + _oklassificerat under {BASE}")
