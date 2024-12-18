import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


class Home:
    def __init__(self):
        stock = pd.read_csv('stock_information.csv')
        st.markdown('### Stock Performance & Insights of Various TATA Group Companies')
        # Tabular data
        st.header('STOCK DATA')
        st.dataframe(stock)
        st.markdown("""
                   This table displays the stock data for various companies under the Tata Group. It includes key financial 
            metrics such as **Market Capitalization**, **NSE Price**, and **BSE Price** for each company. Tata Group's 
            diverse portfolio ranges from technology and automotive to consumer products, energy, and hospitality, 
            and this dataset reflects their stock performance across different sectors.
               """)
        st.markdown("<hr>", unsafe_allow_html=True)

        # Market Capitalization Comparison
        st.header("Market Capitalization Comparison")
        companies = stock['Company Name']
        market_cap = stock['Market Cap']
        st.markdown("""
                   
                   This bar chart visualizes the **Market Capitalization** of various Tata Group companies. Market capitalization 
            represents the total market value of a company's outstanding shares, providing a measure of its size. 
            A higher market cap typically indicates a more established company with a larger market share. For example, 
            companies like **Tata Consultancy Services (TCS)** and **Tata Steel** have large market caps due to their 
            dominant positions in the IT and steel industries, respectively.
               """)
        plt.figure(figsize=(12, 8))
        plt.bar(companies, market_cap, color='skyblue')
        plt.title('Market Capitalization of Companies')
        plt.xlabel('Company Name')
        plt.ylabel('Market Cap (in million)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)
        st.markdown("<hr>", unsafe_allow_html=True)

        # PRICE TRENDS
        st.header('PRICE TRENDS')
        st.markdown("""
                    
                     This section compares the stock price trends of various Tata Group companies. Tata Group operates across 
            various industries, so their stock prices often reflect different business cycles and market conditions. 
            The **NSE (National Stock Exchange)** and **BSE (Bombay Stock Exchange)** prices represent the trading 
            value of the Tata companies on two of India's largest stock exchanges.
                """)
        op = st.selectbox('charts', options=['Bar Plot', 'Linear plot'])
        if op == 'Bar Plot':
            companies = stock['Company Name']
            nse_prices = stock['NSE Price']
            bse_prices = stock['BSE Price']

            # Plot for NSE Price Trends
            st.subheader('NSE Price Trends')
            st.markdown("""
                            This bar plot shows the **NSE price trends** for each Tata Group company. The x-axis represents the 
                names of Tata companies, while the y-axis shows their respective **NSE stock prices**. Companies like 
                **Tata Consultancy Services (TCS)** and **Tata Motors** are expected to have different price trends due to 
                their distinct business domains. For example, TCS may have a more stable price trend due to its strong 
                performance in the IT sector.
                        """)
            plt.figure(figsize=(10, 6))
            plt.bar(companies, nse_prices, color='skyblue')
            plt.title('NSE Price Trends')
            plt.xlabel('Company Name')
            plt.ylabel('NSE Price')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            st.pyplot(plt)

            # Plot for BSE Price Trends
            st.subheader('BSE Price Trends')
            st.markdown("""
                            
                            This bar chart compares the **BSE price trends** for each Tata Group company. Similar to the NSE chart, 
                this visualization helps to see how these companies are performing on the **Bombay Stock Exchange**. 
                Different exchanges may reflect slight variations in pricing based on market dynamics.
                        """)
            plt.figure(figsize=(10, 6))
            plt.bar(companies, bse_prices, color='orange')
            plt.title('BSE Price Trends')
            plt.xlabel('Company Name')
            plt.ylabel('BSE Price')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            st.pyplot(plt)
        else:
            st.subheader('Stock Price Comparison (NSE vs BSE)')
            st.markdown("""
                           
                            This line plot compares the **NSE and BSE prices** of Tata Group companies side by side. The blue line 
                represents the **NSE prices**, while the red line represents the **BSE prices**. This comparison helps 
                to understand how the same company performs across different stock exchanges, reflecting investor behavior 
                and market sentiment.
                       """)
            plt.figure(figsize=(10, 6))
            plt.plot(stock['Company Name'], stock['NSE Price'], label='NSE Price', marker='o', c='b')
            plt.plot(stock['Company Name'], stock['BSE Price'], label='BSE Price', marker='o', c='r')
            plt.title('Stock Price Comparison (NSE vs BSE)')
            plt.xlabel('Company Name')
            plt.ylabel('Price')
            plt.xticks(rotation=45, ha='right')
            plt.legend()
            plt.tight_layout()
            st.pyplot(plt)
        st.markdown("<hr>", unsafe_allow_html=True)
        # Percentage Change
        st.header('Percentage Change')
        st.write('Percentage change in NSE and BSE prices for each company')
        st.markdown("""
                    
                     This bar chart compares the **percentage change** in stock prices for **NSE** and **BSE**. The Tata Group 
            companies often experience different percentage changes due to factors such as market conditions and industry 
            performance. Companies in growth sectors like **Tata Consultancy Services** may show positive changes, while 
            companies in cyclical sectors like **Tata Steel** may exhibit more volatility.
                """)
        plt.figure(figsize=(10, 6))
        plt.barh(stock['Company Name'], stock['NSE Price %'], label='NSE Price %', color='lightblue')
        plt.barh(stock['Company Name'], stock['BSE Price %'], label='BSE Price %', color='salmon',
                 left=stock['NSE Price %'])
        plt.title('NSE vs BSE Price Change (%)')
        plt.xlabel('Percentage Change')
        plt.ylabel('Company Name')
        plt.legend()
        plt.tight_layout()
        st.pyplot(plt)
        st.markdown("<hr>", unsafe_allow_html=True)