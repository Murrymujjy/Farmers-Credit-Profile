import streamlit as st
from streamlit_option_menu import option_menu

# Set page config
st.set_page_config(page_title="Numerixa Credit App", layout="wide")

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        "Numerixa AI Dashboard",
        ["🏠 Chatbot", "🧾 Farmer Credit Profile", "📊 Lender Dashboard", "📈 Insights & Feature Analysis"],
        icons=["robot", "person-check", "bar-chart", "graph-up"],
        menu_icon="cast",
        default_index=0,
    )

# Load each page
if selected == "🏠 Chatbot":
    import HomeChatbotPage  # chatbot.py
elif selected == "🧾 Farmer Credit Profile":
    import farm_profile  # farm_profile.py
elif selected == "📊 Lender Dashboard":
    import lender_dashboard  # lender_dashboard.py
elif selected == "📈 Insights & Feature Analysis":
    import _InsightsFeatureAnalysis  # insights_analysis.py


st.markdown("---")
st.markdown("<div style='text-align: center;'>📌 Made with ❤️ by <strong>Team Numerixa</strong></div>", unsafe_allow_html=True)
