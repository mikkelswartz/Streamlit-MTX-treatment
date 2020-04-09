import streamlit as st
import pandas as pd


# Pandas. Destination of ecxel dataark
Destination_main_file = "Pandas_test_excel.xlsx"
df = pd.read_excel(Destination_main_file, na_filter=False)
# Remove "Unnamed: 0" collums from dataframe
df.drop(['Unnamed: 0'], axis=1, inplace=True)

# Pandas dataframe witch value equals the row in the dataframe witch represent the treatment
Destination_st_file = "df_selected_treatment.xlsx"
df_st = pd.read_excel(Destination_st_file)

# #Variablels
# Dato = None
# Navn = None
# CPR = None
# HDM_kur_nr = None
# Alder = None
# Højde = None
# Vægt = None
# Overflade = None
# Infusions_start = None
# Total_væskemængde = None
# Mindst_2000_væskemængde = None
# Plasma_kreatin_før_start = None
# Durise_600ml_6timer = None
# Furosemid = None
# Forhydrering_6000ml_4timer = None
# Dosis_natriumcarbonat_ved_lav_pH = None
# Sygeplejerske_navn_forhydering = None
# Sygeplejerske_tid_forhydering = None
# one_to_ten_MTX_dose = None
# Sygeplejerske_navn_one_to_ten_MTX_dose = None
# Sygeplejerske_tid_one_to_ten_MTX_dose = None
# Kontinuerlig_infusion_start = None
# nine_to_ten_MTX_dose = None
# total_volume_MTX_and_hydration_liquid = None
# Sygeplejerske_navn_nine_to_ten_MTX_dose = None
# Sygeplejerske_tid_nine_to_ten_MTX_dose = None
# Se_MTX_t36 = None
# P_kreatin_t36 = None
# Hydreing_ved_høj_P_kreatin_t36 = None
# Durise_ved_høj_P_kreatin_t36 = None
# Hydreing_ved_normal_P_kreatin_t36 = None
# Durise_ved_normal_P_kreatin_t36 = None
# Se_MTX_t42 = None
# Første_dosis_calciumfolinat_t42 = None
# Sygeplejerske_navn_Første_dosis_calciumfolinat_t42 = None
# Sygeplejerske_tid_Første_dosis_calciumfolinat_t42 = None
# Ekstra_dosis_calciumfolinat_t42 = None
# Sygeplejerske_navn_Ekstra_dosis_calciumfolinat_t42 = None
# Sygeplejerske_tid_Ekstra_dosis_calciumfolinat_t42 = None
# Se_MTX_t48 = None
# Første_dosis_calciumfolinat_t48 = None
# Sygeplejerske_navn_Første_dosis_calciumfolinat_t48 = None
# Sygeplejerske_tid_Første_dosis_calciumfolinat_t48 = None
# Ekstra_dosis_calciumfolinat_t48 = None
# Sygeplejerske_navn_Ekstra_dosis_calciumfolinat_t48 = None
# Sygeplejerske_tid_Ekstra_dosis_calciumfolinat_t48 = None
# Se_MTX_t54 = None
# Første_dosis_calciumfolinat_t54 = None
# Sygeplejerske_navn_Første_dosis_calciumfolinat_t54 = None
# Sygeplejerske_tid_Første_dosis_calciumfolinat_t54 = None
# Ekstra_dosis_calciumfolinat_t54 = None
# Sygeplejerske_navn_Ekstra_dosis_calciumfolinat_t54 = None
# Sygeplejerske_tid_Ekstra_dosis_calciumfolinat_t54 = None
# Se_MTX_t66 = None
# Første_dosis_calciumfolinat_t66 = None
# Sygeplejerske_navn_Første_dosis_calciumfolinat_t66 = None
# Sygeplejerske_tid_Første_dosis_calciumfolinat_t66 = None
# Ekstra_dosis_calciumfolinat_t66 = None
# Sygeplejerske_navn_Ekstra_dosis_calciumfolinat_t66 = None
# Sygeplejerske_tid_Ekstra_dosis_calciumfolinat_t66 = None