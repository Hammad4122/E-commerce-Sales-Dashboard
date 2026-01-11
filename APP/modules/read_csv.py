import pandas as pd
import streamlit as st

def read_csv():
    df = pd.read_csv(r"C:\Coding\Coding_Journey\Python Journey\Data_Visualization_Projects\E-commerce_Sales_Dashboard\Dataset\Sales_Data.csv",encoding="ISO-8859-1")
    return df