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
        # Get variabels from dataframe
        Vægt = df["Vægt"][df_st["selected_treatment"][0]]
        Overflade = df["Overflade"][df_st["selected_treatment"][0]]
        Treatment_time_t0 = df["Treatment_time_t0"][df_st["selected_treatment"][0]]
        Plasma_kreatinin_før_start = df["Plasma_kreatinin_før_start"][df_st["selected_treatment"][0]]
        

        # Export functions
        def Sygeplejerske_dosis_calciumfolinat_t42():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_dosis_calciumfolinat_t42"] = Sygeplejerske_navn_dosis_calciumfolinat_t42
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_dosis_calciumfolinat_t42"] = Sygeplejerske_tid_dosis_calciumfolinat_t42
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Ekstra_dosis_calciumfolinat_t42():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Ekstra_dosis_calciumfolinat_t42"] = Sygeplejerske_navn_Ekstra_dosis_calciumfolinat_t42
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Ekstra_dosis_calciumfolinat_t42"] = Sygeplejerske_tid_Ekstra_dosis_calciumfolinat_t42
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_dosis_calciumfolinat_t48():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_dosis_calciumfolinat_t48"] = Sygeplejerske_navn_dosis_calciumfolinat_t48
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_dosis_calciumfolinat_t48"] = Sygeplejerske_tid_dosis_calciumfolinat_t48
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")
        
        def Sygeplejerske_dosis_calciumfolinat_t54():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_dosis_calciumfolinat_t54"] = Sygeplejerske_navn_dosis_calciumfolinat_t54
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_dosis_calciumfolinat_t54"] = Sygeplejerske_tid_dosis_calciumfolinat_t54
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_dosis_calciumfolinat_t60():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_dosis_calciumfolinat_t60"] = Sygeplejerske_navn_dosis_calciumfolinat_t60
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_dosis_calciumfolinat_t60"] = Sygeplejerske_tid_dosis_calciumfolinat_t60
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_dosis_calciumfolinat_t66():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_dosis_calciumfolinat_t66"] = Sygeplejerske_navn_dosis_calciumfolinat_t66
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_dosis_calciumfolinat_t66"] = Sygeplejerske_tid_dosis_calciumfolinat_t66
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Første_Ekstra_dosis_calciumfolinat_t66():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t66"] = Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t66
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t66"] = Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t66
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Anden_Ekstra_dosis_calciumfolinat_t66():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t66"] = Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t66
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t66"] = Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t66
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Tredje_Ekstra_dosis_calciumfolinat_t66():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t66"] = Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t66
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t66"] = Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t66
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Fjerde_Ekstra_dosis_calciumfolinat_t66():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t66"] = Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t66
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t66"] = Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t66
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_dosis_calciumfolinat_t90():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_dosis_calciumfolinat_t90"] = Sygeplejerske_navn_dosis_calciumfolinat_t90
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_dosis_calciumfolinat_t90"] = Sygeplejerske_tid_dosis_calciumfolinat_t90
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Første_Ekstra_dosis_calciumfolinat_t90():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t90"] = Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t90
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t90"] = Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t90
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Anden_Ekstra_dosis_calciumfolinat_t90():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t90"] = Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t90
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t90"] = Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t90
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Tredje_Ekstra_dosis_calciumfolinat_t90():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t90"] = Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t90
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t90"] = Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t90
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Fjerde_Ekstra_dosis_calciumfolinat_t90():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t90"] = Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t90
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t90"] = Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t90
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_dosis_calciumfolinat_t114():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_dosis_calciumfolinat_t114"] = Sygeplejerske_navn_dosis_calciumfolinat_t114
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_dosis_calciumfolinat_t114"] = Sygeplejerske_tid_dosis_calciumfolinat_t114
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Første_Ekstra_dosis_calciumfolinat_t114():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t114"] = Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t114
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t114"] = Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t114
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Anden_Ekstra_dosis_calciumfolinat_t114():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t114"] = Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t114
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t114"] = Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t114
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Tredje_Ekstra_dosis_calciumfolinat_t114():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t114"] = Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t114
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t114"] = Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t114
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Fjerde_Ekstra_dosis_calciumfolinat_t114():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t114"] = Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t114
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t114"] = Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t114
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_dosis_calciumfolinat_t138():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_dosis_calciumfolinat_t138"] = Sygeplejerske_navn_dosis_calciumfolinat_t138
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_dosis_calciumfolinat_t138"] = Sygeplejerske_tid_dosis_calciumfolinat_t138
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Første_Ekstra_dosis_calciumfolinat_t138():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t138"] = Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t138
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t138"] = Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t138
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Anden_Ekstra_dosis_calciumfolinat_t138():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t138"] = Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t138
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t138"] = Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t138
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Tredje_Ekstra_dosis_calciumfolinat_t138():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t138"] = Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t138
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t138"] = Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t138
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Fjerde_Ekstra_dosis_calciumfolinat_t138():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t138"] = Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t138
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t138"] = Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t138
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_dosis_calciumfolinat_t162():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_dosis_calciumfolinat_t162"] = Sygeplejerske_navn_dosis_calciumfolinat_t162
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_dosis_calciumfolinat_t162"] = Sygeplejerske_tid_dosis_calciumfolinat_t162
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Første_Ekstra_dosis_calciumfolinat_t162():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t162"] = Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t162
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t162"] = Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t162
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Anden_Ekstra_dosis_calciumfolinat_t162():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t162"] = Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t162
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t162"] = Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t162
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Tredje_Ekstra_dosis_calciumfolinat_t162():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t162"] = Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t162
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t162"] = Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t162
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Fjerde_Ekstra_dosis_calciumfolinat_t162():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t162"] = Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t162
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t162"] = Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t162
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")


        
        # Calculator for ekstra dosis calciumfolinat
        def Ekstra_dosis_calciumfolinat_function(Se_MTX_time):
            Ekstra_dosis_calciumfolinat = 0
            if Se_MTX_time < 1:
                Ekstra_dosis_calciumfolinat = int(round(15 * Overflade))
            if 1 <= Se_MTX_time < 2: 
                Ekstra_dosis_calciumfolinat = int(round(30 * Overflade))
            if 2 <= Se_MTX_time < 3:
                Ekstra_dosis_calciumfolinat = int(round(45 * Overflade))
            if 3 <= Se_MTX_time < 4:
                Ekstra_dosis_calciumfolinat = int(round(60 * Overflade))
            if 4 <= Se_MTX_time < 5:
                Ekstra_dosis_calciumfolinat = int(round(75 * Overflade))
            if Se_MTX_time >= 5:
                Ekstra_dosis_calciumfolinat = int(round(Se_MTX_time * Vægt))
            return Ekstra_dosis_calciumfolinat
        

        # Selected patient info
        st.info(
            "Patient: " + df["Navn"][df_st["selected_treatment"][0]]+ " - "+ str(df["CPR nr."][df_st["selected_treatment"][0]])+ "  \n" 
            "Kur nr.: "+ str(df["HDM_kur_nr"][df_st["selected_treatment"][0]])+ "  \n"+ 
            "Behandlings start t0: "+ str(df["Treatment_time_t0"][df_st["selected_treatment"][0]])
        )


        #### Time 23 ####
        Time_t23 = Treatment_time_t0 + dt.timedelta(hours=23)
        st.subheader('Time 23: ' + str(Time_t23))

        # Input for Se_MTX_t23
        if df["Se_MTX_t23"][df_st["selected_treatment"][0]] != "":
            Se_MTX_t23 = st.number_input('Se-MTX t23 (µmol/l) (Steady state, analyseres næste dag):', min_value=0.00, value=float(df["Se_MTX_t23"][df_st["selected_treatment"][0]]))
        if df["Se_MTX_t23"][df_st["selected_treatment"][0]] == "":
            Se_MTX_t23 = st.number_input('Se-MTX t23 (µmol/l) (Steady state, analyseres næste dag):', min_value=0.00, value=0.00)
        df.loc[df_st["selected_treatment"][0],"Se_MTX_t23"] = Se_MTX_t23
        df.to_excel(Destination_main_file)


        # Input for P_kreatinin_t23
        if df["P_kreatinin_t23"][df_st["selected_treatment"][0]] != "":
            P_kreatinin_t23 = st.number_input('P-kreatinin t23 (µmol/l):', min_value=0.00, value=float(df["P_kreatinin_t23"][df_st["selected_treatment"][0]]))
        if df["P_kreatinin_t23"][df_st["selected_treatment"][0]] == "":
            P_kreatinin_t23 = st.number_input('P-kreatinin t23 (µmol/l):', min_value=0.00, value=0.00)
        df.loc[df_st["selected_treatment"][0],"P_kreatinin_t23"] = P_kreatinin_t23
        df.to_excel(Destination_main_file)

        st.write("Pt. køres på OP til MTX is.")


        #### Time 24 ####
        Time_t24 = Treatment_time_t0 + dt.timedelta(hours=24)
        st.subheader('Time 24: ' + str(Time_t24))
        st.write("MTX infusion afsluttes - hydreringsvækens hastighed øges")


        #### Time 36 ####
        Time_t36 = Treatment_time_t0 + dt.timedelta(hours=36)
        st.subheader("Time 36: " + str(Time_t36))
        st.write('MTX konc t36 analyseres sammen med t23 til time 42 ')

        # Input for Se_MTX_t36
        if df["Se_MTX_t36"][df_st["selected_treatment"][0]] != "":
            Se_MTX_t36 = st.number_input('Se-MTX t36 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t36"][df_st["selected_treatment"][0]]))
        if df["Se_MTX_t36"][df_st["selected_treatment"][0]] == "":
            Se_MTX_t36 = st.number_input('Se-MTX t36 (µmol/l):', min_value=0.00, value=0.00)
        df.loc[df_st["selected_treatment"][0],"Se_MTX_t36"] = Se_MTX_t36
        df.to_excel(Destination_main_file)

        # Input for P_kreatinin_t36
        if df["P_kreatinin_t36"][df_st["selected_treatment"][0]] != "":
            P_kreatinin_t36 = st.number_input('P-kreatinin t36 (µmol/l):', min_value=0.00, value=float(df["P_kreatinin_t36"][df_st["selected_treatment"][0]]))
        if df["P_kreatinin_t36"][df_st["selected_treatment"][0]] == "":
            P_kreatinin_t36 = st.number_input('P-kreatinin t36 (µmol/l):', min_value=0.00, value=0.00)
        df.loc[df_st["selected_treatment"][0],"P_kreatinin_t36"] = P_kreatinin_t36
        df.to_excel(Destination_main_file)

        try:
            if P_kreatinin_t23 > Plasma_kreatinin_før_start*1.5 or P_kreatinin_t36 > Plasma_kreatinin_før_start*1.5 or Se_MTX_t36 > 3.0:
                Hydreing_ved_høj_P_kreatinin_t36 = int(round(Overflade*4500/24)) 
                Durise_ved_høj_P_kreatinin_t36 = int(round(Overflade*900)) 
                st.error(
                    "OPMÆRKSOM: Patienten er i høj-risiko for at have forsinket MTX udskillelse.  \n"
                    "Hydreringen øges til 4500 ml/m²/døgn svt. " + str(Hydreing_ved_høj_P_kreatinin_t36) + " ml/t.  \n"
                    "Duriresen skal være over 900 ml/m²/ 6 timer svt. " + str(Durise_ved_høj_P_kreatinin_t36) + " ml/t."
                )
            elif P_kreatinin_t36 != 0:
                Hydreing_ved_normal_P_kreatinin_t36 = int(round(Overflade*300/24)) 
                Durise_ved_normal_P_kreatinin_t36 = int(round(Overflade*600))
                st.warning(
                    'Hydreringen fortsættes med 3000 ml/m²/døgn svarende til ' + str(Hydreing_ved_normal_P_kreatinin_t36) + ' ml/t.  \n'
                    'Duriresen skal være over 600 ml/m²/ 6 timer svt. ' + str(Durise_ved_normal_P_kreatinin_t36) + ' ml/t.'
                )
        except:
            st.error("Plasma kreatinin før start er ikke indtastet. Gå til siden 'Forhydrering'")
            
        

        #### Time 42 ####
        Time_t42 = Treatment_time_t0 + dt.timedelta(hours=42)
        st.subheader("Time 42: " + str(Time_t42))
        st.write('MTX konc t42 analyseres sammen med t23 til time 36')

        # Input for Se_MTX_t42
        if df["Se_MTX_t42"][df_st["selected_treatment"][0]] != "":
            Se_MTX_t42 = st.number_input('Se-MTX t42 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t42"][df_st["selected_treatment"][0]]))
        if df["Se_MTX_t42"][df_st["selected_treatment"][0]] == "":
            Se_MTX_t42 = st.number_input('Se-MTX t42 (µmol/l):', min_value=0.00, value=0.00)
        df.loc[df_st["selected_treatment"][0],"Se_MTX_t42"] = Se_MTX_t42
        df.to_excel(Destination_main_file)

        Dosis_calciumfolinat_t42 = int(round(15*Overflade))
        st.write("Giv t42 dosis calciumfolinat-dosis 15 mg/m² svt.")
        st.info(str(Dosis_calciumfolinat_t42) + " mg iv.")
        df.loc[df_st["selected_treatment"][0],"Dosis_calciumfolinat_t42"] = Dosis_calciumfolinat_t42
        df.to_excel(Destination_main_file)


        # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
        Sygeplejerske_navn_dosis_calciumfolinat_t42 = st.text_input('Dosis calciumfolinat t42: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_dosis_calciumfolinat_t42"][df_st["selected_treatment"][0]])

        # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
        tid_t42 = df["Sygeplejerske_tid_dosis_calciumfolinat_t42"][df_st["selected_treatment"][0]]
        if tid_t42 == "":
            Sygeplejerske_tid_dosis_calciumfolinat_t42 = st.time_input('Dosis calciumfolinat t42: Tidspunkt:')
        if tid_t42 != "":
            Sygeplejerske_tid_dosis_calciumfolinat_t42 = st.time_input('Dosis calciumfolinat t42: Tidspunkt:', dt.time(int(tid_t42[0:2]),int(tid_t42[3:5])),int(tid_t42[6:8]))
        # Button for saving input for nurse and time to excel
        if st.button("Gem behandlingsdata dosis calciumfolinat t42"):
            Sygeplejerske_dosis_calciumfolinat_t42()


        # If Se_MTX_t42 > 1 this if statement will show next treatment procedure  
        if Se_MTX_t42 > 1:

            Hydreing_ved_sen_udskildelse = int(round(Overflade*4500/24))
            Durise_ved_sen_udskildelse = int(round(Overflade*900))
            st.error(
                "OPMÆRKSOM: Patienten overgår til skema for sen udskildelse!  \n\n"
                "Hydreringen øges til 4500 ml/m²/døgn svt. " + str(Hydreing_ved_sen_udskildelse) + " ml/t.  \n"
                "Duriresen skal være over 900 ml/m²/ 6 timer svt. " + str(Durise_ved_sen_udskildelse) + " ml/t.  \n"
                "Fortsættes indtil se-MTX er < 0,2 µmol/l."
            )
            Ekstra_dosis_calciumfolinat_t42 = Ekstra_dosis_calciumfolinat_function(Se_MTX_t42)
            df.loc[df_st["selected_treatment"][0],"Ekstra_dosis_calciumfolinat_t42"] = Ekstra_dosis_calciumfolinat_t42
            df.to_excel(Destination_main_file)
            st.error(
                "Grundet Se-MTX t42 > 1 µmol/l:  \n"
                "Giv straks 1. ekstra calciumfolinatdosis af " + str(int(round(Ekstra_dosis_calciumfolinat_t42))) + " mg iv."
            )

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            Sygeplejerske_navn_Ekstra_dosis_calciumfolinat_t42 = st.text_input('Ekstra dosis calciumfolinat t42: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Ekstra_dosis_calciumfolinat_t42"][df_st["selected_treatment"][0]])

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            tid_t42_ekstra = df["Sygeplejerske_tid_Ekstra_dosis_calciumfolinat_t42"][df_st["selected_treatment"][0]]
            if tid_t42_ekstra == "":
                Sygeplejerske_tid_Ekstra_dosis_calciumfolinat_t42 = st.time_input('Ekstra dosis calciumfolinat t42: Tidspunkt:')
            if tid_t42_ekstra != "":
                Sygeplejerske_tid_Ekstra_dosis_calciumfolinat_t42 = st.time_input('Ekstra dosis calciumfolinat t42: Tidspunkt:', dt.time(int(tid_t42_ekstra[0:2]),int(tid_t42_ekstra[3:5])),int(tid_t42_ekstra[6:8]))
            # Button for saving input for nurse and time to excel
            if st.button("Gem behandlingsdata ekstra dosis calciumfolinat t42"):
                Sygeplejerske_Ekstra_dosis_calciumfolinat_t42()


            #### Time 48 ####
            Time_t48 = Treatment_time_t0 + dt.timedelta(hours=48)
            st.subheader("Time 48: " + str(Time_t48) + " - (Sen udskildelse)")
            st.write('Tag Se-MTX t48: Analyseres akut. Afvent svar før calciumfolinat.')

            # Input for Se_MTX_t48
            if df["Se_MTX_t48"][df_st["selected_treatment"][0]] != "":
                Se_MTX_t48 = st.number_input('Se-MTX t48 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t48"][df_st["selected_treatment"][0]]), key="Hurtig udskildelse")
            if df["Se_MTX_t48"][df_st["selected_treatment"][0]] == "":
                Se_MTX_t48 = st.number_input('Se-MTX t48 (µmol/l):', min_value=0.00, value=0.00, key="Hurtig udskildelse")
            if Se_MTX_t48 != 0.0:
                df.loc[df_st["selected_treatment"][0],"Se_MTX_t48"] = Se_MTX_t48
                df.to_excel(Destination_main_file)

            # Calciumfolinat dosis t48
            if df["Se_MTX_t48"][df_st["selected_treatment"][0]] == "":
                st.warning("Indtast Se-MTX t48 for at beregne calciumfolinat-dosis.")

            if df["Se_MTX_t48"][df_st["selected_treatment"][0]] != "":
                Dosis_calciumfolinat_t48 = Ekstra_dosis_calciumfolinat_function(Se_MTX_t48)
                df.loc[df_st["selected_treatment"][0],"Dosis_calciumfolinat_t48"] = Dosis_calciumfolinat_t48
                df.to_excel(Destination_main_file)
                st.write("Giv t48 calciumfolinat-dosis " + str(int(round(Dosis_calciumfolinat_t48/Overflade))) + " mg/m² svt.")
                st.info(str(round(Dosis_calciumfolinat_t48)) + " mg iv.")

                # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                Sygeplejerske_navn_dosis_calciumfolinat_t48 = st.text_input('Dosis calciumfolinat t48: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_dosis_calciumfolinat_t48"][df_st["selected_treatment"][0]])

                # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                tid_t48 = df["Sygeplejerske_tid_dosis_calciumfolinat_t48"][df_st["selected_treatment"][0]]
                if tid_t48 == "":
                    Sygeplejerske_tid_dosis_calciumfolinat_t48 = st.time_input('Dosis calciumfolinat t48: Tidspunkt:')
                if tid_t48 != "":
                    Sygeplejerske_tid_dosis_calciumfolinat_t48 = st.time_input('Dosis calciumfolinat t48: Tidspunkt:', dt.time(int(tid_t48[0:2]),int(tid_t48[3:5])),int(tid_t48[6:8]))
                # Button for saving input for nurse and time to excel
                if st.button("Gem behandlingsdata dosis calciumfolinat t48"):
                    Sygeplejerske_dosis_calciumfolinat_t48()


            #### Time 54 ####
            Time_t54 = Treatment_time_t0 + dt.timedelta(hours=54)
            st.subheader("Time 54: " + str(Time_t54) + " - (Sen udskildelse)")
            if Se_MTX_t48 > 1:
                st.write('Tag Se-MTX t54: Analyseres akut. Afvent svar før calciumfolinat.')
            if Se_MTX_t48 <= 1:
                st.write('Tag Se-MTX t54: Akut analyse er ikke nødvendig. Analyse kan vente til næste dag.')

            # Input for Se_MTX_t54
            if df["Se_MTX_t54"][df_st["selected_treatment"][0]] != "":
                Se_MTX_t54 = st.number_input('Se-MTX t54 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t54"][df_st["selected_treatment"][0]]), key="Hurtig udskildelse")
            if df["Se_MTX_t54"][df_st["selected_treatment"][0]] == "":
                Se_MTX_t54 = st.number_input('Se-MTX t54 (µmol/l):', min_value=0.00, value=0.00, key="Hurtig udskildelse")
            if Se_MTX_t54 != 0.0:
                df.loc[df_st["selected_treatment"][0],"Se_MTX_t54"] = Se_MTX_t54
                df.to_excel(Destination_main_file)

            # Calciumfolinat dosis t54
            if df["Se_MTX_t54"][df_st["selected_treatment"][0]] == "":
                st.warning("Indtast Se-MTX t54 for at beregne calciumfolinat-dosis.")

            if df["Se_MTX_t54"][df_st["selected_treatment"][0]] != "":
                Dosis_calciumfolinat_t54 = Ekstra_dosis_calciumfolinat_function(Se_MTX_t54)
                df.loc[df_st["selected_treatment"][0],"Dosis_calciumfolinat_t54"] = Dosis_calciumfolinat_t54
                df.to_excel(Destination_main_file)
                st.write("Giv t54 calciumfolinat-dosis " + str(int(round(Dosis_calciumfolinat_t54/Overflade))) + " mg/m² svt.")
                st.info(str(round(Dosis_calciumfolinat_t54)) + " mg iv.")

                # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                Sygeplejerske_navn_dosis_calciumfolinat_t54 = st.text_input('Dosis calciumfolinat t54: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_dosis_calciumfolinat_t54"][df_st["selected_treatment"][0]])

                # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                tid_t54 = df["Sygeplejerske_tid_dosis_calciumfolinat_t54"][df_st["selected_treatment"][0]]
                if tid_t54 == "":
                    Sygeplejerske_tid_dosis_calciumfolinat_t54 = st.time_input('Dosis calciumfolinat t54: Tidspunkt:')
                if tid_t54 != "":
                    Sygeplejerske_tid_dosis_calciumfolinat_t54 = st.time_input('Dosis calciumfolinat t54: Tidspunkt:', dt.time(int(tid_t54[0:2]),int(tid_t54[3:5])),int(tid_t54[6:8]))
                # Button for saving input for nurse and time to excel
                if st.button("Gem behandlingsdata dosis calciumfolinat t54"):
                    Sygeplejerske_dosis_calciumfolinat_t54()


            #### Time 60 ####
            Time_t60 = Treatment_time_t0 + dt.timedelta(hours=60)
            st.subheader("Time 60: " + str(Time_t60) + " - (Sen udskildelse)")
            st.write('Giv t60 dosis calciumfolinat-dosis, i samme dosis som ved t54.')

            # Calciumfolinat dosis t60
            if df["Se_MTX_t54"][df_st["selected_treatment"][0]] == "":
                st.warning("Indtast Se-MTX t54 for at beregne calciumfolinat-dosis.")

            if df["Se_MTX_t54"][df_st["selected_treatment"][0]] != "":
                Dosis_calciumfolinat_t60 = Ekstra_dosis_calciumfolinat_function(Se_MTX_t54)
                df.loc[df_st["selected_treatment"][0],"Dosis_calciumfolinat_t60"] = Dosis_calciumfolinat_t60
                df.to_excel(Destination_main_file)
                st.write("Giv t60 calciumfolinat-dosis " + str(int(round(Dosis_calciumfolinat_t60/Overflade))) + " mg/m² svt.")
                st.info(str(round(Dosis_calciumfolinat_t60)) + " mg iv.")

                # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                Sygeplejerske_navn_dosis_calciumfolinat_t60 = st.text_input('Dosis calciumfolinat t60: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_dosis_calciumfolinat_t60"][df_st["selected_treatment"][0]])

                # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                tid_t60 = df["Sygeplejerske_tid_dosis_calciumfolinat_t60"][df_st["selected_treatment"][0]]
                if tid_t60 == "":
                    Sygeplejerske_tid_dosis_calciumfolinat_t60 = st.time_input('Dosis calciumfolinat t60: Tidspunkt:')
                if tid_t60 != "":
                    Sygeplejerske_tid_dosis_calciumfolinat_t60 = st.time_input('Dosis calciumfolinat t60: Tidspunkt:', dt.time(int(tid_t60[0:2]),int(tid_t60[3:5])),int(tid_t60[6:8]))
                # Button for saving input for nurse and time to excel
                if st.button("Gem behandlingsdata dosis calciumfolinat t60"):
                    Sygeplejerske_dosis_calciumfolinat_t60()


            #### Time 66 ####
            Time_t66 = Treatment_time_t0 + dt.timedelta(hours=66)
            st.subheader("Time 66: " + str(Time_t66) + " - (Sen udskildelse)")
            st.write('Tag Se-MTX t66: Analyseres akut. Afvent svar før yderligere calciumfolinat.')            

            # Input for Se_MTX_t66
            if df["Se_MTX_t66"][df_st["selected_treatment"][0]] != "":
                Se_MTX_t66 = st.number_input('Se-MTX t66 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t66"][df_st["selected_treatment"][0]]), key="Hurtig udskildelse")
            if df["Se_MTX_t66"][df_st["selected_treatment"][0]] == "":
                Se_MTX_t66 = st.number_input('Se-MTX t66 (µmol/l):', min_value=0.00, value=0.00, key="Hurtig udskildelse")
            if Se_MTX_t66 != 0.0:
                df.loc[df_st["selected_treatment"][0],"Se_MTX_t66"] = Se_MTX_t66
                df.to_excel(Destination_main_file)

            # Input for P_kreatinin_t66
            if df["P_kreatinin_t66"][df_st["selected_treatment"][0]] != "":
                P_kreatinin_t66 = st.number_input('P-kreatinin t66 (µmol/l):', min_value=0.00, value=float(df["P_kreatinin_t66"][df_st["selected_treatment"][0]]))
            if df["P_kreatinin_t66"][df_st["selected_treatment"][0]] == "":
                P_kreatinin_t66 = st.number_input('P-kreatinin t66 (µmol/l):', min_value=0.00, value=0.00)
            if P_kreatinin_t66 != 0.0:    
                df.loc[df_st["selected_treatment"][0],"P_kreatinin_t66"] = P_kreatinin_t66
                df.to_excel(Destination_main_file)
            
            # Need Se-MTX t66 input:
            if df["Se_MTX_t66"][df_st["selected_treatment"][0]] == "":
                st.warning("Indtast Se-MTX t66 for at beregne calciumfolinat-dosis.")

            if df["Se_MTX_t66"][df_st["selected_treatment"][0]] != "":
                if Se_MTX_t66 < 0.2 and df["Se_MTX_t66"][df_st["selected_treatment"][0]] != "":
                    st.success(
                        "Da Se-MTX t66 < 0.2 µmol/l gives der ikke yderligere calciumfolinat.  \n"
                        "Patienten kan udskrives."
                    )


                if Se_MTX_t66 >= 0.2:
                    Dosis_calciumfolinat_t66 = Ekstra_dosis_calciumfolinat_function(Se_MTX_t66)
                    df.loc[df_st["selected_treatment"][0],"Dosis_calciumfolinat_t66"] = Dosis_calciumfolinat_t66
                    df.to_excel(Destination_main_file)
                    st.write("Giv t66 dosis calciumfolinat-dosis " + str(int(round(Dosis_calciumfolinat_t66/Overflade))) + " mg/m² svt.")
                    st.info(str(round(Dosis_calciumfolinat_t66)) + " mg iv.")

                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                    Sygeplejerske_navn_dosis_calciumfolinat_t66 = st.text_input('Dosis calciumfolinat t66: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_dosis_calciumfolinat_t66"][df_st["selected_treatment"][0]])

                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                    tid_t66 = df["Sygeplejerske_tid_dosis_calciumfolinat_t66"][df_st["selected_treatment"][0]]
                    if tid_t66 == "":
                        Sygeplejerske_tid_dosis_calciumfolinat_t66 = st.time_input('Dosis calciumfolinat t66: Tidspunkt:')
                    if tid_t66 != "":
                        Sygeplejerske_tid_dosis_calciumfolinat_t66 = st.time_input('Dosis calciumfolinat t66: Tidspunkt:', dt.time(int(tid_t66[0:2]),int(tid_t66[3:5])),int(tid_t66[6:8]))
                    # Button for saving input for nurse and time to excel
                    if st.button("Gem behandlingsdata dosis calciumfolinat t66"):
                        Sygeplejerske_dosis_calciumfolinat_t66()

                if 0.2 <= Se_MTX_t66 < 0.3:
                    st.success("Patienten udskrives efter t66 dosis calciumfolinat")

                if 0.3 <= Se_MTX_t66 < 0.4:
                    st.success("Patienten udskrives med calciumfolinat 15 mg/m2 (svt. " + str(round(15*Overflade)) + " mg) x 3 po. i 2 døgn efter t66 dosis calciumfolinat.")

                if 0.4 <= Se_MTX_t66 < 0.5:
                    st.success("Patienten udskrives med calciumfolinat 15 mg/m2 (svt. " + str(round(15*Overflade)) + " mg) x 3 po. i 3 døgn efter t66 dosis calciumfolinat.")

                if Se_MTX_t66 >= 0.5:
                    st.warning("Grundet Se-MTX t66 > eller lig 0,5 µmol/l: Giv calciumfolinat hver 6. time.")
                    Ekstra_dosis_calciumfolinat_t66 = Ekstra_dosis_calciumfolinat_function(Se_MTX_t66)
                    df.loc[df_st["selected_treatment"][0],"Ekstra_dosis_calciumfolinat_t66"] = Ekstra_dosis_calciumfolinat_t66
                    df.to_excel(Destination_main_file)

                    #### Ekstra dosis calciumfolinat X4 ####
                    st.subheader("Første ekstra dosis calciumfoliat af Se-MTX t66")
                    st.info(str(round(Ekstra_dosis_calciumfolinat_t66)) + " mg iv.")

                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                    Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t66 = st.text_input('Første ekstra dosis calciumfoliat af Se-MTX t66: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t66"][df_st["selected_treatment"][0]])

                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                    tid_t66 = df["Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t66"][df_st["selected_treatment"][0]]
                    if tid_t66 == "":
                        Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t66 = st.time_input('Første ekstra dosis calciumfoliat af Se-MTX t66: Tidspunkt:')
                    if tid_t66 != "":
                        Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t66 = st.time_input('Første ekstra dosis calciumfoliat af Se-MTX t66: Tidspunkt:', dt.time(int(tid_t66[0:2]),int(tid_t66[3:5])),int(tid_t66[6:8]))
                    # Button for saving input for nurse and time to excel
                    if st.button("Gem behandlingsdata første ekstra dosis calciumfoliat af Se-MTX t66"):
                        Sygeplejerske_Første_Ekstra_dosis_calciumfolinat_t66()

                    
                    st.subheader("Anden ekstra dosis calciumfoliat af Se-MTX t66")
                    st.info(str(round(Ekstra_dosis_calciumfolinat_t66)) + " mg iv.")

                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                    Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t66 = st.text_input('Anden ekstra dosis calciumfoliat af Se-MTX t66: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t66"][df_st["selected_treatment"][0]])

                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                    tid_t66 = df["Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t66"][df_st["selected_treatment"][0]]
                    if tid_t66 == "":
                        Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t66 = st.time_input('Anden ekstra dosis calciumfoliat af Se-MTX t66: Tidspunkt:')
                    if tid_t66 != "":
                        Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t66 = st.time_input('Anden ekstra dosis calciumfoliat af Se-MTX t66: Tidspunkt:', dt.time(int(tid_t66[0:2]),int(tid_t66[3:5])),int(tid_t66[6:8]))
                    # Button for saving input for nurse and time to excel
                    if st.button("Gem behandlingsdata anden ekstra dosis calciumfoliat af Se-MTX t66"):
                        Sygeplejerske_Anden_Ekstra_dosis_calciumfolinat_t66()
                    

                    st.subheader("Tredje ekstra dosis calciumfoliat af Se-MTX t66")
                    st.info(str(round(Ekstra_dosis_calciumfolinat_t66)) + " mg iv.")

                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                    Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t66 = st.text_input('Tredje ekstra dosis calciumfoliat af Se-MTX t66: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t66"][df_st["selected_treatment"][0]])

                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                    tid_t66 = df["Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t66"][df_st["selected_treatment"][0]]
                    if tid_t66 == "":
                        Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t66 = st.time_input('Tredje ekstra dosis calciumfoliat af Se-MTX t66: Tidspunkt:')
                    if tid_t66 != "":
                        Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t66 = st.time_input('Tredje ekstra dosis calciumfoliat af Se-MTX t66: Tidspunkt:', dt.time(int(tid_t66[0:2]),int(tid_t66[3:5])),int(tid_t66[6:8]))
                    # Button for saving input for nurse and time to excel
                    if st.button("Gem behandlingsdata tredje ekstra dosis calciumfoliat af Se-MTX t66"):
                        Sygeplejerske_Tredje_Ekstra_dosis_calciumfolinat_t66()


                    st.subheader("Fjerde ekstra dosis calciumfoliat af Se-MTX t66")
                    st.info(str(round(Ekstra_dosis_calciumfolinat_t66)) + " mg iv.")

                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                    Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t66 = st.text_input('Fjerde ekstra dosis calciumfoliat af Se-MTX t66: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t66"][df_st["selected_treatment"][0]])

                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                    tid_t66 = df["Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t66"][df_st["selected_treatment"][0]]
                    if tid_t66 == "":
                        Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t66 = st.time_input('Fjerde ekstra dosis calciumfoliat af Se-MTX t66: Tidspunkt:')
                    if tid_t66 != "":
                        Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t66 = st.time_input('Fjerde ekstra dosis calciumfoliat af Se-MTX t66: Tidspunkt:', dt.time(int(tid_t66[0:2]),int(tid_t66[3:5])),int(tid_t66[6:8]))
                    # Button for saving input for nurse and time to excel
                    if st.button("Gem behandlingsdata fjerde ekstra dosis calciumfoliat af Se-MTX t66"):
                        Sygeplejerske_Fjerde_Ekstra_dosis_calciumfolinat_t66()
                

                    if Se_MTX_t66 > 2.0:
                        st.warning("Grundet Se-MTX t66 > 2,0 µmol/l: Giv calciumfolinat og mål Se-MTX 2 gange i døgnet til Se-MTX er < 1,0 µmol/l.")

                        #### Time 78 ####
                        Time_t78 = Treatment_time_t0 + dt.timedelta(hours=78)
                        st.subheader("Time 78: " + str(Time_t78) + " - (Sen udskildelse)")
                        st.write('Tag Se-MTX t78')            

                        # Input for Se_MTX_t78
                        if df["Se_MTX_t78"][df_st["selected_treatment"][0]] != "":
                            Se_MTX_t78 = st.number_input('Se-MTX t78 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t78"][df_st["selected_treatment"][0]]), key="Hurtig udskildelse")
                        if df["Se_MTX_t78"][df_st["selected_treatment"][0]] == "":
                            Se_MTX_t78 = st.number_input('Se-MTX t78 (µmol/l):', min_value=0.00, value=0.00, key="Hurtig udskildelse")
                        if Se_MTX_t78 != 0.0:
                            df.loc[df_st["selected_treatment"][0],"Se_MTX_t78"] = Se_MTX_t78
                            df.to_excel(Destination_main_file)


                    #### Time 90 ####
                    Time_t90 = Treatment_time_t0 + dt.timedelta(hours=90)
                    st.subheader("Time 90: " + str(Time_t90) + " - (Sen udskildelse)")
                    st.write('Tag Se-MTX t90: Analyseres akut. Afvent svar før yderligere calciumfolinat.')            

                    # Input for Se_MTX_t90
                    if df["Se_MTX_t90"][df_st["selected_treatment"][0]] != "":
                        Se_MTX_t90 = st.number_input('Se-MTX t90 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t90"][df_st["selected_treatment"][0]]), key="Hurtig udskildelse")
                    if df["Se_MTX_t90"][df_st["selected_treatment"][0]] == "":
                        Se_MTX_t90 = st.number_input('Se-MTX t90 (µmol/l):', min_value=0.00, value=0.00, key="Hurtig udskildelse")
                    if Se_MTX_t90 != 0.0:
                        df.loc[df_st["selected_treatment"][0],"Se_MTX_t90"] = Se_MTX_t90
                        df.to_excel(Destination_main_file)

                    # Input for P_kreatinin_t90
                    if df["P_kreatinin_t90"][df_st["selected_treatment"][0]] != "":
                        P_kreatinin_t90 = st.number_input('P-kreatinin t90 (µmol/l):', min_value=0.00, value=float(df["P_kreatinin_t90"][df_st["selected_treatment"][0]]))
                    if df["P_kreatinin_t90"][df_st["selected_treatment"][0]] == "":
                        P_kreatinin_t90 = st.number_input('P-kreatinin t90 (µmol/l):', min_value=0.00, value=0.00)
                    if P_kreatinin_t90 != 0.0:    
                        df.loc[df_st["selected_treatment"][0],"P_kreatinin_t90"] = P_kreatinin_t90
                        df.to_excel(Destination_main_file)
                    
                    # Need Se-MTX t90 input:
                    if df["Se_MTX_t90"][df_st["selected_treatment"][0]] == "":
                        st.warning("Indtast Se-MTX t90 for at beregne calciumfolinat-dosis.")

                    if df["Se_MTX_t90"][df_st["selected_treatment"][0]] != "":
                        if Se_MTX_t90 < 0.2 and df["Se_MTX_t90"][df_st["selected_treatment"][0]] != "":
                            st.success(
                                "Da Se-MTX t90 < 0.2 µmol/l gives der ikke yderligere calciumfolinat.  \n"
                                "Patienten kan udskrives."
                            )


                        if Se_MTX_t90 >= 0.2:
                            Dosis_calciumfolinat_t90 = Ekstra_dosis_calciumfolinat_function(Se_MTX_t90)
                            df.loc[df_st["selected_treatment"][0],"Dosis_calciumfolinat_t90"] = Dosis_calciumfolinat_t90
                            df.to_excel(Destination_main_file)
                            st.write("Giv t90 dosis calciumfolinat-dosis " + str(int(round(Dosis_calciumfolinat_t90/Overflade))) + " mg/m² svt.")
                            st.info(str(round(Dosis_calciumfolinat_t90)) + " mg iv.")

                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                            Sygeplejerske_navn_dosis_calciumfolinat_t90 = st.text_input('Dosis calciumfolinat t90: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_dosis_calciumfolinat_t90"][df_st["selected_treatment"][0]])

                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                            tid_t90 = df["Sygeplejerske_tid_dosis_calciumfolinat_t90"][df_st["selected_treatment"][0]]
                            if tid_t90 == "":
                                Sygeplejerske_tid_dosis_calciumfolinat_t90 = st.time_input('Dosis calciumfolinat t90: Tidspunkt:')
                            if tid_t90 != "":
                                Sygeplejerske_tid_dosis_calciumfolinat_t90 = st.time_input('Dosis calciumfolinat t90: Tidspunkt:', dt.time(int(tid_t90[0:2]),int(tid_t90[3:5])),int(tid_t90[6:8]))
                            # Button for saving input for nurse and time to excel
                            if st.button("Gem behandlingsdata dosis calciumfolinat t90"):
                                Sygeplejerske_dosis_calciumfolinat_t90()

                        if 0.2 <= Se_MTX_t90 < 0.3:
                            st.success("Patienten udskrives efter t90 dosis calciumfolinat")

                        if 0.3 <= Se_MTX_t90 < 0.4:
                            st.success("Patienten udskrives med calciumfolinat 15 mg/m2 (svt. " + str(round(15*Overflade)) + " mg) x 3 po. i 2 døgn efter t90 dosis calciumfolinat.")

                        if 0.4 <= Se_MTX_t90 < 0.5:
                            st.success("Patienten udskrives med calciumfolinat 15 mg/m2 (svt. " + str(round(15*Overflade)) + " mg) x 3 po. i 3 døgn efter t90 dosis calciumfolinat.")

                        if Se_MTX_t90 >= 0.5:
                            st.warning("Grundet Se-MTX t90 > eller lig 0,5 µmol/l: Giv calciumfolinat hver 6. time.")
                            Ekstra_dosis_calciumfolinat_t90 = Ekstra_dosis_calciumfolinat_function(Se_MTX_t90)
                            df.loc[df_st["selected_treatment"][0],"Ekstra_dosis_calciumfolinat_t90"] = Ekstra_dosis_calciumfolinat_t90
                            df.to_excel(Destination_main_file)

                            #### Ekstra dosis calciumfolinat X4 ####
                            st.subheader("Første ekstra dosis calciumfoliat af Se-MTX t90")
                            st.info(str(round(Ekstra_dosis_calciumfolinat_t90)) + " mg iv.")

                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                            Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t90 = st.text_input('Første ekstra dosis calciumfoliat af Se-MTX t90: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t90"][df_st["selected_treatment"][0]])

                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                            tid_t90 = df["Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t90"][df_st["selected_treatment"][0]]
                            if tid_t90 == "":
                                Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t90 = st.time_input('Første ekstra dosis calciumfoliat af Se-MTX t90: Tidspunkt:')
                            if tid_t90 != "":
                                Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t90 = st.time_input('Første ekstra dosis calciumfoliat af Se-MTX t90: Tidspunkt:', dt.time(int(tid_t90[0:2]),int(tid_t90[3:5])),int(tid_t90[6:8]))
                            # Button for saving input for nurse and time to excel
                            if st.button("Gem behandlingsdata første ekstra dosis calciumfoliat af Se-MTX t90"):
                                Sygeplejerske_Første_Ekstra_dosis_calciumfolinat_t90()

                            
                            st.subheader("Anden ekstra dosis calciumfoliat af Se-MTX t90")
                            st.info(str(round(Ekstra_dosis_calciumfolinat_t90)) + " mg iv.")

                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                            Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t90 = st.text_input('Anden ekstra dosis calciumfoliat af Se-MTX t90: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t90"][df_st["selected_treatment"][0]])

                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                            tid_t90 = df["Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t90"][df_st["selected_treatment"][0]]
                            if tid_t90 == "":
                                Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t90 = st.time_input('Anden ekstra dosis calciumfoliat af Se-MTX t90: Tidspunkt:')
                            if tid_t90 != "":
                                Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t90 = st.time_input('Anden ekstra dosis calciumfoliat af Se-MTX t90: Tidspunkt:', dt.time(int(tid_t90[0:2]),int(tid_t90[3:5])),int(tid_t90[6:8]))
                            # Button for saving input for nurse and time to excel
                            if st.button("Gem behandlingsdata anden ekstra dosis calciumfoliat af Se-MTX t90"):
                                Sygeplejerske_Anden_Ekstra_dosis_calciumfolinat_t90()
                            

                            st.subheader("Tredje ekstra dosis calciumfoliat af Se-MTX t90")
                            st.info(str(round(Ekstra_dosis_calciumfolinat_t90)) + " mg iv.")

                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                            Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t90 = st.text_input('Tredje ekstra dosis calciumfoliat af Se-MTX t90: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t90"][df_st["selected_treatment"][0]])

                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                            tid_t90 = df["Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t90"][df_st["selected_treatment"][0]]
                            if tid_t90 == "":
                                Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t90 = st.time_input('Tredje ekstra dosis calciumfoliat af Se-MTX t90: Tidspunkt:')
                            if tid_t90 != "":
                                Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t90 = st.time_input('Tredje ekstra dosis calciumfoliat af Se-MTX t90: Tidspunkt:', dt.time(int(tid_t90[0:2]),int(tid_t90[3:5])),int(tid_t90[6:8]))
                            # Button for saving input for nurse and time to excel
                            if st.button("Gem behandlingsdata tredje ekstra dosis calciumfoliat af Se-MTX t90"):
                                Sygeplejerske_Tredje_Ekstra_dosis_calciumfolinat_t90()


                            st.subheader("Fjerde ekstra dosis calciumfoliat af Se-MTX t90")
                            st.info(str(round(Ekstra_dosis_calciumfolinat_t90)) + " mg iv.")

                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                            Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t90 = st.text_input('Fjerde ekstra dosis calciumfoliat af Se-MTX t90: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t90"][df_st["selected_treatment"][0]])

                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                            tid_t90 = df["Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t90"][df_st["selected_treatment"][0]]
                            if tid_t90 == "":
                                Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t90 = st.time_input('Fjerde ekstra dosis calciumfoliat af Se-MTX t90: Tidspunkt:')
                            if tid_t90 != "":
                                Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t90 = st.time_input('Fjerde ekstra dosis calciumfoliat af Se-MTX t90: Tidspunkt:', dt.time(int(tid_t90[0:2]),int(tid_t90[3:5])),int(tid_t90[6:8]))
                            # Button for saving input for nurse and time to excel
                            if st.button("Gem behandlingsdata fjerde ekstra dosis calciumfoliat af Se-MTX t90"):
                                Sygeplejerske_Fjerde_Ekstra_dosis_calciumfolinat_t90()

            

                            if Se_MTX_t66 > 2.0 and Se_MTX_t90 >= 1:
                                st.warning("Grundet Se-MTX t66 > 2,0 µmol/l og Se-MTX t90 ikke er < 1 µmol/l: Giv calciumfolinat og mål Se-MTX 2 gange i døgnet til Se-MTX er < 1,0 µmol/l.")

                                #### Time 102 ####
                                Time_t102 = Treatment_time_t0 + dt.timedelta(hours=102)
                                st.subheader("Time 102: " + str(Time_t102) + " - (Sen udskildelse)")
                                st.write('Tag Se-MTX t102')            

                                # Input for Se_MTX_t102
                                if df["Se_MTX_t102"][df_st["selected_treatment"][0]] != "":
                                    Se_MTX_t102 = st.number_input('Se-MTX t102 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t102"][df_st["selected_treatment"][0]]), key="Hurtig udskildelse")
                                if df["Se_MTX_t102"][df_st["selected_treatment"][0]] == "":
                                    Se_MTX_t102 = st.number_input('Se-MTX t102 (µmol/l):', min_value=0.00, value=0.00, key="Hurtig udskildelse")
                                if Se_MTX_t102 != 0.0:
                                    df.loc[df_st["selected_treatment"][0],"Se_MTX_t102"] = Se_MTX_t102
                                    df.to_excel(Destination_main_file)


                            #### Time 114 ####
                            Time_t114 = Treatment_time_t0 + dt.timedelta(hours=114)
                            st.subheader("Time 114: " + str(Time_t114) + " - (Sen udskildelse)")
                            st.write('Tag Se-MTX t114: Analyseres akut. Afvent svar før yderligere calciumfolinat.')            

                            # Input for Se_MTX_t114
                            if df["Se_MTX_t114"][df_st["selected_treatment"][0]] != "":
                                Se_MTX_t114 = st.number_input('Se-MTX t114 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t114"][df_st["selected_treatment"][0]]), key="Hurtig udskildelse")
                            if df["Se_MTX_t114"][df_st["selected_treatment"][0]] == "":
                                Se_MTX_t114 = st.number_input('Se-MTX t114 (µmol/l):', min_value=0.00, value=0.00, key="Hurtig udskildelse")
                            if Se_MTX_t114 != 0.0:
                                df.loc[df_st["selected_treatment"][0],"Se_MTX_t114"] = Se_MTX_t114
                                df.to_excel(Destination_main_file)

                            # Input for P_kreatinin_t114
                            if df["P_kreatinin_t114"][df_st["selected_treatment"][0]] != "":
                                P_kreatinin_t114 = st.number_input('P-kreatinin t114 (µmol/l):', min_value=0.00, value=float(df["P_kreatinin_t114"][df_st["selected_treatment"][0]]))
                            if df["P_kreatinin_t114"][df_st["selected_treatment"][0]] == "":
                                P_kreatinin_t114 = st.number_input('P-kreatinin t114 (µmol/l):', min_value=0.00, value=0.00)
                            if P_kreatinin_t114 != 0.0:    
                                df.loc[df_st["selected_treatment"][0],"P_kreatinin_t114"] = P_kreatinin_t114
                                df.to_excel(Destination_main_file)
                            
                            # Need Se-MTX t114 input:
                            if df["Se_MTX_t114"][df_st["selected_treatment"][0]] == "":
                                st.warning("Indtast Se-MTX t114 for at beregne calciumfolinat-dosis.")

                            if df["Se_MTX_t114"][df_st["selected_treatment"][0]] != "":
                                if Se_MTX_t114 < 0.2 and df["Se_MTX_t114"][df_st["selected_treatment"][0]] != "":
                                    st.success(
                                        "Da Se-MTX t114 < 0.2 µmol/l gives der ikke yderligere calciumfolinat.  \n"
                                        "Patienten kan udskrives."
                                    )


                                if Se_MTX_t114 >= 0.2:
                                    Dosis_calciumfolinat_t114 = Ekstra_dosis_calciumfolinat_function(Se_MTX_t114)
                                    df.loc[df_st["selected_treatment"][0],"Dosis_calciumfolinat_t114"] = Dosis_calciumfolinat_t114
                                    df.to_excel(Destination_main_file)

                                    st.write("Giv t114 dosis calciumfolinat-dosis " + str(int(round(Dosis_calciumfolinat_t114/Overflade))) + " mg/m² svt.")
                                    st.info(str(round(Dosis_calciumfolinat_t114)) + " mg iv.")

                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                    Sygeplejerske_navn_dosis_calciumfolinat_t114 = st.text_input('Dosis calciumfolinat t114: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_dosis_calciumfolinat_t114"][df_st["selected_treatment"][0]])

                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                    tid_t114 = df["Sygeplejerske_tid_dosis_calciumfolinat_t114"][df_st["selected_treatment"][0]]
                                    if tid_t114 == "":
                                        Sygeplejerske_tid_dosis_calciumfolinat_t114 = st.time_input('Dosis calciumfolinat t114: Tidspunkt:')
                                    if tid_t114 != "":
                                        Sygeplejerske_tid_dosis_calciumfolinat_t114 = st.time_input('Dosis calciumfolinat t114: Tidspunkt:', dt.time(int(tid_t114[0:2]),int(tid_t114[3:5])),int(tid_t114[6:8]))
                                    # Button for saving input for nurse and time to excel
                                    if st.button("Gem behandlingsdata dosis calciumfolinat t114"):
                                        Sygeplejerske_dosis_calciumfolinat_t114()

                                if 0.2 <= Se_MTX_t114 < 0.3:
                                    st.success("Patienten udskrives efter t114 dosis calciumfolinat")

                                if 0.3 <= Se_MTX_t114 < 0.4:
                                    st.success("Patienten udskrives med calciumfolinat 15 mg/m2 (svt. " + str(round(15*Overflade)) + " mg) x 3 po. i 2 døgn efter t114 dosis calciumfolinat.")

                                if 0.4 <= Se_MTX_t114 < 0.5:
                                    st.success("Patienten udskrives med calciumfolinat 15 mg/m2 (svt. " + str(round(15*Overflade)) + " mg) x 3 po. i 3 døgn efter t114 dosis calciumfolinat.")

                                if Se_MTX_t114 >= 0.5:
                                    st.warning("Grundet Se-MTX t114 > eller lig 0,5 µmol/l: Giv calciumfolinat hver 6. time.")
                                    Ekstra_dosis_calciumfolinat_t114 = Ekstra_dosis_calciumfolinat_function(Se_MTX_t114)
                                    df.loc[df_st["selected_treatment"][0],"Ekstra_dosis_calciumfolinat_t114"] = Ekstra_dosis_calciumfolinat_t114
                                    df.to_excel(Destination_main_file)

                                    #### Ekstra dosis calciumfolinat X4 ####
                                    st.subheader("Første ekstra dosis calciumfoliat af Se-MTX t114")
                                    st.info(str(round(Ekstra_dosis_calciumfolinat_t114)) + " mg iv.")

                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                    Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t114 = st.text_input('Første ekstra dosis calciumfoliat af Se-MTX t114: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t114"][df_st["selected_treatment"][0]])

                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                    tid_t114 = df["Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t114"][df_st["selected_treatment"][0]]
                                    if tid_t114 == "":
                                        Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t114 = st.time_input('Første ekstra dosis calciumfoliat af Se-MTX t114: Tidspunkt:')
                                    if tid_t114 != "":
                                        Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t114 = st.time_input('Første ekstra dosis calciumfoliat af Se-MTX t114: Tidspunkt:', dt.time(int(tid_t114[0:2]),int(tid_t114[3:5])),int(tid_t114[6:8]))
                                    # Button for saving input for nurse and time to excel
                                    if st.button("Gem behandlingsdata første ekstra dosis calciumfoliat af Se-MTX t114"):
                                        Sygeplejerske_Første_Ekstra_dosis_calciumfolinat_t114()

                                    
                                    st.subheader("Anden ekstra dosis calciumfoliat af Se-MTX t114")
                                    st.info(str(round(Ekstra_dosis_calciumfolinat_t114)) + " mg iv.")

                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                    Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t114 = st.text_input('Anden ekstra dosis calciumfoliat af Se-MTX t114: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t114"][df_st["selected_treatment"][0]])

                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                    tid_t114 = df["Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t114"][df_st["selected_treatment"][0]]
                                    if tid_t114 == "":
                                        Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t114 = st.time_input('Anden ekstra dosis calciumfoliat af Se-MTX t114: Tidspunkt:')
                                    if tid_t114 != "":
                                        Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t114 = st.time_input('Anden ekstra dosis calciumfoliat af Se-MTX t114: Tidspunkt:', dt.time(int(tid_t114[0:2]),int(tid_t114[3:5])),int(tid_t114[6:8]))
                                    # Button for saving input for nurse and time to excel
                                    if st.button("Gem behandlingsdata anden ekstra dosis calciumfoliat af Se-MTX t114"):
                                        Sygeplejerske_Anden_Ekstra_dosis_calciumfolinat_t114()
                                    

                                    st.subheader("Tredje ekstra dosis calciumfoliat af Se-MTX t114")
                                    st.info(str(round(Ekstra_dosis_calciumfolinat_t114)) + " mg iv.")

                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                    Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t114 = st.text_input('Tredje ekstra dosis calciumfoliat af Se-MTX t114: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t114"][df_st["selected_treatment"][0]])

                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                    tid_t114 = df["Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t114"][df_st["selected_treatment"][0]]
                                    if tid_t114 == "":
                                        Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t114 = st.time_input('Tredje ekstra dosis calciumfoliat af Se-MTX t114: Tidspunkt:')
                                    if tid_t114 != "":
                                        Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t114 = st.time_input('Tredje ekstra dosis calciumfoliat af Se-MTX t114: Tidspunkt:', dt.time(int(tid_t114[0:2]),int(tid_t114[3:5])),int(tid_t114[6:8]))
                                    # Button for saving input for nurse and time to excel
                                    if st.button("Gem behandlingsdata tredje ekstra dosis calciumfoliat af Se-MTX t114"):
                                        Sygeplejerske_Tredje_Ekstra_dosis_calciumfolinat_t114()


                                    st.subheader("Fjerde ekstra dosis calciumfoliat af Se-MTX t114")
                                    st.info(str(round(Ekstra_dosis_calciumfolinat_t114)) + " mg iv.")

                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                    Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t114 = st.text_input('Fjerde ekstra dosis calciumfoliat af Se-MTX t114: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t114"][df_st["selected_treatment"][0]])

                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                    tid_t114 = df["Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t114"][df_st["selected_treatment"][0]]
                                    if tid_t114 == "":
                                        Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t114 = st.time_input('Fjerde ekstra dosis calciumfoliat af Se-MTX t114: Tidspunkt:')
                                    if tid_t114 != "":
                                        Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t114 = st.time_input('Fjerde ekstra dosis calciumfoliat af Se-MTX t114: Tidspunkt:', dt.time(int(tid_t114[0:2]),int(tid_t114[3:5])),int(tid_t114[6:8]))
                                    # Button for saving input for nurse and time to excel
                                    if st.button("Gem behandlingsdata fjerde ekstra dosis calciumfoliat af Se-MTX t114"):
                                        Sygeplejerske_Fjerde_Ekstra_dosis_calciumfolinat_t114()

                    

                                    if Se_MTX_t66 > 2.0 and Se_MTX_t114 >= 1:
                                        st.warning("Grundet Se-MTX t66 > 2,0 µmol/l og Se-MTX t114 ikke er < 1 µmol/l: Giv calciumfolinat og mål Se-MTX 2 gange i døgnet til Se-MTX er < 1,0 µmol/l.")

                                        #### Time 126 ####
                                        Time_t126 = Treatment_time_t0 + dt.timedelta(hours=126)
                                        st.subheader("Time 126: " + str(Time_t126) + " - (Sen udskildelse)")
                                        st.write('Tag Se-MTX t126')            

                                        # Input for Se_MTX_t126
                                        if df["Se_MTX_t126"][df_st["selected_treatment"][0]] != "":
                                            Se_MTX_t126 = st.number_input('Se-MTX t126 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t126"][df_st["selected_treatment"][0]]), key="Hurtig udskildelse")
                                        if df["Se_MTX_t126"][df_st["selected_treatment"][0]] == "":
                                            Se_MTX_t126 = st.number_input('Se-MTX t126 (µmol/l):', min_value=0.00, value=0.00, key="Hurtig udskildelse")
                                        if Se_MTX_t126 != 0.0:
                                            df.loc[df_st["selected_treatment"][0],"Se_MTX_t126"] = Se_MTX_t126
                                            df.to_excel(Destination_main_file)

                                    #### Time 138 ####
                                    Time_t138 = Treatment_time_t0 + dt.timedelta(hours=138)
                                    st.subheader("Time 138: " + str(Time_t138) + " - (Sen udskildelse)")
                                    st.write('Tag Se-MTX t138: Analyseres akut. Afvent svar før yderligere calciumfolinat.')            

                                    # Input for Se_MTX_t138
                                    if df["Se_MTX_t138"][df_st["selected_treatment"][0]] != "":
                                        Se_MTX_t138 = st.number_input('Se-MTX t138 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t138"][df_st["selected_treatment"][0]]), key="Hurtig udskildelse")
                                    if df["Se_MTX_t138"][df_st["selected_treatment"][0]] == "":
                                        Se_MTX_t138 = st.number_input('Se-MTX t138 (µmol/l):', min_value=0.00, value=0.00, key="Hurtig udskildelse")
                                    if Se_MTX_t138 != 0.0:
                                        df.loc[df_st["selected_treatment"][0],"Se_MTX_t138"] = Se_MTX_t138
                                        df.to_excel(Destination_main_file)

                                    # Input for P_kreatinin_t138
                                    if df["P_kreatinin_t138"][df_st["selected_treatment"][0]] != "":
                                        P_kreatinin_t138 = st.number_input('P-kreatinin t138 (µmol/l):', min_value=0.00, value=float(df["P_kreatinin_t138"][df_st["selected_treatment"][0]]))
                                    if df["P_kreatinin_t138"][df_st["selected_treatment"][0]] == "":
                                        P_kreatinin_t138 = st.number_input('P-kreatinin t138 (µmol/l):', min_value=0.00, value=0.00)
                                    if P_kreatinin_t138 != 0.0:    
                                        df.loc[df_st["selected_treatment"][0],"P_kreatinin_t138"] = P_kreatinin_t138
                                        df.to_excel(Destination_main_file)
                                    
                                    # Need Se-MTX t138 input:
                                    if df["Se_MTX_t138"][df_st["selected_treatment"][0]] == "":
                                        st.warning("Indtast Se-MTX t138 for at beregne calciumfolinat-dosis.")

                                    if df["Se_MTX_t138"][df_st["selected_treatment"][0]] != "":
                                        if Se_MTX_t138 < 0.2 and df["Se_MTX_t138"][df_st["selected_treatment"][0]] != "":
                                            st.success(
                                                "Da Se-MTX t138 < 0.2 µmol/l gives der ikke yderligere calciumfolinat.  \n"
                                                "Patienten kan udskrives."
                                            )


                                        if Se_MTX_t138 >= 0.2:
                                            Dosis_calciumfolinat_t138 = Ekstra_dosis_calciumfolinat_function(Se_MTX_t138)
                                            df.loc[df_st["selected_treatment"][0],"Dosis_calciumfolinat_t138"] = Dosis_calciumfolinat_t138
                                            df.to_excel(Destination_main_file)


                                            st.write("Giv t138 dosis calciumfolinat-dosis " + str(int(round(Dosis_calciumfolinat_t138/Overflade))) + " mg/m² svt.")
                                            st.info(str(round(Dosis_calciumfolinat_t138)) + " mg iv.")

                                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                            Sygeplejerske_navn_dosis_calciumfolinat_t138 = st.text_input('Dosis calciumfolinat t138: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_dosis_calciumfolinat_t138"][df_st["selected_treatment"][0]])

                                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                            tid_t138 = df["Sygeplejerske_tid_dosis_calciumfolinat_t138"][df_st["selected_treatment"][0]]
                                            if tid_t138 == "":
                                                Sygeplejerske_tid_dosis_calciumfolinat_t138 = st.time_input('Dosis calciumfolinat t138: Tidspunkt:')
                                            if tid_t138 != "":
                                                Sygeplejerske_tid_dosis_calciumfolinat_t138 = st.time_input('Dosis calciumfolinat t138: Tidspunkt:', dt.time(int(tid_t138[0:2]),int(tid_t138[3:5])),int(tid_t138[6:8]))
                                            # Button for saving input for nurse and time to excel
                                            if st.button("Gem behandlingsdata dosis calciumfolinat t138"):
                                                Sygeplejerske_dosis_calciumfolinat_t138()

                                        if 0.2 <= Se_MTX_t138 < 0.3:
                                            st.success("Patienten udskrives efter t138 dosis calciumfolinat")

                                        if 0.3 <= Se_MTX_t138 < 0.4:
                                            st.success("Patienten udskrives med calciumfolinat 15 mg/m2 (svt. " + str(round(15*Overflade)) + " mg) x 3 po. i 2 døgn efter t138 dosis calciumfolinat.")

                                        if 0.4 <= Se_MTX_t138 < 0.5:
                                            st.success("Patienten udskrives med calciumfolinat 15 mg/m2 (svt. " + str(round(15*Overflade)) + " mg) x 3 po. i 3 døgn efter t138 dosis calciumfolinat.")

                                        if Se_MTX_t138 >= 0.5:
                                            st.warning("Grundet Se-MTX t138 > eller lig 0,5 µmol/l: Giv calciumfolinat hver 6. time.")
                                            Ekstra_dosis_calciumfolinat_t138 = Ekstra_dosis_calciumfolinat_function(Se_MTX_t138)
                                            df.loc[df_st["selected_treatment"][0],"Ekstra_dosis_calciumfolinat_t138"] = Ekstra_dosis_calciumfolinat_t138
                                            df.to_excel(Destination_main_file)

                                            #### Ekstra dosis calciumfolinat X4 ####
                                            st.subheader("Første ekstra dosis calciumfoliat af Se-MTX t138")
                                            st.info(str(round(Ekstra_dosis_calciumfolinat_t138)) + " mg iv.")

                                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                            Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t138 = st.text_input('Første ekstra dosis calciumfoliat af Se-MTX t138: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t138"][df_st["selected_treatment"][0]])

                                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                            tid_t138 = df["Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t138"][df_st["selected_treatment"][0]]
                                            if tid_t138 == "":
                                                Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t138 = st.time_input('Første ekstra dosis calciumfoliat af Se-MTX t138: Tidspunkt:')
                                            if tid_t138 != "":
                                                Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t138 = st.time_input('Første ekstra dosis calciumfoliat af Se-MTX t138: Tidspunkt:', dt.time(int(tid_t138[0:2]),int(tid_t138[3:5])),int(tid_t138[6:8]))
                                            # Button for saving input for nurse and time to excel
                                            if st.button("Gem behandlingsdata første ekstra dosis calciumfoliat af Se-MTX t138"):
                                                Sygeplejerske_Første_Ekstra_dosis_calciumfolinat_t138()

                                            
                                            st.subheader("Anden ekstra dosis calciumfoliat af Se-MTX t138")
                                            st.info(str(round(Ekstra_dosis_calciumfolinat_t138)) + " mg iv.")

                                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                            Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t138 = st.text_input('Anden ekstra dosis calciumfoliat af Se-MTX t138: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t138"][df_st["selected_treatment"][0]])

                                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                            tid_t138 = df["Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t138"][df_st["selected_treatment"][0]]
                                            if tid_t138 == "":
                                                Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t138 = st.time_input('Anden ekstra dosis calciumfoliat af Se-MTX t138: Tidspunkt:')
                                            if tid_t138 != "":
                                                Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t138 = st.time_input('Anden ekstra dosis calciumfoliat af Se-MTX t138: Tidspunkt:', dt.time(int(tid_t138[0:2]),int(tid_t138[3:5])),int(tid_t138[6:8]))
                                            # Button for saving input for nurse and time to excel
                                            if st.button("Gem behandlingsdata anden ekstra dosis calciumfoliat af Se-MTX t138"):
                                                Sygeplejerske_Anden_Ekstra_dosis_calciumfolinat_t138()
                                            

                                            st.subheader("Tredje ekstra dosis calciumfoliat af Se-MTX t138")
                                            st.info(str(round(Ekstra_dosis_calciumfolinat_t138)) + " mg iv.")

                                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                            Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t138 = st.text_input('Tredje ekstra dosis calciumfoliat af Se-MTX t138: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t138"][df_st["selected_treatment"][0]])

                                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                            tid_t138 = df["Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t138"][df_st["selected_treatment"][0]]
                                            if tid_t138 == "":
                                                Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t138 = st.time_input('Tredje ekstra dosis calciumfoliat af Se-MTX t138: Tidspunkt:')
                                            if tid_t138 != "":
                                                Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t138 = st.time_input('Tredje ekstra dosis calciumfoliat af Se-MTX t138: Tidspunkt:', dt.time(int(tid_t138[0:2]),int(tid_t138[3:5])),int(tid_t138[6:8]))
                                            # Button for saving input for nurse and time to excel
                                            if st.button("Gem behandlingsdata tredje ekstra dosis calciumfoliat af Se-MTX t138"):
                                                Sygeplejerske_Tredje_Ekstra_dosis_calciumfolinat_t138()


                                            st.subheader("Fjerde ekstra dosis calciumfoliat af Se-MTX t138")
                                            st.info(str(round(Ekstra_dosis_calciumfolinat_t138)) + " mg iv.")

                                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                            Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t138 = st.text_input('Fjerde ekstra dosis calciumfoliat af Se-MTX t138: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t138"][df_st["selected_treatment"][0]])

                                            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                            tid_t138 = df["Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t138"][df_st["selected_treatment"][0]]
                                            if tid_t138 == "":
                                                Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t138 = st.time_input('Fjerde ekstra dosis calciumfoliat af Se-MTX t138: Tidspunkt:')
                                            if tid_t138 != "":
                                                Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t138 = st.time_input('Fjerde ekstra dosis calciumfoliat af Se-MTX t138: Tidspunkt:', dt.time(int(tid_t138[0:2]),int(tid_t138[3:5])),int(tid_t138[6:8]))
                                            # Button for saving input for nurse and time to excel
                                            if st.button("Gem behandlingsdata fjerde ekstra dosis calciumfoliat af Se-MTX t138"):
                                                Sygeplejerske_Fjerde_Ekstra_dosis_calciumfolinat_t138()

                            

                                            if Se_MTX_t66 > 2.0 and Se_MTX_t138 >= 1:
                                                st.warning("Grundet Se-MTX t66 > 2,0 µmol/l og Se-MTX t138 ikke er < 1 µmol/l: Giv calciumfolinat og mål Se-MTX 2 gange i døgnet til Se-MTX er < 1,0 µmol/l.")

                                                #### Time 150 ####
                                                Time_t150 = Treatment_time_t0 + dt.timedelta(hours=150)
                                                st.subheader("Time 150: " + str(Time_t150) + " - (Sen udskildelse)")
                                                st.write('Tag Se-MTX t150')            

                                                # Input for Se_MTX_t150
                                                if df["Se_MTX_t150"][df_st["selected_treatment"][0]] != "":
                                                    Se_MTX_t150 = st.number_input('Se-MTX t150 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t150"][df_st["selected_treatment"][0]]), key="Hurtig udskildelse")
                                                if df["Se_MTX_t150"][df_st["selected_treatment"][0]] == "":
                                                    Se_MTX_t150 = st.number_input('Se-MTX t150 (µmol/l):', min_value=0.00, value=0.00, key="Hurtig udskildelse")
                                                if Se_MTX_t150 != 0.0:
                                                    df.loc[df_st["selected_treatment"][0],"Se_MTX_t150"] = Se_MTX_t150
                                                    df.to_excel(Destination_main_file)


                                            #### Time 162 ####
                                            Time_t162 = Treatment_time_t0 + dt.timedelta(hours=162)
                                            st.subheader("Time 162: " + str(Time_t162) + " - (Sen udskildelse)")
                                            st.write('Tag Se-MTX t162: Analyseres akut. Afvent svar før yderligere calciumfolinat.')            

                                            # Input for Se_MTX_t162
                                            if df["Se_MTX_t162"][df_st["selected_treatment"][0]] != "":
                                                Se_MTX_t162 = st.number_input('Se-MTX t162 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t162"][df_st["selected_treatment"][0]]), key="Hurtig udskildelse")
                                            if df["Se_MTX_t162"][df_st["selected_treatment"][0]] == "":
                                                Se_MTX_t162 = st.number_input('Se-MTX t162 (µmol/l):', min_value=0.00, value=0.00, key="Hurtig udskildelse")
                                            if Se_MTX_t162 != 0.0:
                                                df.loc[df_st["selected_treatment"][0],"Se_MTX_t162"] = Se_MTX_t162
                                                df.to_excel(Destination_main_file)

                                            # Input for P_kreatinin_t162
                                            if df["P_kreatinin_t162"][df_st["selected_treatment"][0]] != "":
                                                P_kreatinin_t162 = st.number_input('P-kreatinin t162 (µmol/l):', min_value=0.00, value=float(df["P_kreatinin_t162"][df_st["selected_treatment"][0]]))
                                            if df["P_kreatinin_t162"][df_st["selected_treatment"][0]] == "":
                                                P_kreatinin_t162 = st.number_input('P-kreatinin t162 (µmol/l):', min_value=0.00, value=0.00)
                                            if P_kreatinin_t162 != 0.0:    
                                                df.loc[df_st["selected_treatment"][0],"P_kreatinin_t162"] = P_kreatinin_t162
                                                df.to_excel(Destination_main_file)
                                            
                                            # Need Se-MTX t162 input:
                                            if df["Se_MTX_t162"][df_st["selected_treatment"][0]] == "":
                                                st.warning("Indtast Se-MTX t162 for at beregne calciumfolinat-dosis.")

                                            if df["Se_MTX_t162"][df_st["selected_treatment"][0]] != "":
                                                if Se_MTX_t162 < 0.2 and df["Se_MTX_t162"][df_st["selected_treatment"][0]] != "":
                                                    st.success(
                                                        "Da Se-MTX t162 < 0.2 µmol/l gives der ikke yderligere calciumfolinat.  \n"
                                                        "Patienten kan udskrives."
                                                    )


                                                if Se_MTX_t162 >= 0.2:
                                                    Dosis_calciumfolinat_t162 = Ekstra_dosis_calciumfolinat_function(Se_MTX_t162)
                                                    df.loc[df_st["selected_treatment"][0],"Dosis_calciumfolinat_t162"] = Dosis_calciumfolinat_t162
                                                    df.to_excel(Destination_main_file)
                                                    
                                                    st.write("Giv t162 dosis calciumfolinat-dosis " + str(int(round(Dosis_calciumfolinat_t162/Overflade))) + " mg/m² svt.")
                                                    st.info(str(round(Dosis_calciumfolinat_t162)) + " mg iv.")

                                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                                    Sygeplejerske_navn_dosis_calciumfolinat_t162 = st.text_input('Dosis calciumfolinat t162: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_dosis_calciumfolinat_t162"][df_st["selected_treatment"][0]])

                                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                                    tid_t162 = df["Sygeplejerske_tid_dosis_calciumfolinat_t162"][df_st["selected_treatment"][0]]
                                                    if tid_t162 == "":
                                                        Sygeplejerske_tid_dosis_calciumfolinat_t162 = st.time_input('Dosis calciumfolinat t162: Tidspunkt:')
                                                    if tid_t162 != "":
                                                        Sygeplejerske_tid_dosis_calciumfolinat_t162 = st.time_input('Dosis calciumfolinat t162: Tidspunkt:', dt.time(int(tid_t162[0:2]),int(tid_t162[3:5])),int(tid_t162[6:8]))
                                                    # Button for saving input for nurse and time to excel
                                                    if st.button("Gem behandlingsdata dosis calciumfolinat t162"):
                                                        Sygeplejerske_dosis_calciumfolinat_t162()

                                                if 0.2 <= Se_MTX_t162 < 0.3:
                                                    st.success("Patienten udskrives efter t162 dosis calciumfolinat")

                                                if 0.3 <= Se_MTX_t162 < 0.4:
                                                    st.success("Patienten udskrives med calciumfolinat 15 mg/m2 (svt. " + str(round(15*Overflade)) + " mg) x 3 po. i 2 døgn efter t162 dosis calciumfolinat.")

                                                if 0.4 <= Se_MTX_t162 < 0.5:
                                                    st.success("Patienten udskrives med calciumfolinat 15 mg/m2 (svt. " + str(round(15*Overflade)) + " mg) x 3 po. i 3 døgn efter t162 dosis calciumfolinat.")

                                                if Se_MTX_t162 >= 0.5:
                                                    st.warning("Grundet Se-MTX t162 > eller lig 0,5 µmol/l: Giv calciumfolinat hver 6. time.")
                                                    Ekstra_dosis_calciumfolinat_t162 = Ekstra_dosis_calciumfolinat_function(Se_MTX_t162)
                                                    df.loc[df_st["selected_treatment"][0],"Ekstra_dosis_calciumfolinat_t162"] = Ekstra_dosis_calciumfolinat_t162
                                                    df.to_excel(Destination_main_file)
                                                    #### Ekstra dosis calciumfolinat X4 ####
                                                    st.subheader("Første ekstra dosis calciumfoliat af Se-MTX t162")
                                                    st.info(str(round(Ekstra_dosis_calciumfolinat_t162)) + " mg iv.")

                                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                                    Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t162 = st.text_input('Første ekstra dosis calciumfoliat af Se-MTX t162: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t162"][df_st["selected_treatment"][0]])

                                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                                    tid_t162 = df["Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t162"][df_st["selected_treatment"][0]]
                                                    if tid_t162 == "":
                                                        Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t162 = st.time_input('Første ekstra dosis calciumfoliat af Se-MTX t162: Tidspunkt:')
                                                    if tid_t162 != "":
                                                        Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t162 = st.time_input('Første ekstra dosis calciumfoliat af Se-MTX t162: Tidspunkt:', dt.time(int(tid_t162[0:2]),int(tid_t162[3:5])),int(tid_t162[6:8]))
                                                    # Button for saving input for nurse and time to excel
                                                    if st.button("Gem behandlingsdata første ekstra dosis calciumfoliat af Se-MTX t162"):
                                                        Sygeplejerske_Første_Ekstra_dosis_calciumfolinat_t162()

                                                    
                                                    st.subheader("Anden ekstra dosis calciumfoliat af Se-MTX t162")
                                                    st.info(str(round(Ekstra_dosis_calciumfolinat_t162)) + " mg iv.")

                                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                                    Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t162 = st.text_input('Anden ekstra dosis calciumfoliat af Se-MTX t162: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t162"][df_st["selected_treatment"][0]])

                                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                                    tid_t162 = df["Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t162"][df_st["selected_treatment"][0]]
                                                    if tid_t162 == "":
                                                        Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t162 = st.time_input('Anden ekstra dosis calciumfoliat af Se-MTX t162: Tidspunkt:')
                                                    if tid_t162 != "":
                                                        Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t162 = st.time_input('Anden ekstra dosis calciumfoliat af Se-MTX t162: Tidspunkt:', dt.time(int(tid_t162[0:2]),int(tid_t162[3:5])),int(tid_t162[6:8]))
                                                    # Button for saving input for nurse and time to excel
                                                    if st.button("Gem behandlingsdata anden ekstra dosis calciumfoliat af Se-MTX t162"):
                                                        Sygeplejerske_Anden_Ekstra_dosis_calciumfolinat_t162()
                                                    

                                                    st.subheader("Tredje ekstra dosis calciumfoliat af Se-MTX t162")
                                                    st.info(str(round(Ekstra_dosis_calciumfolinat_t162)) + " mg iv.")

                                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                                    Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t162 = st.text_input('Tredje ekstra dosis calciumfoliat af Se-MTX t162: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t162"][df_st["selected_treatment"][0]])

                                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                                    tid_t162 = df["Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t162"][df_st["selected_treatment"][0]]
                                                    if tid_t162 == "":
                                                        Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t162 = st.time_input('Tredje ekstra dosis calciumfoliat af Se-MTX t162: Tidspunkt:')
                                                    if tid_t162 != "":
                                                        Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t162 = st.time_input('Tredje ekstra dosis calciumfoliat af Se-MTX t162: Tidspunkt:', dt.time(int(tid_t162[0:2]),int(tid_t162[3:5])),int(tid_t162[6:8]))
                                                    # Button for saving input for nurse and time to excel
                                                    if st.button("Gem behandlingsdata tredje ekstra dosis calciumfoliat af Se-MTX t162"):
                                                        Sygeplejerske_Tredje_Ekstra_dosis_calciumfolinat_t162()


                                                    st.subheader("Fjerde ekstra dosis calciumfoliat af Se-MTX t162")
                                                    st.info(str(round(Ekstra_dosis_calciumfolinat_t162)) + " mg iv.")

                                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                                    Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t162 = st.text_input('Fjerde ekstra dosis calciumfoliat af Se-MTX t162: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t162"][df_st["selected_treatment"][0]])

                                                    # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                                                    tid_t162 = df["Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t162"][df_st["selected_treatment"][0]]
                                                    if tid_t162 == "":
                                                        Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t162 = st.time_input('Fjerde ekstra dosis calciumfoliat af Se-MTX t162: Tidspunkt:')
                                                    if tid_t162 != "":
                                                        Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t162 = st.time_input('Fjerde ekstra dosis calciumfoliat af Se-MTX t162: Tidspunkt:', dt.time(int(tid_t162[0:2]),int(tid_t162[3:5])),int(tid_t162[6:8]))
                                                    # Button for saving input for nurse and time to excel
                                                    if st.button("Gem behandlingsdata fjerde ekstra dosis calciumfoliat af Se-MTX t162"):
                                                        Sygeplejerske_Fjerde_Ekstra_dosis_calciumfolinat_t162()

                                    

                                                    if Se_MTX_t66 > 2.0 and Se_MTX_t162 >= 1:
                                                        st.warning("Grundet Se-MTX t66 > 2,0 µmol/l og Se-MTX t1362 ikke er < 1 µmol/l: Giv calciumfolinat og mål Se-MTX 2 gange i døgnet til Se-MTX er < 1,0 µmol/l.")

                                                        #### Time 174 ####
                                                        Time_t174 = Treatment_time_t0 + dt.timedelta(hours=174)
                                                        st.subheader("Time 174: " + str(Time_t174) + " - (Sen udskildelse)")
                                                        st.write('Tag Se-MTX t174')            

                                                        # Input for Se_MTX_t174
                                                        if df["Se_MTX_t174"][df_st["selected_treatment"][0]] != "":
                                                            Se_MTX_t174 = st.number_input('Se-MTX t174 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t174"][df_st["selected_treatment"][0]]), key="Hurtig udskildelse")
                                                        if df["Se_MTX_t174"][df_st["selected_treatment"][0]] == "":
                                                            Se_MTX_t174 = st.number_input('Se-MTX t174 (µmol/l):', min_value=0.00, value=0.00, key="Hurtig udskildelse")
                                                        if Se_MTX_t174 != 0.0:
                                                            df.loc[df_st["selected_treatment"][0],"Se_MTX_t174"] = Se_MTX_t174
                                                            df.to_excel(Destination_main_file)




        # If Se_MTX_t42 < 0.6 this if statement will show next treatment procedure  
        if Se_MTX_t42 < 0.6 and Se_MTX_t42 != 0.0:

            #### Time 48 ####
            Time_t48 = Treatment_time_t0 + dt.timedelta(hours=48)
            st.subheader("Time 48: " + str(Time_t48) + " - (Hurtig udskildelse)")
            st.write('MTX konc t48 analyseres sammen med t54 næste dag')


            # Input for Se_MTX_t48
            if df["Se_MTX_t48"][df_st["selected_treatment"][0]] != "":
                Se_MTX_t48 = st.number_input('Se-MTX t48 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t48"][df_st["selected_treatment"][0]]), key="Hurtig udskildelse")
            if df["Se_MTX_t48"][df_st["selected_treatment"][0]] == "":
                Se_MTX_t48 = st.number_input('Se-MTX t48 (µmol/l):', min_value=0.00, value=0.00, key="Hurtig udskildelse")
            df.loc[df_st["selected_treatment"][0],"Se_MTX_t48"] = Se_MTX_t48
            df.to_excel(Destination_main_file)

            Dosis_calciumfolinat_t48 = 15*Overflade
            st.write("Giv t48 calciumfolinat-dosis 15 mg/m² svt.")
            st.info(str(round(Dosis_calciumfolinat_t48)) + " mg iv.")

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            Sygeplejerske_navn_dosis_calciumfolinat_t48 = st.text_input('Dosis calciumfolinat t48: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_dosis_calciumfolinat_t48"][df_st["selected_treatment"][0]])

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            tid_t48 = df["Sygeplejerske_tid_dosis_calciumfolinat_t48"][df_st["selected_treatment"][0]]
            if tid_t48 == "":
                Sygeplejerske_tid_dosis_calciumfolinat_t48 = st.time_input('Dosis calciumfolinat t48: Tidspunkt:')
            if tid_t48 != "":
                Sygeplejerske_tid_dosis_calciumfolinat_t48 = st.time_input('Dosis calciumfolinat t48: Tidspunkt:', dt.time(int(tid_t48[0:2]),int(tid_t48[3:5])),int(tid_t48[6:8]))
            # Button for saving input for nurse and time to excel
            if st.button("Gem behandlingsdata dosis calciumfolinat t48"):
                Sygeplejerske_dosis_calciumfolinat_t48()
        

        
            #### Time 54 ####
            Time_t54 = Treatment_time_t0 + dt.timedelta(hours=54)
            st.subheader("Time 54: " + str(Time_t54) + " - (Hurtig udskildelse)")
            st.write('MTX konc t54 analyseres sammen med t48 fra forrige dag')

            # Input for Se_MTX_t54
            if df["Se_MTX_t54"][df_st["selected_treatment"][0]] != "":
                Se_MTX_t54 = st.number_input('Se-MTX t54 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t54"][df_st["selected_treatment"][0]]))
            if df["Se_MTX_t54"][df_st["selected_treatment"][0]] == "":
                Se_MTX_t54 = st.number_input('Se-MTX t54 (µmol/l):', min_value=0.00, value=0.00)
            df.loc[df_st["selected_treatment"][0],"Se_MTX_t54"] = Se_MTX_t54
            df.to_excel(Destination_main_file)

            Dosis_calciumfolinat_t54 = 15*Overflade
            st.write("Giv y54 calciumfolinat-dosis 15 mg/m² svt.")
            st.info(str(round(Dosis_calciumfolinat_t54)) + " mg iv.")

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            Sygeplejerske_navn_dosis_calciumfolinat_t54 = st.text_input('Dosis calciumfolinat t54: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_dosis_calciumfolinat_t54"][df_st["selected_treatment"][0]])

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            tid_t54 = df["Sygeplejerske_tid_dosis_calciumfolinat_t54"][df_st["selected_treatment"][0]]
            if tid_t54 == "":
                Sygeplejerske_tid_dosis_calciumfolinat_t54 = st.time_input('Dosis calciumfolinat t54: Tidspunkt:')
            if tid_t54 != "":
                Sygeplejerske_tid_dosis_calciumfolinat_t54 = st.time_input('Dosis calciumfolinat t54: Tidspunkt:', dt.time(int(tid_t54[0:2]),int(tid_t54[3:5])),int(tid_t54[6:8]))
            # Button for saving input for nurse and time to excel
            if st.button("Gem behandlingsdata dosis calciumfolinat t54"):
                Sygeplejerske_dosis_calciumfolinat_t54()


            if Se_MTX_t54 != 0:
                st.success(
                    "Patienten kobles fra efter t54 + calciumfolinat.  \n"
                    "Patienten udskrives."
                )

        # If 0.6 <= Se_MTX_ <= 1 this if statement will show next treatment procedure  
        if 0.6 <= Se_MTX_t42 <= 1:      

            #### Time 48 ####
            Time_t48 = Treatment_time_t0 + dt.timedelta(hours=48)
            st.subheader("Time 48: " + str(Time_t48) + " - (Normal udskildelse)")
            st.write('MTX konc t48 analyseres sammen med t54 og t66 næste dag')


            # Input for Se_MTX_t48
            if df["Se_MTX_t48"][df_st["selected_treatment"][0]] != "":
                Se_MTX_t48 = st.number_input('Se-MTX t48 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t48"][df_st["selected_treatment"][0]]))
            if df["Se_MTX_t48"][df_st["selected_treatment"][0]] == "":
                Se_MTX_t48 = st.number_input('Se-MTX t48 (µmol/l):', min_value=0.00, value=0.00)
            df.loc[df_st["selected_treatment"][0],"Se_MTX_t48"] = Se_MTX_t48
            df.to_excel(Destination_main_file)

            Dosis_calciumfolinat_t48 = 15*Overflade
            st.write("Giv t48 calciumfolinat-dosis 15 mg/m² svt.")
            st.info(str(round(Dosis_calciumfolinat_t48)) + " mg iv.")

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            Sygeplejerske_navn_dosis_calciumfolinat_t48 = st.text_input('Dosis calciumfolinat t48: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_dosis_calciumfolinat_t48"][df_st["selected_treatment"][0]])

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            tid_t48 = df["Sygeplejerske_tid_dosis_calciumfolinat_t48"][df_st["selected_treatment"][0]]
            if tid_t48 == "":
                Sygeplejerske_tid_dosis_calciumfolinat_t48 = st.time_input('Dosis calciumfolinat t48: Tidspunkt:')
            if tid_t48 != "":
                Sygeplejerske_tid_dosis_calciumfolinat_t48 = st.time_input('Dosis calciumfolinat t48: Tidspunkt:', dt.time(int(tid_t48[0:2]),int(tid_t48[3:5])),int(tid_t48[6:8]))
            # Button for saving input for nurse and time to excel
            if st.button("Gem behandlingsdata dosis calciumfolinat t48"):
                Sygeplejerske_dosis_calciumfolinat_t48()



        
            #### Time 54 ####
            Time_t54 = Treatment_time_t0 + dt.timedelta(hours=54)
            st.subheader("Time 54: " + str(Time_t54) + " - (Normal udskildelse)")
            st.write('MTX konc t54 analyseres sammen med t48 fra forrige dag')

            # Input for Se_MTX_t54
            if df["Se_MTX_t54"][df_st["selected_treatment"][0]] != "":
                Se_MTX_t54 = st.number_input('Se-MTX t54 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t54"][df_st["selected_treatment"][0]]))
            if df["Se_MTX_t54"][df_st["selected_treatment"][0]] == "":
                Se_MTX_t54 = st.number_input('Se-MTX t54 (µmol/l):', min_value=0.00, value=0.00)
            df.loc[df_st["selected_treatment"][0],"Se_MTX_t54"] = Se_MTX_t54
            df.to_excel(Destination_main_file) 

            Dosis_calciumfolinat_t54 = 15*Overflade
            st.write("Giv t54 calciumfolinat-dosis 15 mg/m² svt.")
            st.info(str(round(Dosis_calciumfolinat_t54)) + " mg iv.")

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            Sygeplejerske_navn_dosis_calciumfolinat_t54 = st.text_input('Dosis calciumfolinat t54: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_dosis_calciumfolinat_t54"][df_st["selected_treatment"][0]])

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            tid_t54 = df["Sygeplejerske_tid_dosis_calciumfolinat_t54"][df_st["selected_treatment"][0]]
            if tid_t54 == "":
                Sygeplejerske_tid_dosis_calciumfolinat_t54 = st.time_input('Dosis calciumfolinat t54: Tidspunkt:')
            if tid_t54 != "":
                Sygeplejerske_tid_dosis_calciumfolinat_t54 = st.time_input('Dosis calciumfolinat t54: Tidspunkt:', dt.time(int(tid_t54[0:2]),int(tid_t54[3:5])),int(tid_t54[6:8]))
            # Button for saving input for nurse and time to excel
            if st.button("Gem behandlingsdata dosis calciumfolinat t54"):
                Sygeplejerske_dosis_calciumfolinat_t54()


            #### Time 66 ####
            Time_t66 = Treatment_time_t0 + dt.timedelta(hours=66)   
            st.subheader("Time 66: " + str(Time_t66) + " - (Normal udskildelse)")
            st.write('MTX konc t66 analyseres sammen med t48 og t54. Afvent svar før evt. t66 dosis calciumfolinat')

            # Input for Se_MTX_t66
            if df["Se_MTX_t66"][df_st["selected_treatment"][0]] != "":
                Se_MTX_t66 = st.number_input('Se-MTX t66 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t66"][df_st["selected_treatment"][0]]), key="Hurtig udskildelse")
            if df["Se_MTX_t66"][df_st["selected_treatment"][0]] == "":
                Se_MTX_t66 = st.number_input('Se-MTX t66 (µmol/l):', min_value=0.00, value=0.00, key="Hurtig udskildelse")
            if Se_MTX_t66 != 0.0:
                df.loc[df_st["selected_treatment"][0],"Se_MTX_t66"] = Se_MTX_t66
                df.to_excel(Destination_main_file)


            # Input for P_kreatinin_t66
            if df["P_kreatinin_t66"][df_st["selected_treatment"][0]] != "":
                P_kreatinin_t66 = st.number_input('P-kreatinin t66 (µmol/l):', min_value=0.00, value=float(df["P_kreatinin_t66"][df_st["selected_treatment"][0]]))
            if df["P_kreatinin_t66"][df_st["selected_treatment"][0]] == "":
                P_kreatinin_t66 = st.number_input('P-kreatinin t66 (µmol/l):', min_value=0.00, value=0.00)
            if P_kreatinin_t66 != 0.0:    
                df.loc[df_st["selected_treatment"][0],"P_kreatinin_t66"] = P_kreatinin_t66
                df.to_excel(Destination_main_file)

            if Se_MTX_t66 < 0.2 and df["Se_MTX_t66"][df_st["selected_treatment"][0]] != "":
                st.success(
                    "Da Se-MTX t66 < 0.2 µmol/l gives der ikke yderligere calciumfolinat.  \n"
                    "Patienten kan udskrives."
                )


            if Se_MTX_t66 >= 0.2:
                Dosis_calciumfolinat_t66 = 15*Overflade
                st.write("Giv t66 dosis calciumfolinat-dosis 15 mg/m² svt.")
                st.info(str(round(Dosis_calciumfolinat_t66)) + " mg iv.")
                df.loc[df_st["selected_treatment"][0],"Dosis_calciumfolinat_t66"] = Dosis_calciumfolinat_t66
                df.to_excel(Destination_main_file)
                # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                Sygeplejerske_navn_dosis_calciumfolinat_t66 = st.text_input('Dosis calciumfolinat t66: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_dosis_calciumfolinat_t66"][df_st["selected_treatment"][0]])

                # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                tid_t66 = df["Sygeplejerske_tid_dosis_calciumfolinat_t66"][df_st["selected_treatment"][0]]
                if tid_t66 == "":
                    Sygeplejerske_tid_dosis_calciumfolinat_t66 = st.time_input('Dosis calciumfolinat t66: Tidspunkt:')
                if tid_t66 != "":
                    Sygeplejerske_tid_dosis_calciumfolinat_t66 = st.time_input('Dosis calciumfolinat t66: Tidspunkt:', dt.time(int(tid_t66[0:2]),int(tid_t66[3:5])),int(tid_t66[6:8]))
                # Button for saving input for nurse and time to excel
                if st.button("Gem behandlingsdata dosis calciumfolinat t66"):
                    Sygeplejerske_dosis_calciumfolinat_t66()

            if 0.2 <= Se_MTX_t66 < 0.3:
                st.success("Patienten udskrives efter t66 dosis calciumfolinat")

            if 0.3 <= Se_MTX_t66 < 0.4:
                st.success("Patienten udskrives med calciumfolinat 15 mg/m2 (svt. " + str(round(15*Overflade)) + " mg) x 3 po. i 2 døgn efter t66 dosis calciumfolinat.")

            if 0.4 <= Se_MTX_t66 < 0.5:
                st.success("Patienten udskrives med calciumfolinat 15 mg/m2 (svt. " + str(round(15*Overflade)) + " mg) x 3 po. i 3 døgn efter t66 dosis calciumfolinat.")

            if Se_MTX_t66 >= 0.5:
                st.warning("Patienten overgår til skema for senudskillelse")


        
        # Tells use to input Se-MTX t42 so further treatment can be chosen
        if Se_MTX_t42 == 0.0:
            st.error("Indtast Se-MTX t42 før behandling fortsættes.")
    
    except IndexError:
            st.info("Der er ingen tidligere patienter. Gå til startside og opret ny patient.")




