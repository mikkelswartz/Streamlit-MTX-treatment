import streamlit as st
import math
import pandas as pd

import datetime as dt

from basics import * 
import pages.Startside
import pages.Forhydering
import pages.MTX_infusion
import pages.Monitorering_af_toksicitet

PAGES = {
    "Startside" : pages.Startside,
    "Forhydrering" : pages.Forhydering,
    "MTX infusion" : pages.MTX_infusion,
    "Monitorering af toksicitet" : pages.Monitorering_af_toksicitet
}

def main():
    
    st.sidebar.title("Navigation")
    page_selection = st.sidebar.radio('', options=list(PAGES.keys()))

    page = PAGES[page_selection]
    #testing
    #before = dt.datetime.now()
    #testing
    
    MTX.write_page(page)
    

    # customize width of the content
    MTX.sidebar_settings()

    # remove the steamlit footer and the hamburger menu in top right cornor
    MTX.hide_streamlit_style()
    # display costum footer
    MTX.custom_footer()

    #testing
    #after = dt.datetime.now()
    #st.write(after-before)
    #testing

if __name__ == "__main__":
    main()
