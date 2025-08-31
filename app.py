import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Insights Dashboard", layout="wide")
st.title("📊 Customer Insights Dashboard")

data = {
    "Region": ["North", "South", "East", "West"],
    "Sales": [12000, 9500, 7800, 11000],
    "Profit": [3000, 2500, 1800, 2700]
}
df = pd.DataFrame(data)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Region")
    fig_sales = px.bar(df, x="Region", y="Sales", color="Region")
    st.plotly_chart(fig_sales, use_container_width=True)

with col2:
    st.subheader("Profit by Region")
    fig_profit = px.bar(df, x="Region", y="Profit", color="Region")
    st.plotly_chart(fig_profit, use_container_width=True)

st.markdown("---")
st.caption("Built by Naresh Kumar • Powered by Streamlit")
