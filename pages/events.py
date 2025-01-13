import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from data import get_stock_data


def data_prep():
    stock_data = get_stock_data.GetStockData(symbol='GE', period='1y').get_stock_data_period()
    print(stock_data)
    return stock_data

def event_graph(symbols, start_date, end_date, event_dates=None, title=""):
    data = []
    for s in symbols:
        stock = get_stock_data.GetStockData(symbol=s, start_date=start_date, end_date=end_date)
        df = stock.get_stock_data_between_dates()
        df["Name"] = stock.get_stock_info("shortName")
        data.append(df)
    df = pd.concat(data)
    fig = plt.figure()
    sb.lineplot(data=df.reset_index(), x="Date", y="Close", hue="Name")
    min_close = df["Close"].min()
    max_close = df["Close"].max()
    if event_dates is not None:
        for e in event_dates:
            date = pd.to_datetime(e)
            plt.plot([date, date], [min_close, max_close], color='black', linestyle='--')
    plt.xticks(rotation=45)
    plt.ylabel("Záróár (USD)")
    plt.xlabel("Dátum")
    plt.title(title)
    return fig

data = data_prep()

st.title("Események")
st.write("Teszt adatmegjelnites")
st.write(data)

# Deepwater Horizon: 20 April 2010
st.subheader("Deepwater Horizon - olajkatasztrófa")
st.write(event_graph(["BP", "RIG", "XOM", "SHEL"], "2010-01-01", "2012-12-31",
        event_dates=["2010-04-20"], title="Deepwater Horizon és érintett cégek"))

# Covid: March 2020 + Ukraine war started: 24 Feb 2022
st.subheader("2020-as évek eleje: Covid és Ukrán háború")
st.write(event_graph(["^DJI", "^GSPC", "^IXIC", "^GDAXI"], "2019-01-01", "2023-12-31",
        event_dates=["2020-03-11", "2022-02-24"], title="Tőzsdei indexek alakulása 2020 évek elején"))

# AI Boom: 2023 - NVIDIA, OpenAI, Microsoft stock prices
st.subheader("AI boom")
st.write(event_graph(["MSFT", "NVDA"], "2022-01-01", "2024-12-31", title="AI cégek részvényárfolyamának alakulása"))