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
