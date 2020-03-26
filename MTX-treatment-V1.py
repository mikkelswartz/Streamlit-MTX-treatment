
import streamlit as st
import math
import time
import pandas as pd
from datetime import datetime, timedelta, time # make it possible to add and substrat hours from a time
from decimal import Decimal, ROUND_HALF_UP # makes rounding of floats correct

# Title for all pages
st.title('HØJ-DOSIS METHOTREXAT 5 g/m^2  NOPHO 2008')

# Page navigation
# Overview of the different pages.
pages = ["Startside", "Væskeregnskab", "Forhydrering", "MTX infusion", "Monitorering af Toksicitet"]
frontpage_subpages= ["Find tidligere patient", "Opret ny patient"]

# Navigation selection
page = st.sidebar.radio('Navigation', options=pages)

# Pandas. Destination of ecxel dataark
Destination_file = "Pandas_test_excel.xlsx"
df = pd.read_excel(Destination_file)
# "selected_treatment" equals the row in dataframe witch represent the treatment
selected_treatment = None


#Variablels
Dato = None
Navn = None
CPR = None
HDM_kur_nr = None
Alder = None
Højde = None
Vægt = None
Overflade = None
Infusions_start = None
Total_væskemængde = None
Mindst_2000_væskemængde = None
Plasma_kreatin_før_start = None
Durise_600ml_6timer = None
Furosemid = None
Forhydrering_6000ml_4timer = None
Dosis_natriumcarbonat_ved_lav_pH = None
Sygeplejerske_navn_forhydering = None
Sygeplejerske_tid_forhydering = None
one_to_ten_MTX_dose = None
Sygeplejerske_navn_one_to_ten_MTX_dose = None
Sygeplejerske_tid_one_to_ten_MTX_dose = None
Kontinuerlig_infusion_start = None
nine_to_ten_MTX_dose = None
total_volume_MTX_and_hydration_liquid = None
Sygeplejerske_navn_nine_to_ten_MTX_dose = None
Sygeplejerske_tid_nine_to_ten_MTX_dose = None
Se_MTX_t36 = None
P_kreatin_t36 = None
Hydreing_ved_høj_P_kreatin_t36 = None
Durise_ved_høj_P_kreatin_t36 = None
Hydreing_ved_normal_P_kreatin_t36 = None
Durise_ved_normal_P_kreatin_t36 = None
Se_MTX_t42 = None
Første_dosis_caliumfolinat_t42 = None
Sygeplejerske_navn_Første_dosis_caliumfolinat_t42 = None
Sygeplejerske_tid_Første_dosis_caliumfolinat_t42 = None
Ekstra_dosis_caliumfolinat_t42 = None
Sygeplejerske_navn_Ekstra_dosis_caliumfolinat_t42 = None
Sygeplejerske_tid_Ekstra_dosis_caliumfolinat_t42 = None
Se_MTX_t48 = None
Første_dosis_caliumfolinat_t48 = None
Sygeplejerske_navn_Første_dosis_caliumfolinat_t48 = None
Sygeplejerske_tid_Første_dosis_caliumfolinat_t48 = None
Ekstra_dosis_caliumfolinat_t48 = None
Sygeplejerske_navn_Ekstra_dosis_caliumfolinat_t48 = None
Sygeplejerske_tid_Ekstra_dosis_caliumfolinat_t48 = None
Se_MTX_t54 = None
Første_dosis_caliumfolinat_t54 = None
Sygeplejerske_navn_Første_dosis_caliumfolinat_t54 = None
Sygeplejerske_tid_Første_dosis_caliumfolinat_t54 = None
Ekstra_dosis_caliumfolinat_t54 = None
Sygeplejerske_navn_Ekstra_dosis_caliumfolinat_t54 = None
Sygeplejerske_tid_Ekstra_dosis_caliumfolinat_t54 = None
Se_MTX_t66 = None
Første_dosis_caliumfolinat_t66 = None
Sygeplejerske_navn_Første_dosis_caliumfolinat_t66 = None
Sygeplejerske_tid_Første_dosis_caliumfolinat_t66 = None
Ekstra_dosis_caliumfolinat_t66 = None
Sygeplejerske_navn_Ekstra_dosis_caliumfolinat_t66 = None
Sygeplejerske_tid_Ekstra_dosis_caliumfolinat_t66 = None


def gem_patientoplysninger():
    """
    Denne funktion tager de indtastede grunddata på patienten
    og gemmer værdierne i den dataframe som eksporteres til
    et dataark med Pandas
    """
    # Get global variabels
    global df
    global Navn
    global CPR
    global HDM_kur_nr
    global Alder
    global Højde
    global Vægt
    global Overflade
    global Infusions_start

    df_Patientoplysninger = pd.DataFrame({
        "Dato":[Dato],
        "Navn": [Navn],
        "CPR nr.":[CPR],
        "HDM_kur_nr":[HDM_kur_nr],
        "Alder":[Alder],
        "Højde":[Højde],
        "Vægt":[Vægt],
        "Overflade":[Overflade],
        "Infusions_start":[Infusions_start]
    })
    df = df.append(df_Patientoplysninger, ignore_index=True)
    df.to_excel(Destination_file)
    st.write("Patientoplysninger er gemt")
    

def patient_selection():
    """
    This function makes is possible to choose patiens in the dataark
    and to choose wich cure to be displayed
    """
    global patient
    global selected_treatment

    # We make a list to prevent dublicates
    Patient_list = set()

    # Iterate through names in datasheet 
    for names in range(len(df["Navn"])):
        # Find the first patient
        if len(Patient_list) == 0:
            Patient_list = {str(df["Navn"][names]) + " - " + str(df["CPR nr."][names])}
        # Find the rest of the patients
        if len(Patient_list) != 0:
            Patient_list.add(str(df["Navn"][names]) + " - " + str(df["CPR nr."][names]))
    
    # Streamlit seletbox can't handle sets, so we convert to a list
    Patient_list = list(Patient_list)
    Patient_list.sort()

    # Selectbox for selection patient
    if len(Patient_list) == 0:
        st.info("Der er ingen tidligere patienter. Opret ny patient.")
    if len(Patient_list) != 0:
        patient = st.selectbox("Navn - CRP nr.:", options=Patient_list)
        selected_patient = patient.split(" - ")


        # Make list of treatments
        row_in_excel = -1
        treatments = dict() # key: number of the treatment, value: the row in ecxel witch represent the treatment
        for cpr in range(len(df["CPR nr."])):
            row_in_excel += 1
            if str(selected_patient[1]) in str(df["CPR nr."][cpr]):
                treatments[str(df["HDM_kur_nr"][cpr])] = row_in_excel
        # Make list of treatmentsession for use in treatment selection
        treatment_list = list(treatments.keys())

        # Selectbox for selection treatment
        treatment = st.selectbox("Gå til i gangværende behandling:", options=treatment_list)
        # "selected_treatment" equals the row in dataframe witch represent the treatment
        selected_treatment = treatments[treatment]
        return selected_treatment
    



# This if-statement contains the page "Startside"
if page == "Startside":
    frontpage_subpage = st.radio("Find patient", options=frontpage_subpages)

    if frontpage_subpage == "Find tidligere patient":
        patient_selection()
        

    if frontpage_subpage == "Opret ny patient":
        # User input with patient data
        Dato = st.date_input('Ønsket dato for start af behandling')
        Navn = st.text_input('Navn')
        CPR = st.number_input('CPR nr.:', value=0)
        HDM_kur_nr = st.number_input('HDM kur nr:', min_value=0, max_value=8, value=0)
        Alder = st.number_input('Alder (år)', value=0)
        Højde = st.number_input('Højde (cm)', value=0)
        Vægt = st.number_input('Vægt (kg)', value=0)
        st.text('Overflade')
        Overflade = float((math.sqrt(Vægt * Højde))/60)
        if Overflade != 0.0:
            st.info(str(round(Overflade,2)) + " m^2")
        else:
            st.info("Indtast højde og vægt for at få beregnet overfladen")
        Infusions_start = st.time_input('Ønsket MTX infusionsstart')
        if st.button("Gem patiensoplysninger"):
            gem_patientoplysninger()
            
    

# This if-statement contains the page "Væskeregnskab"
if page == "Væskeregnskab":

    #### for testing ####
    Vægt = 25
    Højde=120
    Overflade = float((math.sqrt(Vægt * Højde))/60)
    Infusions_start = "12:00"
    #### for testing ####


    st.header(page)

    st.write('Total væskemængde 3000 ml/m²/døgn')
    Total_væskemængde = round(((((3000*(Overflade))/10))*10)/24)
    if Total_væskemængde != 0.0:
        st.info(str(Total_væskemængde) + " ml/time")

    st.write('Heraf mindst 2000 ml/m²/døgn iv.')
    Mindst_2000_væskemængde = round(((((2000*(Overflade))/10))*10)/24)
    if Mindst_2000_væskemængde != 0.0:
        st.info(str(Mindst_2000_væskemængde) + " ml/time")
    
    Plasma_kreatin_før_start = st.number_input('Plasma kreatinin før start af kuren µmol/l', value=0)
    
    st.write('Hydreringsvæske: 5% glucose tilsat 40 mmol Na-bicarbonat og 20 mmol KCl/liter.')
    st.write('Begræns peroralt indtag til 1000 ml/ under infusion af MTX.')
    st.write('Væskedøgn starter ved start på MTX-infusion (til tiden 0).')

    st.write('Diuresen skal være over 600 ml/m²/ 6 timer svt.')
    Durise_600ml_6timer = round(600*(Overflade))
    if Durise_600ml_6timer != 0.0:
        st.info(str(Durise_600ml_6timer) + " ml/6 timer")
    
    st.write('Hvis diuresen er mindre gives furosemid 0.5 mg/kg iv.')
    Furosemid = Decimal(0.5*Vægt).quantize(0, ROUND_HALF_UP)
    if Furosemid != 0.0:
        st.info(str(Furosemid) + " mg")



# This if-statement contains the page "Forhydrering"
if page == "Forhydrering":

    #### for testing ####
    Vægt = 25
    Højde=120
    Overflade = float((math.sqrt(Vægt * Højde))/60)
    Infusions_start = "12:00"
    #### for testing ####

    st.header(page)
    
    Forhydreringstid = str(Infusions_start) #+ timedelta(hours=9)[11:19]
    st.warning('Forhydrering er planlagt til kl ' + Forhydreringstid)
    #########################################
    #########################################
    # There is som problems with the time
    #########################################
    #########################################

    st.write('Start iv. hydrering:')
    st.write('Forhydrering med 600 ml/m² over 4 timer svt.')
    Forhydrering_6000ml_4timer = round(150*(Overflade))
    if Forhydrering_6000ml_4timer != 0.0:
        st.info(str(Forhydrering_6000ml_4timer) + " ml/t")

    st.warning('Urin pH skal være over 6.5 før start på MTX')

    st.write('Ved urin pH<7 skal patienten have:')
    st.write('Na-bicarbonat 20 mmol/m² iv over 30 min. i 40 ml hydreringsvæske.')

    st.write('Dosis af natriumbicarbonat ved urin pH <7.0:')
    Dosis_natriumcarbonat_ved_lav_pH = round(20*(Overflade))
    if Dosis_natriumcarbonat_ved_lav_pH != 0.0:
        st.info(str(Dosis_natriumcarbonat_ved_lav_pH) + " mmol")

    st.write('Ved urin pH > 8 skiftes til KNaG uden bicarbonat i 3 time.')
    st.write('Når pH er under 8 skiftes til bicarbonatholdig hydrering')

    Sygeplejerske_navn_forhydering = st.text_input('Givet af sygeplejerske:')
    Sygeplejerske_tid_forhydering = st.time_input('Tidspunkt:')
    


# This if-statement contains the page "MTX infusion"
if page == "MTX infusion":

    #### for testing ####
    Vægt = 25
    Højde=120
    Overflade = float((math.sqrt(Vægt * Højde))/60)
    Infusions_start = "12:00"
    Total_væskemængde=0
    #### for testing ####


    st.header(page)

    st.warning('Infusionsstart er planlagt til kl ' + str(Infusions_start))

    st.write('Start blodinfusion og angiv tidspunkt. 1/10 af MTX dosis gives over 1 time')
    one_to_ten_MTX_dose = (round((5000*(Overflade)*0.1)/10))*10
    if one_to_ten_MTX_dose != 0.0:
        st.info("1/10 dosis: " + str(one_to_ten_MTX_dose) + " mg")

    Sygeplejerske_navn_one_to_ten_MTX_dose = st.text_input('1/10 dosis: Givet af sygeplejerske:')
    Sygeplejerske_tid_one_to_ten_MTX_dose = st.time_input('1/10 dosis: Tidspunkt:')



    Kontinuerlig_infusion_start = str(Infusions_start) #+ timedelta(hours=1)[11:19]
    st.warning('Kontinuerlig infusion er planlagt til kl ' + str(Kontinuerlig_infusion_start))
    #########################################
    #########################################
    # There is som problems with the time
    #########################################
    #########################################

    st.write('Start kontinuerlig infusion af MTX. 9/10 af MTX dosis gives over 23 timer')
    nine_to_ten_MTX_dose = (round((5000*(Overflade)*0.9)/10))*10
    if nine_to_ten_MTX_dose != 0.0:
        st.info("9/10 dosis: " + str(nine_to_ten_MTX_dose) + " mg")

    st.write('Samlet mængde af MTX og hydreringsvæske: ')
    total_volume_MTX_and_hydration_liquid = Total_væskemængde
    if total_volume_MTX_and_hydration_liquid != 0.0:
        st.info(str(total_volume_MTX_and_hydration_liquid) + " ml/time")

    Sygeplejerske_navn_nine_to_ten_MTX_dose = st.text_input('9/10 dosis: Givet af sygeplejerske:')
    Sygeplejerske_tid_nine_to_ten_MTX_dose = st.time_input('9/10 dosis: Tidspunkt:')

# This if-statement contains the page "Monitorering af Toksicitet"
if page == "Monitorering af Toksicitet":
    st.header(page)

    #### for testing ####
    Vægt = 25
    Højde=120
    Overflade = float((math.sqrt(Vægt * Højde))/60)
    Infusions_start = "12:00"
    Total_væskemængde=0
    Plasma_kreatin_før_start=20
    #### for testing ####

    def Ekstra_dosis_caliumfolinat_function(Se_MTX_time):
        global Overflade
        global Vægt
        Ekstra_dosis_caliumfolinat = 0
        if 1 <= Se_MTX_time < 2: 
            Ekstra_dosis_caliumfolinat = 15 * Overflade
        if 2 <= Se_MTX_time < 3:
            Ekstra_dosis_caliumfolinat = 30 * Overflade
        if 3 <= Se_MTX_time < 4:
            Ekstra_dosis_caliumfolinat = 45 * Overflade
        if 4 <= Se_MTX_time < 5:
            Ekstra_dosis_caliumfolinat = 60 * Overflade
        if Se_MTX_time >= 5:
            Ekstra_dosis_caliumfolinat = Se_MTX_time * Vægt
        return Ekstra_dosis_caliumfolinat

    st.subheader("Time 36")
    st.warning('Blodprøver af plasma MTX og kreation er planlagt til kl  ' + str(Infusions_start))

    st.write('MTX konc t36 analyseres sammen med t23 til time 42 ')

    Se_MTX_t36 = st.number_input('Se-MTX t36 (µmol/l):')
    P_kreatin_t36 = st.number_input('P-kreatin (µmol/l):')

    if P_kreatin_t36 > Plasma_kreatin_før_start*1.5:
        Hydreing_ved_høj_P_kreatin_t36 = round(Overflade*4500/24) 
        Durise_ved_høj_P_kreatin_t36 = round(Overflade*900) 
        st.error("OPMÆRKSOM: Patienten er i høj-risiko for at have forsinket MTX udskillelse. " )  
        st.error("Hydreringen øges til 4500 ml/m²/døgn svt. " + str(Hydreing_ved_høj_P_kreatin_t36) + " ml/t " )
        st.error("Duriresen skal være over 900 ml/m²/ 6 timer svt. " + str(Durise_ved_høj_P_kreatin_t36) + " ml/t" )
    elif P_kreatin_t36 != 0:
        Hydreing_ved_normal_P_kreatin_t36 = round(Overflade*300/24) 
        Durise_ved_normal_P_kreatin_t36 = round(Overflade*600) 
        st.warning('Hydreringen fortsættes med 3000 ml/m²/døgn svarende til ' + str(Hydreing_ved_normal_P_kreatin_t36) + ' ml/t')
        st.warning('Duriresen skal være over 600 ml/m²/ 6 timer svt. ' + str(Durise_ved_normal_P_kreatin_t36) + ' ml/t')
    



    st.subheader("Time 42")
    st.warning('Blodprøver af plasma MTX er planlagt til kl  ' + str(Infusions_start))

    Se_MTX_t42 = st.number_input('Se-MTX t42 (µmol/l):', min_value=0.0, value=0.0, step=0.1) 
    Første_dosis_caliumfolinat_t42 = 15*Overflade
    st.write("Første dosis calciumfolinat-dosis 15 mg/m² svt.")
    st.info(str(round(Første_dosis_caliumfolinat_t42)) + " mg iv.")

    Sygeplejerske_navn_Første_dosis_caliumfolinat_t42 = st.text_input('Første dosis calciumfolinat t42: Givet af sygeplejerske:')
    Sygeplejerske_tid_Første_dosis_caliumfolinat_t42 = st.time_input('Første dosis calciumfolinat t42: Tidspunkt:')

    Ekstra_dosis_caliumfolinat_t42 = Ekstra_dosis_caliumfolinat_function(Se_MTX_t42)
    if Ekstra_dosis_caliumfolinat_t42 ==0.0:
        st.info("MTX t42 er ikke forhøjet. Der skal ikke gives ekstra dosis calciumfolinat. ")
    elif Ekstra_dosis_caliumfolinat_t42 !=0.0:
        st.info("Ekstra dosis calciumfolinat grundet forhøjet MTX t42 : " + str(round(Ekstra_dosis_caliumfolinat_t42)) + " mg iv.")
        st.info("Opstart evt. calciumfolinat mundskyl")
        Sygeplejerske_navn_Ekstra_dosis_caliumfolinat_t42 = st.text_input('Ekstra dosis calciumfolinat t42: Givet af sygeplejerske:')
        Sygeplejerske_tid_Ekstra_dosis_caliumfolinat_t42 = st.time_input('Ekstra dosis calciumfolinat t42: Tidspunkt:')
    




    st.subheader("Time 48")
    st.warning('Blodprøver af plasma MTX er planlagt til kl  ' + str(Infusions_start))

    Se_MTX_t48 = st.number_input('Se-MTX t48 (µmol/l):', min_value=0.0, value=0.0, step=0.1) 

    Første_dosis_caliumfolinat_t48 = 15*Overflade
    st.write("Første dosis calciumfolinat-dosis 15 mg/m² svt.")
    st.info(str(round(Første_dosis_caliumfolinat_t48)) + " mg iv.")

    Sygeplejerske_navn_Første_dosis_caliumfolinat_t48 = st.text_input('Første dosis calciumfolinat t48: Givet af sygeplejerske:')
    Sygeplejerske_tid_Første_dosis_caliumfolinat_t48 = st.time_input('Første dosis calciumfolinat t48: Tidspunkt:')

    Ekstra_dosis_caliumfolinat_t48 = Ekstra_dosis_caliumfolinat_function(Se_MTX_t48)
    if Ekstra_dosis_caliumfolinat_t48 ==0.0:
        st.info("MTX t48 er ikke forhøjet. Der skal ikke gives ekstra dosis calciumfolinat. ")
    elif Ekstra_dosis_caliumfolinat_t48 !=0.0:
        st.info("Ekstra dosis calciumfolinat grundet forhøjet MTX t48 : " + str(round(Ekstra_dosis_caliumfolinat_t48)) + " mg iv.")
        Sygeplejerske_navn_Ekstra_dosis_caliumfolinat_t48 = st.text_input('Ekstra dosis calciumfolinat t48: Givet af sygeplejerske:')
        Sygeplejerske_tid_Ekstra_dosis_caliumfolinat_t48 = st.time_input('Ekstra dosis calciumfolinat t48: Tidspunkt:')

    

    
    
    st.subheader("Time 54")
    st.warning('Blodprøver af plasma MTX er planlagt til kl  ' + str(Infusions_start))

    Se_MTX_t54 = st.number_input('Se-MTX t54 (µmol/l):', min_value=0.0, value=0.0, step=0.1) 

    Første_dosis_caliumfolinat_t54 = 15*Overflade
    st.write("Første dosis calciumfolinat-dosis 15 mg/m² svt.")
    st.info(str(round(Første_dosis_caliumfolinat_t54)) + " mg iv.")

    Sygeplejerske_navn_Første_dosis_caliumfolinat_t54 = st.text_input('Første dosis calciumfolinat t54: Givet af sygeplejerske:')
    Sygeplejerske_tid_Første_dosis_caliumfolinat_t54 = st.time_input('Første dosis calciumfolinat t54: Tidspunkt:')

    Ekstra_dosis_caliumfolinat_t54 = Ekstra_dosis_caliumfolinat_function(Se_MTX_t54)
    if Ekstra_dosis_caliumfolinat_t54 ==0.0:
        st.info("MTX t54 er ikke forhøjet. Der skal ikke gives ekstra dosis calciumfolinat. ")
    elif Ekstra_dosis_caliumfolinat_t54 !=0.0:
        st.info("Ekstra dosis calciumfolinat grundet forhøjet MTX t54 : " + str(round(Ekstra_dosis_caliumfolinat_t54)) + " mg iv.")
        Sygeplejerske_navn_Ekstra_dosis_caliumfolinat_t54 = st.text_input('Ekstra dosis calciumfolinat t54: Givet af sygeplejerske:')
        Sygeplejerske_tid_Ekstra_dosis_caliumfolinat_t54 = st.time_input('Ekstra dosis calciumfolinat t54: Tidspunkt:')
    



    
    st.subheader("Time 66")
    st.warning('Blodprøver af plasma MTX er planlagt til kl  ' + str(Infusions_start))

    Se_MTX_t66 = st.number_input('Se-MTX t66 (µmol/l):', min_value=0.0, value=0.0, step=0.1) 

    Første_dosis_caliumfolinat_t66 = 15*Overflade
    st.write("Første dosis calciumfolinat-dosis 15 mg/m² svt.")
    st.info(str(round(Første_dosis_caliumfolinat_t66)) + " mg iv.")

    Sygeplejerske_navn_Første_dosis_caliumfolinat_t66 = st.text_input('Første dosis calciumfolinat t66: Givet af sygeplejerske:')
    Sygeplejerske_tid_Første_dosis_caliumfolinat_t66 = st.time_input('Første dosis calciumfolinat t66: Tidspunkt:')

    Ekstra_dosis_caliumfolinat_t66 = Ekstra_dosis_caliumfolinat_function(Se_MTX_t66)
    if Ekstra_dosis_caliumfolinat_t66 == 0.0:
        st.info("MTX t66 er ikke forhøjet. Der skal ikke gives ekstra dosis calciumfolinat. ")
    elif Ekstra_dosis_caliumfolinat_t66 > 0.1:
        st.info("Ekstra dosis calciumfolinat grundet forhøjet MTX t66 : " + str(round(Ekstra_dosis_caliumfolinat_t66)) + " mg iv.")
        Sygeplejerske_navn_Ekstra_dosis_caliumfolinat_t66 = st.text_input('Ekstra dosis calciumfolinat t66: Givet af sygeplejerske:')
        Sygeplejerske_tid_Ekstra_dosis_caliumfolinat_t66 = st.time_input('Ekstra dosis calciumfolinat t66: Tidspunkt:')
    elif Ekstra_dosis_caliumfolinat_t66 <= 0.1:
        st.info("Patienten må udskrives og skal komme til kontrol af blodprøver om 7 døgn")



