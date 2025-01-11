import streamlit as st


home = st.Page("pages/home.py", title="Bevezető", icon=":material/house:")
trends = st.Page("pages/trends.py", title="Trendek", icon=":material/stacked_line_chart:")
events = st.Page("pages/events.py", title="Események", icon=":material/globe:")

pg = st.navigation([home, trends, events])
st.set_page_config(page_title="Tőzsdei Adatok", page_icon=":material/edit:")
pg.run()



