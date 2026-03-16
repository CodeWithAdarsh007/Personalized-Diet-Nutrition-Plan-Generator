# 🥗 Personalized Diet & Nutrition Plan Generator

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

An intelligent **diet planning web application** that generates personalised meal plans based on user health metrics, dietary preferences, and food intolerances.  
It leverages a **machine learning model** (Random Forest) trained on Indian nutritional requirements to predict the user’s diet goal (Weight Loss / Maintenance / Weight Gain) from age and BMI.

---

## ✨ Features

- **User‑friendly interface** – Enter your age, weight, height, activity level, health goal, diet preference (Veg/NonVeg/Mixed) and any food intolerances.
- **Automatic BMI & BMR calculation** – Real‑time health metrics.
- **Calorie target adjustment** – TDEE (Total Daily Energy Expenditure) is computed and adjusted for weight loss/gain goals.
- **Smart meal generation** – Selects foods from an Indian food dataset while respecting:
  - Diet type & intolerances.
  - Meal type (Breakfast/Lunch/Dinner).
  - Duplicate food type avoidance (per meal).
  - Animal protein limit (max one per meal).
- **ML‑based goal prediction** – If no explicit goal is chosen, a trained Random Forest classifier predicts the most suitable goal using your age and BMI.
- **Portion size mapping** – Common Indian foods are shown with realistic portions (e.g., “1 bowl”, “2 pieces”).

---

## 🛠️ Tech Stack

| Component          | Technology                                      |
|--------------------|-------------------------------------------------|
| Frontend / Backend | [Streamlit](https://streamlit.io/)              |
| Data Manipulation  | Pandas, NumPy                                   |
| Machine Learning   | Scikit‑learn (Logistic Regression, Random Forest) |
| Model Persistence  | Joblib                                           |
| Visualisation      | Matplotlib, Seaborn (used in exploratory notebook) |

---

## 📁 Project Structure
.
├── app.py # Main Streamlit application

├── diet_model.ipynb # Jupyter notebook for model training & EDA

├── diet_model.pkl # Trained Random Forest model (output from notebook)

├── Indian_meal_dataset.xlsx # Food items with calories, meal type, diet type

├── MP_Indian_Personal_Nutrition_Requirements.xlsx # Dataset for model training

├── Indian_Food_Master_Dataset.xlsx # Additional food info (not used by app)

└── README.md # This file

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8+**
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/diet-plan-generator.git

   cd diet-plan-generator

   Create and activate a virtual environment (recommended)

bash

python -m venv venv

source venv/bin/activate      # On Windows: venv\Scripts\activate

Install dependencies


bash

pip install -r requirements.txt

If no requirements.txt is present, install manually:


bash

pip install streamlit pandas numpy scikit-learn matplotlib seaborn joblib openpyxl

Place the required datasets in the project root:


Indian_meal_dataset.xlsx


MP_Indian_Personal_Nutrition_Requirements.xlsx (for model training)


Indian_Food_Master_Dataset.xlsx (optional)


Train the ML model (or use the provided diet_model.pkl):


Run diet_model.ipynb in Jupyter to generate a new model.


The notebook will produce diet_model.pkl.


Running the App

Start the Streamlit server:


bash

streamlit run app.py

Then open your browser at http://localhost:8501.


📊 How It Works

User inputs are collected via the sidebar.


BMI and BMR are calculated using standard formulas.


Daily calorie target is derived from TDEE and adjusted by the selected goal.


Food dataset filtering applies diet type and intolerance rules.


Meal generation function picks foods that fit within the calorie target for each meal (Breakfast ~25%, Lunch ~40%, Dinner ~35% of daily calories).


Health metrics and the final diet plan are displayed in three columns.


🤖 Machine Learning Model

The model (diet_model.pkl) is a Random Forest Classifier trained on the MP_Indian_Personal_Nutrition_Requirements.xlsx dataset.


Features: Age, BMI (calculated from weight/height)


Target: Diet goal – Weight Gain, Maintenance, Weight Loss


Preprocessing: BMI computed, missing values handled.


Performance: Achieved 100% accuracy on the test set (dataset is small and deterministic).


Feature importance: BMI is the dominant predictor.


You can re‑train or experiment with the model using the provided Jupyter notebook diet_model.ipynb.


📈 Future Enhancements

Expand food database – Include more Indian dishes with detailed macronutrients (protein, carbs, fat) and micronutrients (iron, vitamin C).


Optimised meal planning – Use knapsack or linear programming to hit exact calorie targets.


User accounts – Save history and track progress.


Nutritional balance – Ensure meals meet daily recommended intakes for key vitamins/minerals.


Deploy online – Host on Streamlit Cloud / Heroku for public access.


🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the issues page or submit a pull request.


Fork the project.


Create your feature branch (git checkout -b feature/AmazingFeature).


Commit your changes (git commit -m 'Add some AmazingFeature').


Push to the branch (git push origin feature/AmazingFeature).


Open a pull request.


📝 License

Distributed under the MIT License. See LICENSE for more information.


🙏 Acknowledgements

The Indian food datasets were compiled from public nutrition resources.


Built with Streamlit – the fastest way to build data apps.


Machine learning powered by scikit-learn.


Enjoy your personalized diet plan! 🥑🍛🥗
