import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import helper
import Home_dash
import Graphs
import plotly.graph_objects as go

#data loading
stock=pd.read_csv('stock_information.csv')

#header section
st.title('TATA GROUPS PERFORMANCE DASHBOARD')
st.markdown("<hr>", unsafe_allow_html=True)

#sidebar image
image_path = "images/Tata_logo.png"
st.sidebar.image(image_path, caption="Tata Group Logo", use_container_width=True)

# Sidebar Styling
st.sidebar.header("TATA GROUPS COMPANY SELECTION")
st.sidebar.markdown('Use the dropdown to select a company or compare multiple companies.')

company_files = {
    'Tata Consultancy Services Limited': 'Tata_Consultancy_Services_Limited.csv',
    'Tata Steel Limited': 'Tata_Steel_Limited.csv',
    'Tata Motors Limited': 'Tata_Motors_Limited.csv',
    'Titan Company Limited': 'Titan_Company_Limited.csv',
    'Tata Chemicals Limited': 'Tata_Chemicals_Limited.csv',
    'The Tata Power Company Limited': 'The_Tata_Power_Company_Limited.csv',
    'The Indian Hotels Company Limited': 'The_Indian_Hotels_Company_Limited.csv',
    'Tata Consumer Products Limited': 'Tata_Consumer_Products_Limited.csv',
    'Tata Communications Limited': 'Tata_Communications_Limited.csv',
    'Voltas Limited': 'Voltas_Limited.csv',
    'Trent Limited': 'Trent_Limited.csv',
    'Tata Investment Corporation Limited': 'Tata_Investment_Corporation_Limited.csv',
    'Tata Metaliks Limited': 'Tata_Metaliks_Limited.csv',
    'Tata Elxsi Limited': 'Tata_Elxsi_Limited.csv',
    'Nelco Limited': 'Nelco_Limited.csv',
    'Tata Technologies Limited': 'Tata_Technologies_Limited.csv'
}
values=stock['Company Name'].unique().tolist()
values.insert(0,'Overall')
selected_company =  st.sidebar.selectbox("Select a Company:", values)

if  selected_company=='Overall':
    s=Home_dash.Home()



# Function to load data and generate graphs
def handle_company(selected_company):
    if selected_company in company_files:
        # Load the corresponding CSV file
        file_name = company_files[selected_company]
        data = pd.read_csv(file_name)

        # Ensure the DataFrame has required columns
        data = data.loc[:, ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
        st.title(selected_company+' Analysis')
        # Call plotting functions
        Graphs.plot_line_chart(data)
        Graphs.plot_volume_by_year(data)
        Graphs.plot_avg_daily_return(data)
    else:
        print(f"Company '{selected_company}' not found in the list.")
if  selected_company!='Overall':
    handle_company(selected_company)

#overall closing prices graphs
st.header("Tata Group Performance Comparison (All Divisions)")
def plot_multi_company_comparison(selected_companies):
    fig = go.Figure()

    for company in selected_companies:
        if company in company_files:
            # Load data for the company
            file_name = company_files[company]
            data = pd.read_csv(file_name)
            data['Date'] = pd.to_datetime(data['Date'])  # Ensure date format

            # Add a trace for the company's closing prices
            fig.add_trace(go.Scatter(
                x=data['Date'], y=data['Close'], mode='lines', name=company
            ))
        else:
            print(f"Company '{company}' not found in the dataset.")

    # Update the layout of the chart
    fig.update_layout(
        title="Historical Close Prices",
        xaxis_title="Date",
        yaxis_title="Close Price",
        template="plotly_white",
        legend_title="Companies",
        width = 2000 # Specify custom width

    )

    # Show the chart
    st.plotly_chart(fig, use_container_width=True)
st.subheader("Analyze the historical stock prices of the selected Tata Group companies.")
selected_companies = st.multiselect(
    "Select Tata Group Companies to Compare:",
    list(company_files.keys()),
    help="Choose one or more companies from the Tata Group to view their historical performance comparison."
)

st.write(
    "This graph compares the closing prices of all Tata Group companies over time. "
    "You can select specific companies above to narrow down the comparison."
)
if selected_companies:

    plot_multi_company_comparison(selected_companies)
else:

    plot_multi_company_comparison(list(company_files.keys()))





