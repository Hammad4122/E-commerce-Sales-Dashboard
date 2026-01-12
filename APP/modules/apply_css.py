import streamlit as st
def apply_css():
    st.markdown(
        '''<style>
            div.block-container{
                padding-top:10px;
                transition:0.5s;

            }
            #e-commerce-sales-dashboard{
                font-size:42px;
                width:100%;
                color: #2ee872;
                text-decoration:underline;
                text-underline-offset: 10px;
                text-decoration-thickness: 3px;
                text-decoration-color: #1216c7;
                font-family: sans-serif,"Times New Roman", Times, serif;
                text-align: center;
            }
            .st-key-metrics-cards{
                border: 2px solid #1216c7 !important;
                border-radius: 10px;
                padding:5px;
                padding-left: 15px;
                box-shadow: 0 5px 10px rgba(0,0,0,0.2);
                transition: 0.5s;
                # background: #f6fcf5;
            }
            .st-key-metrics-cards:hover {
                transform: translateY(-3px);
            }
            # .stColumn.st-emotion-cache-1o3yd6l.eertqu01{
            #     border: 2px solid #1216c7 !important;
            #     border-radius: 10px;
            #     padding:5px;
            #     padding-left: 15px;
            #     box-shadow: 0 5px 10px rgba(0,0,0,0.2);
            #     transition: 0.5s;
            #     # background: #f6fcf5;
            # }
            # .stColumn.st-emotion-cache-1o3yd6l.eertqu01:hover {
            #     transform: translateY(-3px);
            # }

            /* Animate whole Streamlit app on page load */
            [data-testid="stAppViewContainer"] {
                opacity: 1;
                transform: translateY(-40px);
                animation: pageDrop 0.7s ease forwards;
            }

            @keyframes pageDrop {
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            .st-key-side-by-side-chart{
                height:210px;
                font-weight: bold;
            }
            .stSelectbox{
                position: relative;
                bottom: 40px;
                width: 550px;
            }
            .st-key-TOP3CUSTOMERS{
                position: relative;
                bottom: 245px;
                width: 550px;
                border: 2px solid cyan;
            }
            .st-key-Monthly_Sales_Graph{
                position: relative;
                bottom: 140px;
            }
            .st-key-multiselect{
                position: relative;
                bottom: 160px;
            }
            .st-key-CompareMonths{
                position: relative;
                bottom: 160px;
            }
            .st-key-top10BestSellingProducts{
                position: relative;
                bottom: 50px;
            }

        </style>''',unsafe_allow_html=True)