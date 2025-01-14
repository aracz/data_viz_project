import streamlit as st


home = st.Page("pages/home.py", title="Bevezető", icon=":material/house:")
trends = st.Page("pages/trends.py", title="Trendek", icon=":material/stacked_line_chart:")
events = st.Page("pages/events.py", title="Események", icon=":material/globe:")
dow30 = st.Page("pages/dow30.py", title="Dow 30 Index", icon=":material/cadence:")

pg = st.navigation([home, trends, events, dow30])
st.set_page_config(page_title="Tőzsdei Adatok", page_icon=":material/edit:")
pg.run()



