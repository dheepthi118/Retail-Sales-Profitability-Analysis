# Retail Sales & Profitability Analysis

A Python-based data analytics project that explores retail sales, profitability, regional performance, product categories, and the impact of discounts using the Superstore Sales Dataset.

## Project Overview

This project analyzes retail transaction data to identify business trends and understand the factors associated with sales and profitability. It includes data inspection, cleaning, exploratory data analysis, business insights, and data visualizations.

## Objectives

- Analyze overall retail sales and profit.
- Compare sales and profitability across product categories.
- Evaluate regional sales and profit performance.
- Investigate the relationship between discounts and profit.
- Identify the most and least profitable product sub-categories.
- Present findings through visualizations and a business report.

## Dataset

The project uses the Superstore Sales Dataset.

- **Records:** 9,994
- **Columns:** 21
- **Key fields:** Order Date, Ship Date, Region, Category, Sub-Category, Sales, Quantity, Discount, and Profit.
- **Missing values:** None detected.
- **Duplicate rows:** None detected.

The dataset contains retail order and product information used to evaluate business performance.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Visual Studio Code
- Git and GitHub

## Project Structure

```text
Retail-Sales-Profitability-Analysis/
│
├── data/
│   ├── superstore_sales.csv
│   └── superstore_sales_cleaned.csv
│
├── visualizations/
│   ├── 01_sales_by_category.png
│   ├── 02_profit_by_region.png
│   ├── 03_monthly_sales_trend.png
│   ├── 04_top_products_by_sales.png
│   ├── 05_discount_vs_profit.png
│   └── 06_profit_by_subcategory.png
│
├── retail_analysis.py
├── report.md
└── README.md
```

## Key Results

| Metric | Result |
|---|---:|
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Distinct Orders | 5,009 |
| Overall Profit Margin | 12.47% |
| Highest-Sales Category | Technology |
| Highest-Profit Category | Technology |
| Highest-Profit Region | West |
| Most Profitable Sub-Category | Copiers |
| Least Profitable Sub-Category | Tables |

## Key Insights

### 1. Category Performance

Technology generated the highest sales and profit among the three main product categories. Furniture generated considerable sales but comparatively lower profit.

### 2. Regional Performance

The West region recorded the highest total sales and profit. The Central region generated the lowest total profit among the four regions.

### 3. Discount and Profit

The correlation between discount and profit was approximately **-0.219**, indicating a negative relationship in the dataset. Several high-discount groups recorded negative average profits.

Correlation does not prove causation, and other factors may also influence profitability.

### 4. Sub-Category Performance

Copiers were the most profitable sub-category, while Tables were the least profitable based on the analysis.

## Visualizations

The project generates six charts:

1. Sales by Category
2. Profit by Region
3. Monthly Sales Trend
4. Top Products by Sales
5. Discount vs. Profit
6. Profit by Sub-Category

The charts are saved in the `visualizations/` directory.

## How to Run the Project

### Step 1: Install Python

Install Python if it is not already available on your computer.

### Step 2: Install the Required Libraries

Open the terminal in the project folder and run:

```bash
pip install pandas matplotlib seaborn
```

### Step 3: Run the Analysis

```bash
python retail_analysis.py
```

The script inspects and cleans the dataset, generates visualizations, and prints business insights.

Ensure that `data/superstore_sales.csv` is available in the project folder before running the script.

## Business Recommendations

- Review Furniture pricing, costs, and discount strategies.
- Evaluate high-discount transactions to protect profit margins.
- Investigate the factors behind the Central region's lower profitability.
- Explore opportunities to grow sales of profitable products.
- Use regional and category-level insights to support business decisions.

## Conclusion

This project demonstrates how Python-based data analysis can turn retail transaction data into meaningful business insights. The findings highlight differences in category performance, regional profitability, and discount patterns that can support better-informed retail decisions.

## Author

**B.E. Computer Science and Engineering Student**

## Project Purpose

Developed as part of a data analytics internship project to practice data cleaning, exploratory data analysis, visualization, and business insight generation.
