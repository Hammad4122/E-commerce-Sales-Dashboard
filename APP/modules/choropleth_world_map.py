#---------Importing Modules---------
import pandas as pd
import streamlit as st
import plotly.express as px
from modules.read_csv import read_csv


def plot_choropleth_world_map():
    #---------Collecting Data----------
    data = read_csv()
    #-----Grouping Countries by Revenue-----
    grouped_COUNTRY_BY_REVENUE = data.groupby('Country')['Revenue'].sum().reset_index('Country')

    #---------Plotting World Map-------
    '''Choropleth map: highlights countries by revenue (darker = higher revenue)'''
    fig = px.choropleth(
        grouped_COUNTRY_BY_REVENUE,
        locations='Country',
        locationmode='country names',
        color='Revenue',
        color_continuous_scale='cividis',
        title="Global Revenue Distribution from Sales"
    )
    fig.update_layout(
    title="<span style='font-size:20px;'>Global Revenue Distribution from Sales</span>"
    )
    st.plotly_chart(fig,use_container_width=True)

