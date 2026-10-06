import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.joblib")
meta = joblib.load("columns.joblib")

st.title("Fertilizer recommendation")
st.caption("Trained model: " + meta["model_name"])
st.warning(
    "Soil pH is collected because the brief asks for it. "
    "The training CSV has no pH column, so pH is not a model feature."
)

soil = st.selectbox("Soil type", ["Sandy", "Loamy", "Black", "Red", "Clayey"])
crop = st.selectbox("Crop type", [
    "Maize", "Sugarcane", "Cotton", "Tobacco", "Paddy", "Barley",
    "Millets", "Oil seeds", "Pulses", "Wheat", "Ground Nuts",
])
nitrogen = st.number_input("Nitrogen", min_value=0, max_value=50, value=15)
phosphorus = st.number_input("Phosphorus", min_value=0, max_value=50, value=15)
potassium = st.number_input("Potassium", min_value=0, max_value=30, value=0)
moisture = st.number_input("Moisture", min_value=20, max_value=70, value=40)
ph = st.number_input("Soil pH (not used by the model)", min_value=3.5, max_value=9.0, value=6.5, step=0.1)
temperature = st.number_input("Temperature", min_value=20, max_value=45, value=30)
humidity = st.number_input("Humidity", min_value=40, max_value=80, value=60)

if st.button("Recommend"):
    row = pd.DataFrame([{
        "Temperature": temperature,
        "Humidity": humidity,
        "Moisture": moisture,
        "Soil_Type": soil,
        "Crop_Type": crop,
        "Nitrogen": nitrogen,
        "Potassium": potassium,
        "Phosphorus": phosphorus,
    }])
    pred = model.predict(row)[0]
    st.success("Recommended fertilizer: " + pred)
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(row)[0]
        classes = model.classes_
        table = pd.DataFrame({"Fertilizer": classes, "Probability": proba})
        st.write(table.sort_values("Probability", ascending=False))
    st.info(f"Entered pH {ph} was stored for the form only.")
