import streamlit as st
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

from data import get_stock_data

dow_30_symbols = [
    "MMM",  # 3M Company
    "AXP",  # American Express
    "AMGN",  # Amgen
    "AAPL",  # Apple Inc.
    "BA",  # Boeing
    "CAT",  # Caterpillar Inc.
    "CVX",  # Chevron
    "CSCO",  # Cisco Systems
    "KO",  # Coca-Cola Company
    "DIS",  # Disney (The Walt Disney Company)
    "DOW",  # Dow Inc.
    "GS",  # Goldman Sachs
    "HD",  # Home Depot
    "HON",  # Honeywell International
    "IBM",  # IBM
    "INTC",  # Intel Corporation
    "JNJ",  # Johnson & Johnson
    "JPM",  # JPMorgan Chase & Co.
    "MCD",  # McDonald's
    "MRK",  # Merck & Co.
    "MSFT",  # Microsoft
    "NKE",  # Nike
    "PFE",  # Pfizer
    "PG",  # Procter & Gamble
    "RTX",  # Raytheon Technologies
    "CRM",  # Salesforce
    "TRV",  # The Travelers Companies
    "UNH",  # UnitedHealth Group
    "VZ",  # Verizon Communications
    "V"  # Visa Inc.
]


def get_dow30(period="1y"):
    dow30 = []
    for symbol in dow_30_symbols:
        stock = get_stock_data.GetStockData(symbol, period=period)
        df = stock.get_stock_data_period()
        df["yy-mm"] = pd.to_datetime(df.index.strftime('%Y-%m'))
        df["symbol"] = symbol
        df["Sector"] = stock.get_stock_info("sector")
        df["Volatility"] = 200 * (df["High"] - df["Low"]) / (df["High"] + df["Low"])
        dow30.append(df)
    dow30 = pd.concat(dow30)
    return dow30


def get_monthly_volatility(df):
    monthly = df.groupby(["yy-mm", "Sector"])
    monthly_vol = (200 * (monthly.max("High")["High"] - monthly.min("Low")["Low"])
                   / (monthly.max("High")["High"] + monthly.min("Low")["Low"])).reset_index()
    return monthly_vol


def hilo_and_divs(df, name=None):
    hl = df[["High", "Low"]].reset_index().melt(id_vars="Date")
    divs = df[["Stock Splits", "Dividends"]].reset_index().melt(id_vars="Date")
    divs = divs[divs["value"] != 0.0]
    divs["y"] = hl.min()["value"]
    hl["Name"] = name
    divs["Name"] = name
    return hl, divs


def draw_hilo_divs(symbol):
    stock = get_stock_data.GetStockData(symbol, period="1y")
    sname = stock.get_stock_info("shortName")
    hilo, divs = hilo_and_divs(stock.get_stock_data_period(), name=sname)
    fig = plt.figure(figsize=(10, 6))
    sb.lineplot(data=hilo, x="Date", y="value", hue="variable")
    sb.scatterplot(data=divs, x="Date", y="y", hue="variable", size="value")
    plt.title(f"{sname} ({symbol}) árfolyam és osztalék")
    plt.xticks(rotation=45)
    plt.ylabel("Érték (USD)")
    plt.xlabel("Dátum")
    return fig


def candlesticks(symbol):
    stock = get_stock_data.GetStockData(symbol, period="3mo")
    sname = stock.get_stock_info("shortName")
    df = stock.get_stock_data_period()
    up = df[df["Close"] > df["Open"]]
    down = df[df["Close"] <= df["Open"]]
    fig = plt.figure()
    #candles
    plt.bar(up.index, up.High - up.Low, width=0.1, bottom=up.Low, color="green")
    plt.bar(up.index, up.Close - up.Open, bottom=up.Open, color="green")
    plt.bar(down.index, down.High - down.Low, width=0.1, bottom=down.Low, color="red")
    plt.bar(down.index, down.Open - down.Close, bottom=down.Close, color="red")
    #volumes
    min_price = df["Low"].min()
    min_vol = df["Volume"].min()
    max_vol = df["Volume"].max()
    scale = 0.2 * (df["High"].max() - min_price) / (max_vol - min_vol)
    plt.bar(df.index, scale * df["Volume"], bottom=min_price - scale * (max_vol - min_vol) / 2, color="blue", alpha=0.3)
    plt.title(f"{sname} ({symbol}) gyertyaábrája az elmúlt 3 hónapban")
    plt.xticks(rotation=45)
    plt.ylabel("Érték (USD)")
    plt.xlabel("Dátum")
    return fig


st.title("Trendek")
st.markdown("A tőzsdei trendek vizualizálása kulcsfontosságú eszközként szolgál a befektetők és elemzők számára a pénzügyi piacok megértésében. A piacok ármozgásainak nyomon követése és elemzése segíti a megalapozott döntéshozatalt, a fontos trendeket azonosítását és a jövőbeli ármozgások előrejelzését.")
st.markdown("Ezen az oldalon az árfolyamok alakulásának különböző megjelenítései találhatóak különös tekintettel a Dow 30 Index cégeinek adataira.")

# Dividends vs stock price
st.subheader("Nagy tech cégek részvényárfolyamának alakulása és osztalékai")
st.write(draw_hilo_divs("IBM"))
st.write(candlesticks("MSFT"))

# Dow 30 companies by sector
st.subheader("A Dow 30 cégek szektorai")

st.markdown("A Dow Jones Industrial Average (DJIA), ismertebb nevén a Dow 30, egyike a világ legismertebb és legfontosabb tőzsdei indexeinek. Ez az index a 30 legnagyobb amerikai vállalat részvényeinek teljesítményét követi, és gyakran a tőzsdei piacon uralkodó gazdasági trendek és piaci hangulat mutatójaként szolgál.")
st.markdown("Az index 30 különböző céget tartalmaz, amelyek az amerikai gazdaság különböző szegmenseit képviselik, beleértve a technológiát (pl. Apple, Microsoft), az ipart (pl. Boeing, Caterpillar), a pénzügyi szektort (pl. JPMorgan Chase), az egészségügyet (pl. Johnson & Johnson, Merck) és más fontos ágazatokat.")
st.markdown("Az alábbi ábrákon a részvényárfolyamok és a volatilitás szektoronkénti trendjeinek megjelenítését helyeztük a középpontba.")

dow30_10y = get_dow30(period="10y")

fig = plt.figure()
sb.lineplot(data=dow30_10y, x="yy-mm", y="Close", hue="Sector", errorbar=None)
plt.title(f"Dow 30 cégek részvényárfolyamának alakulása szektoronként")
plt.ylabel("Érték (USD)")
plt.xlabel("Dátum")
st.write(fig)

# Volatility of stocks in some sectors of dow 30
secs = ["Industrials", "Financial Services", "Technology"]
fig = plt.figure()
sb.lineplot(data=dow30_10y[dow30_10y["Sector"].isin(secs)].groupby(["yy-mm", "Sector"]).mean(numeric_only=True),
            x="yy-mm", y="Volatility", errorbar=None, hue="Sector")
plt.title(f"Dow 30 cégek napi volatilitása szektoronként")
plt.ylabel("Volatilitás százalékban")
plt.xlabel("Dátum")
st.write(fig)

monthly_vol = get_monthly_volatility(dow30_10y)
fig = plt.figure()
sb.lineplot(data=monthly_vol[monthly_vol["Sector"].isin(secs)], x="yy-mm", y=0, errorbar=None, hue="Sector")
plt.title(f"Dow 30 cégek havi volatilitása szektoronként")
plt.ylabel("Volatilitás százalékban")
plt.xlabel("Dátum")
st.write(fig)
