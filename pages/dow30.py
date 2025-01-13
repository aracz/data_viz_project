import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


st.title("DOW 30 Index")

st.markdown("A Dow Jones Industrial Average (DJIA), ismertebb nevén a Dow 30, egyike a világ legismertebb és legfontosabb tőzsdei indexeinek. Ez az index a 30 legnagyobb amerikai vállalat részvényeinek teljesítményét követi, és gyakran a tőzsdei piacon uralkodó gazdasági trendek és piaci hangulat mutatójaként szolgál.")
st.markdown("Az index 30 különböző céget tartalmaz, amelyek az amerikai gazdaság különböző szegmenseit képviselik, beleértve a technológiát (pl. Apple, Microsoft), az ipart (pl. Boeing, Caterpillar), a pénzügyi szektort (pl. JPMorgan Chase), az egészségügyet (pl. Johnson & Johnson, Merck) és más fontos ágazatokat.")

st.subheader("ESG score")
st.markdown("Az ESG score-k segítenek meghatározni, hogy egy vállalat milyen mértékben felelős és fenntartható működést folytat, figyelembe véve három kulcsfontosságú szempontot:")
st.markdown("**1. Környezeti (Environmental):** A vállalat környezetvédelmi hatásai, például a szén-dioxid-kibocsátás, az energiahatékonyság, a vízhasználat és az erőforrások fenntartható kezelése.")
st.markdown("**2. Társadalmi (Social):** A vállalat társadalmi felelőssége, beleértve a munkavállalói jogokat, a közösségi kapcsolatok ápolását, az emberi jogok tiszteletben tartását és az etikus beszállítói láncokat.")
st.markdown("**3. Vállalatirányítás (Governance):** A vállalat vezetése, a döntéshozatali folyamatok átláthatósága, a korrupcióellenes intézkedések és az etikai normák betartása.")
st.markdown("Az ESG score-k kiszámítása egy összetett folyamat, amely számos tényezőt vesz figyelembe, ill. gyakran különböző módszertanok és súlyozások alapján történik. A pontszám értéke 0 és 100 közötti skálán mozoghat, ahol a magasabb pontszám jobb megítélést jelent.")