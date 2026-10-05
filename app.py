import streamlit as st
import pandas as pd

# Page title
st.title("Nassau Candy Distributor Analysis")

st.write(
    "Analysis of shipping modes, regions, states, cities, "
    "product divisions, sales and gross profit."
)

# Load dataset
df = pd.read_csv("Nassau Candy Distributor.csv")

# Convert dates
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True,
    errors="coerce"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    dayfirst=True,
    errors="coerce"
)

# Shipping lead time
df["Shipping Lead Time"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days


# ------------------------------------------------
# Dataset Preview
# ------------------------------------------------

st.header("1. Dataset Preview")

st.dataframe(df.head(10))


# ------------------------------------------------
# Key Metrics
# ------------------------------------------------

st.header("2. Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Orders", df["Order ID"].nunique())
col2.metric("Total Sales", f"${df['Sales'].sum():,.2f}")
col3.metric("Total Gross Profit", f"${df['Gross Profit'].sum():,.2f}")


# ------------------------------------------------
# Sales by Shipping Mode
# ------------------------------------------------

st.header("3. Sales by Shipping Mode")

ship_mode = df.groupby("Ship Mode")["Sales"].sum()

st.bar_chart(ship_mode)


# ------------------------------------------------
# Sales by Region
# ------------------------------------------------

st.header("4. Sales by Region")

region = df.groupby("Region")["Sales"].sum()

st.bar_chart(region)


# ------------------------------------------------
# Top 10 States
# ------------------------------------------------

st.header("5. Top 10 States by Sales")

state = (
    df.groupby("State/Province")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(state)


# ------------------------------------------------
# Sales by Product Division
# ------------------------------------------------

st.header("6. Sales by Product Division")

division = df.groupby("Division")["Sales"].sum()

st.bar_chart(division)


# ------------------------------------------------
# Gross Profit by Shipping Mode
# ------------------------------------------------

st.header("7. Gross Profit by Shipping Mode")

profit_mode = df.groupby("Ship Mode")["Gross Profit"].sum()

st.bar_chart(profit_mode)


# ------------------------------------------------
# Gross Profit by Region
# ------------------------------------------------

st.header("8. Gross Profit by Region")

profit_region = df.groupby("Region")["Gross Profit"].sum()

st.bar_chart(profit_region)


# ------------------------------------------------
# Top 10 Cities
# ------------------------------------------------

st.header("9. Top 10 Cities by Sales")

city = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(city)


# ------------------------------------------------
# Shipping Lead Time
# ------------------------------------------------

st.header("10. Shipping Lead Time")

st.write(
    "The dataset contains inconsistent order and ship dates, "
    "so this metric should not be interpreted as actual delivery time."
)

st.write("Minimum recorded days:", df["Shipping Lead Time"].min())
st.write("Maximum recorded days:", df["Shipping Lead Time"].max())
st.write("Average recorded days:", round(df["Shipping Lead Time"].mean(), 2))

st.bar_chart(
    df["Shipping Lead Time"].value_counts().sort_index()
)


# ------------------------------------------------
# Data Limitations
# ------------------------------------------------

st.header("11. Data Limitations")

st.write(
    "The dataset does not contain a factory or shipment-origin "
    "location, so actual factory-to-customer routes cannot be analyzed."
)

st.write(
    "The recorded order and ship dates also appear inconsistent. "
    "The date differences should therefore be validated before "
    "being treated as actual delivery times."
)
