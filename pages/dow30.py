import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from data import get_stock_data


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
def get_dow30_data():
    dow30 = []
    for symbol in dow_30_symbols:
        stock = get_stock_data.GetStockData(symbol, period="1y")
        dow30.append({
            "Symbol": symbol,
            "Name": stock.get_stock_info("shortName"),
            "Sector": stock.get_stock_info("sector"),
            "Debt": stock.get_stock_info("totalDebt"),
            "environmentScore": stock.get_sustainability("environmentScore"),
            "governanceScore": stock.get_sustainability("governanceScore"),
            "socialScore": stock.get_sustainability("socialScore"),
            "totalEsg": stock.get_sustainability("totalEsg")
        })
    return pd.DataFrame.from_dict(dow30)

def get_holders():
    holders = []
    for symbol in dow_30_symbols:
        stock = get_stock_data.GetStockData(symbol, period="1y")
        df = stock.get_holders()
        df["symbol"] = symbol
        holders.append(df)
    return pd.concat(holders)
 
st.title("DOW 30 Index")
dow30 = get_dow30_data()
st.write(dow30)

fig = plt.figure()
dow30.value_counts("Sector").plot(kind="pie")
plt.ylabel("")
plt.title("A DOW 30 index szektorainak eloszlása")
st.write(fig)

st.subheader("Fenntarthatóság")
fig, ax = plt.subplots()
dow30[["Sector", "environmentScore", "governanceScore", "socialScore"]].groupby("Sector").mean(numeric_only=True).plot(kind="barh", stacked=True, ax=ax)
plt.title("A DOW 30 index szektorainak ESG pontszámai")
st.write(fig)
fig, ax = plt.subplots(figsize=(10, 12))
dow30[["Name", "environmentScore", "governanceScore", "socialScore"]].groupby("Name").mean(numeric_only=True).plot(kind="barh", stacked=True, ax=ax)
plt.title("A DOW 30 index cégeinek ESG pontszámai")
st.write(fig)

st.subheader("Intézményi tulajdonosok")
holders = get_holders()
fig = plt.figure()
holders.groupby("Holder").sum("Value")["Value"].sort_values().head(10).plot(kind="barh")
plt.xlabel("Billió USD")
plt.ylabel("Tulajdonos")
plt.title("A DOW 30 index legnagyobb intézményi tulajdonosai")
st.write(fig)

st.subheader("Adósságok")
fig = plt.figure()
sb.barplot(data=dow30, x="Debt", y="Sector", orient="h", errorbar=None)
plt.xlabel("Adósság (USD)")
plt.ylabel("Szektor")
st.write(fig)