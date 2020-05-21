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
        Vægt = df["Vægt"][df_st["selected_treatment"][0]]
        Overflade = df["Overflade"][df_st["selected_treatment"][0]]
        Treatment_time_t0 = df["Treatment_time_t0"][df_st["selected_treatment"][0]]
        Plasma_kreatinin_før_start = df["Plasma_kreatinin_før_start"][df_st["selected_treatment"][0]]
        Udskillelsesskema = df["Udskillelsesskema"][df_st["selected_treatment"][0]]
        Time_t23 = MTX.Treatment_time_t0_validering(23, df, df_st)
        Time_t36 = MTX.Treatment_time_t0_validering(36, df, df_st)
        Time_t42 = MTX.Treatment_time_t0_validering(42, df, df_st)
        Time_t48 = MTX.Treatment_time_t0_validering(48, df, df_st)
        Time_t54 = MTX.Treatment_time_t0_validering(54, df, df_st)
        Time_t60 = MTX.Treatment_time_t0_validering(60, df, df_st)
        Time_t66 = MTX.Treatment_time_t0_validering(66, df, df_st)
        Durise_600ml_6timer = df["Durise_600ml_6timer"][df_st["selected_treatment"][0]]
        Dosis_natriumcarbonat_ved_lav_pH = df["Dosis_natriumcarbonat_ved_lav_pH"][df_st["selected_treatment"][0]]
        
        
        # Selected patient info
        MTX.patient_information_box(df, df_st)

        # Oversigt over blodprøver og deres værdier
        MTX.Blood_sample_overview(Udskillelsesskema, df, df_st)


        if Dosis_natriumcarbonat_ved_lav_pH != 0.0 and Durise_600ml_6timer != 0.0:
            st.info(
                "Diuresen skal være over 600 ml/m²/ 6 timer svt. " + str(Durise_600ml_6timer) + " ml/6 timer.  \n\n"
                "Ved urin pH<7.0 skal der gives ekstra bicarbonat:  \n"
                "Na-bicarbonat 20 mmol/m² blandes i 40 ml af hydreringsvæsken og gives over over 30 min. samtidig med forhydreringen. "
                "Svarende til: **" + str(Dosis_natriumcarbonat_ved_lav_pH) + "** mmol Na-bicarbonat.  \n\n"
                "Ved urin pH > 8 skiftes til KNaG uden bicarbonat i 3 time.  \n"
                "Når pH er under 8 skiftes til bicarbonatholdig hydrering."
            )

        #### Time 23 ####
        st.subheader("Time 23: " + str(Time_t23))
        # Text area for notes
        MTX.Fritekst_indtastningsfelt("Time 23", df, df_st)

        # Input for Se_MTX_t23
        Se_MTX_t23 = MTX.Blood_sample_input(23, "Se-MTX", df, df_st)

        # Input for P_kreatinin_t23
        P_kreatinin_t23= MTX.Blood_sample_input(23, "P-kreatinin", df, df_st)

        st.write("Pt. køres på OP til MTX is.")

        #### Time 36 ####
        st.subheader("Time 36: " + str(Time_t36))
        # Text area for notes
        MTX.Fritekst_indtastningsfelt("Time 36", df, df_st)
        st.write("MTX konc t36 analyseres sammen med t23 til time 42 ")

        # Input for Se_MTX_t36
        Se_MTX_t36 = MTX.Blood_sample_input(36, "Se-MTX", df, df_st)
        MTX.MTX_input_check(Se_MTX_t23, Se_MTX_t36)

        # Input for P_kreatinin_t36
        P_kreatinin_t36 = MTX.Blood_sample_input(36, "P-kreatinin", df, df_st)

        try:
            if P_kreatinin_t23 > Plasma_kreatinin_før_start*1.5 or P_kreatinin_t36 > Plasma_kreatinin_før_start*1.5 or Se_MTX_t36 > 3.0:
                Hydreing_ved_høj_P_kreatinin_t36 = int(round(Overflade*4500/24)) 
                Durise_ved_høj_P_kreatinin_t36 = int(round(Overflade*900)) 
                st.error(
                    "OPMÆRKSOM: Patienten er i høj-risiko for at have forsinket MTX udskillelse.  \n"
                    "Hydreringen øges til 4500 ml/m²/døgn svt. **" + str(Hydreing_ved_høj_P_kreatinin_t36) + " ml/t.**  \n"
                    "Duriresen skal være over 900 ml/m²/ 6 timer svt. **" + str(Durise_ved_høj_P_kreatinin_t36) + " ml/6t.**"
                )
            elif P_kreatinin_t36 != 0:
                Hydreing_ved_normal_P_kreatinin_t36 = int(round(Overflade*300/24)) 
                Durise_ved_normal_P_kreatinin_t36 = int(round(Overflade*600))
                st.warning(
                    "Hydreringen fortsættes med 3000 ml/m²/døgn svarende til **" + str(Hydreing_ved_normal_P_kreatinin_t36) + " ml/t.**  \n"
                    "Duriresen skal være over 600 ml/m²/ 6 timer svt. **" + str(Durise_ved_normal_P_kreatinin_t36) + " ml/t.**"
                )
        except TypeError as error:
            if str(error) == "can't multiply sequence by non-int of type 'float'":
                st.error(
                    "!!!  \n"
                    "Forhydreringen er ikke registreret. Gå til forhydrering og indtast data for forhydrering."
                    "  \n!!!"
                    )
    
            
        #### Time 42 ####
        st.subheader("Time 42: " + str(Time_t42))
        # Text area for notes
        MTX.Fritekst_indtastningsfelt("Time 42", df, df_st)

        st.write("MTX konc t42 analyseres sammen med t23 til time 36.")
        st.warning("OBS: Hvis Se-MTX t42 > 1 µM skal der straks gives ekstra calciumfolinat.")

        # Input for Se_MTX_t42
        Se_MTX_t42 = MTX.Blood_sample_input(42, "Se-MTX", df, df_st)
        MTX.MTX_input_check(Se_MTX_t36, Se_MTX_t42)

        try:
            if (Se_MTX_t42 < 0.5 or Se_MTX_t42 > 3.0) and Se_MTX_t42 != 0.0:
                st.error(
                    "OPMÆRMSOM: Du har indtastet en Se-MTX værdi som ikke ligger intervallet 0.5-3.0 µM hvilket er uden for normalen ved time 42."
                )
        except TypeError as error:
            if error == "'<' not supported between instances of 'str' and 'float'":
                pass

        try:
            # Determine witch hydration scheme the patient shall follow
            if Udskillelsesskema == "":
                if Se_MTX_t42 > 1:
                    Udskillelsesskema = "Sen udskillelse"
                elif 0.6 <= Se_MTX_t42 <= 1:
                    Udskillelsesskema = "Normal udskillelse"
                elif Se_MTX_t42 < 0.6 and Se_MTX_t42 != 0.0:
                    Udskillelsesskema = "Hurtig udskillelse"
                df.loc[df_st["selected_treatment"][0], "Udskillelsesskema"] = Udskillelsesskema
        except TypeError as error:
            if error == "'>' not supported between instances of 'str' and 'int'":
                pass


        # Makes it possible to change hydration scheme if Se-MTX t42 is changed
        if Udskillelsesskema != "":
            if Se_MTX_t42 > 1 and Udskillelsesskema != "Sen udskillelse":
                Udskillelsesskema_ny = "Sen udskillelse"
                
            elif 0.6 <= Se_MTX_t42 <= 1 and Udskillelsesskema != "Normal udskillelse":
                Udskillelsesskema_ny = "Normal udskillelse"

            elif Se_MTX_t42 < 0.6 and Se_MTX_t42 != 0.0 and Udskillelsesskema != "Hurtig udskillelse":
                Udskillelsesskema_ny = "Hurtig udskillelse"

            try:
                if Udskillelsesskema_ny != Udskillelsesskema:
                    st.warning(
                        "Du har ændret i værdien for Se-MTX t42. "
                        "Den gamle værdi angav at patienten skal følge skema for _" + str.lower(Udskillelsesskema) + 
                        "_, hvorimod den nye værdi angiver at patienten skal følge skema for _" + str.lower(Udskillelsesskema_ny)+ "_  \n"
                        "Vil du bekræfte at patienten skal skifte til skema for _" + str.lower(Udskillelsesskema_ny) + "_?"
                    )
                    if st.button("Ja, overgå til skema for " + str.lower(Udskillelsesskema_ny)):
                        df.loc[df_st["selected_treatment"][0], "Udskillelsesskema"] = Udskillelsesskema_ny
                        df.to_excel(Destination_main_file)
            except UnboundLocalError:
                pass


        # Calculate dosis calciumfolinat and display to user
        MTX.Dosis_calciumfolinat_function(42, False, df, df_st)

        # Input function for validation of administration of dosis
        MTX.Sygeplejerske_navn_tid_validering(
            "Sygeplejerske_navn_dosis_calciumfolinat_t42",
            "Sygeplejerske_tid_dosis_calciumfolinat_t42",
            "Dosis calciumfoliat af Se-MTX t42 er givet",
            df,df_st)
            

        # If the hydration scheme is determined if statement will show next treatment procedure
        if Udskillelsesskema in {"Hurtig udskillelse","Normal udskillelse","Sen udskillelse"}:
            if Udskillelsesskema == "Sen udskillelse":
                Ekstra_dosis_calciumfolinat_t42 = MTX.Ekstra_dosis_calciumfolinat_function(42, Se_MTX_t42, df, df_st)
                st.error(
                    "Grundet Se-MTX t42 > 1 µmol/l:  \n"
                    "Giv straks 1. ekstra calciumfolinatdosis af **" + str(int(round(Ekstra_dosis_calciumfolinat_t42))) + " mg iv.**"
                )

                # Input function for validation of administration of dosis
                MTX.Sygeplejerske_navn_tid_validering(
                    "Sygeplejerske_navn_Ekstra_dosis_calciumfolinat_t42",
                    "Sygeplejerske_tid_Ekstra_dosis_calciumfolinat_t42",
                    "Ekstra dosis calciumfoliat af Se-MTX t42 er givet",
                    df,df_st)

                Hydreing_ved_sen_udskillelse = int(round(Overflade*4500/24))
                Durise_ved_sen_udskillelse = int(round(Overflade*900))
                st.error(
                    "OPMÆRKSOM: Patienten overgår til skema for sen udskillelse!  \n\n"
                    "Hydreringen øges til 4500 ml/m²/døgn svt. **" + str(Hydreing_ved_sen_udskillelse) + " ml/t.**  \n"
                    "Duriresen skal være over 900 ml/m²/ 6 timer svt. **" + str(Durise_ved_sen_udskillelse) + " ml/6t.**  \n"
                    "Fortsættes indtil se-MTX er < 0,2 µmol/l."
                )

            #### Time 48 ####
            st.subheader("Time 48: " + str(Time_t48) + " - (" + str(Udskillelsesskema) + ")")
            # Text area for notes
            MTX.Fritekst_indtastningsfelt("Time 48", df, df_st)

            if Udskillelsesskema == "Hurtig udskillelse":
                st.write("MTX konc t48 analyseres sammen med t54 næste dag")
            if Udskillelsesskema == "Normal udskillelse":
                st.write("MTX konc t48 analyseres sammen med t54 og t66 næste dag")
            if Udskillelsesskema == "Sen udskillelse":
                st.write("Tag Se-MTX t48: Analyseres akut. Afvent svar før calciumfolinat.")

            # Input for Se_MTX_t48
            Se_MTX_t48 = MTX.Blood_sample_input(48, "Se-MTX", df, df_st)
            MTX.MTX_input_check(Se_MTX_t42, Se_MTX_t48)
            
            # Calculate dosis calciumfolinat and display to user
            if Udskillelsesskema in {"Hurtig udskillelse","Normal udskillelse"}:
                MTX.Dosis_calciumfolinat_function(48, False, df, df_st)
            if Udskillelsesskema == "Sen udskillelse":
                MTX.Dosis_calciumfolinat_function(48, True, df, df_st)

            # Input function for validation of administration of dosis
            MTX.Sygeplejerske_navn_tid_validering(
                "Sygeplejerske_navn_dosis_calciumfolinat_t48",
                "Sygeplejerske_tid_dosis_calciumfolinat_t48",
                "Dosis calciumfoliat af Se-MTX t48 er givet",
                df,df_st)

            #### Time 54 ####
            st.subheader("Time 54: " + str(Time_t54) + " - (" + str(Udskillelsesskema) + ")")
            # Text area for notes
            MTX.Fritekst_indtastningsfelt("Time 54", df, df_st)


            if Udskillelsesskema == "Hurtig udskillelse":
                st.write("MTX konc t54 analyseres sammen med t48 fra forrige dag")
            if Udskillelsesskema == "Normal udskillelse":
                st.write("MTX konc t54 analyseres sammen med t48 og t66 næste dag")
            if Udskillelsesskema == "Sen udskillelse":
                if Se_MTX_t48 > 1:
                    st.write("Tag Se-MTX t54: Analyseres akut. Afvent svar før calciumfolinat.")
                if Se_MTX_t48 <= 1:
                    st.write("Tag Se-MTX t54: Akut analyse er ikke nødvendig. Analyse kan vente til næste dag.")

            # Input for Se_MTX_t54
            Se_MTX_t54 = MTX.Blood_sample_input(54, "Se-MTX", df, df_st)
            MTX.MTX_input_check(Se_MTX_t48, Se_MTX_t54)

            # Calculate dosis calciumfolinat and display to user
            if Udskillelsesskema in {"Hurtig udskillelse","Normal udskillelse"}:
                MTX.Dosis_calciumfolinat_function(54, False, df, df_st)
            if Udskillelsesskema == "Sen udskillelse":
                MTX.Dosis_calciumfolinat_function(54, True, df, df_st)

            # Input function for validation of administration of dosis
            MTX.Sygeplejerske_navn_tid_validering(
                "Sygeplejerske_navn_dosis_calciumfolinat_t54",
                "Sygeplejerske_tid_dosis_calciumfolinat_t54",
                "Dosis calciumfoliat af Se-MTX t54 er givet",
                df,df_st)

            if Udskillelsesskema == "Hurtig udskillelse":
                MTX.Tjek_for_udskrivelse_af_patient(54, Se_MTX_t54, True, df, df_st)
            
            if Udskillelsesskema == "Normal udskillelse":         
                MTX.Tjek_for_udskrivelse_af_patient(54, Se_MTX_t54, False, df, df_st)

                #### Time 66 #### 
                st.subheader("Time 66: " + str(Time_t66) + " - (" + str(Udskillelsesskema) + ")")
                # Text area for notes
                MTX.Fritekst_indtastningsfelt("Time 66", df, df_st)
                st.write("MTX konc t66 analyseres sammen med t48 og t54. Afvent svar før evt. t66 dosis calciumfolinat")

                # Input for Se_MTX_t66
                Se_MTX_t66 = MTX.Blood_sample_input(66, "Se-MTX", df, df_st)
                MTX.MTX_input_check(Se_MTX_t54, Se_MTX_t66)

                # Input for P_kreatinin_t66
                P_kreatinin_t66 = MTX.Blood_sample_input(66, "P-kreatinin", df, df_st)

                if Se_MTX_t66 >= 0.2:
                    # Calculate dosis calciumfolinat and display to user
                    MTX.Dosis_calciumfolinat_function(66, False, df, df_st)

                    # Input function for validation of administration of dosis
                    MTX.Sygeplejerske_navn_tid_validering(
                        "Sygeplejerske_navn_dosis_calciumfolinat_t66",
                        "Sygeplejerske_tid_dosis_calciumfolinat_t66",
                        "Dosis calciumfoliat af Se-MTX t66 er givet",
                        df,df_st)

                MTX.Tjek_for_udskrivelse_af_patient(66, Se_MTX_t66, True, df, df_st)

            if Udskillelsesskema == "Sen udskillelse":
                
                #### Time 60 ####
                st.subheader("Time 60: " + str(Time_t60) + " - (" + str(Udskillelsesskema) + ")")
                # Text area for notes
                MTX.Fritekst_indtastningsfelt("Time 60", df, df_st)
                st.write("Giv t60 dosis calciumfolinat-dosis, i samme dosis som ved t54.")

                # Calciumfolinat dosis t60
                if df["Se_MTX_t54"][df_st["selected_treatment"][0]] == "":
                    st.warning("Indtast Se-MTX t54 for at beregne calciumfolinat-dosis.")

                if df["Se_MTX_t54"][df_st["selected_treatment"][0]] != "":
                    Dosis_calciumfolinat_t60 = MTX.Ekstra_dosis_calciumfolinat_function(60, Se_MTX_t54, df, df_st)
                    st.write(
                        "Giv t60 calciumfolinat-dosis " +
                        str(int(round(Dosis_calciumfolinat_t60/Overflade))) + " mg/m² svt. **" +
                        str(round(Dosis_calciumfolinat_t60)) + " mg iv.**"
                    )

                # Input function for validation of administration of dosis
                MTX.Sygeplejerske_navn_tid_validering(
                    "Sygeplejerske_navn_dosis_calciumfolinat_t60",
                    "Sygeplejerske_tid_dosis_calciumfolinat_t60",
                    "Dosis calciumfoliat af Se-MTX t60 er givet",
                    df,df_st)

                # While-loop for delayed excretion that continues until the treatment ends.
                # Get value to dertermine of patient is still Hospitalized
                Udskrevet = df["Udskrevet"][df_st["selected_treatment"][0]]
                Fortsæt_behandling = True
                
                Tid_while_loop_str = df["Tid_while_loop"][df_st["selected_treatment"][0]]
                if Tid_while_loop_str != "start-66":
                    #st.success(")")
                    Tid_while_loop_list = list(Tid_while_loop_str.split("-"))
                    #st.write(Tid_while_loop_list)
                if Tid_while_loop_str == "start-66":
                    #st.success("")
                    Tid_while_loop_list = list(Tid_while_loop_str.split("-"))
                    #st.write(Tid_while_loop_list)
                    

                for i in range(1, len(Tid_while_loop_list)):
                    tid0 = str(Tid_while_loop_list[i])
                    Time_t_start = Treatment_time_t0 + dt.timedelta(hours=int(tid0))
                    tid12 = str(int(tid0) + 12)
                    Time_t_12 = Treatment_time_t0 + dt.timedelta(hours=int(tid0)+12)

                    # Get values for blood sample check
                    Se_MTX_T_start_minus_12 = df["Se_MTX_t" + str(int(tid0)-12)][df_st["selected_treatment"][0]]
                    Se_MTX_T_start_minus_24 = df["Se_MTX_t" + str(int(tid0)-24)][df_st["selected_treatment"][0]]

                    try:
                        keyerror_check = df["Fritekst_Time "+tid0][df_st["selected_treatment"][0]] 
                    except KeyError as error:
                        MTX.Forlæng_behandling_indsæt_nye_kolonner(tid0, tid12, df)               

                    #### Time start ####
                    st.subheader("Time " + tid0 + ": " + str(Time_t_start) + " - (Sen udskillelse)")
                    # Text area for notes
                    MTX.Fritekst_indtastningsfelt("Time "+tid0, df, df_st)

                    st.write("Tag Se-MTX t" + tid0 + ": Analyseres akut. Afvent svar før yderligere calciumfolinat.")            

                    # Input for Se_MTX_t_start
                    Se_MTX_t_start = MTX.Blood_sample_input(int(tid0), "Se-MTX", df, df_st)
                    # Input check for Se-MTX
                    if Se_MTX_T_start_minus_12 != "":
                        MTX.MTX_input_check(Se_MTX_T_start_minus_12, Se_MTX_t_start)
                    elif Se_MTX_T_start_minus_24 != "":
                        MTX.MTX_input_check(Se_MTX_T_start_minus_24, Se_MTX_t_start)

                    # Input for P_kreatinin_t_start
                    P_kreatinin_t_start = MTX.Blood_sample_input(int(tid0), "P-kreatinin", df, df_st)


                    # Need Se-MTX t_start input:
                    if df["Se_MTX_t" + tid0][df_st["selected_treatment"][0]] == "":
                        st.warning("Indtast Se-MTX t" + tid0 + " for at beregne calciumfolinat-dosis.")
                    
                    if df["Se_MTX_t" + tid0][df_st["selected_treatment"][0]] != "":
                        if Se_MTX_t_start >= 0.2:
                            Dosis_calciumfolinat_t_start = MTX.Ekstra_dosis_calciumfolinat_function(tid0, Se_MTX_t_start, df, df_st)
                            st.info(
                                "Giv t" + tid0 + " dosis calciumfolinat-dosis " + 
                                str(int(round(Dosis_calciumfolinat_t_start/Overflade))) + " mg/m² svt. **" +
                                str((Dosis_calciumfolinat_t_start)) + " mg iv. **"
                            )

                            # Input function for validation of administration of dosis
                            MTX.Sygeplejerske_navn_tid_validering(
                                "Sygeplejerske_navn_dosis_calciumfolinat_t" + tid0,
                                "Sygeplejerske_tid_dosis_calciumfolinat_t" + tid0,
                                "Dosis calciumfoliat af Se-MTX t" + tid0 + " er givet",
                                df,df_st)

                        MTX.Tjek_for_udskrivelse_af_patient(tid0, Se_MTX_t_start, False, df, df_st)    

                        if Se_MTX_t_start >= 0.5:
                            # Make calculation of ekstra calciumfolinat dosis and input fields for four ekstra doses
                            MTX.Fire_ekstra_dosis_calciumfolinat(int(tid0), Se_MTX_t_start, df, df_st)    

                            if Se_MTX_t_start > 2.0 or (Se_MTX_t_start > 1.0 and Se_MTX_T_start_minus_24 != ""):
                                st.warning("Grundet Se-MTX t" + tid0 + " > 2,0 µmol/l: Giv calciumfolinat og mål Se-MTX 2 gange i døgnet til Se-MTX er < 1,0 µmol/l.")

                                #### Time t start + 12 timer ####
                                st.subheader("Time " + tid12 + ": " + str(Time_t_12) + " - (Sen udskillelse)")
                                # Text area for notes
                                MTX.Fritekst_indtastningsfelt("Time "+tid12, df, df_st)

                                st.write("Tag Se-MTX t" + tid12)            

                                # Input for Se_MTX_t_start_plus_12
                                Se_MTX_t_start_plus_12 = MTX.Blood_sample_input(int(tid12), "Se-MTX", df, df_st)
                                MTX.MTX_input_check(Se_MTX_t_start, Se_MTX_t_start_plus_12)
                                MTX.Tjek_for_udskrivelse_af_patient(tid12, Se_MTX_t_start_plus_12, False, df, df_st)   

                    # Treatment stops as default and wait for user to prolong
                    Fortsæt_behandling = False

                    # If blood sample values is present, the user can prolong treatment
                    if Se_MTX_t_start != 0 and Udskrevet == False and int(Tid_while_loop_list[i]) == int(Tid_while_loop_list[-1]): 
                        Fortsæt_behandling = st.button("Patienten er endnu ikke udskrevet. Tryk for at fortsætte behandlingen.", key=tid0)

                        if Fortsæt_behandling:
                            # update time variable so treatment can continue for 24 hours
                            Tid_while_loop_str += "-"+str(int(tid0)+24)
                            df.loc[df_st["selected_treatment"][0], "Tid_while_loop"] = Tid_while_loop_str
                            df.to_excel(Destination_main_file)
                

        # Tells use to input Se-MTX t42 so further treatment can be chosen
        elif Se_MTX_t42 == 0.0:
            st.error("Indtast Se-MTX t42 før behandling fortsættes.")

            Ingen_Se_MTX_t42 = st.checkbox("Fortsæt uden Se-MTX t42 værdi.")
            if Ingen_Se_MTX_t42:
                st.error(
                    "ADVARSEL: Værdien af Se-MTX t42 afgør om patienten har normal, hurtig eller sen udskillelse.  \n"
                    "Du er i gang med at gå videre uden denne værdi, hvilket ikke anbefales.  \n"
                )
                Udskillelsesskema = st.radio(
                    "Vælg hvilket udskillelsesskema patienten skal behandles ved:", 
                    options=["Hurtig udskillelse", "Normal udskillelse", "Sen udskillelse"],
                    index=1
                )
                if st.button("Bekræft at du har valgt " + str.lower(Udskillelsesskema)):
                    df.loc[df_st["selected_treatment"][0], "Udskillelsesskema"] = Udskillelsesskema
                    df.to_excel(Destination_main_file)

    except IndexError:
            st.info("Der er ingen tidligere patienter. Gå til startside og opret ny patient.")
    except KeyError:
       st.warning(
           "Der er ikke valg en patient.  \n"
           "Gå til 'Startside', vælg patient og behandling og tryk på knappen 'Vælg patient'."
           )
