# 🥗 Personalized Diet & Nutrition Plan Generator

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io) [![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org) [![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

An intelligent **diet planning web application** that generates personalized meal plans based on user health metrics, dietary preferences, and food intolerances. It leverages a **Machine Learning model** (Random Forest) trained on Indian nutritional requirements to predict the most suitable diet goal (Weight Loss, Maintenance, or Weight Gain) based on age and BMI.

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

```
.
├── app.py                # Main Streamlit application
├── diet_model.ipynb      # Jupyter notebook for EDA and model training
├── diet_model.pkl        # Trained Random Forest model
├── data/                 # Directory for datasets
│   ├── Indian_meal_dataset.xlsx
│   ├── MP_Indian_Personal_Nutrition_Requirements.xlsx
│   └── Indian_Food_Master_Dataset.xlsx
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
* Python **3.8+**
* `pip` (Python package manager)

### Installation

1. **Clone the Repository**
   ```
   git clone https://github.com/codewithadarsh007/Personalized-Diet-Nutrition-Plan-Generator.git
   cd diet-plan-generator
   ```

2. **Set Up a Virtual Environment (Recommended)**
   # Windows
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```
   # macOS/Linux
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```
   pip install streamlit pandas numpy scikit-learn matplotlib seaborn joblib openpyxl
   ```

4. **Running the App**
   Start the Streamlit server:
   ```
   streamlit run app.py
   ```
   Then open your browser at http://localhost:8501

---

## ⚙️ How It Works

The engine follows a multi-step logic to ensure the diet plan is both healthy and personalized:

1. **User Input:** Physical metrics and lifestyle activity are collected via the sidebar.
2. **Calorie Targeting:** Daily calorie needs are calculated using the BMR and Activity Level. The final target is adjusted by approximately $\pm 500$ calories depending on the user's weight goal.
3. **Dataset Filtering:** The Indian food dataset is filtered by Diet Type (Veg/Non-Veg) and excludes any food containing the user's specific intolerances.
4. **Meal Allocation:**
   - **Breakfast:** ~25% of daily calories.
   - **Lunch:** ~40% of daily calories.
   - **Dinner:** ~35% of daily calories.

---

## 🤖 Machine Learning Model

The `diet_model.pkl` is a **Random Forest Classifier** trained on the `MP_Indian_Personal_Nutrition_Requirements.xlsx` dataset.
- **Inputs:** Age, BMI.
- **Outputs:** Predicted Diet Goal (Weight Gain, Maintenance, Weight Loss).
- **Insight:** Feature importance analysis indicates that **BMI** is the strongest predictor for determining a user's health path.
*You can explore the training process and metrics in `diet_model.ipynb`.*

---

## 📈 Future Enhancements

- [ ] **Macro Breakdown:** Detailed Protein, Carbs, and Fat tracking for every generated meal.
- [ ] **Optimization:** Implement Linear Programming to hit exact calorie targets more efficiently.
- [ ] **User Profiles:** Cloud-based storage for users to save and track their weight progress.

---

## 🤝 Contributing

1. **Fork** the project.
2. **Create** your feature branch (`git checkout -b feature/AmazingFeature`).
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`).
4. **Push** to the branch (`git push origin feature/AmazingFeature`).
5. **Open** a Pull Request.

---

## 📝 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

**Made with ❤️ by Adarsh**
