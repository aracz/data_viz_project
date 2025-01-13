import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from data import get_stock_data


def data_prep():
    stock_data = get_stock_data.GetStockData(symbol='GE', period='1y').get_stock_data_period()
    print(stock_data)
    return stock_data


data = data_prep()

st.title("Események")
st.write("Teszt adatmegjelnites")
st.write(data)

# Deepwater Horizon: 20 April 2010
bp = get_stock_data.GetStockData(symbol='BP', start_date="2010-01-01", end_date="2012-12-31").get_stock_data_between_dates()
bp["Name"] = "British Petrolum"
tr = get_stock_data.GetStockData(symbol='RIG', start_date="2010-01-01", end_date="2012-12-31").get_stock_data_between_dates()
tr["Name"] = "Transocean"
xom = get_stock_data.GetStockData(symbol='XOM', start_date="2010-01-01", end_date="2012-12-31").get_stock_data_between_dates()
xom["Name"] = "Exxon Mobil Corp"
shell = get_stock_data.GetStockData(symbol='SHEL', start_date="2010-01-01", end_date="2012-12-31").get_stock_data_between_dates()
shell["Name"] = "Shell"
deepwter = pd.concat([bp, tr, xom, shell])
fig = plt.figure()
sb.lineplot(data=deepwter.reset_index(), x="Date", y="Close", hue="Name")
plt.plot([pd.to_datetime("2010-04-20"), pd.to_datetime("2010-04-20")], [0, 100], color='black', linestyle='--')
st.write(fig)

# Ukraine war started: 24 Feb 2022
# Covid: March 2020

# AI Boom: 2023 - NVIDIA, OpenAI, Microsoft stock prices
nvdia = get_stock_data.GetStockData(symbol='NVDA', start_date="2022-01-01", end_date="2024-12-31").get_stock_data_between_dates()
nvdia["Name"] = "NVIDIA"
msft = get_stock_data.GetStockData(symbol='MSFT', start_date="2022-01-01", end_date="2024-12-31").get_stock_data_between_dates()
msft["Name"] = "Microsoft"
ai_boom = pd.concat([nvdia, msft])
fig = plt.figure()
sb.lineplot(data=ai_boom.reset_index(), x="Date", y="Close", hue="Name")
st.write(fig)