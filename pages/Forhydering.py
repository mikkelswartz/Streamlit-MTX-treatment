import streamlit as st
import datetime as dt

from basics import *

def write():
    # Load dataframes from excel sheets
    df = pd.read_excel(Destination_main_file, na_filter=False)
    df_st = pd.read_excel(Destination_st_file)
    # Remove "Unnamed: 0" collums from dataframe
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    # in case of KeyError for [df_st["selected_treatment"][0], exception is rasied an user is referred to startpage
    try:
        # Export functions
        def Sygeplejerske_forhydrering_export():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_forhydering"] = Sygeplejerske_navn_forhydering
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_forhydering"] = Sygeplejerske_tid_forhydering
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        # Get variabels from dataframe
        Overflade = df["Overflade"][df_st["selected_treatment"][0]]
        Treatment_time_t0 = df["Treatment_time_t0"][df_st["selected_treatment"][0]]

        

        # Selected patient info
        st.info(
            "Patient: " + df["Navn"][df_st["selected_treatment"][0]]+ " - "+ str(df["CPR nr."][df_st["selected_treatment"][0]])+ "  \n"
            "Kur nr.: "+ str(df["HDM_kur_nr"][df_st["selected_treatment"][0]])+ "  \n"+ 
            "Behandlings start t0: "+ str(df["Treatment_time_t0"][df_st["selected_treatment"][0]])
        )

        st.subheader("Væskeregnskab")
        st.write('Hydreringsvæske: 5% glucose tilsat 40 mmol Na-bicarbonat og 20 mmol KCl/liter.  \n'
            'Total væskemængde 3000 ml/m²/døgn'
        )
        Total_væskemængde = int(round(((((3000*(Overflade))/10))*10)/24))
        if Total_væskemængde != 0.0:
            st.info(str(Total_væskemængde) + " ml/time")
            df.loc[df_st["selected_treatment"][0],"Total_væskemængde"] = Total_væskemængde
            df.to_excel(Destination_main_file)

        st.write('Heraf mindst 2000 ml/m²/døgn iv.')
        Mindst_2000_væskemængde = int(round(((((2000*(Overflade))/10))*10)/24))
        if Mindst_2000_væskemængde != 0.0:
            st.info(str(Mindst_2000_væskemængde) + " ml/time")
            df.loc[df_st["selected_treatment"][0],"Mindst_2000_væskemængde"] = Mindst_2000_væskemængde
            df.to_excel(Destination_main_file)

        st.write(
            'Begræns peroralt indtag til 1000 ml/m² under infusion af MTX.  \n'
            'Væskedøgn starter ved start på MTX-infusion (til tiden 0).  MTX-Væsken medregnes.'
        ) 

        Forhydreringstid = Treatment_time_t0 + dt.timedelta(hours=-4)
        st.subheader("Time -4. Forhydrering: " + str(Forhydreringstid))
        st.write(
            'Start iv. hydrering:  \n'
            'Forhydrering med 600 ml/m² hydreringsvæske over 4 timer svt.'
        )
        Forhydrering_6000ml_4timer = int(round(150*(Overflade))) 
        if Forhydrering_6000ml_4timer != 0.0:
            st.info(str(Forhydrering_6000ml_4timer) + " ml/t")
            df.loc[df_st["selected_treatment"][0],"Forhydrering_6000ml_4timer"] = Forhydrering_6000ml_4timer
            df.to_excel(Destination_main_file)


        if df["Plasma_kreatinin_før_start"][df_st["selected_treatment"][0]] == "":
            Plasma_kreatinin_før_start = st.number_input('Plasma kreatinin før start af kuren µmol/l', min_value=0, value=0)
        if df["Plasma_kreatinin_før_start"][df_st["selected_treatment"][0]] != "":
            Plasma_kreatinin_før_start = st.number_input('Plasma kreatinin før start af kuren µmol/l', min_value=0, value=int(df["Plasma_kreatinin_før_start"][df_st["selected_treatment"][0]]))
        if Plasma_kreatinin_før_start != 0.0:
            df.loc[df_st["selected_treatment"][0],"Plasma_kreatinin_før_start"] = Plasma_kreatinin_før_start
            df.to_excel(Destination_main_file)
        
        

        # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
        Sygeplejerske_navn_forhydering = st.text_input('Forhydrering givet af sygeplejerske:', value=df["Sygeplejerske_navn_forhydering"][df_st["selected_treatment"][0]])
    
        # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
        tid__4 = df["Sygeplejerske_tid_forhydering"][df_st["selected_treatment"][0]]
        if tid__4 == "":
            Sygeplejerske_tid_forhydering = st.time_input('Tidspunkt forhydrering:')
        if tid__4 != "":
            Sygeplejerske_tid_forhydering = st.time_input('Tidspunkt forhydrering:', dt.time(int(tid__4[0:2]),int(tid__4[3:5]),int(tid__4[6:8])))
        # Button for saving input for nurse and time to excel
        if st.button("Gem behandlingsdata"):
            Sygeplejerske_forhydrering_export()
        
    except IndexError:
        st.info("Der er ingen tidligere patienter. Gå til startside og opret ny patient.")