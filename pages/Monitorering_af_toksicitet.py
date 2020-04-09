import streamlit as st
import datetime as dt

from basics import *


def write():
    df = pd.read_excel(Destination_main_file, na_filter=False)
    # The next two if statemens make sure, that if there is no patient in the dataframe, user is informed and referred to startpage
    if len(df) == 0:
        st.info("Der er ingen tidligere patienter. Gå til startside og opret ny patient.")
    if len(df) != 0:
        # Get variabels from dataframe
        Vægt = df["Vægt"][df_st["selected_treatment"][0]]
        Overflade = df["Overflade"][df_st["selected_treatment"][0]]
        Treatment_time_t0 = df["Treatment_time_t0"][df_st["selected_treatment"][0]]
        Plasma_kreatin_før_start = df["Plasma_kreatin_før_start"][df_st["selected_treatment"][0]]
        

        # Export functions
        def Sygeplejerske_Første_dosis_calciumfolinat_t42():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Første_dosis_calciumfolinat_t42"] = Sygeplejerske_navn_Første_dosis_calciumfolinat_t42
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Første_dosis_calciumfolinat_t42"] = Sygeplejerske_tid_Første_dosis_calciumfolinat_t42
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Anden_dosis_calciumfolinat_t48():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Anden_dosis_calciumfolinat_t48"] = Sygeplejerske_navn_Anden_dosis_calciumfolinat_t48
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Anden_dosis_calciumfolinat_t48"] = Sygeplejerske_tid_Anden_dosis_calciumfolinat_t48
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")
        
        def Sygeplejerske_Tredje_dosis_calciumfolinat_t54():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Tredje_dosis_calciumfolinat_t54"] = Sygeplejerske_navn_Tredje_dosis_calciumfolinat_t54
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Tredje_dosis_calciumfolinat_t54"] = Sygeplejerske_tid_Tredje_dosis_calciumfolinat_t54
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        def Sygeplejerske_Fjerde_dosis_calciumfolinat_t66():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_Fjerde_dosis_calciumfolinat_t66"] = Sygeplejerske_navn_Fjerde_dosis_calciumfolinat_t66
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_Fjerde_dosis_calciumfolinat_t66"] = Sygeplejerske_tid_Fjerde_dosis_calciumfolinat_t66
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")


        
        # Calculator for ekstra dosis calciumfolinat
        def Ekstra_dosis_calciumfolinat_function(Se_MTX_time):
            Ekstra_dosis_calciumfolinat = 0
            if 1 <= Se_MTX_time < 2: 
                Ekstra_dosis_calciumfolinat = 15 * Overflade
            if 2 <= Se_MTX_time < 3:
                Ekstra_dosis_calciumfolinat = 30 * Overflade
            if 3 <= Se_MTX_time < 4:
                Ekstra_dosis_calciumfolinat = 45 * Overflade
            if 4 <= Se_MTX_time < 5:
                Ekstra_dosis_calciumfolinat = 60 * Overflade
            if Se_MTX_time >= 5:
                Ekstra_dosis_calciumfolinat = Se_MTX_time * Vægt
            return Ekstra_dosis_calciumfolinat
        

        # Selected patient info
        st.info(
            "Patient: " + df["Navn"][df_st["selected_treatment"][0]]+ " - "+ str(df["CPR nr."][df_st["selected_treatment"][0]])+ "  \n"+ 
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


        # Input for P_kreatin_t23
        if df["P_kreatin_t23"][df_st["selected_treatment"][0]] != "":
            P_kreatin_t23 = st.number_input('P-kreatin t23 (µmol/l):', min_value=0.00, value=float(df["P_kreatin_t23"][df_st["selected_treatment"][0]]))
        if df["P_kreatin_t23"][df_st["selected_treatment"][0]] == "":
            P_kreatin_t23 = st.number_input('P-kreatin t23 (µmol/l):', min_value=0.00, value=0.00)
        df.loc[df_st["selected_treatment"][0],"P_kreatin_t23"] = P_kreatin_t23
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

        # Input for P_kreatin_t36
        if df["P_kreatin_t36"][df_st["selected_treatment"][0]] != "":
            P_kreatin_t36 = st.number_input('P-kreatin t36 (µmol/l):', min_value=0.00, value=float(df["P_kreatin_t36"][df_st["selected_treatment"][0]]))
        if df["P_kreatin_t36"][df_st["selected_treatment"][0]] == "":
            P_kreatin_t36 = st.number_input('P-kreatin t36 (µmol/l):', min_value=0.00, value=0.00)
        df.loc[df_st["selected_treatment"][0],"P_kreatin_t36"] = P_kreatin_t36#
        df.to_excel(Destination_main_file)


        if P_kreatin_t23 > Plasma_kreatin_før_start*1.5 or P_kreatin_t36 > Plasma_kreatin_før_start*1.5 or Se_MTX_t36 > 3:
            Hydreing_ved_høj_P_kreatin_t36 = round(Overflade*4500/24) 
            Durise_ved_høj_P_kreatin_t36 = round(Overflade*900) 
            st.error(
                "OPMÆRKSOM: Patienten er i høj-risiko for at have forsinket MTX udskillelse.  \n"
                "Hydreringen øges til 4500 ml/m²/døgn svt. " + str(Hydreing_ved_høj_P_kreatin_t36) + " ml/t.  \n"
                "Duriresen skal være over 900 ml/m²/ 6 timer svt. " + str(Durise_ved_høj_P_kreatin_t36) + " ml/t."
            )
        elif P_kreatin_t36 != 0:
            Hydreing_ved_normal_P_kreatin_t36 = round(Overflade*300/24) 
            Durise_ved_normal_P_kreatin_t36 = round(Overflade*600) 
            st.warning(
                'Hydreringen fortsættes med 3000 ml/m²/døgn svarende til ' + str(Hydreing_ved_normal_P_kreatin_t36) + ' ml/t.  \n'
                'Duriresen skal være over 600 ml/m²/ 6 timer svt. ' + str(Durise_ved_normal_P_kreatin_t36) + ' ml/t.'
            )
        

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

        Første_dosis_calciumfolinat_t42 = int(round(15*Overflade))
        st.write("Første dosis calciumfolinat-dosis 15 mg/m² svt.")
        st.info(str(Første_dosis_calciumfolinat_t42) + " mg iv.")
        df.loc[df_st["selected_treatment"][0],"Første_dosis_calciumfolinat_t42"] = Første_dosis_calciumfolinat_t42
        df.to_excel(Destination_main_file)


        # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
        Sygeplejerske_navn_Første_dosis_calciumfolinat_t42 = st.text_input('Første dosis calciumfolinat t42: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Første_dosis_calciumfolinat_t42"][df_st["selected_treatment"][0]])

        # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
        tid_t42 = df["Sygeplejerske_tid_Første_dosis_calciumfolinat_t42"][df_st["selected_treatment"][0]]
        if tid_t42 == "":
            Sygeplejerske_tid_Første_dosis_calciumfolinat_t42 = st.time_input('Første dosis calciumfolinat t42: Tidspunkt:')
        if tid_t42 != "":
            Sygeplejerske_tid_Første_dosis_calciumfolinat_t42 = st.time_input('Første dosis calciumfolinat t42: Tidspunkt:', dt.time(int(tid_t42[0:2]),int(tid_t42[3:5])),int(tid_t42[6:8]))
        # Button for saving input for nurse and time to excel
        if st.button("Gem behandlingsdata første dosis calciumfolinat t42"):
            Sygeplejerske_Første_dosis_calciumfolinat_t42()


        # If Se_MTX_t42 > 1 this if statement will show next treatment procedure  
        if Se_MTX_t42 > 1:
            st.write("Fedt")

            Hydreing_ved_sen_udskildelse = round(Overflade*4500/24) 
            Durise_ved_sen_udskildelse = round(Overflade*900) 
            st.error(
                "OPMÆRKSOM:  \n"
                "Hydreringen øges til 4500 ml/m²/døgn svt. " + str(Hydreing_ved_sen_udskildelse) + " ml/t.  \n"
                "Duriresen skal være over 900 ml/m²/ 6 timer svt. " + str(Durise_ved_sen_udskildelse) + " ml/t.  \n"
                "Fortsættes indtil se-MTX er < 0,2 µmol/l."
            )
























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

            Anden_dosis_calciumfolinat_t48 = 15*Overflade
            st.write("Anden calciumfolinat-dosis 15 mg/m² svt.")
            st.info(str(round(Anden_dosis_calciumfolinat_t48)) + " mg iv.")

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            Sygeplejerske_navn_Anden_dosis_calciumfolinat_t48 = st.text_input('Anden dosis calciumfolinat t48: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Anden_dosis_calciumfolinat_t48"][df_st["selected_treatment"][0]])

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            tid_t48 = df["Sygeplejerske_tid_Anden_dosis_calciumfolinat_t48"][df_st["selected_treatment"][0]]
            if tid_t48 == "":
                Sygeplejerske_tid_Anden_dosis_calciumfolinat_t48 = st.time_input('Anden dosis calciumfolinat t48: Tidspunkt:')
            if tid_t48 != "":
                Sygeplejerske_tid_Anden_dosis_calciumfolinat_t48 = st.time_input('Anden dosis calciumfolinat t48: Tidspunkt:', dt.time(int(tid_t48[0:2]),int(tid_t48[3:5])),int(tid_t48[6:8]))
            # Button for saving input for nurse and time to excel
            if st.button("Gem behandlingsdata Anden dosis calciumfolinat t48"):
                Sygeplejerske_Anden_dosis_calciumfolinat_t48()
        

        
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

            Tredje_dosis_calciumfolinat_t54 = 15*Overflade
            st.write("Tredje calciumfolinat-dosis 15 mg/m² svt.")
            st.info(str(round(Tredje_dosis_calciumfolinat_t54)) + " mg iv.")

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            Sygeplejerske_navn_Tredje_dosis_calciumfolinat_t54 = st.text_input('Tredje calciumfolinat t54: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Tredje_dosis_calciumfolinat_t54"][df_st["selected_treatment"][0]])

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            tid_t54 = df["Sygeplejerske_tid_Tredje_dosis_calciumfolinat_t54"][df_st["selected_treatment"][0]]
            if tid_t54 == "":
                Sygeplejerske_tid_Tredje_dosis_calciumfolinat_t54 = st.time_input('Tredje calciumfolinat t54: Tidspunkt:')
            if tid_t54 != "":
                Sygeplejerske_tid_Tredje_dosis_calciumfolinat_t54 = st.time_input('Tredje calciumfolinat t54: Tidspunkt:', dt.time(int(tid_t54[0:2]),int(tid_t54[3:5])),int(tid_t54[6:8]))
            # Button for saving input for nurse and time to excel
            if st.button("Gem behandlingsdata tredje calciumfolinat t54"):
                Sygeplejerske_Tredje_dosis_calciumfolinat_t54()


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

            Anden_dosis_calciumfolinat_t48 = 15*Overflade
            st.write("Anden calciumfolinat-dosis 15 mg/m² svt.")
            st.info(str(round(Anden_dosis_calciumfolinat_t48)) + " mg iv.")

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            Sygeplejerske_navn_Anden_dosis_calciumfolinat_t48 = st.text_input('Anden dosis calciumfolinat t48: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Anden_dosis_calciumfolinat_t48"][df_st["selected_treatment"][0]])

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            tid_t48 = df["Sygeplejerske_tid_Anden_dosis_calciumfolinat_t48"][df_st["selected_treatment"][0]]
            if tid_t48 == "":
                Sygeplejerske_tid_Anden_dosis_calciumfolinat_t48 = st.time_input('Anden dosis calciumfolinat t48: Tidspunkt:')
            if tid_t48 != "":
                Sygeplejerske_tid_Anden_dosis_calciumfolinat_t48 = st.time_input('Anden dosis calciumfolinat t48: Tidspunkt:', dt.time(int(tid_t48[0:2]),int(tid_t48[3:5])),int(tid_t48[6:8]))
            # Button for saving input for nurse and time to excel
            if st.button("Gem behandlingsdata Anden dosis calciumfolinat t48"):
                Sygeplejerske_Anden_dosis_calciumfolinat_t48()

    

        
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

            Tredje_dosis_calciumfolinat_t54 = 15*Overflade
            st.write("Tredje calciumfolinat-dosis 15 mg/m² svt.")
            st.info(str(round(Tredje_dosis_calciumfolinat_t54)) + " mg iv.")

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            Sygeplejerske_navn_Tredje_dosis_calciumfolinat_t54 = st.text_input('Tredje calciumfolinat t54: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Tredje_dosis_calciumfolinat_t54"][df_st["selected_treatment"][0]])

            # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
            tid_t54 = df["Sygeplejerske_tid_Tredje_dosis_calciumfolinat_t54"][df_st["selected_treatment"][0]]
            if tid_t54 == "":
                Sygeplejerske_tid_Tredje_dosis_calciumfolinat_t54 = st.time_input('Tredje calciumfolinat t54: Tidspunkt:')
            if tid_t54 != "":
                Sygeplejerske_tid_Tredje_dosis_calciumfolinat_t54 = st.time_input('Tredje calciumfolinat t54: Tidspunkt:', dt.time(int(tid_t54[0:2]),int(tid_t54[3:5])),int(tid_t54[6:8]))
            # Button for saving input for nurse and time to excel
            if st.button("Gem behandlingsdata tredje calciumfolinat t54"):
                Sygeplejerske_Tredje_dosis_calciumfolinat_t54()


            #### Time 66 ####
            Time_t66 = Treatment_time_t0 + dt.timedelta(hours=66)   
            st.subheader("Time 66: " + str(Time_t66) + " - (Normal udskildelse)")
            st.write('MTX konc t66 analyseres sammen med t48 og t54. Afvent svar før evt. fjerde dosis calciumfolinat')

            # Input for Se_MTX_t66
            if df["Se_MTX_t66"][df_st["selected_treatment"][0]] != "":
                Se_MTX_t66 = st.number_input('Se-MTX t66 (µmol/l):', min_value=0.00, value=float(df["Se_MTX_t66"][df_st["selected_treatment"][0]]))
            if df["Se_MTX_t66"][df_st["selected_treatment"][0]] == "":
                Se_MTX_t66 = st.number_input('Se-MTX t66 (µmol/l):', min_value=0.00, value=0.00)
            df.loc[df_st["selected_treatment"][0],"Se_MTX_t66"] = Se_MTX_t66
            df.to_excel(Destination_main_file)


            # Input for P_kreatin_t66
            if df["P_kreatin_t66"][df_st["selected_treatment"][0]] != "":
                P_kreatin_t66 = st.number_input('P-kreatin t66 (µmol/l):', min_value=0.00, value=float(df["P_kreatin_t66"][df_st["selected_treatment"][0]]))
            if df["P_kreatin_t66"][df_st["selected_treatment"][0]] == "":
                P_kreatin_t66 = st.number_input('P-kreatin t66 (µmol/l):', min_value=0.00, value=0.00)
            df.loc[df_st["selected_treatment"][0],"P_kreatin_t66"] = P_kreatin_t66
            df.to_excel(Destination_main_file)

            if Se_MTX_t66 < 0.2 and df["Se_MTX_t66"][df_st["selected_treatment"][0]] != 0.0:
                st.success("Patienten kan udskrives.")


            if Se_MTX_t66 >= 0.2:
                Fjerde_dosis_calciumfolinat_t66 = 15*Overflade
                st.write("Fjerde dosis calciumfolinat-dosis 15 mg/m² svt.")
                st.info(str(round(Fjerde_dosis_calciumfolinat_t66)) + " mg iv.")

                # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                Sygeplejerske_navn_Fjerde_dosis_calciumfolinat_t66 = st.text_input('Fjerde dosis calciumfolinat t66: Givet af sygeplejerske:', value=df["Sygeplejerske_navn_Fjerde_dosis_calciumfolinat_t66"][df_st["selected_treatment"][0]])

                # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                tid_t66 = df["Sygeplejerske_tid_Fjerde_dosis_calciumfolinat_t66"][df_st["selected_treatment"][0]]
                if tid_t66 == "":
                    Sygeplejerske_tid_Fjerde_dosis_calciumfolinat_t66 = st.time_input('Fjerde dosis calciumfolinat t66: Tidspunkt:')
                if tid_t66 != "":
                    Sygeplejerske_tid_Fjerde_dosis_calciumfolinat_t66 = st.time_input('Fjerde dosis calciumfolinat t66: Tidspunkt:', dt.time(int(tid_t66[0:2]),int(tid_t66[3:5])),int(tid_t66[6:8]))
                # Button for saving input for nurse and time to excel
                if st.button("Gem behandlingsdata fjerde dosis calciumfolinat t66"):
                    Sygeplejerske_Fjerde_dosis_calciumfolinat_t66()

            if 0.2 <= Se_MTX_t66 < 0.3:
                st.success("Patienten udskrives efter fjerde dosis calciumfolinat")

            if 0.3 <= Se_MTX_t66 < 0.4:
                st.success("Patienten udskrives med calciumfolinat 15 mg/m2 (svt. " + str(round(15*Overflade)) + " mg) x 3 po. i 2 døgn efter fjerde dosis calciumfolinat.")

            if 0.4 <= Se_MTX_t66 < 0.5:
                st.success("Patienten udskrives med calciumfolinat 15 mg/m2 (svt. " + str(round(15*Overflade)) + " mg) x 3 po. i 3 døgn efter fjerde dosis calciumfolinat.")

            if Se_MTX_t66 >= 0.5:
                st.warning("Patienten overgår til skema for senudskillelse")


        
        # Tells use to input Se-MTX t42 so further treatment can be chosen
        if Se_MTX_t42 == 0.0:
            st.error("Indtast Se-MTX t42 før behandling fortsættes.")



        
        







