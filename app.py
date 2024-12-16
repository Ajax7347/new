import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Page configuration
st.set_page_config(page_title="Sample Dashboard", layout="wide")

# Add title
st.title("📊 Sample Analytics Dashboard")

# Create some sample data
def generate_sample_data():
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    data = {
        'Date': dates,
        'Sales': np.random.randint(100, 1000, size=len(dates)),
        'Customers': np.random.randint(10, 100, size=len(dates)),
        'Category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Books'], size=len(dates))
    }
    return pd.DataFrame(data)

# Load data
df = generate_sample_data()

# Sidebar filters
st.sidebar.header("Filters")
selected_category = st.sidebar.multiselect(
    "Select Category",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)

# Filter the data
filtered_df = df[df['Category'].isin(selected_category)]

# Create three columns
col1, col2, col3 = st.columns(3)

# KPI metrics
with col1:
    st.metric("Total Sales", f"${filtered_df['Sales'].sum():,}")
with col2:
    st.metric("Average Daily Sales", f"${filtered_df['Sales'].mean():.2f}")
with col3:
    st.metric("Total Customers", f"{filtered_df['Customers'].sum():,}")

# Create charts
# Sales over time
st.subheader("Sales Trend")
fig_sales = px.line(filtered_df, x='Date', y='Sales', color='Category')
st.plotly_chart(fig_sales, use_container_width=True)

# Sales by category
st.subheader("Sales by Category")
fig_category = px.pie(filtered_df.groupby('Category')['Sales'].sum().reset_index(), 
                     values='Sales', names='Category')
st.plotly_chart(fig_category, use_container_width=True)

# Raw data
st.subheader("Raw Data")
st.dataframe(filtered_df)