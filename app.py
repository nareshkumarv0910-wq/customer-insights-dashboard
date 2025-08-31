import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Customer Insights Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Sales by Region
region_data = pd.DataFrame({...})

# Monthly Sales
monthly_data = pd.DataFrame({...})

# Customer Segments
segment_data = pd.DataFrame({...})

# Funnel Data
funnel_data = pd.DataFrame({...})

# Product Ratings
ratings = pd.DataFrame({...})
# KPI calculations
total_sales = ...
growth_rate = ...
conversion_rate = ...
avg_rating = ...

# KPI display
st.markdown("## 📊 Customer Insights Dashboard")
st.markdown("### 🔢 Key Performance Indicators")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
...
fig1 = px.bar(...)
st.plotly_chart(fig1)

fig2 = px.pie(...)
st.plotly_chart(fig2)


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
st.markdown("""
    <hr>
    <div style='text-align:center; font-size:13px; color:#888;'>Built by Naresh Kumar • Powered by Streamlit</div>
""", unsafe_allow_html=True)
