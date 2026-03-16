# 🥗 Personalized Diet & Nutrition Plan Generator

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

An intelligent **diet planning web application** that generates personalized meal plans based on user health metrics, dietary preferences, and food intolerances. 

It leverages a **Machine Learning model** (Random Forest) trained on Indian nutritional requirements to predict the most suitable diet goal (Weight Loss, Maintenance, or Weight Gain) based on age and BMI.

---

## ✨ Features

* **Interactive UI** – Simple sidebar for entering age, weight, height, activity level, and dietary preferences.
* **Real-time Metrics** – Automatic calculation of BMI, BMR, and TDEE (Total Daily Energy Expenditure).
* **Smart Meal Generation** – Filters an Indian food dataset based on:
    * Diet type (Veg/Non-Veg/Mixed) and specific intolerances.
    * Meal-specific calorie targets (Breakfast, Lunch, Dinner).
    * Nutritional constraints (e.g., limit of one animal protein per meal).
* **ML-Driven Predictions** – Uses a Random Forest classifier to suggest health goals if none are explicitly chosen.
* **Localized Context** – Focused on common Indian foods with realistic portion size mapping.

---

## 🛠️ Tech Stack

| Component          | Technology                                      |
| ------------------ | ----------------------------------------------- |
| **Frontend/Backend** | [Streamlit](https://streamlit.io/)              |
| **Data Handling** | Pandas, NumPy, Openpyxl                         |
| **Machine Learning** | Scikit-learn (Random Forest, Logistic Regression)|
| **Persistence** | Joblib                                          |
| **Visualizations** | Matplotlib, Seaborn                             |

---

## 📁 Project Structure

```text
.
├── app.py                # Main Streamlit application
├── diet_model.ipynb      # Jupyter notebook for EDA and model training
├── diet_model.pkl        # Trained Random Forest model
├── requirements.txt      # List of dependencies
├── data/                 # Directory for datasets
│   ├── Indian_meal_dataset.xlsx
│   ├── MP_Indian_Personal_Nutrition_Requirements.xlsx
│   └── Indian_Food_Master_Dataset.xlsx
└── README.md             # Project documentation
