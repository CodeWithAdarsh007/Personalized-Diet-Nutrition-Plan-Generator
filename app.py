import streamlit as st
import pandas as pd

# -----------------------------
# Page Setup
# -----------------------------
st.set_page_config(page_title="Diet Plan Generator", page_icon="🥗")

st.title("🥗 Personalized Diet & Nutrition Plan Generator")
st.write("Generate a personalized diet plan based on your health parameters.")

# -----------------------------
# Load Dataset
# -----------------------------
food = pd.read_excel("Indian_meal_dataset.xlsx")

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("User Details")

age = st.sidebar.number_input("Age", 10, 80)

weight = st.sidebar.number_input("Weight (kg)", 30, 150)

height = st.sidebar.number_input("Height (cm)", 120, 220)

activity = st.sidebar.selectbox(
    "Activity Level",
    ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"]
)

goal = st.sidebar.selectbox(
    "Health Goal",
    ["Weight Loss", "Maintain Weight", "Weight Gain"]
)

diet_type = st.sidebar.selectbox(
    "Diet Preference",
    ["Veg", "NonVeg", "Mixed"]
)

intolerance = st.sidebar.text_input(
    "Food Intolerance (optional)", placeholder="example: egg, paneer"
)

# -----------------------------
# BMI
# -----------------------------
height_m = height / 100
bmi = weight / (height_m ** 2)

if bmi < 18.5:
    bmi_status = "Underweight"
elif bmi < 25:
    bmi_status = "Normal"
elif bmi < 30:
    bmi_status = "Overweight"
else:
    bmi_status = "Obese"

# -----------------------------
# BMR
# -----------------------------
bmr = 10 * weight + 6.25 * height - 5 * age + 5

# -----------------------------
# Activity Multiplier
# -----------------------------
activity_factor = {
    "Sedentary": 1.2,
    "Lightly Active": 1.375,
    "Moderately Active": 1.55,
    "Very Active": 1.725
}

tdee = bmr * activity_factor[activity]

# -----------------------------
# Goal Adjustment
# -----------------------------
if goal == "Weight Loss":
    calories = tdee - 400
elif goal == "Weight Gain":
    calories = tdee + 400
else:
    calories = tdee

# -----------------------------
# Meal Distribution
# -----------------------------
breakfast_target = calories * 0.25
lunch_target = calories * 0.40
dinner_target = calories * 0.35

# -----------------------------
# Diet Preference Filtering
# -----------------------------
if diet_type == "Veg":
    filtered_food = food[food["DietType"] == "Veg"]
else:
    filtered_food = food

# -----------------------------
# Intolerance Filtering
# -----------------------------
if intolerance:
    filtered_food = filtered_food[
        ~filtered_food["Food"].str.lower().str.contains(intolerance.lower())
    ]

# -----------------------------
# Goal Based Filtering
# -----------------------------
if goal == "Weight Gain":
    filtered_food = filtered_food[filtered_food["Calories"] >= 150]

elif goal == "Weight Loss":
    filtered_food = filtered_food[filtered_food["Calories"] <= 250]

# -----------------------------
# Meal Type Filtering
# -----------------------------
breakfast_foods = filtered_food[filtered_food["MealType"] == "Breakfast"]
lunch_foods = filtered_food[filtered_food["MealType"] == "Lunch"]
dinner_foods = filtered_food[filtered_food["MealType"] == "Dinner"]

# -----------------------------
# Portion Mapping
# -----------------------------
portion_sizes = {
    "Rice":"1 bowl",
    "Chapati":"2 pieces",
    "Milk":"1 glass",
    "Banana":"1 medium",
    "Oats":"1 bowl",
    "Dal":"1 bowl",
    "Chicken curry":"1 serving",
    "Paneer curry":"1 serving"
}

# -----------------------------
# Meal Generator
# -----------------------------
def generate_meal(food_df, target):

    meal = []
    total = 0

    used_foods = set()
    used_keywords = set()

    animal_protein = 0

    foods = food_df.sample(frac=1).reset_index(drop=True)

    for i in range(len(foods)):

        name = foods.loc[i,"Food"]
        cal = foods.loc[i,"Calories"]

        keyword = name.lower().split()[0]

        if name in used_foods:
            continue

        if keyword in used_keywords:
            continue

        if any(x in name.lower() for x in ["chicken","fish","egg"]):

            if animal_protein >= 1:
                continue

            animal_protein += 1

        if total + cal <= target:

            portion = portion_sizes.get(name,"1 serving")

            meal.append({
                "name":name,
                "portion":portion,
                "calories":cal
            })

            used_foods.add(name)
            used_keywords.add(keyword)

            total += cal

        if total >= target*0.9 or len(meal)>=4:
            break

    return meal,total

# -----------------------------
# Generate Diet Plan
# -----------------------------
if st.button("Generate Diet Plan"):

    breakfast,b_cal = generate_meal(breakfast_foods,breakfast_target)
    lunch,l_cal = generate_meal(lunch_foods,lunch_target)
    dinner,d_cal = generate_meal(dinner_foods,dinner_target)

    st.subheader("Health Metrics")

    c1,c2,c3 = st.columns(3)

    c1.metric("BMI",round(bmi,2))
    c2.metric("BMI Category",bmi_status)
    c3.metric("Daily Calories",round(calories))

    st.divider()

    st.subheader("🍽 Your Personalized Diet Plan")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown("### 🌅 Breakfast")
        for item in breakfast:
            st.write(f"• {item['name']} ({item['portion']}) — {item['calories']} kcal")
        st.write("Total:",round(b_cal),"kcal")

    with col2:
        st.markdown("### 🍛 Lunch")
        for item in lunch:
            st.write(f"• {item['name']} ({item['portion']}) — {item['calories']} kcal")
        st.write("Total:",round(l_cal),"kcal")

    with col3:
        st.markdown("### 🌙 Dinner")
        for item in dinner:
            st.write(f"• {item['name']} ({item['portion']}) — {item['calories']} kcal")
        st.write("Total:",round(d_cal),"kcal")