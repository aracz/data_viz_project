import streamlit as st
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
# Ukraine war started: 24 Feb 2022
# Covid: March 2020
# AI Boom: 2023 - NVIDIA, OpenAI, Microsoft stock prices
