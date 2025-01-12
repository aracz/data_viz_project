import streamlit as st
from data import get_stock_data


def data_prep():
    stock_data = get_stock_data.GetStockData(symbol='AAPL', period='1y').get_stock_data_period()
    print(stock_data)
    return stock_data


data = data_prep()

st.title("Trendek")
st.write("Teszt adatmegjelnites")
st.write(data)

# Index vs underlying companies values
# eg. Dow 30 companies vs the dow 30 index

# Price trends in 1 sector

dow_30_symbols = [
    "MMM",  # 3M Company
    "AXP",  # American Express
    "AMGN", # Amgen
    "AAPL", # Apple Inc.
    "BA",   # Boeing
    "CAT",  # Caterpillar Inc.
    "CVX",  # Chevron
    "CSCO", # Cisco Systems
    "KO",   # Coca-Cola Company
    "DIS",  # Disney (The Walt Disney Company)
    "DOW",  # Dow Inc.
    "GS",   # Goldman Sachs
    "HD",   # Home Depot
    "HON",  # Honeywell International
    "IBM",  # IBM
    "INTC", # Intel Corporation
    "JNJ",  # Johnson & Johnson
    "JPM",  # JPMorgan Chase & Co.
    "MCD",  # McDonald's
    "MRK",  # Merck & Co.
    "MSFT", # Microsoft
    "NKE",  # Nike
    "PFE",  # Pfizer
    "PG",   # Procter & Gamble
    "RTX",  # Raytheon Technologies
    "CRM",  # Salesforce
    "TRV",  # The Travelers Companies
    "UNH",  # UnitedHealth Group
    "VZ",   # Verizon Communications
    "V"     # Visa Inc.
]
