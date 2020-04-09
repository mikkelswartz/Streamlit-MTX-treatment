import streamlit as st
import datetime as dt

from basics import *

def write():
    df = pd.read_excel(Destination_main_file, na_filter=False)
    # The next two if statemens make sure, that if there is no patient in the dataframe, user is informed and referred to startpage
    if len(df) == 0:
        st.info("Der er ingen tidligere patienter. Gå til startside og opret ny patient.")
    if len(df) != 0:
        # Export functions
        def Sygeplejerske_one_to_ten_MTX_dose_export():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_one_to_ten_MTX_dose"] = Sygeplejerske_navn_one_to_ten_MTX_dose
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_one_to_ten_MTX_dose"] = Sygeplejerske_tid_one_to_ten_MTX_dose
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")


        def Sygeplejerske_nine_to_ten_MTX_dose_export():
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_navn_nine_to_ten_MTX_dose"] = Sygeplejerske_navn_nine_to_ten_MTX_dose
            df.loc[df_st["selected_treatment"][0],"Sygeplejerske_tid_nine_to_ten_MTX_dose"] = Sygeplejerske_tid_nine_to_ten_MTX_dose
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")

        # Get variabels from dataframe
        Vægt = df["Vægt"][df_st["selected_treatment"][0]]
        Overflade = df["Overflade"][df_st["selected_treatment"][0]]
        Treatment_time_t0 = df["Treatment_time_t0"][df_st["selected_treatment"][0]]
        Total_væskemængde = df["Total_væskemængde"][df_st["selected_treatment"][0]]
        
        # Selected patient info
        st.info(
            "Patient: " + df["Navn"][df_st["selected_treatment"][0]]+ " - "+ str(df["CPR nr."][df_st["selected_treatment"][0]])+ "  \n"+ 
            "Kur nr.: "+ str(df["HDM_kur_nr"][df_st["selected_treatment"][0]])+ "  \n"+ 
            "Behandlings start t0: "+ str(df["Treatment_time_t0"][df_st["selected_treatment"][0]])
        )

        #### Time 0 ####
        Infusions_start = Treatment_time_t0 + dt.timedelta(hours=0)
        st.subheader('Time 0. 1/10 infusionsstart: ' + str(Infusions_start))
        st.write('Diuresen skal være over 600 ml/m²/ 6 timer svt.')
        Durise_600ml_6timer = int(round(600*(Overflade)))
        if Durise_600ml_6timer != 0.0:
            st.info(str(Durise_600ml_6timer) + " ml/6 timer")
            df.loc[df_st["selected_treatment"][0],"Durise_600ml_6timer"] = Durise_600ml_6timer
            df.to_excel(Destination_main_file)



        st.write('Hvis diuresen er mindre gives furosemid 0.5 mg/kg iv.')
        Furosemid = int(round(0.5*Vægt))
        if Furosemid != 0.0:
            st.info(str(Furosemid) + " mg")
            df.loc[df_st["selected_treatment"][0],"Furosemid"] = Furosemid
            df.to_excel(Destination_main_file)

        st.warning('Urin pH skal være lig eller over 6 før start på MTX')
        st.write(
            'Ved urin pH<7 skal patienten have:  \n'
            'Na-bicarbonat 20 mmol/m² iv over 30 min. i 40 ml hydreringsvæske.  \n'
            'Svarende til:'
        )
        Dosis_natriumcarbonat_ved_lav_pH = int(round(20*(Overflade)))
        if Dosis_natriumcarbonat_ved_lav_pH != 0.0:
            st.info(str(Dosis_natriumcarbonat_ved_lav_pH) + " mmol Na-bicarbonat")
            df.loc[df_st["selected_treatment"][0],"Dosis_natriumcarbonat_ved_lav_pH"] = Dosis_natriumcarbonat_ved_lav_pH
            df.to_excel(Destination_main_file)

        st.warning(
            'Ved urin pH > 8 skiftes til KNaG uden bicarbonat i 3 time.  \n'
            'Når pH er under 8 skiftes til bicarbonatholdig hydrering'
        )


        st.write('Start blodinfusion og angiv tidspunkt. 1/10 af MTX dosis gives over 1 time')
        one_to_ten_MTX_dose = int(round(5000*round(Overflade,2)*0.1))
        if one_to_ten_MTX_dose != 0.0:
            st.info(str(one_to_ten_MTX_dose) + " mg")


        # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
        Sygeplejerske_navn_one_to_ten_MTX_dose = st.text_input('1/10 dosis givet af sygeplejerske:', value=df["Sygeplejerske_navn_one_to_ten_MTX_dose"][df_st["selected_treatment"][0]])

        # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
        tid_1_10_dosis = df["Sygeplejerske_tid_one_to_ten_MTX_dose"][df_st["selected_treatment"][0]]
        if tid_1_10_dosis == "":
            Sygeplejerske_tid_one_to_ten_MTX_dose = st.time_input('1/10 dosis: Tidspunkt:')
        if tid_1_10_dosis != "":
            Sygeplejerske_tid_one_to_ten_MTX_dose = st.time_input('1/10 dosis: Tidspunkt:', dt.time(int(tid_1_10_dosis[0:2]),int(tid_1_10_dosis[3:5]),int(tid_1_10_dosis[6:8])))
        # Button for saving input for nurse and time to excel
        if st.button("Gem behandlingsdata 1/10 dosis"):
            Sygeplejerske_one_to_ten_MTX_dose_export()


        #### Time 1 ####
        Kontinuerlig_infusion_start = Treatment_time_t0 + dt.timedelta(hours=1)
        st.subheader('Time 1. 9/10 infusionsstart: ' + str(Kontinuerlig_infusion_start))
        st.write('Start kontinuerlig infusion af MTX. 9/10 af MTX dosis gives over 23 timer')
        nine_to_ten_MTX_dose = int(round(5000*round(Overflade,2)*0.9))
        if nine_to_ten_MTX_dose != 0.0:
            st.info(str(nine_to_ten_MTX_dose) + " mg")
        
        st.write('Samlet mængde af MTX og hydreringsvæske: ')
        total_volume_MTX_and_hydration_liquid = Total_væskemængde
        if total_volume_MTX_and_hydration_liquid != 0.0:
            st.info(str(total_volume_MTX_and_hydration_liquid) + " ml/time")
        
        st.write("Hydreringsvæske reduceret til samlet 3000 ml/m2/døgn.")


        # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
        Sygeplejerske_navn_nine_to_ten_MTX_dose = st.text_input('9/10 dosis givet af sygeplejerske:', value=df["Sygeplejerske_navn_nine_to_ten_MTX_dose"][df_st["selected_treatment"][0]])

        # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
        tid_9_10_dosis = df["Sygeplejerske_tid_nine_to_ten_MTX_dose"][df_st["selected_treatment"][0]]
        if tid_9_10_dosis == "":
            Sygeplejerske_tid_nine_to_ten_MTX_dose = st.time_input('9/10 dosis: Tidspunkt:')
        if tid_9_10_dosis != "":
            Sygeplejerske_tid_nine_to_ten_MTX_dose = st.time_input('9/10 dosis: Tidspunkt:', dt.time(int(tid_9_10_dosis[0:2]),int(tid_9_10_dosis[3:5]),int(tid_9_10_dosis[6:8])))
        # Button for saving input for nurse and time to excel
        if st.button("Gem behandlingsdata 9/10 dosis"):
            Sygeplejerske_nine_to_ten_MTX_dose_export()
        
