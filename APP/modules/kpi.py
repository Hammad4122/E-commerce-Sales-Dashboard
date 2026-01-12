#-----Importing modules-----
import pandas as pd
import streamlit as st
from modules.read_csv import read_csv

def KPI():
    try:
        #-----Collecting Data-----
        df = read_csv()
        #-----Calculating Metrics-----
        #-----Calculating Total Revenue-----
        total_revenue = str(round((df["Revenue"].sum())/1000000,2))
        #-----Best Selling Product-----
        grouped_description_revenue_sum = df.groupby("Description")["Revenue"].sum().reset_index("Description")
        best_selling_product = str(grouped_description_revenue_sum.loc[grouped_description_revenue_sum["Revenue"].idxmax(),"Description"]).capitalize()
        #-----Country with Highest Sales-----
        grouped_country_by_revenue_sum = df.groupby("Country")["Revenue"].sum().reset_index("Country")
        Country_with_Highest_Sales = str(grouped_country_by_revenue_sum.loc[grouped_country_by_revenue_sum["Revenue"].idxmax(),"Country"])

        #-----Average revenue per customer-----
        average_revenue_per_customer = str(round(df["Revenue"].sum()/df["InvoiceNo"].nunique(),2))
        #-----Repeat Purchase Rate-----
        repeat_purchase_rate = str(round((df.groupby("CustomerID")["InvoiceNo"].nunique() > 1).sum() / df["CustomerID"].nunique() * 100,2))
        st.title("Metrics")
        st.markdown('''
            <style>
                    #metrics{
                        padding-bottom:0px;
                        font-size: 35px;
                    }
            </style>
        ''',unsafe_allow_html=True)
        #-----KPI-----
        with st.container(key = "metrics-cards"):
            col1,col2,col3 = st.columns(3)
            col1.metric("Total Revenue",total_revenue + " million$",border=False,help="Total company revenue generated across all sales, expressed in millions (Revenue ÷ 1,000,000).")
            col2.metric("Country with Highest Sales",Country_with_Highest_Sales,border=False,help="The country that generated the highest total revenue from sales.")
            col3.metric("Average Revenue Per Customer",average_revenue_per_customer + "$",border = False,help="Total revenue divided by the number of unique customers, representing the average spending contribution per customer.")

            col4,col5 = st.columns([2,1])
            col4.metric("Best Selling Product", best_selling_product,border=False,width="stretch",help="The product with the highest revenue contribution based on total sales.")
            col5.metric("Repeat Purchase Rate", repeat_purchase_rate + "%", border=False,help="The percentage of customers who have made more than one purchase, indicating customer loyalty and repeat business.")
    except:
        st.error("Couldn't load data. Try refreshing the page.")