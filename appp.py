import streamlit as st
from streamlit_option_menu import option_menu
import HomeChatbotPage
import farm_profile
import lender_dashboard
import insights_feature_analysis

# ---- Background Animation ----
def set_bg_animation():
    st.markdown("""
        <style>
        .stApp {
            background-color: #f9f9f9;
            background-image: url("https://www.transparenttextures.com/patterns/clean-gray-paper.png");
        }
        </style>
    """, unsafe_allow_html=True)

set_bg_animation()

# ---- Sidebar Navigation ----
with st.sidebar:
    selected = option_menu("Navigation", 
        ["🏠 Home", "🤖 Chatbot", "📋 Farmer Credit Profile", "📊 Lender Dashboard", "📈 Insights & Analysis"],
        icons=["house", "robot", "file-earmark-text", "bar-chart-line", "graph-up"],
        default_index=0)

# ---- Main Area ----
if selected == "🏠 Home":
    st.title("🌾 Farmers Creditworthiness Platform")
    st.markdown("""
    Welcome to **Farmers Credit Scoring App**, your intelligent tool for evaluating loan eligibility of farmers.  
    Built with 💡 machine learning, this platform supports both **farmers** and **lenders** in making data-driven decisions.

    ---
    """)

    # Clickable Cards
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🤖 Chatbot")
        st.markdown("Ask natural language questions and get simulated credit advice.")
        if st.button("Go to Chatbot"):
            st.experimental_set_query_params(page="chatbot")
            st.switch_page("HomeChatbotPage.py")

    with col2:
        st.markdown("### 📋 Farmer Profile")
        st.markdown("Enter one farmer's details to predict creditworthiness using AI.")
        if st.button("Go to Farmer Credit Form"):
            st.experimental_set_query_params(page="profile")
            st.switch_page("farm_profile.py")

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("### 📊 Lender Dashboard")
        st.markdown("Upload a dataset and view loan predictions for multiple farmers.")
        if st.button("Go to Dashboard"):
            st.experimental_set_query_params(page="dashboard")
            st.switch_page("lender_dashboard.py")

    with col4:
        st.markdown("### 📈 Insights & Analysis")
        st.markdown("Understand feature importance and SHAP-based model insights.")
        if st.button("Go to Insights"):
            st.experimental_set_query_params(page="insights")
            st.switch_page("insights_feature_analysis.py")

    st.markdown("---")
    st.markdown("<div style='text-align: center;'>📌 Made with ❤️ by <strong>Team Numerixa</strong></div>", unsafe_allow_html=True)

# ---- Routing Logic ----
elif selected == "🤖 Chatbot":
    HomeChatbotPage

elif selected == "📋 Farmer Credit Profile":
    farm_profile

elif selected == "📊 Lender Dashboard":
    lender_dashboard

elif selected == "📈 Insights & Analysis":
    insights_feature_analysis.render()
