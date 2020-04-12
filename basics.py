import streamlit as st
import pandas as pd

# Pandas. Destination of ecxel dataark
Destination_main_file = "MTX-dataark.xlsx"
df = pd.read_excel(Destination_main_file, na_filter=False)
# Remove "Unnamed: 0" collums from dataframe
df.drop(['Unnamed: 0'], axis=1, inplace=True)

# Pandas dataframe witch value equals the row in the dataframe witch represent the treatment
Destination_st_file = "df_selected_treatment.xlsx"
df_st = pd.read_excel(Destination_st_file)

def write_page(page):  # pylint: disable=redefined-outer-name
    """Writes the specified page/module
    Our multipage app is structured into sub-files with a `def write()` function
    Arguments:
        page {module} -- A module with a 'def write():' function
    """
    # _reload_module(page)
    page.write()


