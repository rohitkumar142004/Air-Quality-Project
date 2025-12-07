import streamlit as st
import numpy as np
import joblib

# ------------------------------------------------
# LOAD SCALER & MODEL
# ------------------------------------------------
try:
    scaler = joblib.load("scaler.pkl")
    model = joblib.load("model.pkl")
except:
    st.error("❌ scaler.pkl or model.pkl missing! Place them in the same folder as app.py")
    st.stop()

# ------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------
st.set_page_config(
    page_title="Air Quality Predictor",
    page_icon="🌫️",
    layout="wide",
)

# ------------------------------------------------
# CUSTOM CSS FOR MODERN UI
# ------------------------------------------------
st.markdown("""
<style>
.result-card {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    color: white;
}
.low { background-color: #2ecc71; }
.moderate { background-color: #f39c12; }
.high { background-color: #e74c3c; }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# TITLE
# ------------------------------------------------
st.title("🌫️ Air Quality Prediction Dashboard")
st.write("Enter pollutant values below to estimate pollution level.")

st.divider()

# ------------------------------------------------
# SIDEBAR INPUTS
# ------------------------------------------------
st.sidebar.header("📌 Input Values")

pollutant_min = st.sidebar.number_input(
    "Pollutant MIN Value", 0.0, 2000.0, 40.0
)

pollutant_max = st.sidebar.number_input(
    "Pollutant MAX Value", 0.0, 2000.0, 120.0
)

predict_btn = st.sidebar.button("🔮 Predict")

# ------------------------------------------------
# MAIN DASHBOARD METRICS
# ------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Pollutant Overview")
    st.metric("Pollutant MIN", pollutant_min)
    st.metric("Pollutant MAX", pollutant_max)

with col2:
    st.subheader("📉 Range Spread")
    st.metric("Difference", pollutant_max - pollutant_min)

st.divider()

# ------------------------------------------------
# PREDICTION SECTION
# ------------------------------------------------
if predict_btn:

    # 🎈 BALLOONS + TOAST CELEBRATION
    st.balloons()
    st.toast("Prediction Completed! 🎉")

    # Prepare input
    X = np.array([[pollutant_min, pollutant_max]])
    X_scaled = scaler.transform(X)

    # Predict
    prediction = model.predict(X_scaled)[0]

    # Determine category (if regression output)
    try:
        value = float(prediction)

        if value <= 50:
            category = "Low"
            css_class = "low"
        elif value <= 100:
            category = "Moderate"
            css_class = "moderate"
        else:
            category = "High"
            css_class = "high"

        st.subheader("🎯 Prediction Result")

        st.markdown(f"""
        <div class="result-card {css_class}">
            Predicted Pollution Level: {category}<br>
            Predicted Avg Value: {value:.2f}
        </div>
        """, unsafe_allow_html=True)

    except:
        category = prediction
        css_class = "high"
        if category == "Low":
            css_class = "low"
        elif category == "Moderate":
            css_class = "moderate"

        st.subheader("🎯 Prediction Result")
        st.markdown(f"""
        <div class="result-card {css_class}">
            Predicted Category: {category}
        </div>
        """, unsafe_allow_html=True)

    # Gauge progress bar
    st.subheader("📍 Pollution Gauge")

    gauge_val = 0
    if category == "Low":
        gauge_val = 20
    elif category == "Moderate":
        gauge_val = 50
    else:
        gauge_val = 90

    st.progress(gauge_val / 100)

else:
    st.info("Enter values and click Predict for results.")
