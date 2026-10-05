import streamlit as st
import pandas as pd

st.title("Nassau Candy Distributor Analysis")

st.write("Shipping, Sales and Profit Analysis")

df = pd.read_csv("Nassau Candy Distributor.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head(10))

st.subheader("Sales by Shipping Mode")

sales_mode = df.groupby("Ship Mode")["Sales"].sum()
st.bar_chart(sales_mode)

st.subheader("Sales by Region")

sales_region = df.groupby("Region")["Sales"].sum()
st.bar_chart(sales_region)

st.subheader("Top 10 States by Sales")

sales_state = df.groupby("State/Province")["Sales"].sum()
sales_state = sales_state.sort_values(ascending=False).head(10)

st.bar_chart(sales_state)