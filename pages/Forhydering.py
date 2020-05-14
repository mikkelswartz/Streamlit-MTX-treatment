import streamlit as st
import datetime as dt

from basics import *

def write():
    # Load dataframes from excel sheets
    df = MTX.MTX_pandas_main_file(Destination_main_file)
    # Pandas dataframe witch value equals the row in the dataframe witch represent the selected treatment
    df_st = MTX.MTX_pandas_st_file(Destination_st_file)


    # in case of KeyError for [df_st["selected_treatment"][0], exception is rasied an user is referred to startpage
    try:
        # Get variabels from dataframe
        Overflade = df["Overflade"][df_st["selected_treatment"][0]]
        Alder = df["Alder"][df_st["selected_treatment"][0]]
        Køn = df["Køn"][df_st["selected_treatment"][0]]
        
        # Selected patient info
        MTX.patient_information_box(df, df_st)

        st.subheader("Væskeregnskab")
        # Text area for notes
        MTX.Fritekst_indtastningsfelt("Væskeregnskab", df, df_st)

        Total_væskemængde = int(round(((((3000*(Overflade))/10))*10)/24))
        if Total_væskemængde != 0.0:
            st.write(
                "Hydreringsvæske: 5% glucose tilsat 40 mmol Na-bicarbonat og 20 mmol KCl/liter.  \n"
                "Total væskemængde 3000 ml/m²/døgn svt. **" + str(Total_væskemængde) + " ml/t **")
            df.loc[df_st["selected_treatment"][0],"Total_væskemængde"] = Total_væskemængde
            df.to_excel(Destination_main_file)

        st.write(
            "Begræns peroralt indtag til 1000 ml/m² under infusion af MTX.  \n"
            "Væskedøgn starter ved start på MTX-infusion (til tiden 0).  MTX-Væsken medregnes."
        ) 

        st.subheader("Forhydrering")
        # Text area for notes
        MTX.Fritekst_indtastningsfelt("Forhydrering", df, df_st)

        Forhydrering_6000ml_4timer = int(round(150*(Overflade))) 
        if Forhydrering_6000ml_4timer != 0.0:
            st.write(
                "Start iv. hydrering:  \n"
                "Forhydrering med 600 ml/m² hydreringsvæske over 4 timer svt. **" + str(Forhydrering_6000ml_4timer) + " ml/t**"
            )
            df.loc[df_st["selected_treatment"][0],"Forhydrering_6000ml_4timer"] = Forhydrering_6000ml_4timer
            df.to_excel(Destination_main_file)

        if df["Plasma_kreatinin_før_start"][df_st["selected_treatment"][0]] == "":
            Plasma_kreatinin_før_start = MTX.custom_number_input("Plasma kreatinin før start af kuren µmol/l", int_or_float=int)
        if df["Plasma_kreatinin_før_start"][df_st["selected_treatment"][0]] != "":
            Plasma_kreatinin_før_start = MTX.custom_number_input("Plasma kreatinin før start af kuren µmol/l", int_or_float=int, value=int(df["Plasma_kreatinin_før_start"][df_st["selected_treatment"][0]]))
        if Plasma_kreatinin_før_start != 0:
            df.loc[df_st["selected_treatment"][0],"Plasma_kreatinin_før_start"] = Plasma_kreatinin_før_start
            df.to_excel(Destination_main_file)

        try:
            # P-Kreatinin check
            if Plasma_kreatinin_før_start != 0:
                if 1 <= Alder < 3:
                    if not 15 <= Plasma_kreatinin_før_start <= 30:
                        st.error("P-Kreatinin ligger uden for normalområdet på 15-30 µM som er gældende for patientens alder. Tjek indtastning.")
                if 3 <= Alder < 5:
                    if not 25 <= Plasma_kreatinin_før_start <= 35:
                        st.error("P-Kreatinin ligger uden for normalområdet på 25-35 µM som er gældende for patientens alder. Tjek indtastning.")
                if 5 <= Alder < 7:
                    if not 25 <= Plasma_kreatinin_før_start <= 40:
                        st.error("P-Kreatinin ligger uden for normalområdet på 25-40 µM som er gældende for patientens alder. Tjek indtastning.")
                if 7 <= Alder < 9:
                    if not 30 <= Plasma_kreatinin_før_start <= 50:
                        st.error("P-Kreatinin ligger uden for normalområdet på 30-50 µM som er gældende for patientens alder. Tjek indtastning.")
                if 9 <= Alder < 11:
                    if not 30 <= Plasma_kreatinin_før_start <= 55:
                        st.error("P-Kreatinin ligger uden for normalområdet på 30-55 µM som er gældende for patientens alder. Tjek indtastning.")
                if 11 <= Alder < 13:
                    if not 35 <= Plasma_kreatinin_før_start <= 65:
                        st.error("P-Kreatinin ligger uden for normalområdet på 35-65 µM som er gældende for patientens alder. Tjek indtastning.")
                if 13 <= Alder < 16:
                    if not 35 <= Plasma_kreatinin_før_start <= 70:
                        st.error("P-Kreatinin ligger uden for normalområdet på 35-70 µM som er gældende for patientens alder. Tjek indtastning.")
                if 16  <= Alder:
                    if Køn == "Mand":
                        if not 60 <= Plasma_kreatinin_før_start <= 105:
                            st.error("P-Kreatinin ligger uden for normalområdet på 60-105 µM som er gældende for patientens alder og køn. Tjek indtastning.")
                    if Køn == "Kvinde":
                        if not 45 <= Plasma_kreatinin_før_start <= 90:
                            st.error("P-Kreatinin ligger uden for normalområdet på 45-90 µM som er gældende for patientens alder og køn. Tjek indtastning.")
        except TypeError as error:
            if error == "'<=' not supported between instances of 'int' and 'NoneType'":
                pass
    
                
        # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
        Sygeplejerske_navn_værdi = st.text_input("Forhydrering er opsat af sygeplejerske:", value=df["Sygeplejerske_navn_forhydering"][df_st["selected_treatment"][0]])
        
        # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
        tid = df["Sygeplejerske_tid_forhydering"][df_st["selected_treatment"][0]]
        if tid == "":
            Sygeplejerske_tid_værdi = st.time_input("Forhydrering er opsat til tidspunktet:")
            Dato = st.date_input("Forhydrering er opsat den:")
        if tid != "":
            Sygeplejerske_tid_værdi = st.time_input("Forhydrering er opsat til tidspunktet:", dt.time(int(tid[0:2]),int(tid[3:5])),int(tid[6:8]))
            Dato = st.date_input("Forhydrering er opsat den:")
    
        # Input for the duration of forhydrering
        if str(df["Forhydrering_varighed_værdi"][df_st["selected_treatment"][0]]) == "4" or "NaT":
            Forhydrering_varighed = st.radio("Varighed af forhydrering:", options=["4 timer", "Andet"], index=0)
        elif str(df["Forhydrering_varighed_værdi"][df_st["selected_treatment"][0]]) != "4": 
            Forhydrering_varighed = st.radio("Varighed af forhydrering:", options=["4 timer", "Andet"], index=1)
        # Input if the duration of forhydrering is different for 4 hours
        if Forhydrering_varighed == "4 timer":
            Forhydrering_varighed_værdi = float(4.00)
        if Forhydrering_varighed == "Andet":
            if df["Forhydrering_varighed_værdi"][df_st["selected_treatment"][0]] != "":
                Forhydrering_varighed_værdi = st.number_input("Angiv varighed af forhydrering (i timer)", value=float(df["Forhydrering_varighed_værdi"][df_st["selected_treatment"][0]]), min_value=0.0, step=0.25)
            else:
                Forhydrering_varighed_værdi = st.number_input("Angiv varighed af forhydrering (i timer)", value=4.0, min_value=0.0, step=0.25)


        # Combine input date and input time to af datetime.datetime object
        Forhydreringstidspunkt = dt.datetime.combine(dt.date(Dato.year,Dato.month,Dato.day),dt.time(Sygeplejerske_tid_værdi.hour,Sygeplejerske_tid_værdi.minute))
        # Finds the treatment t0 based on date and time input from user.
        Treatment_time_t0 = Forhydreringstidspunkt + dt.timedelta(hours=Forhydrering_varighed_værdi)

        # Input check if Forhydrering_varighed_værdi is < 4 hours
        if Forhydrering_varighed_værdi < 4:
            st.error(
                "Du har valgt at varigheden af forhydreringen skal være mindre end 4 timer.  \n"
                "Er du sikker på at du vil fortsætte?"
                )
            Fortsæt_tid = st.checkbox("Ja, fortsæt en forhydreringstid på mindre end 4 timer.")

        # Input check for input date.
        if Dato != dt.date.today() and tid == "":
            st.error(
                "Du har valgt en anden dato end dags dato.  \n"
                "Vil du fortsætte for at gemme?"
            )
            Fortsæt_dato = st.checkbox("Ja, fortsæt.")
        if Dato != dt.date.today() and tid != "":
            st.warning(
                "Vil du ændre datoen for forhyderingen og fortæstte for at genne ny nato?"
            )
            Fortsæt_dato = st.checkbox("Ja, fortsæt.")

        # Safes data to dataframe
        if Dato == dt.date.today() or (Dato != dt.date.today() and Fortsæt_dato is True):
            if Forhydrering_varighed_værdi >= 4 or (Forhydrering_varighed_værdi < 4 and Fortsæt_tid is True):
                # Button for saving input for nurse and time to excel
                if st.button("Gem behandlingsdata for: Forhydrering"):
                    df.loc[df_st["selected_treatment"][0], "Sygeplejerske_navn_forhydering"] = Sygeplejerske_navn_værdi
                    df.loc[df_st["selected_treatment"][0], "Sygeplejerske_tid_forhydering"] = Sygeplejerske_tid_værdi
                    df.loc[df_st["selected_treatment"][0], "Treatment_time_t0"] = Treatment_time_t0
                    df.loc[df_st["selected_treatment"][0], "Forhydrering_varighed_værdi"] = Forhydrering_varighed_værdi
                    df.to_excel(Destination_main_file)
                    st.write("Behandlingsdata er gemt")

        st.info(
            "Urin pH måles i hver vandladning indtil pt. udskrives.  \n"
            "Patienten opfordres til at tisse mindst hver 3. time.  \n"
            "Ved urin-pH < 7.0 skal der gives ekstra bicarbonat:  \n"
            "Na-bicarbonat 20 mmol/m² blandes i 40 ml af hydreringsvæsken og gives over 30 min. samtidig med forhydreringen.  \n\n"
            "Højdosis MTX må startes:  \n"
            " - Efter mindst 4 timers forhydrering.  \n"
            " - Efter urin pH har været ≥7.0 i mindst 3 timer"
        )

        if Treatment_time_t0 != None:
            st.info("MTX infusion bør startes den " + str(Treatment_time_t0.date()) + " kl. " + str(Treatment_time_t0.time())[:-3])

    except IndexError:
        st.info("Der er ingen tidligere patienter. Gå til startside og opret ny patient.")
    except KeyError:
        st.warning(
            "Der er ikke valg en patient.  \n"
            "Gå til 'Startside', vælg patient og behandling og tryk på knappen 'Vælg patient'."
            )