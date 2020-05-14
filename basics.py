import streamlit as st
import pandas as pd
import datetime as dt
import re



###### Setup of dataframes ######
Destination_main_file = "MTX-dataark.xlsx"
Destination_st_file = "df_selected_treatment.xlsx"

class MTX:
    def MTX_pandas_main_file(Destination_main_file):
        """
        Function:   Imports data from main excelark to a dataframe

        Input:
            [str]	A string that contains the destination of the main file.

        Output:
            [pandas.dataframe]	Pandas dataframe that contains the data from the excelark
        """
        # Reads dataframe from excel
        df = pd.read_excel(Destination_main_file, na_filter=False)

        # Remove "Unnamed: 0" collums from dataframe
        df.drop(["Unnamed: 0"], axis=1, inplace=True)

        return df

    def MTX_pandas_st_file(Destination_st_file):
        """
        Function:   Imports data from selected treatment excelark to a dataframe

        Input:
            [str]	A string that contains the destination of the selected treatment file.

        Output:
            [pandas.dataframe]	Pandas dataframe that contains the data from the excelark
                                The value in the st_dataframe equals the row in the main_dataframe witch represent the selected treatment
        """
        # Reads dataframe from excel
        df_st = pd.read_excel(Destination_st_file)

        return df_st


    # The two following functions makes is possible to change the width of the content.
    def sidebar_settings():
        """Add selection section for setting setting the max-width and padding
        of the main block container"""
        st.sidebar.markdown("")
        st.sidebar.markdown("")
        max_width_100_percent = st.sidebar.checkbox("Maks bredde?", False)
        if not max_width_100_percent:
            max_width = st.sidebar.slider("Vælg maks bredde i px", 100, 2500, 900, 100)
        else:
            max_width = 900

        MTX._set_block_container_style(max_width, max_width_100_percent)


    def _set_block_container_style(max_width: int = 900, max_width_100_percent: bool = False):
        """## Helper Function to set the max width of the main block container"""
        if max_width_100_percent:
            max_width_str = f"max-width: 95%;"
        else:
            max_width_str = f"max-width: {max_width}px;"
        st.markdown(
            f"""
            <style>
            .reportview-container .main .block-container{{
                {max_width_str}
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )

    # This function is copyed from the awesome_streamlit package by Marc Skov Madsen
    # https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/package/awesome_streamlit/shared/components.py
    def write_page(page):  # pylint: disable=redefined-outer-name
        """Writes the specified page/module
        Our multipage app is structured into sub-files with a `def write()` function
        Arguments:
            page {module} -- A module with a 'def write():' function
        """
        # _reload_module(page)
        page.write()

    def hide_streamlit_style():
        hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    
    def custom_footer():
        """ Makes a custom footer """ 
        custom_footer = """
            <style>
                body { 
                    margin: 0; 
                    font-family: Arial, Helvetica, sans-serif;
                } 
                .footer {
                    position: fixed;
                    padding: 10px;
                    left: 0;
                    bottom: 0;
                    width: 100%;
                    background-color: #fafafa;
                    color: #262730;
                    text-align: center;
                    font-size: small;
                    z-index: 95
                }
            </style>

            <div class="footer">
                MTX Treatment Tool (beta v2) - Et værktøj udviklet af DTU til brug ved HDM behandling af ALL patienter
            </div>
        """
        st.markdown(custom_footer, unsafe_allow_html=True) 



    def gem_patientoplysninger(Navn, CPR, Alder, Køn, HDM_kur_nr, Højde, Vægt, Overflade, df, df_st):
        """
        Function:   Safes basic data of the patient to a pandas dataframe that have been given as input and export to an Excel dataark with Pandas

        Input:
            [value] A value containing the patient Name
            [value] A value containing the patient CPR number
            [value] A value containing the patient Age
            [value] A value containing the patient Sex
            [value] A value containing the patient HDM treatment number
            [value] A value containing the patient Hight
            [value] A value containing the patient Waigth
            [value] A value containing the patient Bodysurface
            [pandas.dataframe]	The dataframe for the main file

        Output:
            [pandas.dataframe]	Updated dataframe with the data from the input
            [pandas.dataframe]  The dataframe for the st file]
        """

        df_Patientoplysninger = pd.DataFrame({
            "Navn": [Navn],
            "CPR nr.": [CPR],
            "Alder": [Alder],
            "Køn": [Køn],
            "HDM_kur_nr": [HDM_kur_nr],
            "Højde": [Højde],
            "Vægt": [Vægt],
            "Overflade": [Overflade],
            "Udskrevet": [False],
            "Tid_while_loop": ["start-66"]
        })
        df = df.append(df_Patientoplysninger, ignore_index=True, sort=False)
        df.to_excel(Destination_main_file)
        st.write("Patientoplysninger er gemt")

        # When patient data is saved, the patients treatment is selected
        selected_treatment = len(df.index)-1
        df_st = pd.DataFrame({"selected_treatment":[selected_treatment]})
        df_st.to_excel(Destination_st_file)



    def patient_information_box(df, df_st):
        """
        Function:   Displays an infobox with some basic info about the selected patient
        
        Input:
            [pandas.dataframe]  The dataframe for the main file
            [pandas.dataframe]  The dataframe for the st file]
        """
        
        Navn = df["Navn"][df_st["selected_treatment"][0]]
        CPR = str(df["CPR nr."][df_st["selected_treatment"][0]])
        Kur_nr = str(df["HDM_kur_nr"][df_st["selected_treatment"][0]])
        Treatment_time_t0 = str(df["Treatment_time_t0"][df_st["selected_treatment"][0]])
        MTX_stop = str(df["Sygeplejerske_tid_MTX_afsluttet"][df_st["selected_treatment"][0]])
        Udskrevet = str(df["Udskrevet"][df_st["selected_treatment"][0]])



        if Treatment_time_t0 == "" or Treatment_time_t0 == "NaT":
            Behandlingsstart = "Forhydrering er ikke påbegyndt. t0 kan derfor ikke beregnes."
            Behandlingsstop = ""
        elif Treatment_time_t0 != "" and (MTX_stop == "" or MTX_stop == "NaT"):
            Behandlingsstart = str("Behandlings start t0: " + Treatment_time_t0)
            Behandlingsstop = "Kontinuerlig infusion af MTX er fortsat i gang."
        elif Treatment_time_t0 != "" and MTX_stop != "":
            Behandlingsstart = str("Behandlings start t0: " + Treatment_time_t0)
            Behandlingsstop = str("Kontinuerlig infusion af MTX er stoppet den: " + MTX_stop)

        # Make some space at the top of the page
        st.header('')

        infobox1 = str("Patient: " + Navn + " - " + CPR)
        infobox2 = str("Kur nr.: " + Kur_nr)
        infobox3 = str(Behandlingsstart)
        infobox4 = str(Behandlingsstop)
        if Udskrevet == "True":
            infobox5 = str("Patienten er udskrevet for denne behandling")
        else:
            infobox5 = ""

        st.markdown(
            """<style>
                body { 
                    margin: 0; 
                    font-family: Arial, Helvetica, sans-serif;
                } 
                .header {
                    position: fixed;
                    padding: 10px;
                    padding-left: 40%;
                    left: 0;
                    top: 0;
                    width: 100%;
                    background-color: #f0f2f6;
                    color: #262730;
                    text-align: left;
                    z-index: 95
                }
            </style>"""
            '<div class="header" id="myHeader">'
                + infobox1 + "</br>"
                + infobox2 + "</br>"
                + infobox3 + "</br>"
                + infobox4 + "</br>"
                + infobox5 +
            '</div>'
            , unsafe_allow_html=True)

        
    def patient_information_box_full(df, df_st):
        """
        Function:   Displays an infobox with some basic info about the selected patient
        
        Input:
            [pandas.dataframe]  The dataframe for the main file
            [pandas.dataframe]  The dataframe for the st file]
        """
        try:
            Navn = df["Navn"][df_st["selected_treatment"][0]]
            CPR = str(df["CPR nr."][df_st["selected_treatment"][0]])
            Kur_nr = str(df["HDM_kur_nr"][df_st["selected_treatment"][0]])
            Treatment_time_t0 = str(df["Treatment_time_t0"][df_st["selected_treatment"][0]])
            MTX_stop = str(df["Sygeplejerske_tid_MTX_afsluttet"][df_st["selected_treatment"][0]])
            Alder = str(df["Alder"][df_st["selected_treatment"][0]]) + " år"
            Køn = df["Køn"][df_st["selected_treatment"][0]] 
            Højde = str(df["Højde"][df_st["selected_treatment"][0]]) + " cm"
            Vægt = str(df["Vægt"][df_st["selected_treatment"][0]]) + " kg"
            Overflade = str(df["Overflade"][df_st["selected_treatment"][0]]) + " m2"
            Udskillelsesskema = str(df["Udskillelsesskema"][df_st["selected_treatment"][0]])
            
            if Udskillelsesskema == "":
                Udskillelse = "Det er ikke afgjort hvor hurtigt patienten udskiller MTX"
            if Udskillelsesskema != "":
                Udskillelse = "Patienten følger skema for " + str.lower(Udskillelsesskema)
            
            if str(df["Udskrevet"][df_st["selected_treatment"][0]]) == "False":
                Udskrevet = "Patienten er ikke udskrevet for denne behandling"
            if str(df["Udskrevet"][df_st["selected_treatment"][0]]) == "True":
                Udskrevet = "Patienten er udskrevet for denne behandling"

        
            if Treatment_time_t0 == "" or Treatment_time_t0 == "NaT":
                Behandlingsstart = "Forhydrering er ikke påbegyndt. t0 kan derfor ikke beregnes.  \n\n"
                Behandlingsstop = ""
            elif Treatment_time_t0 != "" and (MTX_stop == "" or MTX_stop == "NaT"):
                Behandlingsstart = str("Behandlings start t0: " + Treatment_time_t0 + "  \n")
                Behandlingsstop = str("Kontinuerlig infusion af MTX er fortsat i gang.  \n\n")
            elif Treatment_time_t0 != "" and MTX_stop != "":
                Behandlingsstart = str("Behandlings start t0: " + Treatment_time_t0 + "  \n")
                Behandlingsstop = str("Kontinuerlig infusion af MTX er stoppet den: " + MTX_stop + "  \n\n")

            st.info(
                "Patient: " + Navn + " - " + CPR + "  \n" 
                "Kur nr.: " + Kur_nr + "  \n"
                + Behandlingsstart
                + Behandlingsstop
                + Udskillelse + "  \n"
                "Alder: " + Alder + "  \n"
                "Køn: " + Køn + "  \n"
                "Højde: " + Højde + "  \n"
                "Vægt: " + Vægt + "  \n"
                "Overflade: " + Overflade + "  \n\n" +
                Udskrevet
            )
        except (KeyError, TypeError):   
            st.warning("Der er ikke valg en patient. Vælg patient og behandling ovenfor og tryk på knappen 'Vælg patient'.")


    def Blood_sample_overview(Udskillelsesskema, df, df_st):
        """
        Function:   Displays an infobox scheduled blood samples and their values.
        
        Input:
            [str]   The value for hydration scheme 
            [pandas.dataframe]  The dataframe for the main file
            [pandas.dataframe]  The dataframe for the st file]
        """

        Oversigt = "Der skal tages blodprøver til følgende tidspunkter:  \n"

        Faste_tidspunkter_MTX = [23,36,42,48,54,66]
        Faste_tidspunkter_P_kreatinin = [23,36]
        for tid in range(0,len(Faste_tidspunkter_MTX)):
            Time_dato = MTX.Treatment_time_t0_validering(Faste_tidspunkter_MTX[tid], df, df_st)
            if Time_dato == "Tidspunkt kan ikke udregnes da forhydrering ikke er påbegyndt":
                Time_dato = "_____Tidspunkt kan ikke udregnes da forhydrering ikke er påbegyndt___"
            Time = str(Faste_tidspunkter_MTX[tid])
            if Faste_tidspunkter_MTX[tid] in Faste_tidspunkter_P_kreatinin:
                Oversigt += "Time "+Time+" ("+str(Time_dato)[5:-3]+"): MTX "+MTX.Value_udregning(Time,df,df_st)+" og kreatinin "+MTX.Value_udregning(Time,df,df_st, "P_kreatinin")+"  \n"
            else: 
                Oversigt += "Time "+Time+" ("+str(Time_dato)[5:-3]+"): MTX "+MTX.Value_udregning(Time,df,df_st)+"  \n"

        try:
            if Udskillelsesskema == "Sen udskillelse":
                while_tid = 90
                Oversigt += "  \n Herfra følger patienten skema for _sen udskillelse_.  \n"
                Oversigt += "Der tages Se-MTX hver 24. time, eller hver 12. time hvis Se-MTX er over 2 µM indtil Se-MTX er under 1 µM.  \n"
                while str(df["Se_MTX_t"+str(while_tid)][df_st["selected_treatment"][0]]) != "":
                    Time = str(while_tid)
                    Time_dato = MTX.Treatment_time_t0_validering(while_tid, df, df_st)
                    Oversigt += "Time "+Time+" ("+str(Time_dato)[5:-3]+"): MTX "+MTX.Value_udregning(Time,df,df_st)+" og kreatinin "+MTX.Value_udregning(Time,df,df_st, "P_kreatinin")+"  \n"

                    if str(df["Se_MTX_t"+str(while_tid+12)][df_st["selected_treatment"][0]]) != "":
                        Time12 = str(while_tid+12)
                        Time_dato12 = MTX.Treatment_time_t0_validering(while_tid+12, df, df_st)
                        Oversigt += "Time "+Time12+" ("+str(Time_dato12)[5:-3]+"): MTX "+MTX.Value_udregning(Time12,df,df_st)+"  \n"
                    while_tid += 24
        except KeyError:
            pass

        st.info(Oversigt)


    def CPR_to_age(CPR):
        """
        Function:   Calculate the age from a danish social security number

        Input:
            [int]	An integer that contains the social security number (CPR)

        Output:
            [int]	An integer that contains the age
        """
        Tiden_nu = dt.datetime.now()
        CPR_str = str(CPR)
        Fødselsår = CPR_str[4:6]

        # Code to check for invalid dates
        # At this point, CPR_str[4:6] holds the year, CPR_str[2:4] the month and CPR_str[0:2] the day of the date entered
        if int(CPR_str[0:2]) == 31 and (int(CPR_str[2:4]) == 4 or int(CPR_str[2:4])  == 6 or int(CPR_str[2:4])  == 9 or int(CPR_str[2:4])  == 11) :
            st.error("CPR nummer eksisterer ikke. " + CPR_str[0:2] + "/" + CPR_str[2:4] + "-" + CPR_str[4:6] + " er ikke en gyldig dato.")
            # 31st of a month with 30 days
        elif int(CPR_str[0:2]) >= 30 and int(CPR_str[2:4]) == 2:
            st.error("CPR nummer eksisterer ikke. " + CPR_str[0:2] + "/" + CPR_str[2:4] + "-" + CPR_str[4:6] + " er ikke en gyldig dato.")
            # February 30th or 31st
        elif (int(CPR_str[2:4]) == 2 and int(CPR_str[0:2]) == 29 and not (int(CPR_str[4:6]) % 4 == 0 and (int(CPR_str[4:6]) % 100 != 0 or int(CPR_str[4:6]) % 400 == 0))):
            st.error("CPR nummer eksisterer ikke. " + CPR_str[0:2] + "/" + CPR_str[2:4] + "-" + CPR_str[4:6] + " er ikke en gyldig dato.")
            # February 29th outside a leap year
        else:
            # The rest of the code is exercuted if the date is valid.
            # The two if statements add the corret two numbers to get a four number birthyear
            
            # If patient is born in the last centery
            if int(Fødselsår) > int(str(Tiden_nu.year)[2:4]):
                Fødselsår_fuld = str(Tiden_nu.year-100)[0:2] + Fødselsår
            # If patient is born in this centery
            if int(Fødselsår) < int(str(Tiden_nu.year)[2:4]):
                Fødselsår_fuld = str(Tiden_nu.year)[0:2] + Fødselsår

            # Finds birthday and calculate age from the birthday
            Fødselsdag=dt.date(int(Fødselsår_fuld),int(CPR_str[2:4]),int(CPR_str[0:2]))
            Alder=int((Tiden_nu.date()-Fødselsdag).days /365.25)
            return Alder


    def Treatment_time_t0_validering(tid, df, df_st):
        """
        Function:   Checks if "infusions_start" is present and calculate time_variable

        Input:
            [[int/str]	A integer or a string containing the number and hours after time t0
            [pandas.dataframe]  The dataframe for the main file
            [pandas.dataframe]  The dataframe for the st file

        Output:
            [datetime.datetime]	Datetime objekt with wanted time.
        """
        
        Treatment_time_t0 = df["Treatment_time_t0"][df_st["selected_treatment"][0]]
        if str(Treatment_time_t0) != "NaT":
            variabel_navn = Treatment_time_t0 + dt.timedelta(hours=int(tid))
        if str(Treatment_time_t0) == "NaT":
            variabel_navn = "Tidspunkt kan ikke udregnes da forhydrering ikke er påbegyndt"
        return variabel_navn



    def Sygeplejerske_navn_tid_validering(Sygeplejerske_navn_destination,Sygeplejerske_tid_destination,Input_tekst,df,df_st):
        """
        Function:   Makes input fields for nurces when signing for medication with thier name and time of administration.
                    Saves the input to the Excel dataark

        Input:
            [str]	A string containing the distination in the Excel dataark for the name of the nurse for the relevent dosis 
            [str]	A string containing the distination in the Excel dataark for the time of for the relevent dosis 
            [str]	A string containing the text for the input fields and the save button
            [pandas.dataframe]  The dataframe for the main file
            [pandas.dataframe]  The dataframe for the st file

        Output:
            [str]	"Behandlingsdata er gemt"
        """

        # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
        Sygeplejerske_navn_værdi = st.text_input(Input_tekst + " af sygeplejerske:", value=df[Sygeplejerske_navn_destination][df_st["selected_treatment"][0]])
        
        # If the variable already has a value, the value is displayed. Otherwise a new value can be given or an old updated.
        tid = df[Sygeplejerske_tid_destination][df_st["selected_treatment"][0]]
        if tid == "":
            Sygeplejerske_tid_værdi = st.time_input(Input_tekst+ " til tidspunktet:")
        if tid != "":
            Sygeplejerske_tid_værdi = st.time_input(Input_tekst+ " til tidspunktet:", dt.time(int(tid[0:2]),int(tid[3:5])),int(tid[6:8]))

        # Button for saving input for nurse and time to excel
        if st.button("Gem behandlingsdata for: " + Input_tekst):
            df.loc[df_st["selected_treatment"][0], Sygeplejerske_navn_destination] = Sygeplejerske_navn_værdi
            df.loc[df_st["selected_treatment"][0], Sygeplejerske_tid_destination] = Sygeplejerske_tid_værdi
            df.to_excel(Destination_main_file)
            st.write("Behandlingsdata er gemt")


    def Value_udregning(tid, df, df_st, prøve="Se_MTX"):
        """Funktionen viser den indtastede prøves værdi hvis den er indtastet"""
        tid = prøve + "_t" + str(tid)
        if df[tid][df_st["selected_treatment"][0]] == 0 or df[tid][df_st["selected_treatment"][0]] == "":
            sample_value = ""
        else: 
            sample_value = "(Værdi: " + str(df[tid][df_st["selected_treatment"][0]]) + " µM)"
        return sample_value


    def Blood_sample_input(tid, sample_type, df, df_st):
        """
        Function:   Makes input fields for blood samples and exports the value to dataframe and dataark 

        Input:
            [int/str]	A integer or a string containing the number and hours after time t0
            [str]       A string containg "Se-MTX" og "P-kreatinin"
            [pandas.dataframe]  The dataframe for the main file
            [pandas.dataframe]  The dataframe for the st file

        Output:
            [MTX.custom_number_input]   Input field for blood sample
            [pandas.dataframe]  The dataframe with updated values
            [float/int]  Returns value for the sample_value
        """
        
        # Determine value-type
        if sample_type == "Se-MTX":
            sample = "Se_MTX_t" + str(tid)
            sample_type_tekst = "Se-MTX t" + str(tid) + " (µmol/l):"

            if df[sample][df_st["selected_treatment"][0]] != "":
                sample_value = MTX.custom_number_input(sample_type_tekst, int_or_float=float, value=float(df[sample][df_st["selected_treatment"][0]]))
            if df[sample][df_st["selected_treatment"][0]] == "":
                sample_value = MTX.custom_number_input(sample_type_tekst, int_or_float=float)
            if sample_value != 0.0 or sample_value != 0:
                df.loc[df_st["selected_treatment"][0],sample] = sample_value
                df.to_excel(Destination_main_file)

        if sample_type == "P-kreatinin":
            sample = "P_kreatinin_t" + str(tid)
            sample_type_tekst = "P-kreatinin t" + str(tid) + " (µmol/l):"

            if df[sample][df_st["selected_treatment"][0]] != "":
                sample_value = MTX.custom_number_input(sample_type_tekst, int_or_float=int, value=int(df[sample][df_st["selected_treatment"][0]]))
            if df[sample][df_st["selected_treatment"][0]] == "":
                sample_value = MTX.custom_number_input(sample_type_tekst, int_or_float=int)
            if sample_value != 0.0 or sample_value != 0:
                df.loc[df_st["selected_treatment"][0],sample] = sample_value
                df.to_excel(Destination_main_file)
        
        return sample_value


    def MTX_input_check(Sidste_MTX, Nuværende_MTX):
        """
        Function:   Check MTX-input for unrealistic values.

        Input:
            [float]	A variable containing af float with the previous MTX-value
            [float]	A variable containing af float with the new MTX-value
        
        Output:
            Makes a red warning if necessary
        """
        try:
            if float(Sidste_MTX) != 0 and float(Nuværende_MTX) != 0:
                if float(Sidste_MTX) < float(Nuværende_MTX):
                    st.error(
                        "OPMÆRKSOM: Du har indtastet en Se-MTX værdi som er højere end den forrige.  \n"
                        "Tjek indtastning."
                    )
                if float(Sidste_MTX) >= float(Nuværende_MTX)*2:
                    st.error(
                        "OPMÆRKSOM: Du har indtastet en Se-MTX værdi som angiver at Se-MTX er faldet mere end 50% siden sidste indtastning.  \n"
                        "Tjek indtastning."
                    )
        except ValueError as error:
            if error == "could not convert string to float:":
                pass
        except TypeError as error:
            if error == "float() argument must be a string or a number, not 'NoneType'":
                pass

    def Ekstra_dosis_calciumfolinat_function(tid, Se_MTX_value, df, df_st):
        """
        Function:   Calculate ekstra dosis calciumfolinate

        Input:
            [int/str]	A integer or a string containing the number and hours after time t0
            [Se_MTX variable]   The Se-MTX variabale containing the relevent Se-MTX value
            [pandas.dataframe]  The dataframe for the main file
            [pandas.dataframe]  The dataframe for the st file
        
        Output:
            [int]   Ekstra_dosis_calciumfolinat
        """
        # Makes sure that the time is a string
        tid = str(tid)
        
        # Get relevent patient data
        Vægt = df["Vægt"][df_st["selected_treatment"][0]]
        Overflade = df["Overflade"][df_st["selected_treatment"][0]]

        Ekstra_dosis_calciumfolinat = 0
        if Se_MTX_value < 1:
            Ekstra_dosis_calciumfolinat = int(round(15 * Overflade))
        if 1 <= Se_MTX_value < 2: 
            Ekstra_dosis_calciumfolinat = int(round(30 * Overflade))
        if 2 <= Se_MTX_value < 3:
            Ekstra_dosis_calciumfolinat = int(round(45 * Overflade))
        if 3 <= Se_MTX_value < 4:
            Ekstra_dosis_calciumfolinat = int(round(60 * Overflade))
        if 4 <= Se_MTX_value < 5:
            Ekstra_dosis_calciumfolinat = int(round(75 * Overflade))
        if Se_MTX_value >= 5:
            Ekstra_dosis_calciumfolinat = int(round(Se_MTX_value * Vægt))

        df.loc[df_st["selected_treatment"][0],"Dosis_calciumfolinat_t"+tid] = Ekstra_dosis_calciumfolinat
        df.to_excel(Destination_main_file)

        return Ekstra_dosis_calciumfolinat


    def Dosis_calciumfolinat_function(tid, Sen_udskillelse, df, df_st):
        """
        Function:   Calculate standard dosis calciumfolinate

        Input:
            [int/str]	A integer or a string containing the number and hours after time t0
            [Bool]              'True' the pation follows the scheme for delayed excretion, else 'False'
            [pandas.dataframe]  The dataframe for the main file
            [pandas.dataframe]  The dataframe for the st file
        
        """
        # Makes sure that the time is a string
        tid = str(tid)
        
        # Get relevent patient data
        Overflade = df["Overflade"][df_st["selected_treatment"][0]]
        Se_MTX = df["Se_MTX_t"+tid][df_st["selected_treatment"][0]]

        # Calculate dosis and display to user
        if Sen_udskillelse is False:
            Dosis_calciumfolinat = int(round(15 * Overflade))
            st.write("Giv t" + tid + " dosis calciumfolinat-dosis 15 mg/m² svt. **" + str(Dosis_calciumfolinat) + " mg iv. **")
        if Sen_udskillelse is True:
            if df["Se_MTX_t"+tid][df_st["selected_treatment"][0]] == "":
                st.warning("Indtast Se-MTX t" + tid + " for at beregne calciumfolinat-dosis.")

            if df["Se_MTX_t"+tid][df_st["selected_treatment"][0]] != "":
                Dosis_calciumfolinat = MTX.Ekstra_dosis_calciumfolinat_function(int(tid), Se_MTX, df, df_st)
                st.write(
                    "Giv t" + tid + " calciumfolinat-dosis " + 
                    str(int(round(Dosis_calciumfolinat/Overflade))) + " mg/m² svt. **" + 
                    str(round(Dosis_calciumfolinat)) + " mg iv.**"
                )

                # Safes to dataframe and dataark
                df.loc[df_st["selected_treatment"][0],"Dosis_calciumfolinat_t"+tid] = Dosis_calciumfolinat
                df.to_excel(Destination_main_file)


    def Fire_ekstra_dosis_calciumfolinat(tid, Se_MTX_value, df, df_st):
        """
        Function:   Calculate ekstra dosis calciumfolinate by using the 'Ekstra_dosis_calciumfolinat_function'
                    and makes input fiels using the funktion 'Sygeplejerske_navn_tid_validering'
                    All input values are eksported to dataframe and dataark

        Input:
            [int/str]	A integer or a string containing the number and hours after time t0
            [Se_MTX variable]   The Se-MTX variabale containing the relevent Se-MTX value
            [pandas.dataframe]  The dataframe for the main file
            [pandas.dataframe]  The dataframe for the st file

        """
        tid = int(tid)
        Time_t_plus_3 = MTX.Treatment_time_t0_validering(tid+3, df, df_st)
        Time_t_plus_9 = MTX.Treatment_time_t0_validering(tid+9, df, df_st)
        Time_t_plus_15 = MTX.Treatment_time_t0_validering(tid+15, df, df_st)
        Time_t_plus_21 = MTX.Treatment_time_t0_validering(tid+21, df, df_st)


        # Makes sure that the time is a string
        tid = str(tid)

        st.warning("Grundet Se-MTX t" + tid + " > eller lig 0,5 µmol/l: Giv calciumfolinat hver 6. time.")
        Ekstra_dosis_calciumfolinat = MTX.Ekstra_dosis_calciumfolinat_function(tid, Se_MTX_value, df, df_st)

        #### Ekstra dosis calciumfolinat X4 ####
        st.subheader("Første ekstra dosis calciumfoliat af Se-MTX t" + tid + " - " + str(Time_t_plus_3))
        st.write("Giv calciumfolinat dosis svt. **" + str(round(Ekstra_dosis_calciumfolinat)) + " mg iv.**")

        # Input function for validation of administration of dosis
        MTX.Sygeplejerske_navn_tid_validering(
            "Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t" + tid,
            "Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t" + tid,
            "Første ekstra dosis calciumfoliat af Se-MTX t" + tid + " er givet",
            df,df_st)

        st.subheader("Anden ekstra dosis calciumfoliat af Se-MTX t" + tid + " - " + str(Time_t_plus_9))
        st.write("Giv calciumfolinat dosis svt. **" + str(round(Ekstra_dosis_calciumfolinat)) + " mg iv.**")

        # Input function for validation of administration of dosis
        MTX.Sygeplejerske_navn_tid_validering(
            "Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t" + tid,
            "Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t" + tid,
            "Anden ekstra dosis calciumfoliat af Se-MTX t" + tid + " er givet",
            df,df_st)
        
        st.subheader("Tredje ekstra dosis calciumfoliat af Se-MTX t" + tid + " - " + str(Time_t_plus_15))
        st.write("Giv calciumfolinat dosis svt. **" + str(round(Ekstra_dosis_calciumfolinat)) + " mg iv.**")

        # Input function for validation of administration of dosis
        MTX.Sygeplejerske_navn_tid_validering(
            "Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t" + tid,
            "Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t" + tid,
            "Tredje ekstra dosis calciumfoliat af Se-MTX t" + tid + " er givet",
            df,df_st)

        st.subheader("Fjerde ekstra dosis calciumfoliat af Se-MTX t" + tid + " - " + str(Time_t_plus_21))
        st.write("Giv calciumfolinat dosis svt. **" + str(round(Ekstra_dosis_calciumfolinat)) + " mg iv.**")

        # Input function for validation of administration of dosis
        MTX.Sygeplejerske_navn_tid_validering(
            "Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t" + tid,
            "Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t" + tid,
            "Fjerde ekstra dosis calciumfoliat af Se-MTX t" + tid + " er givet",
            df,df_st)

    def Bekræft_udskrivelse(tid, df, df_st):
        """
        Function:   Ask user if the patient is ready for discharge and saves value in dataframe and dataark.

        Input:
            [str]   Stirng containing the time of treatment.
            [pandas.dataframe]  The dataframe for the main file
            [pandas.dataframe]  The dataframe for the st file

        """

        Udskrevet = str(df["Udskrevet"][df_st["selected_treatment"][0]])

        if Udskrevet == "False":
            st.warning("Bekærft venligst at patienten bliver udskrevet.")
            Bekræft_udskrivelse = st.button("Ja, patienten udskrives.", key=tid)
            if Bekræft_udskrivelse:
                st.success("Patientens udskrivelse er registreret.")
                df.loc[df_st["selected_treatment"][0],"Udskrevet"] = True
                df.to_excel(Destination_main_file)
        
        if Udskrevet == "True":
            st.success("Patientens udskrivelse er registreret.")


    def Send_patient_til_nyt_skema(Patient_kan_udskrives, df, df_st):
        """
        Function:   If the patient is not ready for discharge, patient can be transferred to a different hydration scheme

        Input:
            [Bool]  'True' if patient can be discharged, else 'False'
            [pandas.dataframe]  The dataframe for the main file
            [pandas.dataframe]  The dataframe for the st file

        """

        Udskillelsesskema = str(df["Udskillelsesskema"][df_st["selected_treatment"][0]])
        if Udskillelsesskema == "Hurtig udskillelse":
            Nyt_skema = "Normal udskillelse"
        if Udskillelsesskema == "Normal udskillelse":
            Nyt_skema = "Sen udskillelse"

        if Patient_kan_udskrives is True:
            button_text = "Nej, lad patienten overgå til skema for "+str.lower(Nyt_skema)
        if Patient_kan_udskrives is False:
            st.warning("Patientens værdier er ikke lave nok til at patienten kan udskrives.")
            button_text = "Lad patienten overgå til skema for "+str.lower(Nyt_skema)

        if Udskillelsesskema == "Hurtig udskillelse" or Udskillelsesskema == "Normal udskillelse":
            Bekræft_udskrivelse_Negativ = st.button(button_text)
            if Bekræft_udskrivelse_Negativ:
                df.loc[df_st["selected_treatment"][0],"Udskillelsesskema"] = Nyt_skema
                df.to_excel(Destination_main_file)
                st.write("Patienten overgår til skema for " + str.lower(Nyt_skema) + ". Opdater siden for at se skema.")

    def Sen_udskillelse(tid, df, df_st):
        """
        Function:   When patients are in delayed excretion this function can make sure that the patient get
                    ekstra calciumfolinat if needed and ekstra blood samples are taked. 
                    The function uses the functions "Blood_sample_input", "Ekstra_dosis_calciumfolinat_function" and
                    "Fire_ekstra_dosis_calciumfolinat"

        Input:
            [int/str]	A integer or a string containing the number and hours after time t0
            [pandas.dataframe]  The dataframe for the main file
            [pandas.dataframe]  The dataframe for the st file

        """
        Treatment_time_t0 = df["Treatment_time_t0"][df_st["selected_treatment"][0]]
        Overflade = df["Overflade"][df_st["selected_treatment"][0]]

        Time_t_start = Treatment_time_t0 + dt.timedelta(hours=tid)
        tid12 = str(int(tid) + 12)
        Time_t_12 = Treatment_time_t0 + dt.timedelta(hours=int(tid)+12)

        # Get values for blood sample check
        Se_MTX_T_start_minus_12 = df["Se_MTX_t" + str(int(tid)-12)][df_st["selected_treatment"][0]]
        Se_MTX_T_start_minus_24 = df["Se_MTX_t" + str(int(tid)-24)][df_st["selected_treatment"][0]]

        # Makes sure that the time is a string
        tid0 = str(tid)

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

                if Se_MTX_t_start > 2.0:
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
                df.loc[df_st["selected_treatment"][0],"Udskrevet"] = False
                df.to_excel(Destination_main_file)


    def Tjek_for_udskrivelse_af_patient(tid, Se_MTX_value, Sidste_på_skema, df, df_st):
        """
        Function:   Checks if Se-MTX value is low enougth to discharge patient

        Input:
            [int/str]	A integer or a string containing the number and hours after time t0
            [Se_MTX variable]   The Se-MTX variabale containing the relevent Se-MTX value
            [Bool]              'True' the function is called as the last at the hydration scheme, else 'False'
            [pandas.dataframe]  The dataframe for the main file
            [pandas.dataframe]  The dataframe for the st file
        """
        Overflade = df["Overflade"][df_st["selected_treatment"][0]]
        Udskrevet = df["Udskrevet"][df_st["selected_treatment"][0]]

        # Makes sure that the time is a string
        tid = str(tid)

        if Se_MTX_value < 0.2 and df["Se_MTX_t" + tid][df_st["selected_treatment"][0]] != "":
            st.success(
                "Da Se-MTX t" + tid + " < 0.2 µmol/l gives der ikke yderligere calciumfolinat.  \n"
                "Patienten kan udskrives."
            )

        elif 0.2 <= Se_MTX_value < 0.3:
            st.success("Patienten udskrives efter t" + tid + " dosis calciumfolinat")

        elif 0.3 <= Se_MTX_value < 0.4:
            st.success(
                "Patienten udskrives med calciumfolinat 15 mg/m2 (svt. **" + 
                str(round(15*Overflade)) + " mg**) x 3 po. i 2 døgn efter t" + tid + " dosis calciumfolinat."
            )

        elif 0.4 <= Se_MTX_value < 0.5:
            st.success(
                "Patienten udskrives med calciumfolinat 15 mg/m2 (svt. **" + 
                str(round(15*Overflade)) + " mg**) x 3 po. i 3 døgn efter t" + tid + " dosis calciumfolinat."
            )

        if Se_MTX_value < 0.5 and df["Se_MTX_t" + tid][df_st["selected_treatment"][0]] != "":
            MTX.Bekræft_udskrivelse(tid, df, df_st)

        if Sidste_på_skema is True and df["Se_MTX_t" + tid][df_st["selected_treatment"][0]] != "" and str(Udskrevet) == "False":
            if Se_MTX_value < 0.5:
                MTX.Send_patient_til_nyt_skema(True, df, df_st)
            elif Se_MTX_value >= 0.5:
                MTX.Send_patient_til_nyt_skema(False, df, df_st)


    def Fritekst_indtastningsfelt(label, df, df_st):
        """
        Function:   Makes text areas for notes. If af note is registred, the note will always be displayed.

        Input:
            [str]	A label that refers to the time in the treatment
            [pandas.dataframe]  The dataframe for the main file
            [pandas.dataframe]  The dataframe for the st file
        """
        try:   
            Indtastet_note = str(df["Fritekst_" + str(label)][df_st["selected_treatment"][0]])

            Fritekst_indtastning = st.checkbox("Vis indtastningsfelt for fritekst ("+str(label)+")")
            if Fritekst_indtastning:
                Fritekst = st.text_area("Her kan du skrive noter:", value=df["Fritekst_" + str(label)][df_st["selected_treatment"][0]])
                if st.button("Gem note"):
                    df.loc[df_st["selected_treatment"][0], "Fritekst_" + str(label)] = Fritekst
                    df.to_excel(Destination_main_file)
                    st.write("Noten er gemt")
        
            if Indtastet_note != "":
                st.info(
                    "_Følgende note er indtastet:_  \n" +
                    Indtastet_note
                )
        except (KeyError, UnboundLocalError):
            pass

    
    def Forlæng_behandling_indsæt_nye_kolonner(tid0, tid12, df):
        """
        Function:   Extends dataframe and dataark with ekstra 24 hours

        Input:
            [str]   A string kontaining an interger with the starttime
            [str]   A string kontaining an interger with the starttime+12 hours
            [pandas.dataframe]  The dataframe for the main file
        """

        Nye_kolonner = [
            "Fritekst_Time "+tid0,
            "Se_MTX_t"+tid0,
            "P_kreatinin_t"+tid0,
            "Dosis_calciumfolinat_t"+tid0,
            "Sygeplejerske_navn_dosis_calciumfolinat_t"+tid0,
            "Sygeplejerske_tid_dosis_calciumfolinat_t"+tid0,
            "Sygeplejerske_navn_Første_Ekstra_dosis_calciumfolinat_t"+tid0,
            "Sygeplejerske_tid_Første_Ekstra_dosis_calciumfolinat_t"+tid0,
            "Sygeplejerske_navn_Anden_Ekstra_dosis_calciumfolinat_t"+tid0,
            "Sygeplejerske_tid_Anden_Ekstra_dosis_calciumfolinat_t"+tid0,
            "Sygeplejerske_navn_Tredje_Ekstra_dosis_calciumfolinat_t"+tid0,
            "Sygeplejerske_tid_Tredje_Ekstra_dosis_calciumfolinat_t"+tid0,
            "Sygeplejerske_navn_Fjerde_Ekstra_dosis_calciumfolinat_t"+tid0,
            "Sygeplejerske_tid_Fjerde_Ekstra_dosis_calciumfolinat_t"+tid0,
            "Fritekst_Time "+tid12,
            "Se_MTX_t"+tid12
        ]
        Kolonne_placering = len(df.columns)
        liste = ["" for i in range(len(df.index))]
        for kolonne in range(0,len(Nye_kolonner)):
            df.insert(Kolonne_placering+kolonne, Nye_kolonner[kolonne], liste)
        df.to_excel(Destination_main_file)

    def custom_number_input(label, int_or_float, value=""):
        """
        Function:   Converts a st.text_input to a number_input

        Input:
            [str]   A short label explaining to the user what this input is for
            [value] int or float
            [value] (int or float or None) The value of this widget when it first renders. Defaults None
            [pandas.dataframe]  The dataframe for the main file
        """
        
        if int_or_float == int:
            int_or_float = "heltal"
            user_input = st.text_input(label, value=value)
            try:
                user_input = int(user_input)
            except ValueError as error:
                if str(error)[0:38] == "invalid literal for int() with base 10" and str(error) != "invalid literal for int() with base 10: ''":
                    st.error("Indtastning skal være et positivt heltal")

        if int_or_float == float:
            int_or_float = "kommatal"
            user_input = st.text_input(label, value=value)
            if user_input != "":
                REresult_float = re.search(r'^(\d+)(([\.\,])?(\d+)?)$', user_input)
                if REresult_float is None:
                    st.error("Indtastning skal være et positivt heltal eller kommatal")
                else:
                    if REresult_float.group(4) is None:
                        user_input = float(REresult_float.group(1)+".0")
                    else:
                        user_input = float(REresult_float.group(1)+"."+REresult_float.group(4))

        try:
            if type(user_input) is int or type(user_input) is float:
                return user_input
            elif int_or_float == "heltal":
                return int()
            elif int_or_float == "kommatal":
                return float()
        except UnboundLocalError as error:
            if error == "local variable 'user_input' referenced before assignment":
                pass
