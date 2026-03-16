# Diet Recommendation System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)

## Description

This project is a machine learning-based diet recommendation system designed to classify users into diet categories (Weight Gain, Maintenance, Weight Loss) based on their BMI, age, and nutritional requirements. It uses datasets of Indian personal nutrition requirements and food master data to train models and provide personalized meal recommendations via a Streamlit web application.

The system includes:
- Data preprocessing and BMI calculation from user attributes.
- Training of Logistic Regression and Random Forest classifiers.
- Model evaluation with accuracy scores and classification reports.
- A web app for generating diet plans with breakfast, lunch, and dinner suggestions, including calorie counts.

## Features

- **Data Analysis**: Loads and processes Excel datasets for nutrition requirements and food items.
- **BMI Classification**: Automatically classifies diet types based on BMI thresholds.
- **Machine Learning Models**: Implements and compares Logistic Regression and Random Forest for diet prediction.
- **Model Evaluation**: Provides accuracy metrics, confusion matrices, and classification reports.
- **Web Application**: Interactive Streamlit app for diet recommendations, displaying meal plans with food portions and total calories.
- **Visualization**: Includes plots for data distribution (e.g., BMI histogram, diet category bar chart, model accuracy comparison).

## Installation

### Prerequisites
- Python 3.8 or higher
- Required libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, streamlit

### Setup
1. Clone or download the repository.
2. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn streamlit
   ```
3. Place the required Excel files in the project directory:
   - `MP_Indian_Personal_Nutrition_Requirements.xlsx`
   - `Indian_Food_Master_Dataset.xlsx`

## Usage

### Running the Jupyter Notebook
1. Open `diet_model.ipynb` in Jupyter Notebook or JupyterLab.
2. Execute the cells to:
   - Load and preprocess data.
   - Train and evaluate models.
   - Visualize results.

### Running the Streamlit App
1. Navigate to the project directory.
2. Run the app:
   ```bash
   streamlit run app.py
   ```
3. Open the provided URL in your browser to interact with the diet recommendation interface.

## Project Structure

- `app.py`: Streamlit application for diet recommendations.
- `diet_model.ipynb`: Jupyter notebook containing data analysis, model training, and evaluation.
- `document.md`: This README file.
- `MP_Indian_Personal_Nutrition_Requirements.xlsx`: Dataset for personal nutrition data.
- `Indian_Food_Master_Dataset.xlsx`: Dataset for food nutritional information.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support or questions, open an issue on GitHub or contact the project maintainer.
