import streamlit as st
import pandas as pd
from forecasting import forecast_demand
from inventory_optimizer import calculate_reorder_and_safety_stock

st.title("📦 Warehouse AI – Inventory Forecast Dashboard")

df = pd.read_csv("data/demand_data.csv")
items = df['title'].unique()
item = st.selectbox("Choose an Item", items)

if st.button("Forecast Demand"):
    forecast = forecast_demand(item)
    st.line_chart(forecast.set_index('ds'))

    result = calculate_reorder_and_safety_stock(forecast)
    st.write("**Reorder Point:**", result['Reorder Point'])
    st.write("**Safety Stock:**", result['Safety Stock'])
