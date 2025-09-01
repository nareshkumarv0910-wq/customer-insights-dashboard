# ------------------ SETUP ------------------
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
https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1920&q=80
st.markdown("""
    <style>
        body {
            background-image: url('https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1920&q=80');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        .stApp {
            background-color: rgba(12, 12, 20, 0.85);
        }
    </style>
""", unsafe_allow_html=True)


st.markdown("## 📊 Customer Insights Dashboard")

region_data = pd.DataFrame({
    "Region": ["North", "South", "East", "West"],
    "Sales": [12000, 9500, 7800, 11000]
})

monthly_data = pd.DataFrame({
    "Month": pd.date_range(start="2023-01-01", periods=6, freq="M"),
    "Sales": [8000, 9500, 11000, 10500, 12000, 13000]
})

segment_data = pd.DataFrame({
    "Segment": ["Premium", "Regular", "Budget"],
    "Spend": [4200, 2800, 1300]
})

funnel_data = pd.DataFrame({
    "Stage": ["Visitors", "Leads", "Purchases"],
    "Count": [10000, 2500, 600]
})

ratings = pd.DataFrame({
    "Rating": [5, 4, 3, 5, 2, 4, 5, 3, 4, 5, 1, 2, 3, 4, 5]
})

total_sales = int(region_data["Sales"].sum())
growth_rate = (monthly_data["Sales"].iloc[-1] - monthly_data["Sales"].iloc[-2]) / monthly_data["Sales"].iloc[-2]
conversion_rate = funnel_data["Count"].iloc[2] / funnel_data["Count"].iloc[0]
avg_rating = ratings["Rating"].mean()

st.markdown("### 🔢 Key Performance Indicators")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Sales", f"{total_sales:,}")
kpi2.metric("MoM Growth", f"{growth_rate:.1%}")
kpi3.metric("Conversion Rate", f"{conversion_rate:.1%}")
kpi4.metric("Avg Rating", f"{avg_rating:.2f} ⭐")

st.markdown("---")
st.markdown("### 🏢 Sales by Region")
fig1 = px.bar(region_data, x="Region", y="Sales", color="Region", title="Sales by Region")
st.plotly_chart(fig1, use_container_width=True)

st.markdown("### 🧍‍♂️ Spend by Customer Segment")
fig2 = px.pie(segment_data, names="Segment", values="Spend", title="Spend by Segment")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("### 📈 Monthly Sales Trend")
fig3 = px.line(monthly_data, x="Month", y="Sales", markers=True, title="Monthly Sales Trend")
st.plotly_chart(fig3, use_container_width=True)

st.markdown("### 🔁 Conversion Funnel")
fig4 = px.funnel(funnel_data, x="Count", y="Stage", title="Conversion Funnel")
st.plotly_chart(fig4, use_container_width=True)

st.markdown("### ⭐ Product Rating Distribution")
fig5 = px.histogram(ratings, x="Rating", nbins=5, title="Product Rating Distribution")
st.plotly_chart(fig5, use_container_width=True)

st.markdown("""
    <hr>
    <div style='text-align:center; font-size:13px; color:#888;'>Built by Naresh Kumar • Powered by Streamlit</div>
""", unsafe_allow_html=True)
