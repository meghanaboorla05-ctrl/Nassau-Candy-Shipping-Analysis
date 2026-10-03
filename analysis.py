import pandas as pd
import matplotlib.pyplot as plt

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

# Calculate shipping lead time
df["Shipping Lead Time"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

# Shipping Mode Analysis
ship_mode = df.groupby("Ship Mode").agg(
    Orders=("Order ID", "nunique"),
    Sales=("Sales", "sum"),
    Units=("Units", "sum"),
    Gross_Profit=("Gross Profit", "sum")
)

print("\nShipping Mode Analysis:")
print(ship_mode)

# Graph 1: Sales by Shipping Mode
ship_mode["Sales"].plot(kind="bar")
plt.title("Sales by Shipping Mode")
plt.xlabel("Shipping Mode")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Region Analysis
region = df.groupby("Region").agg(
    Orders=("Order ID", "nunique"),
    Sales=("Sales", "sum"),
    Units=("Units", "sum"),
    Gross_Profit=("Gross Profit", "sum")
)

print("\nRegion Analysis:")
print(region)

# Graph 2: Sales by Region
region["Sales"].plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
# State-wise Analysis

state = df.groupby("State/Province").agg(
    Orders=("Order ID", "nunique"),
    Sales=("Sales", "sum"),
    Units=("Units", "sum"),
    Gross_Profit=("Gross Profit", "sum")
)

# Sort by sales
state = state.sort_values("Sales", ascending=False)

print("\nTop 10 States by Sales:")
print(state.head(10))
# Graph: Top 10 States by Sales

state.head(10)["Sales"].sort_values().plot(kind="barh")

plt.title("Top 10 States by Sales")
plt.xlabel("Sales")
plt.ylabel("State")
plt.tight_layout()
plt.show()
# Product Division Analysis
division = df.groupby("Division").agg(
    Orders=("Order ID", "nunique"),
    Sales=("Sales", "sum"),
    Units=("Units", "sum"),
    Gross_Profit=("Gross Profit", "sum")
)

division = division.sort_values("Sales", ascending=False)

print("\nProduct Division Analysis:")
print(division)
# Graph: Sales by Product Division
division["Sales"].plot(kind="bar")

plt.title("Sales by Product Division")
plt.xlabel("Product Division")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()
# Profit Analysis by Shipping Mode
profit_mode = df.groupby("Ship Mode")["Gross Profit"].sum()

print("\nGross Profit by Shipping Mode:")
print(profit_mode)
# Graph: Gross Profit by Shipping Mode
profit_mode.plot(kind="bar")

plt.title("Gross Profit by Shipping Mode")
plt.xlabel("Shipping Mode")
plt.ylabel("Gross Profit")

plt.tight_layout()
plt.show()
# Profit Analysis by Region
profit_region = df.groupby("Region")["Gross Profit"].sum()

print("\nGross Profit by Region:")
print(profit_region)
# Graph: Gross Profit by Region
profit_region.plot(kind="bar")

plt.title("Gross Profit by Region")
plt.xlabel("Region")
plt.ylabel("Gross Profit")

plt.tight_layout()
plt.show()
# City-wise Sales Analysis
city = df.groupby("City")["Sales"].sum()

city = city.sort_values(ascending=False)

print("\nTop 10 Cities by Sales:")
print(city.head(10))
# Graph: Top 10 Cities by Sales
city.head(10).sort_values().plot(kind="barh")

plt.title("Top 10 Cities by Sales")
plt.xlabel("Sales")
plt.ylabel("City")

plt.tight_layout()
plt.show()
# Shipping Lead Time Analysis
print("\nShipping Lead Time Analysis:")

print("Minimum days:", df["Shipping Lead Time"].min())
print("Maximum days:", df["Shipping Lead Time"].max())
print("Average days:", df["Shipping Lead Time"].mean())
print("Median days:", df["Shipping Lead Time"].median())
# Graph: Shipping Lead Time Distribution
df["Shipping Lead Time"].plot(kind="hist", bins=20)

plt.title("Shipping Lead Time Distribution")
plt.xlabel("Shipping Lead Time (Days)")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.show()
# Final Project Findings
print("\n========== FINAL PROJECT FINDINGS ==========")

print("\n1. Total Sales:")
print(round(df["Sales"].sum(), 2))

print("\n2. Total Gross Profit:")
print(round(df["Gross Profit"].sum(), 2))

print("\n3. Total Orders:")
print(df["Order ID"].nunique())

print("\n4. Top 5 States by Sales:")
print(state.head(5)["Sales"])

print("\n5. Sales by Region:")
print(region["Sales"])

print("\n6. Gross Profit by Shipping Mode:")
print(profit_mode)

print("\n============================================")
# Save analysis results to CSV files

state.to_csv("state_sales_analysis.csv")
region.to_csv("region_sales_analysis.csv")
ship_mode.to_csv("shipping_mode_analysis.csv")
division.to_csv("division_sales_analysis.csv")

print("\nAnalysis results saved successfully!")