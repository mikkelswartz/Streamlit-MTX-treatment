import streamlit as st
import math 
import datetime as dt
import time
import re
import importlib


from basics import * 

def write():
    # Load dataframes from excel sheets
    df = MTX.MTX_pandas_main_file(Destination_main_file)
    # Pandas dataframe witch value equals the row in the dataframe witch represent the selected treatment
    df_st = MTX.MTX_pandas_st_file(Destination_st_file)

    # subpage navigation
    frontpage_subpages= ["Find tidligere patient", "Opret ny patient"]
    frontpage_subpage = st.radio("Find patient", options=frontpage_subpages)

    if frontpage_subpage == "Find tidligere patient":
    
        # Overwiew of hospitalized patients
        Vis_indlagte = st.checkbox("Vis indlagte patienter")
        if Vis_indlagte:
            df_indskrevet = pd.DataFrame({})
            for names in range(len(df["Navn"])):
                #st.write(df["CPR nr."][names])
                if df["Udskrevet"][names] == False:
                    if str(df["Treatment_time_t0"][names]) == "NaT":
                        Behandlingsstart = "Behandling ikke startet"
                    if str(df["Treatment_time_t0"][names]) != "NaT":
                        Behandlingsstart = str(df["Treatment_time_t0"][names])
                        
                    df_indskrevet_ny = pd.DataFrame({
                        "Navn": [df["Navn"][names]],
                        "CPR nr.": [df["CPR nr."][names]],
                        "HDM kur nr.": [df["HDM_kur_nr"][names]],
                        "MTX infusionsstart": [Behandlingsstart],
                    })
                    df_indskrevet = df_indskrevet.append(df_indskrevet_ny, ignore_index=True, sort=False)
            st.dataframe(df_indskrevet)



        # We make a set to prevent dublicates
        Patient_set = set()

        # Iterate through names in datasheet 
        for names in range(len(df["Navn"])):
            # Find the first patient
            if len(Patient_set) == 0:
                Patient_set = {str(df["Navn"][names]) + " - " + str(df["CPR nr."][names])}
            # Find the rest of the patients
            if len(Patient_set) != 0:
                Patient_set.add(str(df["Navn"][names]) + " - " + str(df["CPR nr."][names]))
        
        # Streamlit selectbox can't handle sets, so we convert to a list
        Patient_list = list(Patient_set)
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
            # information box is displayed
            MTX.patient_information_box_full(df, df_st)
            # Text area for notes
            MTX.Fritekst_indtastningsfelt("Grundnote", df, df_st)


            # in case of KeyError for [df_st["selected_treatment"][0], exception is rasied
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
            except (KeyError, TypeError):
                pass



    if frontpage_subpage == "Opret ny patient":
        # User input with patient data
        Navn = st.text_input("Navn")
        CPR = st.text_input("CPR nr.: (DDMMYY-XXX)")
        
        # CPR check
        if CPR != "":
            try:
                REresult_CPR = re.search(r'^(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[012])(\d\d)-(\d{4})$', CPR)
                if REresult_CPR is None:
                    st.error(
                        "Det indtastede CPR nummer er ikke gyldigt.  \n"
                        "CPR nummer skal indtastes som 'DDMMYY-XXXX'"
                    )
                if int(CPR[-1:]) % 2 == 0 :
                    Køn = "Kvinde"
                if int(CPR[-1:]) % 2 != 0:
                    Køn = "Mand"
                Alder = str(MTX.CPR_to_age(CPR))
                if Alder != "None":
                    st.write(
                        "Alder: " + Alder + "  \n"
                        "Køn: " + Køn
                    )
            except (ValueError, UnboundLocalError):
                pass


        HDM_kur_nr = MTX.custom_number_input("HDM kur nr:",  int_or_float=int)
        Højde = MTX.custom_number_input("Højde (cm)",  int_or_float=int)
        Vægt = MTX.custom_number_input("Vægt (kg)",  int_or_float=int)

        # Check for relation between weigh, height and age
        try:
            if  Vægt != 0 and Højde != 0 and Alder != "":
                if 1 <= int(Alder) <= 18:
                    if not int(Vægt)*0.90 <= ((int(Alder) + 4)*2) <= int(Vægt)*1.1:
                        Teoretisk_vægt_alder = ((int(Alder) + 4)*2)
                        st.error(
                            "Patienten bør veje " + str(Teoretisk_vægt_alder) + " kg ifølge formlen $(Alder \ i \ år +4) \cdot 2=kg$   \n"
                            "Patientens vægt på " + str(Vægt) + " kg afviger med mere end 10%. Tjek indtastningerne."
                        ) 
                if 2 <= int(Alder) <= 18:
                    if Køn == "Mand":
                        Teoretisk_vægt_højde = round(2.329*math.exp(1.895*(Højde*0.01)))
                        if not Vægt*0.9 <= Teoretisk_vægt_højde <= Vægt*1.1:
                            st.error(
                                "Patienten bør veje " + str(Teoretisk_vægt_højde) + " kg ifølge formlen   \n"
                                "$$Kg=2,329 \cdot exp(1,895 \cdot højde \ i \ m)$$"
                                "  \nPatientens vægt på " + str(Vægt) + " kg afviger med mere end 10%. Tjek indtastningerne."
                            )
                    if Køn == "Kvinde":
                        Teoretisk_vægt_højde = round(2.120*math.exp(1.993*(Højde*0.01)))
                        if not Vægt*0.9 <= Teoretisk_vægt_højde <= Vægt*1.1:
                            st.error(
                                "Patienten bør veje " + str(Teoretisk_vægt_højde) + " kg ifølge formlen   \n"
                                "$$Kg=2,120 \cdot exp(1,993 \cdot højde \ i \ m)$$"
                                "  \nPatientens vægt på " + str(Vægt) + " kg afviger med mere end 10%. Tjek indtastningerne."
                            )
        except (UnboundLocalError, TypeError):
            pass

        # Calculate surface
        try:
            Overflade = round(float((math.sqrt(Vægt * Højde))/60),2)
        except TypeError as error:
            if error == "unsupported operand type(s) for *: 'NoneType' and 'NoneType'":
                pass
            if error == "int() argument must be a string, a bytes-like object or a number, not 'NoneType'":
                pass


        try:

            if REresult_CPR is None and CPR != "":
                st.error(
                    "Kan ikke gemme patientdata:  \n"
                    "CPR nummer er ikke gyldigt."
                )
            if REresult_CPR is not None and HDM_kur_nr is not None and Vægt is not None and Højde is not None:
                if st.button("Gem patiensoplysninger"):
                    # checks if patient is in dataframe whit the gived HDM traetment
                    Patient_i_dataframe = False
                    for patient in range(0,len(df["CPR nr."])):             
                        if str(CPR) == str(df["CPR nr."][patient]) and str(HDM_kur_nr) == str(df["HDM_kur_nr"][patient]):
                            st.error(
                                "En patient med det angivede CPR nummer er allerede registreret for en HDM kur nr. " + str(HDM_kur_nr) + "  \n"
                                "De indtastede oplysninger kan derfor ikke gemmes."
                            )
                            Patient_i_dataframe = True
                    if Patient_i_dataframe is False:
                        MTX.gem_patientoplysninger(Navn, CPR, Alder, Køn, HDM_kur_nr, Højde, Vægt, Overflade, df, df_st)
        except UnboundLocalError:
            pass
        

        