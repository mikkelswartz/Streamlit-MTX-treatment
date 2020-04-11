import streamlit as st
import math
import pandas as pd

import awesome_streamlit as ast

from basics import * 
import pages.Startside
import pages.Forhydering
import pages.MTX_infusion
import pages.Monitorering_af_toksicitet

ast.core.services.other.set_logging_format()

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

    with st.spinner(f"Loading {page_selection} ..."):
        ast.shared.components.write_page(page)


if __name__ == "__main__":
    main()
