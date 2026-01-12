import os
import pandas as pd
import streamlit as st

def read_csv():
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        csv_path = os.path.join(base_dir, "Dataset", "Sales_Data.csv")
        return pd.read_csv(csv_path)
    except :
        st.error("Couldn't load the data. Try refreshing the page.")
