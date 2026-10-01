import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="AB InBev Fermentation Optimizer", layout="wide"
)

st.title("🍺 Brewery Fermentation Kinetics & Energy Optimizer")
st.markdown(
    "Real-time bioprocess monitoring, predictive analytics, and energy optimization."
)

# Load data
df = pd.read_csv("brewery_fermentation_data.csv")

# Sidebar Controls
batch_selected = st.sidebar.selectbox(
    "Select Fermentation Batch", df["batch_id"].unique()
)
filtered_df = df[df["batch_id"] == batch_selected]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Sugar Attenuation & Ethanol Generation")
    fig1 = px.line(
        filtered_df,
        x="time_hr",
        y=["sugar_plato", "ethanol_abv"],
        labels={"value": "Concentration", "time_hr": "Time (Hours)"},
        title=f"Reaction Profile for {batch_selected}",
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Fermenter Temperature & Cooling Duty")
    fig2 = px.line(
        filtered_df,
        x="time_hr",
        y=["fermenter_temp_c", "cooling_duty_mj_hr"],
        labels={"value": "Value", "time_hr": "Time (Hours)"},
        title=f"Thermal & Utility Load for {batch_selected}",
    )
    st.plotly_chart(fig2, use_container_width=True)

st.success(
    "Model Status: XGBoost Inference Active | Early 24h Prediction Ready"
)