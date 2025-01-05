"""
Week 1 – Sales KPI Calculator
Author: JKWebfolio
Date: 2025-01-06 
Description:
    This script reads sales data from sales_data.csv,
    calculates KPIs, and generates summary tables and charts.
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Load the dataset
data_file = "../data/sales_data.csv"
df = pd.read_csv(data_file)

# 2. Calculate KPIs
# Total revenue per salesperson
revenue_per_salesperson = df.groupby("Salesperson")["Revenue"].sum()

# Total revenue per product
revenue_per_product = df.groupby("Product")["Revenue"].sum()

# Top-selling product
top_product = revenue_per_product.idxmax()

# Daily sales trend
daily_sales = df.groupby("Date")["Revenue"].sum()

# 3. Print summaries
print("Revenue per Salesperson:\n", revenue_per_salesperson)
print("\nRevenue per Product:\n", revenue_per_product)
print("\nTop-selling product:", top_product)
print("\nDaily Sales Trend:\n", daily_sales)

# 4. Generate charts (saved to outputs/charts/)
output_dir = "../outputs/charts/"
os.makedirs(output_dir, exist_ok=True)

# Revenue per salesperson bar chart
revenue_per_salesperson.plot(kind="bar", title="Revenue per Salesperson")
plt.savefig(os.path.join(output_dir, "revenue_per_salesperson.png"))
plt.clf()

# Revenue per product bar chart
revenue_per_product.plot(kind="bar", title="Revenue per Product", color="green")
plt.savefig(os.path.join(output_dir, "revenue_per_product.png"))
plt.clf()

# Daily sales trend line chart
daily_sales.plot(kind="line", marker="o", title="Daily Sales Trend")
plt.savefig(os.path.join(output_dir, "daily_sales_trend.png"))
plt.clf()
