import streamlit as st


# #### for testing ####
# Overflade = 0
# Vægt = 0
# Infusions_start = 0
# #### for testing ####

from basics import *
from pages.Startside import *


def write():
    # Get variabels from dataframe
    Overflade = df["Overflade"][0]
    

    # Selected patient info
    st.info(
        "Patient: " + df["Navn"][0]+ " - "+ str(df["CPR nr."][0])+ "  \n"+ 
        "Kur nr.: "+ str(df["HDM_kur_nr"][0])+ "  \n"+ 
        "Behandlings start t0: "+ str(df["Treatment_time_t0"][0])
    )

    

    
        
