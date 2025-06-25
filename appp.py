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

if selected == "🏠 Chatbot":
    import HomeChatbotPage
    HomeChatbotPage.render()
elif selected == "🧾 Farmer Credit Profile":
    import farm_profile
    farm_profile.render()
elif selected == "📊 Lender Dashboard":
    import lender_dashboard
    lender_dashboard.render()
elif selected == "📈 Insights & Feature Analysis":
    import insights_feature_analysis
    insights_feature_analysis.render()

st.markdown("---")
st.markdown("<div style='text-align: center;'>📌 Made with ❤️ by <strong>Team Numerixa</strong></div>", unsafe_allow_html=True)
