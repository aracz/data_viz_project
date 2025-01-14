import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from data import get_stock_data


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


st.title("Események")

st.markdown("A tőzsdei árfolyamok mozgása közvetlenül vagy közvetve reagálhat a piacon kívüli eseményekre. A piaci reakciók megértése és vizualizálása kulcsfontosságú lehet a befektetők és elemzők számára, hogy felismerjék a piaci trendeket és segithet a kockázatok kezelésében.")

# Deepwater Horizon: 20 April 2010
st.subheader("Deepwater Horizon - olajkatasztrófa")
st.markdown("A Deepwater Horizon katasztrófa 2010. április 20-án következett be a Mexikói-öbölben, amikor a BP olajfúrótornya felrobbant, és hatalmas olajszivárgás indult el a tengerfenéken. A katasztrófa hatalmas környezeti károkat okozott: a szennyezés súlyosan érintette a tengeri élővilágot, a part menti ökoszisztémákat és a halászati ipart.")
st.markdown("A fúrótórony a Transocean tulajdonában állt és a BP számára végzett olajkitermelést. A katasztrófa és annak következményei jelentős hatással voltak az olajipari cégek, különösen a Transocean és a BP tőzsdei árfolyamaira. ")
st.write(event_graph(["BP", "RIG", "XOM", "SHEL"], "2010-01-01", "2012-12-31",
        event_dates=["2010-04-20"], title="Deepwater Horizon és érintett cégek"))

# Covid: March 2020 + Ukraine war started: 24 Feb 2022
st.subheader("2020-as évek eleje: Covid és Ukrán háború")
st.markdown("A tőzsdei indexek alakulása fontos mutatója a globális gazdaság és a pénzügyi piacok hangulatának. Az elmúlt években a COVID világjárvány és az ahhoz kapcsolódó lezárások, valamint az ukrajnai háború kirobbanása olyan kulcsfontosságú események, amelyek jelentős hatással voltak a tőzsdék és így az indexek mozgására.")
st.write(event_graph(["^DJI", "^GSPC", "^IXIC", "^GDAXI"], "2019-01-01", "2023-12-31",
        event_dates=["2020-03-11", "2022-02-24"], title="Tőzsdei indexek alakulása 2020 évek elején"))

# AI Boom: 2023 - NVIDIA, OpenAI, Microsoft stock prices
st.subheader("AI boom")
st.markdown("Az AI boom az utóbbi években új üzleti lehetőségeket teremtett a technológiai szektorban, kiemelkedő szereplőkké téve a Microsoftot és az NVIDIA-t. Az ábránk jól tükrözi az AI térnyerésének gazdasági hatásait és a technológiai szektor iránti növekvő befektetői érdeklődést.")
st.write(event_graph(["MSFT", "NVDA"], "2022-01-01", "2024-12-31", title="AI cégek részvényárfolyamának alakulása"))