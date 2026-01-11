import pandas as pd
import streamlit as st
from modules.choropleth_world_map import plot_choropleth_world_map
from modules.kpi import KPI
from modules.visualization import plot
from modules.apply_css import apply_css

def runAPP():
    st.set_page_config(
        layout="wide"
    )
    apply_css()
    st.title("🛍️ E-commerce Sales Dashboard")
    KPI()
    st.divider()
    plot_choropleth_world_map()
    st.divider()
    plot()