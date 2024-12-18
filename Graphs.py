import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go



def plot_line_chart(data):

    st.header('Historical Close Prices')
    st.markdown("""
        **Purpose**: This visualization shows the historical trend of the stock's closing prices over time.
        \n**Description**: The line chart illustrates how the closing prices of a Tata Group company’s stock have fluctuated over time. This can help identify trends, peaks, and drops in the stock's price.
        \n**Insights**: Investors can assess long-term performance, volatility, and growth patterns.
        """)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], mode='lines', name='Close Price'))
    fig.update_layout(
        title="Historical Close Price",
        xaxis_title="Date",
        yaxis_title="Price (Close)",
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("<hr>", unsafe_allow_html=True)


def plot_volume_by_year(data):
    """
    Plots the volume trends for TCS, aggregated by year using a bar chart.

    Parameters:
    - data: DataFrame with 'Date' and 'Volume' columns for TCS.
    """
    st.header('Trading Volume by Year')
    st.markdown("""
        **Purpose**: This chart displays the total trading volume for each year, aggregating daily trading volumes.
        \n**Description**: The bar chart helps visualize how much the stock has been traded in a given year. Higher volumes may indicate increased interest or significant market events.
        \n**Insights**: A higher trading volume could signify greater market activity, investor interest, or reactions to company news.
        """)
    # Ensure 'Date' is in datetime format
    data['Date'] = pd.to_datetime(data['Date'])

    # Extract the year from the 'Date' column
    data['Year'] = data['Date'].dt.year

    # Aggregate the data by year, summing the volume for each year
    annual_volume = data.groupby('Year')['Volume'].sum()

    # Create a bar chart to visualize the aggregated volume by year
    plt.figure(figsize=(15, 8))
    plt.bar(annual_volume.index, annual_volume.values, color='skyblue', alpha=0.7)

    # Add labels and title
    plt.ylabel('Total Volume', fontsize=20)
    plt.xlabel('Year', fontsize=20)
    plt.title('Trading Volume by Year', fontsize=14)

    # Show grid and layout adjustments
    plt.grid(visible=True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    st.pyplot(plt)
    st.markdown("<hr>", unsafe_allow_html=True)




def plot_avg_daily_return(data):
    """
    Calculates and plots the average daily return of the stock year-wise.

    Parameters:
    - data: DataFrame with 'Date' and 'Close' columns for the stock.
    """
    st.header('Average daily return')
    st.markdown("""
        **Purpose**: This chart calculates and visualizes the average daily return of a Tata Group company’s stock on a year-by-year basis.
        \n**Description**: The average daily return measures how much the stock has changed on average each day during the year, as a percentage of the closing price.
        \n**Insights**: Investors can assess the stock's risk and potential profitability by analyzing the average return over different years.
        """)
    # Ensure 'Date' is in datetime format
    data['Date'] = pd.to_datetime(data['Date'])

    # Calculate daily return
    data['Daily_Return'] = data['Close'].pct_change()  # pct_change computes (Close_t - Close_t-1) / Close_t-1

    # Extract year from the 'Date' column
    data['Year'] = data['Date'].dt.year

    # Group by year and compute the average daily return
    avg_daily_return = data.groupby('Year')['Daily_Return'].mean()

    # Plot the average daily return year-wise
    plt.figure(figsize=(15, 6))
    plt.bar(avg_daily_return.index, avg_daily_return.values, color='skyblue')

    # Add labels and title
    plt.ylabel('Average Daily Return', fontsize=12)
    plt.xlabel('Year', fontsize=12)
    plt.title('Average Daily Return of this company Stock (Year-Wise)', fontsize=14)

    # Show grid and layout adjustments
    plt.grid(visible=True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    st.pyplot(plt)
    st.markdown("<hr>", unsafe_allow_html=True)



