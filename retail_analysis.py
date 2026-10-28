
import pandas as pd
import os

# Load the retail sales dataset
file_path = os.path.join("data", "superstore_sales.csv")
df = pd.read_csv(file_path, encoding="latin1")

print("=" * 50)
print("RETAIL SALES & PROFITABILITY ANALYSIS")
print("=" * 50)

# 1. Display the first five records
print("\n1. FIRST FIVE ROWS")
print(df.head())

# 2. Dataset dimensions
print("\n2. DATASET SHAPE")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 3. Column names
print("\n3. COLUMN NAMES")
print(df.columns.tolist())

# 4. Dataset information
print("\n4. DATASET INFORMATION")
df.info()

# 5. Missing values
print("\n5. MISSING VALUES")
print(df.isnull().sum())

# 6. Duplicate records
print("\n6. DUPLICATE ROWS")
print(df.duplicated().sum())

# 7. Numerical summary
print("\n7. NUMERICAL SUMMARY")
print(df.describe())

print("\nInitial dataset inspection completed!")

# ============================================
# DATA CLEANING AND PREPARATION
# ============================================

print("\n" + "=" * 50)
print("DATA CLEANING AND PREPARATION")
print("=" * 50)

# Remove duplicate rows
duplicates_before = df.duplicated().sum()
df = df.drop_duplicates()

print(f"\nDuplicate rows removed: {duplicates_before}")

# Convert date columns when they exist
for column in ["Order Date", "Ship Date"]:
    if column in df.columns:
        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )
        print(f"{column} converted to date format.")

# Check missing values
print("\nMissing values after duplicate removal:")
print(df.isnull().sum())

# Check for important sales columns
required_columns = ["Sales", "Profit"]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    print("\nWarning: Expected columns not found:", missing_columns)
else:
    print("\nSales and Profit columns are available.")

# Save the prepared dataset
os.makedirs("data", exist_ok=True)

df.to_csv(
    "data/superstore_sales_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved to:")
print("data/superstore_sales_cleaned.csv")
print("\nData preparation completed!")

# ============================================
# RETAIL SALES ANALYSIS - VISUALIZATIONS
# ============================================

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", context="notebook")
os.makedirs("visualizations", exist_ok=True)

# Load the cleaned dataset
clean_df = pd.read_csv("data/superstore_sales_cleaned.csv")

# Convert numerical columns safely
for column in ["Sales", "Profit", "Discount", "Quantity"]:
    if column in clean_df.columns:
        clean_df[column] = pd.to_numeric(
            clean_df[column], errors="coerce"
        )

print("\nCreating retail sales visualizations...")

# 1. Total sales by product category
if {"Category", "Sales"}.issubset(clean_df.columns):
    category_sales = (
        clean_df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(
        category_sales.index,
        category_sales.values,
        color=sns.color_palette("viridis", len(category_sales))
    )

    ax.bar_label(
        bars,
        labels=[f"${v:,.0f}" for v in category_sales.values],
        padding=3
    )
    ax.set_title("Total Sales by Product Category", weight="bold")
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Total Sales ($)")
    ax.grid(axis="y", alpha=0.25)
    sns.despine()
    plt.tight_layout()
    plt.savefig("visualizations/01_sales_by_category.png", dpi=300)
    plt.show()
    plt.close()

# 2. Profit by region
if {"Region", "Profit"}.issubset(clean_df.columns):
    region_profit = (
        clean_df.groupby("Region")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(
        region_profit.index,
        region_profit.values,
        color=sns.color_palette("crest", len(region_profit))
    )
    ax.axhline(0, color="black", linewidth=0.8)
    ax.bar_label(
        bars,
        labels=[f"${v:,.0f}" for v in region_profit.values],
        padding=3
    )
    ax.set_title("Total Profit by Region", weight="bold")
    ax.set_xlabel("Region")
    ax.set_ylabel("Total Profit ($)")
    ax.grid(axis="y", alpha=0.25)
    sns.despine()
    plt.tight_layout()
    plt.savefig("visualizations/02_profit_by_region.png", dpi=300)
    plt.show()
    plt.close()

# 3. Monthly sales trend
if {"Order Date", "Sales"}.issubset(clean_df.columns):
    clean_df["Order Date"] = pd.to_datetime(
        clean_df["Order Date"], errors="coerce"
    )

    monthly_sales = (
        clean_df.dropna(subset=["Order Date"])
        .set_index("Order Date")["Sales"]
        .resample("ME")
        .sum()
    )

    if not monthly_sales.empty:
        fig, ax = plt.subplots(figsize=(13, 6))
        ax.plot(
            monthly_sales.index,
            monthly_sales.values,
            color="#2878B5",
            linewidth=2.5
        )
        ax.fill_between(
            monthly_sales.index,
            monthly_sales.values,
            alpha=0.15,
            color="#2878B5"
        )
        ax.set_title("Monthly Sales Trend", weight="bold")
        ax.set_xlabel("Month")
        ax.set_ylabel("Total Sales ($)")
        ax.grid(alpha=0.25)
        sns.despine()
        plt.tight_layout()
        plt.savefig("visualizations/03_monthly_sales_trend.png", dpi=300)
        plt.show()
        plt.close()

# 4. Top 10 products by sales
product_column = next(
    (col for col in ["Product Name", "Product"] if col in clean_df.columns),
    None
)

if product_column and "Sales" in clean_df.columns:
    top_products = (
        clean_df.groupby(product_column)["Sales"]
        .sum()
        .nlargest(10)
        .sort_values()
    )

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.barh(
        top_products.index,
        top_products.values,
        color=sns.color_palette("mako", len(top_products))
    )
    ax.set_title("Top 10 Products by Total Sales", weight="bold")
    ax.set_xlabel("Total Sales ($)")
    ax.set_ylabel("Product")
    ax.grid(axis="x", alpha=0.25)
    sns.despine()
    plt.tight_layout()
    plt.savefig("visualizations/04_top_products_by_sales.png", dpi=300)
    plt.show()
    plt.close()

# 5. Discount versus profit
if {"Discount", "Profit"}.issubset(clean_df.columns):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        data=clean_df,
        x="Discount",
        y="Profit",
        alpha=0.45,
        s=35,
        color="#E76F51",
        ax=ax
    )
    ax.axhline(0, color="black", linestyle="--", linewidth=1)
    ax.set_title("Relationship Between Discounts and Profit", weight="bold")
    ax.set_xlabel("Discount")
    ax.set_ylabel("Profit ($)")
    sns.despine()
    plt.tight_layout()
    plt.savefig("visualizations/05_discount_vs_profit.png", dpi=300)
    plt.show()
    plt.close()
if {"Sub-Category", "Sales", "Profit"}.issubset(clean_df.columns):
    subcategory = (
        clean_df.groupby("Sub-Category")[["Sales", "Profit"]]
        .sum()
        .sort_values("Profit")
    )

    fig, ax = plt.subplots(figsize=(12, 8))
    subcategory["Profit"].plot(
        kind="barh",
        ax=ax,
        color=[
            "#E76F51" if value < 0 else "#1DB954"
            for value in subcategory["Profit"]
        ]
    )
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_title("Profitability by Product Sub-Category", weight="bold")
    ax.set_xlabel("Total Profit ($)")
    ax.set_ylabel("Sub-Category")
    ax.grid(axis="x", alpha=0.25)
    sns.despine()
    plt.tight_layout()
    plt.savefig("visualizations/06_profit_by_subcategory.png", dpi=300)
    plt.show()
    plt.close()

print("\nVisualization generation completed!")
print("Check the visualizations folder for saved charts.")

# ============================================
# KEY BUSINESS INSIGHTS
# ============================================

print("\n" + "=" * 55)
print("KEY BUSINESS INSIGHTS")
print("=" * 55)

# Overall performance
total_sales = clean_df["Sales"].sum()
total_profit = clean_df["Profit"].sum()
total_orders = (
    clean_df["Order ID"].nunique()
    if "Order ID" in clean_df.columns
    else len(clean_df)
)

print(f"\nTotal Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Number of Orders/Records: {total_orders:,}")

if total_sales != 0:
    profit_margin = (total_profit / total_sales) * 100
    print(f"Overall Profit Margin: {profit_margin:.2f}%")

# Best-performing category
if {"Category", "Sales", "Profit"}.issubset(clean_df.columns):
    category_summary = clean_df.groupby("Category").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )

    print("\nCATEGORY PERFORMANCE")
    print(category_summary.round(2))

    print(
        "\nHighest-sales category:",
        category_summary["Total_Sales"].idxmax()
    )
    print(
        "Highest-profit category:",
        category_summary["Total_Profit"].idxmax()
    )

# Regional performance
if {"Region", "Sales", "Profit"}.issubset(clean_df.columns):
    region_summary = clean_df.groupby("Region").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )

    print("\nREGIONAL PERFORMANCE")
    print(region_summary.round(2))

    print(
        "\nHighest-profit region:",
        region_summary["Total_Profit"].idxmax()
    )

# Discount analysis
if {"Discount", "Profit"}.issubset(clean_df.columns):
    print("\nDISCOUNT ANALYSIS")

    discount_summary = clean_df.groupby("Discount").agg(
        Average_Profit=("Profit", "mean"),
        Total_Profit=("Profit", "sum"),
        Record_Count=("Profit", "size")
    ).sort_index()

    print(discount_summary.round(2))

    correlation = clean_df[["Discount", "Profit"]].corr().iloc[0, 1]
    print(f"\nDiscount-profit correlation: {correlation:.3f}")

# Most and least profitable sub-categories
if {"Sub-Category", "Profit"}.issubset(clean_df.columns):
    subcategory_profit = clean_df.groupby("Sub-Category")["Profit"].sum()

    print("\nSUB-CATEGORY INSIGHTS")
    print("Most profitable:", subcategory_profit.idxmax())
    print("Least profitable:", subcategory_profit.idxmin())

print("\nBusiness insights calculation completed!")
