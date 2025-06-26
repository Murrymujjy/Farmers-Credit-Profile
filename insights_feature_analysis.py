import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import shap
import matplotlib.pyplot as plt
import warnings
import io

warnings.filterwarnings("ignore")

def render():
    st.title("📈 Insights & Feature Analysis")

    # Load model
    model = joblib.load("models_random_forest_model.pkl")

    # 📌 Sample CSV download
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

            # Map and encode inputs
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

            # ✅ Predict loan approval for trend plot
            df['Loan Approved (1=Yes)'] = model.predict(features)

            # ✅ SHAP Analysis
            features_sampled = features.sample(n=min(200, len(features)), random_state=42)
            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(features_sampled)

            st.markdown("### 🔍 Feature Importance (SHAP Summary Plot)")
            shap.summary_plot(shap_values[1], features_sampled, show=False)
            st.pyplot(plt.gcf())

            st.markdown("### 📊 Mean Absolute SHAP Values")
            mean_abs_shap = np.abs(shap_values[1]).mean(axis=0)
            shap_df = pd.DataFrame({"Feature": features.columns, "Mean |SHAP|": mean_abs_shap})
            fig = px.bar(shap_df.sort_values("Mean |SHAP|", ascending=False),
                        x="Mean |SHAP|", y="Feature", orientation='h',
                        title="Top Features Impacting Loan Approval")
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("### 📉 Trend Exploration")
            selected = st.selectbox("Select a Feature to Explore", features.columns)
            fig2 = px.box(df, x='Loan Approved (1=Yes)', y=selected,
                        title=f"Distribution of {selected} by Loan Outcome")
            st.plotly_chart(fig2, use_container_width=True)

        except Exception as e:
            st.error("⚠️ Something went wrong. Please ensure your CSV file follows the sample format.")
            st.exception(e)  # Optional: shows developer-friendly trace. Can remove in production.
    else:
        st.info("Please upload a CSV file to view insights.")

    st.markdown("---")
    st.markdown("<div style='text-align: center;'>📌 Made with ❤️ by <strong>Team Numerixa</strong></div>", unsafe_allow_html=True)
