import streamlit as st
import pandas as pd
import joblib
import re

# -----------------------------
# Page Setup
# -----------------------------
st.set_page_config(page_title="Diet Plan Generator", page_icon="🥗")

st.title("🥗 Personalized Diet & Nutrition Plan Generator")
st.write("Generate a personalized diet plan based on your health parameters.")

# -----------------------------
# Load Dataset (per‑100g meals with _100g columns + Ingredients)
# -----------------------------
food = pd.read_excel("changed_Indian_meal_dataset.xlsx")

# Optional: display column names for debugging (can be removed later)
# st.write("Columns in dataset:", food.columns.tolist())

# -----------------------------
# Load ML Model and Label Encoder (optional)
# -----------------------------
try:
    model = joblib.load("diet_model.pkl")
    label_encoder = joblib.load("label_encoder.pkl")
    ml_available = True
except:
    ml_available = False
    st.sidebar.info("ML model not found. Diet goal prediction will not be used.")

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("User Details")

age = st.sidebar.number_input("Age", 10, 80, value=20)
weight = st.sidebar.number_input("Weight (kg)", 30, 150, value=52)
height = st.sidebar.number_input("Height (cm)", 120, 220, value=165)

activity = st.sidebar.selectbox(
    "Activity Level",
    ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"],
    help="""\
**Sedentary**: Little or no physical activity, typically a desk job or minimal movement.  
**Lightly Active**: Light physical activity or exercise 1–3 days/week (e.g., light walking, casual biking).  
**Moderately Active**: On your feet most of the day or moderate exercise 3–5 days/week (e.g., gym, running).  
**Very Active**: Very physical job, hard exercise, or athletic training (e.g., pro athletes, military)."""
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
# BMI Calculation
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

# Optional ML suggestion
if ml_available and st.sidebar.checkbox("Use ML to suggest goal"):
    input_data = pd.DataFrame([[age, bmi]], columns=['Age', 'BMI'])
    pred_encoded = model.predict(input_data)[0]
    predicted_goal = label_encoder.inverse_transform([pred_encoded])[0]
    st.sidebar.info(f"ML suggests: **{predicted_goal}**")

# -----------------------------
# BMR (Mifflin-St Jeor – male version)
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
# Meal Distribution (25% breakfast, 40% lunch, 35% dinner)
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
    filtered_food = food   # includes both Veg and NonVeg for Mixed

# -----------------------------
# Intolerance Filtering
# -----------------------------
if intolerance:
    filtered_food = filtered_food[
        ~filtered_food["Food"].str.lower().str.contains(intolerance.lower())
    ]

# -----------------------------
# Meal Type Filtering
# -----------------------------
breakfast_foods = filtered_food[filtered_food["MealType"] == "Breakfast"]
lunch_foods = filtered_food[filtered_food["MealType"] == "Lunch"]
dinner_foods = filtered_food[filtered_food["MealType"] == "Dinner"]

# -----------------------------
# Helper: Parse and scale ingredients
# -----------------------------
def scale_ingredients(ingredient_str, servings, total_calories_per_100g):
    """
    ingredient_str: e.g., "Rice 300g, Dal 300g, Roti 40g, Salad 50g, Ghee 5g"
    servings: number of 100g portions selected
    Returns a string with scaled ingredients.
    """
    if pd.isna(ingredient_str) or ingredient_str == "N/A":
        return "N/A"
    
    # Parse each ingredient: name, number, unit (g assumed)
    items = ingredient_str.split(',')
    parsed = []
    total_weight = 0
    for item in items:
        item = item.strip()
        # Match pattern: <name> <number>g
        match = re.match(r'^(.*?)\s+(\d+(?:\.\d+)?)g$', item)
        if match:
            name = match.group(1).strip()
            qty = float(match.group(2))
            parsed.append((name, qty))
            total_weight += qty
        else:
            # If parsing fails, keep original
            parsed.append((item, None))
    
    if total_weight == 0:
        return ingredient_str  # fallback

    # Scale factor = (servings * 100) / total_weight
    scale = (servings * 100) / total_weight

    scaled_items = []
    for name, qty in parsed:
        if qty is not None:
            scaled_qty = round(qty * scale, 1)
            scaled_items.append(f"{name} {scaled_qty}g")
        else:
            scaled_items.append(name)  # keep as is
    
    return ", ".join(scaled_items)

# -----------------------------
# Meal Generator (with goal‑based sorting)
# -----------------------------
def generate_meal(food_df, target, meal_name, goal):
    """
    Generate a meal by adding multiple 100g servings of foods until reaching ~90% of target.
    Foods are sorted according to the goal:
        - Weight Loss: ascending by calories (light foods first)
        - Weight Gain: descending by calories (dense foods first)
        - Maintain: random shuffle
    Returns a list of items with name, servings, calories, and scaled ingredients.
    """
    if food_df.empty:
        st.warning(f"No {meal_name} options available with your current filters. Try changing your preferences.")
        return [], 0

    # Apply goal‑based sorting
    if goal == "Weight Loss":
        # Sort by calories ascending (lightest first)
        foods = food_df.sort_values("Calories_100g", ascending=True).reset_index(drop=True)
    elif goal == "Weight Gain":
        # Sort by calories descending (densest first)
        foods = food_df.sort_values("Calories_100g", ascending=False).reset_index(drop=True)
    else:  # Maintain Weight
        # Random shuffle for variety
        foods = food_df.sample(frac=1).reset_index(drop=True)

    n_foods = len(foods)
    
    # Dictionary to count servings per food index
    servings = {i: 0 for i in range(n_foods)}
    total_cal = 0
    max_iter = 100  # prevent infinite loop
    iter_count = 0
    idx = 0

    # Keep adding servings until we hit target or run out of iterations
    while total_cal < target * 0.9 and iter_count < max_iter:
        i = idx % n_foods
        row = foods.iloc[i]
        cal_per_serving = row["Calories_100g"]
        
        # Add one serving (100g)
        servings[i] += 1
        total_cal += cal_per_serving
        
        idx += 1
        iter_count += 1

    # Group servings by food name
    meal_dict = {}
    for i, count in servings.items():
        if count > 0:
            row = foods.iloc[i]
            name = row["Food"]
            cal_per = row["Calories_100g"]
            total_food_cal = cal_per * count
            ingredient_str = row.get("Ingredients (for reference)", "N/A")
            # Scale ingredients for this item
            scaled_ingredients = scale_ingredients(ingredient_str, count, cal_per)
            
            if name in meal_dict:
                meal_dict[name]["servings"] += count
                meal_dict[name]["total_calories"] += total_food_cal
                # For simplicity, we keep the ingredients from the first occurrence (they are the same)
            else:
                meal_dict[name] = {
                    "servings": count,
                    "calories_per_serving": cal_per,
                    "total_calories": total_food_cal,
                    "ingredients": scaled_ingredients
                }
    
    # Convert dict to list
    meal = [{"name": name, **details} for name, details in meal_dict.items()]
    return meal, total_cal

# -----------------------------
# Generate Diet Plan
# -----------------------------
if st.button("Generate Diet Plan"):
    breakfast, b_cal = generate_meal(breakfast_foods, breakfast_target, "breakfast", goal)
    lunch, l_cal = generate_meal(lunch_foods, lunch_target, "lunch", goal)
    dinner, d_cal = generate_meal(dinner_foods, dinner_target, "dinner", goal)

    st.subheader("Health Metrics")
    c1, c2, c3 = st.columns(3)
    c1.metric("BMI", round(bmi, 2))
    c2.metric("BMI Category", bmi_status)
    c3.metric("Daily Calories", round(calories))

    st.divider()
    st.subheader("🍽 Your Personalized Diet Plan (based on 100g servings)")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🌅 Breakfast")
        for item in breakfast:
            with st.expander(f"{item['name']} – {item['servings']}×100g ({item['total_calories']} kcal)"):
                st.write(f"**Calories per 100g:** {item['calories_per_serving']} kcal")
                st.write(f"**Scaled Ingredients (for your portion):** {item['ingredients']}")
        st.write(f"**Total Breakfast:** {round(b_cal)} kcal")

    with col2:
        st.markdown("### 🍛 Lunch")
        for item in lunch:
            with st.expander(f"{item['name']} – {item['servings']}×100g ({item['total_calories']} kcal)"):
                st.write(f"**Calories per 100g:** {item['calories_per_serving']} kcal")
                st.write(f"**Scaled Ingredients (for your portion):** {item['ingredients']}")
        st.write(f"**Total Lunch:** {round(l_cal)} kcal")

    with col3:
        st.markdown("### 🌙 Dinner")
        for item in dinner:
            with st.expander(f"{item['name']} – {item['servings']}×100g ({item['total_calories']} kcal)"):
                st.write(f"**Calories per 100g:** {item['calories_per_serving']} kcal")
                st.write(f"**Scaled Ingredients (for your portion):** {item['ingredients']}")
        st.write(f"**Total Dinner:** {round(d_cal)} kcal")
