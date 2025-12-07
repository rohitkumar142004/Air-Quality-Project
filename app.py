import streamlit as st
import joblib
import numpy as np

# -------------------------------
# LOAD SCALER & MODEL
# -------------------------------
try:
    scaler = joblib.load("scaler.pkl")     # Scaler trained on pollutant_min, pollutant_max
    model = joblib.load("model.pkl")       # Your ML model (regression/classification)
except FileNotFoundError:
    st.error("❌ scaler.pkl or model.pkl not found. Please place them in the same folder as app.py")
    st.stop()

# -------------------------------
# STREAMLIT APP TITLE
# -------------------------------
st.title("🌫️ Air Quality Prediction App")

st.write("Enter pollutant values below and hit Predict to estimate pollution level.")

st.divider()

# -------------------------------
# USER INPUTS
# -------------------------------

pollutant_min = st.number_input(
    "Enter pollutant MIN value",
    min_value=0.0,
    max_value=1000.0,
    value=50.0
)

pollutant_max = st.number_input(
    "Enter pollutant MAX value",
    min_value=0.0,
    max_value=1000.0,
    value=120.0
)

st.divider()

# -------------------------------
# PREDICT BUTTON
# -------------------------------
predict_btn = st.button("Predict")

if predict_btn:
    # Create array in correct order used in training
    X = [pollutant_min, pollutant_max]

    # Convert to numpy array and reshape for model
    X_array = np.array(X).reshape(1, -1)

    # Scale using loaded scaler
    X_scaled = scaler.transform(X_array)

    # Predict using loaded model
    prediction = model.predict(X_scaled)[0]

    # -----------------------
    # INTERPRETATION
    # -----------------------

    # If your model is regression → predicting pollutant_avg
    try:
        predicted_value = float(prediction)

        if predicted_value <= 50:
            category = "Low"
        elif predicted_value <= 100:
            category = "Moderate"
        else:
            category = "High"

        st.success(f"🌫️ Predicted Pollutant Average: **{predicted_value:.2f}**")
        st.info(f"📌 Pollution Level: **{category}**")

    # If your model is classification → predicting category directly
    except:
        st.success(f"📌 Predicted Pollution Category: **{prediction}**")

else:
    st.info("Enter values and click Predict to see the results.")
