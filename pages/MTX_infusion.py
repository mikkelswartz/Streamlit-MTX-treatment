import streamlit as st
import datetime as dt
import sys

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
        Sygeplejerske_tid_forhydering = df["Sygeplejerske_tid_forhydering"][df_st["selected_treatment"][0]]
        Treatment_time_t0 = df["Treatment_time_t0"][df_st["selected_treatment"][0]]
        Forhydrering_varighed_værdi = df["Forhydrering_varighed_værdi"][df_st["selected_treatment"][0]]
        Total_væskemængde = df["Total_væskemængde"][df_st["selected_treatment"][0]]
        Plasma_kreatinin_før_start = df["Plasma_kreatinin_før_start"][df_st["selected_treatment"][0]]
        Infusions_start = MTX.Treatment_time_t0_validering(0, df, df_st)

        Kontinuerlig_infusion_start = MTX.Treatment_time_t0_validering(1, df, df_st)
        Time_t23 = MTX.Treatment_time_t0_validering(23, df, df_st)
        Time_t24 = MTX.Treatment_time_t0_validering(24, df, df_st)
        Time_t36 = MTX.Treatment_time_t0_validering(36, df, df_st)
        Time_t42 = MTX.Treatment_time_t0_validering(42, df, df_st)
        Time_t48 = MTX.Treatment_time_t0_validering(48, df, df_st)
        Time_t54 = MTX.Treatment_time_t0_validering(54, df, df_st)
        Time_t66 = MTX.Treatment_time_t0_validering(66, df, df_st)

        # Selected patient info
        MTX.patient_information_box(df, df_st)

        #### Time 0 ####
        st.subheader("Time 0. 1/10 infusionsstart: " + str(Infusions_start))
        # Text area for notes
        MTX.Fritekst_indtastningsfelt("Time 0", df, df_st)

        Durise_600ml_6timer = int(round(600*(Overflade)))
        if Durise_600ml_6timer != 0.0:
            st.write(
                "Durisen skal være over 600 ml/m²/ 6 timer svt. **" + str(Durise_600ml_6timer) + " ml/6 timer**"
            )
            df.loc[df_st["selected_treatment"][0],"Durise_600ml_6timer"] = Durise_600ml_6timer
            df.to_excel(Destination_main_file)

        Furosemid = int(round(0.5*Vægt))
        if Furosemid != 0.0:
            st.write(
                "Hvis durisen er mindre gives furosemid 0.5 mg/kg iv. svt. **" +str(Furosemid) + " mg **"
            )
            df.loc[df_st["selected_treatment"][0],"Furosemid"] = Furosemid
            df.to_excel(Destination_main_file)

        st.warning(
            "Højdosis MTX må først startes:  \n"
            " - Efter mindst 4 timers forhydrering.  \n"
            " - Efter urin pH har været ≥7.0 i mindst 3 timer"
        )

        Dosis_natriumcarbonat_ved_lav_pH = int(round(20*(Overflade)))
        if Dosis_natriumcarbonat_ved_lav_pH != 0.0:
            st.info(
                "Ved urin pH<7.0 skal der gives ekstra bicarbonat:  \n"
                "Na-bicarbonat 20 mmol/m² blandes i 40 ml af hydreringsvæsken og gives over over 30 min. samtidig med forhydreringen.  \n"
                "Svarende til: **" + str(Dosis_natriumcarbonat_ved_lav_pH) + " mmol** Na-bicarbonat"
            )
            df.loc[df_st["selected_treatment"][0],"Dosis_natriumcarbonat_ved_lav_pH"] = Dosis_natriumcarbonat_ved_lav_pH
            df.to_excel(Destination_main_file)

        st.warning(
            "Ved urin pH > 8 skiftes til KNaG uden bicarbonat i 3 time.  \n"
            "Når pH er under 8 skiftes til bicarbonatholdig hydrering"
        )

        one_to_ten_MTX_dose = int(round(5000*round(Overflade,2)*0.1))
        if one_to_ten_MTX_dose != 0.0:
            st.write(
                "Start blodinfusion og angiv tidspunkt. 1/10 af MTX dosis gives over 1 time, svt. **" + str(one_to_ten_MTX_dose) + " mg**"
            )
            df.loc[df_st["selected_treatment"][0],"one_to_ten_MTX_dose"] = one_to_ten_MTX_dose
            df.to_excel(Destination_main_file)

        # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
        Sygeplejerske_navn_one_to_ten_MTX_dose = st.text_input("1/10 dosis er givet af sygeplejerske:", value=df["Sygeplejerske_navn_one_to_ten_MTX_dose"][df_st["selected_treatment"][0]])
        
        # An error is raised if forhydrering data is not present
        try:
            # Convert Sygeplejerske_tid_forhydering to a datetime.time object
            Forhydreringstidspunkt = dt.time(int(Sygeplejerske_tid_forhydering[0:2]),int(Sygeplejerske_tid_forhydering[3:5]),int(Sygeplejerske_tid_forhydering[6:8]))

            # Finds the difference between treatment_timt_t0 and Forhydreringstidspunkt
            Forskel_tid = (df["Treatment_time_t0"][df_st["selected_treatment"][0]] + dt.timedelta(hours=-Forhydreringstidspunkt.hour,minutes=-Forhydreringstidspunkt.minute,seconds=-Forhydreringstidspunkt.second))
            Forskel_tid_float = Forskel_tid.hour+Forskel_tid.minute/60.0

            # Input for the duration of forhydrering
            if Forhydrering_varighed_værdi == Forskel_tid_float:
                MTX_start = st.radio("1/10 dosis er givet til tidspunktet:", options=[str(df["Treatment_time_t0"][df_st["selected_treatment"][0]]), "Andet"], index=0)
            elif Forhydrering_varighed_værdi != Forskel_tid_float:
                MTX_start = st.radio("1/10 dosis er givet til tidspunktet:", options=[str(df["Treatment_time_t0"][df_st["selected_treatment"][0]]), "Andet"], index=1)
            
            # Input if the MTX-infusion start is different form the schedule
            if MTX_start == "Andet":
                # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
                tid = df["Sygeplejerske_tid_one_to_ten_MTX_dose"][df_st["selected_treatment"][0]]
                if tid == "":
                    Sygeplejerske_tid_one_to_ten_MTX_dose = st.time_input("1/10 dosis er givet til tidspunktet:")
                    Dato_updated = st.date_input("Forhydrering er givet den:")
                if tid != "":
                    Sygeplejerske_tid_one_to_ten_MTX_dose = st.time_input("1/10 dosis er givet til tidspunktet:", dt.time(int(tid[0:2]),int(tid[3:5])),int(tid[6:8]))
                    Dato_updated = st.date_input("Forhydrering er givet den:")
                # Update Treatment_time_t0
                Treatment_time_t0_updated = dt.datetime.combine(dt.date(Dato_updated.year,Dato_updated.month,Dato_updated.day),dt.time(Sygeplejerske_tid_one_to_ten_MTX_dose.hour,Sygeplejerske_tid_one_to_ten_MTX_dose.minute))

            # If MTX-infusion start is the same as the schedule
            else:
                Sygeplejerske_tid_one_to_ten_MTX_dose = Treatment_time_t0.time()

            # Checkbox that have to be checked before the nurce can safe treatment data
            if str(df["Tilstrækkelig_forhydrering_og_pH"][df_st["selected_treatment"][0]]) != "True":
                Tilstrækkelig_forhydrering_og_pH = st.checkbox("Har der været mindst 4 timers forhydrering og har pH vøret ≥7.0 i mindst 3 timer?")
                if Tilstrækkelig_forhydrering_og_pH is True or str(df["Tilstrækkelig_forhydrering_og_pH"][df_st["selected_treatment"][0]]) is True:
                    df.loc[df_st["selected_treatment"][0],"Tilstrækkelig_forhydrering_og_pH"] = True
                    df.to_excel(Destination_main_file)
            elif str(df["Tilstrækkelig_forhydrering_og_pH"][df_st["selected_treatment"][0]]) == "True":
                Tilstrækkelig_forhydrering_og_pH = st.checkbox("Har der været mindst 4 timers forhydrering og har pH vøret ≥7.0 i mindst 3 timer?", value=True)


            if Tilstrækkelig_forhydrering_og_pH is True or df["Tilstrækkelig_forhydrering_og_pH"][df_st["selected_treatment"][0]] is True:
                # Button for saving input for nurse and time to excel
                if st.button("Gem behandlingsdata for: 1/10 dosis"):
                    df.loc[df_st["selected_treatment"][0], "Sygeplejerske_navn_one_to_ten_MTX_dose"] = Sygeplejerske_navn_one_to_ten_MTX_dose
                    df.loc[df_st["selected_treatment"][0], "Sygeplejerske_tid_one_to_ten_MTX_dose"] = Sygeplejerske_tid_one_to_ten_MTX_dose
                    if MTX_start == "Andet":
                        df.loc[df_st["selected_treatment"][0], "Treatment_time_t0"] = Treatment_time_t0_updated
                    df.to_excel(Destination_main_file)
                    st.write("Behandlingsdata er gemt")
                    st.info(
                        "Der skal tages blodprøver til følgende tidspunkter:  \n"
                        "Time 23 (" + str(Time_t23)[5:-3] + "): MTX og kreatinin  \n"
                        "Time 36 (" + str(Time_t36)[5:-3] + "): MTX og kreatinin  \n"
                        "Time 42 (" + str(Time_t42)[5:-3] + "): MTX  \n"
                        "Time 48 (" + str(Time_t48)[5:-3] + "): MTX  \n"
                        "Time 54 (" + str(Time_t54)[5:-3] + "): MTX  \n"
                        "Time 66 (" + str(Time_t66)[5:-3] + "): MTX"
                    )
            else:
                st.error("Du skal godkende at der været mindst 4 timers forhydrering og har pH vøret ≥7.0 i mindst 3 timer før du kan gemme behandlingsdata")


            #### Time 1 ####
            st.subheader("Time 1. Kontinuerlig infusionsstart: " + str(Kontinuerlig_infusion_start))
            # Text area for notes
            MTX.Fritekst_indtastningsfelt("Time 1", df, df_st)
            nine_to_ten_MTX_dose = int(round(5000*round(Overflade,2)*0.9))
            if nine_to_ten_MTX_dose != 0.0:
                st.write(
                    "Start kontinuerlig infusion af MTX.  \n"
                    "Kontinuerlig infusion af MTX dosis gives over 23 timer af samlet **" + str(nine_to_ten_MTX_dose) + " mg**"
                )
                df.loc[df_st["selected_treatment"][0],"nine_to_ten_MTX_dose"] = nine_to_ten_MTX_dose
                df.to_excel(Destination_main_file)
            
            
            total_volume_MTX_and_hydration_liquid = Total_væskemængde
            if total_volume_MTX_and_hydration_liquid != 0.0:
                st.write("Samlet mængde af MTX og hydreringsvæske: **" + str(total_volume_MTX_and_hydration_liquid) + " ml/time**")
                df.loc[df_st["selected_treatment"][0],"total_volume_MTX_and_hydration_liquid"] = total_volume_MTX_and_hydration_liquid
                df.to_excel(Destination_main_file)
                
            st.write("Hydreringsvæske reduceret til samlet 3000 ml/m2/døgn.")

            # Input function for validation of administration of dosis
            MTX.Sygeplejerske_navn_tid_validering(
                "Sygeplejerske_navn_nine_to_ten_MTX_dose",
                "Sygeplejerske_tid_nine_to_ten_MTX_dose",
                "Den kontinuerlige infusion af MTX er startet",
                df,df_st)

            #### Time 23 ####
            P_kreatinin_t23_advarsel = int(Plasma_kreatinin_før_start)*1.5
            st.warning(
                "Blodprøven 'Time 23 MTX og kreatinin' skal tages til time 23 (" + str(Time_t23) + "), altså inden MTX kuren er løbet ind.  \n"
                "Hvis plasma kreatinin time 23 er mere end **" + str(P_kreatinin_t23_advarsel) + " µM**, så skal hydreringen øges til 4500 ml/m2/døgn.  \n"
                "Blodprøveresultater skal tastes ind under siden 'Monitorering af toksicitet'."
            )

            #### Time 24 ####
            st.subheader("Time 24: " + str(Time_t24))
            # Text area for notes
            MTX.Fritekst_indtastningsfelt("Time 24", df, df_st)

            st.write("MTX infusion afsluttes - hydreringsvækens hastighed øges")

            # Input function for validation of administration of dosis
            MTX.Sygeplejerske_navn_tid_validering(
                "Sygeplejerske_navn_MTX_afsluttet",
                "Sygeplejerske_tid_MTX_afsluttet",
                "Den kontinuerlige infusion af MTX er stoppet",
                df,df_st)

        except ValueError:
            st.error("Forhydreringen er ikke registreret. Gå til forhydrering og indtast data for forhydrering.")

    except IndexError:
            st.info("Der er ingen tidligere patienter. Gå til startside og opret ny patient.")
    except KeyError:
        st.warning(
            "Der er ikke valg en patient.  \n"
            "Gå til 'Startside', vælg patient og behandling og tryk på knappen 'Vælg patient'."
            )
    
