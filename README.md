# 🌾 Farmers Credit Scoring App

A user-friendly AI-powered web application that predicts the creditworthiness of farmers based on demographic and socio-economic data. Built with Streamlit, this app supports farmers, lenders, and policymakers in making data-driven decisions.

---

## 🌍 Live Demo

Check out the hosted app: [Streamlit App](https://farmers-credit-profile-numerixa.streamlit.app/)

---

## 🌀 Problem Statement

In many rural areas, access to formal credit is limited due to a lack of reliable data for decision-making. This app uses Machine Learning to help:

* Farmers check their loan eligibility.
* Lenders assess multiple farmers via CSV upload.
* Stakeholders gain insights from feature analysis.

---

## 📊 Key Features

* **🧠 Chatbot Assistant** – Ask questions in natural language.
* **📋 Farmer Profile Form** – Input details to get loan prediction.
* **📊 Lender Dashboard** – Upload CSV and view batch predictions.
* **🔹 Insights & Visualizations** – Explore feature importance and Power BI dashboard.

---

## 🧰 Technologies Used

* **Streamlit** – Interactive web app
* **Scikit-learn** – ML modeling (Logistic Regression, Random Forest, Decision Tree)
* **Pandas / NumPy** – Data manipulation
* **Power BI** – Visual storytelling
* **OpenAI API** – For Chatbot reasoning

---

## 📁 Sample Data

You can test the Lender Dashboard with the provided CSV:

* [sample\_farmer\_data.csv](./data/sample_farmer_data.csv)

---

## 📅 Folder Structure

```
├─ app/                          # Streamlit code modules
│   ├─ appp.py
│   ├─ HomeChatbotPage.py
│   ├─ farm_profile.py
│   ├─ lender_dashboard.py
│   └─ insights_feature_analysis.py
├─ models/                       # Trained ML models
│   └─ logistic_regression_model.pkl
├─ data/
│   ├─ sample_farmer_data.csv
├─ notebooks/                   # EDA & model training notebooks
│   └─ datacinity.ipynb
├─ requirements.txt
└─ README.md
```

---

## 🛠️ Installation & Setup

```bash
# Clone repo
https://github.com/Murrymujjy/farmers-credit-scoring-app.git
cd farmers-credit-scoring-app

# Create environment and install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app/app.py
```

---

## 📊 Insights Example

* Most influential features: **Education Level**, **Phone Access**, **Age**
* Rural farmers with tertiary education and access to mobile phones had the highest predicted credit scores.

---

## 🎓 About the Author

**Mujeebat Muritala** – Machine Learning Engineer passionate about building practical AI solutions.
[LinkedIn](https://www.linkedin.com/in/mujeebat-muritala-134210175)

**Lawal AbdSalam** - Data Analyst 

**Aderoju AbdulSalam** - Machine Learning Engineer and Pipeline Expert 

**Owodunni Aminat** - Data Engineer 

---

## ✨ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
