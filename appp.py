import streamlit as st
from streamlit_option_menu import option_menu
import HomeChatbotPage
import farm_profile
import lender_dashboard
import insights_feature_analysis as insights

# --- Background Theme ---
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
    }
    .intro-text {
        font-size: 15px;
        line-height: 1.5;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

set_bg_animation()

# --- Navigation State ---
if "selected_nav" not in st.session_state:
    st.session_state.selected_nav = "🏠 Home"

if "redirect_to" not in st.session_state:
    st.session_state.redirect_to = None

# Handle redirect
if st.session_state.redirect_to:
    st.session_state.selected_nav = st.session_state.redirect_to
    st.session_state.redirect_to = None
    st.experimental_rerun()

# Sidebar
with st.sidebar:
    selected = option_menu("Navigation", 
        ["🏠 Home", "🤖 Chatbot", "📋 Farmer Credit Profile", "📊 Lender Dashboard", "📈 Insights & Visualizations"],
        icons=["house", "robot", "file-earmark-text", "bar-chart-line", "graph-up"],
        default_index=["🏠 Home", "🤖 Chatbot", "📋 Farmer Credit Profile", "📊 Lender Dashboard", "📈 Insights & Visualizations"].index(st.session_state.selected_nav)
    )

# Update state
st.session_state.selected_nav = selected

# --- HOME PAGE ---
if selected == "🏠 Home":
    st.title("🌾 Farmers Creditworthiness Platform")

    st.markdown("""
    <div class="intro-text">
    Welcome to <strong>Farmers Credit Scoring App</strong>, your intelligent tool for evaluating loan eligibility of farmers.  
    Built with 💡 machine learning, this platform supports both <strong>farmers</strong> and <strong>lenders</strong> in making data-driven decisions.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🤖 Chatbot")
        st.markdown("Ask natural language questions and get simulated credit advice.")
        if st.button("Open Chatbot"):
            st.session_state.redirect_to = "🤖 Chatbot"
            st.experimental_rerun()

    with col2:
        st.subheader("📋 Farmer Profile")
        st.markdown("Enter a farmer's details to predict creditworthiness.")
        if st.button("Open Farmer Profile"):
            st.session_state.redirect_to = "📋 Farmer Credit Profile"
            st.experimental_rerun()

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("📊 Lender Dashboard")
        st.markdown("Upload CSV data and view loan predictions.")
        if st.button("Open Lender Dashboard"):
            st.session_state.redirect_to = "📊 Lender Dashboard"
            st.experimental_rerun()

    with col4:
        st.subheader("📈 Insights & Analysis")
        st.markdown("Explore model reasoning and feature importance.")
        if st.button("Open Insights & Visualizations"):
            st.session_state.redirect_to = "📈 Insights & Visualizations"
            st.experimental_rerun()

# --- Page Logic ---
elif selected == "🤖 Chatbot":
    HomeChatbotPage.render()

elif selected == "📋 Farmer Credit Profile":
    farm_profile.render()

elif selected == "📊 Lender Dashboard":
    lender_dashboard.render()

elif selected == "📈 Insights & Visualizations":
    insights.render()
