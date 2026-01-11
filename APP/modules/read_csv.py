import pandas as pd
import streamlit as st

def read_csv():
    df = pd.read_csv("Dataset\Sales_Data.csv",encoding="ISO-8859-1")
    return df