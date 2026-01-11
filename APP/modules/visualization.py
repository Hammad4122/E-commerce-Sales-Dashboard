#-----Importing Modules-----
import pandas as pd
import streamlit as st
from modules.read_csv import read_csv

#-----Collecting Data-----
df = read_csv()
#-----Analysing Data for Visualization-----

#-----Grouping Year by Revenue.sum()-----
grouped_Year_by_Revenue = df.groupby("Year")["Revenue"].sum().reset_index("Year")

#-----Top 10 countries by revenue-----
top10_countries_by_revenue = df.groupby("Country")["Revenue"].sum().reset_index().nlargest(10,"Revenue")
top10_countries_by_sum= df.groupby("Country")["Revenue"].sum().reset_index().nlargest(5,"Revenue")

#-----Customer Spending Comparison-----
top3_customers = df.groupby("CustomerID")["Revenue"].sum().reset_index().nlargest(3,"Revenue")

#-----Top 10 Products-----
top10_products_by_revenue = df.groupby("Description")["Revenue"].sum().reset_index().nlargest(10,"Revenue")

def plot():
    #-----Total Revenue in 2010 and 2011 and Sales in each country with st.column(2)-----
    col1,col2 = st.columns(2)
    with col1:
        st.text("Revenue Generated in 2010 and 2011")
        st.bar_chart(
            data=grouped_Year_by_Revenue,
            x = "Year",
            y="Revenue",
            x_label="Total Revenue",
            y_label="Year",
            use_container_width=True,
            color="#f6ec61f0",
            horizontal=True,
            height=155
            )
    with col2:
        st.text("Top 10 countries by revenue")
        st.bar_chart(
            data = top10_countries_by_revenue,
            x = "Country",
            y = "Revenue",
            x_label = "Country",
            y_label = "Revenue",
            use_container_width=True,
            color = "#6555fae9"
        )
    with st.container(key = "TOP3CUSTOMERS"):
        st.write("Top 3 Customers")
        st.bar_chart(
            data=top3_customers,
            x = "CustomerID",
            y = "Revenue",
            x_label = "Total Spend",
            y_label = "CustomerID",
            color = "#9F10FFDD",
            horizontal = True,
            height=165
        )
    
    with st.container(key = "top10BestSellingProducts"):
        st.header("Top 10 Best Selling Products")
        st.bar_chart(
            data = top10_products_by_revenue,
            x = "Description",
            y = "Revenue",
            x_label = "Description",
            y_label = "Revenue",
            color = "#1B31F3CF",
            use_container_width = True,
            height = 500
        )

    select_year_col1,select_month_col2 = st.columns(2)
    select_year = select_year_col1.selectbox(
        "Select Year",
        ["2010", "2011"],
        placeholder="Select Year",
        index=None,
        help="Choose a month from the selected year to view detailed monthly sales. The chart will display daily revenue or total sales for that month."
    )

    if select_year:
        select_year = int(select_year)

        if select_year == 2010:
            months = ["December"]
        elif select_year == 2011:
            months = [
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ]

        select_month = select_month_col2.selectbox(
            "Select Month",
            months,
            placeholder="Select Month",
            index=None
        )

        if select_month:
            filtered_df = df[
                (df["Year"] == select_year) &
                (df["Months"] == select_month)
            ]

            grouped_monthly_revenue = (
                filtered_df
                .groupby(filtered_df["InvoiceDate"])["Revenue"]
                .sum()
                .reset_index()
            )
            grouped_monthly_revenue.columns = ["Day", "Revenue"]

            with st.container(key = "Monthly_Sales_Graph"):
                st.header("Monthly Sales")
                st.write(f"Sales in {select_month}: {filtered_df['Revenue'].sum():.1f}$")
                st.line_chart(
                    grouped_monthly_revenue.set_index("Day"),
                    x_label="Date",
                    y_label="Sales",
                    use_container_width=True,
                    color="#3c00ff"
                    )
            with st.container(key = "multiselect"):
                selected_multiple_months = st.multiselect(
                    label="Compare multiple months' sales",
                    options=months,
                    placeholder="Select multiple months",
                    help = "Select one or more months to compare their sales side by side. The bar chart will display revenue for each selected month, aligned by day, even if some days are missing in certain months."
                )
            # --- Prepare pivoted data for bar chart ---
            df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
            df['Day'] = df["InvoiceDate"].dt.day
            # Filter data by selected year
            df_year = df[df['Year'] == int(select_year)]
            if selected_multiple_months:
                # Filter selected months
                filtered = df_year[df_year['Months'].isin(selected_multiple_months)]
                
                # Aggregate revenue by Day and Month
                monthly_day_revenue = filtered.groupby(['Months', 'Day'])['Revenue'].sum().reset_index()
                
                # Pivot so each month is a separate column
                pivot = monthly_day_revenue.pivot(index='Day', columns='Months', values='Revenue').fillna(0)
                
                # Sort days
                pivot = pivot.sort_index()
                with st.container(key = "CompareMonths"):
                    # --- Display bar chart ---
                    st.bar_chart(
                        pivot,
                        x_label="Day",
                        y_label="Sales",
                        use_container_width=True,
                        )
