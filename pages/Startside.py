import streamlit as st
import math
import datetime as dt
import time

from basics import * 

def write():
    # Load dataframes from excel sheets
    df = pd.read_excel(Destination_main_file, na_filter=False)
    df_st = pd.read_excel(Destination_st_file)
    # Remove "Unnamed: 0" collums from dataframe
    df.drop(['Unnamed: 0'], axis=1, inplace=True)

    global Navn
    global CPR
    global HDM_kur_nr
    global Alder
    global Højde
    global Vægt
    global Overflade
    global Infusions_start
    global selected_treatment

    frontpage_subpages= ["Find tidligere patient", "Opret ny patient"]

    def gem_patientoplysninger():
        """
        Denne funktion tager de indtastede grunddata på patienten
        og gemmer værdierne i den dataframe som eksporteres til
        et dataark med Pandas
        """
        # Get global variabel for dataframe
        global df

        Treatment_time_t0 = dt.datetime.combine(dt.date(Dato.year,Dato.month,Dato.day),dt.time(Infusions_start.hour,Infusions_start.minute))

        df_Patientoplysninger = pd.DataFrame({
            "Navn": [Navn],
            "CPR nr.": [CPR],
            "HDM_kur_nr": [HDM_kur_nr],
            "Alder": [Alder],
            "Højde": [Højde],
            "Vægt": [Vægt],
            "Overflade": [Overflade],
            "Treatment_time_t0": [Treatment_time_t0]
        })
        df = df.append(df_Patientoplysninger, ignore_index=True, sort=False)
        df.to_excel(Destination_main_file)
        st.write("Patientoplysninger er gemt")
    
    def patient_selection():
        """
        This function makes is possible to choose patients in the dataark
        and to choose wich cure to be displayed
        """
        # Get global variabel for dataframe
        global df_st
        global df


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

            if st.button("Vælg patient"):
                df_st = pd.DataFrame({"selected_treatment":[selected_treatment]})
                df_st.to_excel(Destination_st_file)
            
            st.subheader("Følgende patient er valg:")
            # in case of KeyError for [df_st["selected_treatment"][0], exception is rasied
            try:
                st.info(
                    "Patient: " + df["Navn"][df_st["selected_treatment"][0]]+ " - "+ str(df["CPR nr."][df_st["selected_treatment"][0]])+ "  \n" 
                    "Kur nr.: "+ str(df["HDM_kur_nr"][df_st["selected_treatment"][0]])+ "  \n"+ 
                    "Behandlings start t0: "+ str(df["Treatment_time_t0"][df_st["selected_treatment"][0]])
                )
            except KeyError:   
                st.warning("Der er ikke valg en patient. Vælg patient og behandling ovenfor og tryk på knappen 'Vælg patient'.")
            except TypeError:   
                st.warning("Der er ikke valg en patient. Vælg patient og behandling ovenfor og tryk på knappen 'Vælg patient'.")
            
            try:
                # Give posibility to delete a treatment
                slet_patient = st.checkbox("Slet patientens behandlingsdata (" + df["Navn"][df_st["selected_treatment"][0]] + " - Kur nr.: " + str(df["HDM_kur_nr"][df_st["selected_treatment"][0]]) + ")")
                if slet_patient:
                    st.error(
                        "Er du sikker på at du vil slette behandlingsdataen for følgende patient?  \n\n"
                        "Patient: " + df["Navn"][df_st["selected_treatment"][0]]+ " - "+ str(df["CPR nr."][df_st["selected_treatment"][0]])+ "  \n"+ 
                        "Kur nr.: "+ str(df["HDM_kur_nr"][df_st["selected_treatment"][0]])+ "  \n"+ 
                        "Behandlings start t0: "+ str(df["Treatment_time_t0"][df_st["selected_treatment"][0]]) + "  \n\n"
                        "Det er ikke muligt at fortryde."
                    )
                    if st.button("Ja, slet behandlingsdata"):
                        df.drop(axis=0, index=df_st["selected_treatment"][0], inplace=True)
                        df.to_excel(Destination_main_file)
                        st.write("Behandlingen er slettet.")
            except KeyError:
                pass
            except TypeError:
                pass



    # content starts here
    frontpage_subpage = st.radio("Find patient", options=frontpage_subpages)

    if frontpage_subpage == "Find tidligere patient":
        patient_selection()
    

    if frontpage_subpage == "Opret ny patient":
        # User input with patient data
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
        Dato = st.date_input('Ønsket dato for start af behandling')
        Infusions_start = st.time_input('Ønsket MTX infusionsstart')
        if st.button("Gem patiensoplysninger"):
            gem_patientoplysninger()
        