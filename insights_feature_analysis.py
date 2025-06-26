import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import warnings
import io

warnings.filterwarnings("ignore")

def render():
    st.title("📈 Insights & Feature Analysis")

    # Load model
    try:
        model = joblib.load("models_random_forest_model.pkl")
    except Exception as e:
        st.error("❌ Failed to load the machine learning model.")
        st.exception(e)
        return

    # 📥 Sample CSV download
    st.markdown("### 📥 Need help with the right format?")
    st.info("To avoid errors, download and use the sample CSV format below:")

    sample_data = pd.DataFrame({
        "age": [30, 45],
        "years_lived_in_community": [5, 20],
        "level_of_education": ["SENIOR SECONDARY", "1st DEGREE"],
        "phone_access": ["Yes", "No"],
        "sector": ["Rural", "Urban"],
        "women_access": ["Yes", "No"]
    })

    buffer = io.BytesIO()
    sample_data.to_csv(buffer, index=False)
    buffer.seek(0)

    st.download_button(
        label="📥 Download Sample CSV",
        data=buffer,
        file_name="sample_farmer_data.csv",
        mime="text/csv"
    )

    st.markdown("---")
    st.markdown("### 📂 Upload Farmer Dataset")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)

            # Validate required columns
            required_columns = [
                "age", "years_lived_in_community", "level_of_education",
                "phone_access", "sector", "women_access"
            ]
            missing_cols = [col for col in required_columns if col not in df.columns]
            if missing_cols:
                st.error(f"❌ Your file is missing the following required columns: {missing_cols}")
                return

            # Feature encoding
            education_mapping = {
                'NONE': 0, 'NURSERY': 0,
                'QUARANIC/INTEGRATED QUARANIC': 1, 'OTHER RELIGIOUS': 1,
                'PRIMARY': 2, 'ADULT EDUCATION': 2,
                'JUNIOR SECONDARY': 3, 'MODERN SCHOOL': 3, 'LOWER/UPPER 6': 3,
                'SENIOR SECONDARY': 4,
                'SECONDARY VOCATIONAL/TECHNICAL/COMMERCIAL': 4,
                'TEACHER TRAINING': 5, 'TERTIARY VOCATIONAL/TECHNICAL/COMMERCIAL': 5,
                'POLYTECHNIC/PROF': 6, 'NATIONAL CERTIFICATE OF EDUCATION (NCE)': 6,
                '1st DEGREE': 6, 'HIGHER DEGREE (POST-GRADUATE)': 7,
                'OTHER': 8
            }
            sector_map = {"Urban": 0, "Rural": 1}

            df['education_encoded'] = df['level_of_education'].map(education_mapping).fillna(8).astype(int)
            df['phone_access'] = df['phone_access'].apply(lambda x: 1 if str(x).lower() == 'yes' else 0)
            df['sector_encoded'] = df['sector'].map(sector_map).fillna(0).astype(int)
            df['women_access'] = df['women_access'].apply(lambda x: 1 if str(x).lower() == 'yes' else 0)

            features = df[['age', 'years_lived_in_community', 'education_encoded',
                           'phone_access', 'sector_encoded', 'women_access']]

            # Predict
            df['Loan Approved (1=Yes)'] = model.predict(features)

            # Trend Exploration
            st.markdown("### 📉 Trend Exploration")
            selected = st.selectbox("Select a Feature to Explore", features.columns)
            fig = px.box(df, x='Loan Approved (1=Yes)', y=selected,
                         title=f"Distribution of {selected} by Loan Outcome")
            st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error("⚠️ Something went wrong. Please ensure your CSV file follows the sample format.")
            st.exception(e)
    else:
        st.info("📂 Please upload a CSV file to view insights.")

    st.markdown("---")
    st.markdown("<div style='text-align: center;'>📌 Made with ❤️ by <strong>Team Numerixa</strong></div>", unsafe_allow_html=True)
