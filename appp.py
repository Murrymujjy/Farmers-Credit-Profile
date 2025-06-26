import streamlit as st
from streamlit_option_menu import option_menu
import HomeChatbotPage
import farm_profile
import lender_dashboard
import insights_feature_analysis as insights

# ---- Background + Button Styling ----
def set_bg_animation():
    st.markdown("""
    <style>
    .main {
        background-color: #e6f0ff;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        color: white;
        background-color: #1f77b4;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

set_bg_animation()

# ---- Sidebar Navigation ----
with st.sidebar:
    selected = option_menu(
        "Navigation", 
        ["🏠 Home", "🤖 Chatbot", "📋 Farmer Credit Profile", "📊 Lender Dashboard", "📈 Insights & Visualizations"],
        icons=["house", "robot", "file-earmark-text", "bar-chart-line", "graph-up"],
        default_index=0
    )

# ---- Main Area ----
if selected == "🏠 Home":
    st.title("🌾 Farmers Creditworthiness Platform")
    st.markdown("""
    Welcome to **Farmers Credit Scoring App**, your intelligent tool for evaluating loan eligibility of farmers.  
    Built with 💡 machine learning, this platform supports both **farmers** and **lenders** in making data-driven decisions.
    ---
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🤖 Chatbot")
        st.markdown("Ask natural language questions and get simulated credit advice.")
        if st.button("Go to Chatbot"):
            st.session_state.selected = "🤖 Chatbot"
            st.experimental_rerun()

    with col2:
        st.subheader("📋 Farmer Profile")
        st.markdown("Enter a farmer's details to predict creditworthiness.")
        if st.button("Go to Farmer Profile"):
            st.session_state.selected = "📋 Farmer Credit Profile"
            st.experimental_rerun()

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("📊 Lender Dashboard")
        st.markdown("Upload CSV data and view loan predictions.")
        if st.button("Go to Lender Dashboard"):
            st.session_state.selected = "📊 Lender Dashboard"
            st.experimental_rerun()

    with col4:
        st.subheader("📈 Insights & Visualizations")
        st.markdown("Explore model reasoning and feature importance.")
        if st.button("Go to Insights & Visualizations"):
            st.session_state.selected = "📈 Insights & Visualizations"
            st.experimental_rerun()

elif selected == "🤖 Chatbot":
    HomeChatbotPage.render()

elif selected == "📋 Farmer Credit Profile":
    farm_profile.render()

elif selected == "📊 Lender Dashboard":
    lender_dashboard.render()

elif selected == "📈 Insights & Visualizations":
    insights.render()
