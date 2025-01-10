import streamlit as st

from pages.events import events_page
from pages.trends import trends_page


class StreamlitApp:
    def __init__(self):
        """Initialize the Streamlit app."""
        st.set_page_config(page_title="Áttekintés", layout="wide")
        self.pages = {
            "Trends": events_page,
            "Events": trends_page
        }

    def run(self):
        """Run the Streamlit app."""
        st.sidebar.title("Menu")
        page = st.sidebar.selectbox("Select a page:", list(self.pages.keys()))
        return self.pages[page]


if __name__ == "__main__":
    app = StreamlitApp()
    app.run()
