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
├── app.py # Main Streamlit application/n
├── diet_model.ipynb # Jupyter notebook for model training & EDA/n
├── diet_model.pkl # Trained Random Forest model (output from notebook)/n
├── Indian_meal_dataset.xlsx # Food items with calories, meal type, diet type/n
├── MP_Indian_Personal_Nutrition_Requirements.xlsx # Dataset for model training/n
├── Indian_Food_Master_Dataset.xlsx # Additional food info (not used by app)/n
└── README.md # This file

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8+**
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/diet-plan-generator.git/n
   cd diet-plan-generator/n
   Create and activate a virtual environment (recommended)

bash/n
python -m venv venv/n
source venv/bin/activate      # On Windows: venv\Scripts\activate/n
Install dependencies/n

bash/n
pip install -r requirements.txt/n
If no requirements.txt is present, install manually:/n

bash/n
pip install streamlit pandas numpy scikit-learn matplotlib seaborn joblib openpyxl/n
Place the required datasets in the project root:/n

Indian_meal_dataset.xlsx/n

MP_Indian_Personal_Nutrition_Requirements.xlsx (for model training)/n

Indian_Food_Master_Dataset.xlsx (optional)/n

Train the ML model (or use the provided diet_model.pkl):/n

Run diet_model.ipynb in Jupyter to generate a new model./n

The notebook will produce diet_model.pkl./n

Running the App/n
Start the Streamlit server:/n

bash/n
streamlit run app.py/n
Then open your browser at http://localhost:8501./n

📊 How It Works/n
User inputs are collected via the sidebar./n

BMI and BMR are calculated using standard formulas./n

Daily calorie target is derived from TDEE and adjusted by the selected goal./n

Food dataset filtering applies diet type and intolerance rules./n

Meal generation function picks foods that fit within the calorie target for each meal (Breakfast ~25%, Lunch ~40%, Dinner ~35% of daily calories)./n

Health metrics and the final diet plan are displayed in three columns./n

🤖 Machine Learning Model/n
The model (diet_model.pkl) is a Random Forest Classifier trained on the MP_Indian_Personal_Nutrition_Requirements.xlsx dataset./n

Features: Age, BMI (calculated from weight/height)/n

Target: Diet goal – Weight Gain, Maintenance, Weight Loss/n

Preprocessing: BMI computed, missing values handled./n

Performance: Achieved 100% accuracy on the test set (dataset is small and deterministic)./n

Feature importance: BMI is the dominant predictor./n

You can re‑train or experiment with the model using the provided Jupyter notebook diet_model.ipynb./n

📈 Future Enhancements/n
Expand food database – Include more Indian dishes with detailed macronutrients (protein, carbs, fat) and micronutrients (iron, vitamin C)./n

Optimised meal planning – Use knapsack or linear programming to hit exact calorie targets./n

User accounts – Save history and track progress./n

Nutritional balance – Ensure meals meet daily recommended intakes for key vitamins/minerals./n

Deploy online – Host on Streamlit Cloud / Heroku for public access./n

🤝 Contributing/n
Contributions, issues, and feature requests are welcome!/n
Feel free to check the issues page or submit a pull request./n

Fork the project./n

Create your feature branch (git checkout -b feature/AmazingFeature)./n

Commit your changes (git commit -m 'Add some AmazingFeature')./n

Push to the branch (git push origin feature/AmazingFeature)./n

Open a pull request./n

📝 License/n
Distributed under the MIT License. See LICENSE for more information./n

🙏 Acknowledgements/n
The Indian food datasets were compiled from public nutrition resources./n

Built with Streamlit – the fastest way to build data apps./n

Machine learning powered by scikit-learn./n

Enjoy your personalized diet plan! 🥑🍛🥗
