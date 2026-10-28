# Retail Sales and Profitability Analysis

## 1. Project Overview

This project analyzes retail sales data to understand sales performance, profitability, regional trends, product category performance, and the relationship between discounts and profit.

The analysis uses Python, Pandas, Matplotlib, and Seaborn to clean the dataset, calculate business metrics, and generate visualizations.

## 2. Dataset Information

- **Dataset:** Superstore Sales Dataset
- **Total records:** 9,994
- **Total columns:** 21
- **Missing values:** None detected
- **Duplicate rows:** None detected in the original dataset
- **Main metrics:** Sales, Profit, Quantity, and Discount

The dataset includes order details, customer information, product categories, regions, sales values, discounts, and profits.

## 3. Data Cleaning and Preparation

The following steps were performed:

- Inspected the dataset structure and column names.
- Checked for missing values and duplicate records.
- Removed duplicate rows, with zero duplicates found.
- Converted Order Date and Ship Date into date formats.
- Verified that Sales and Profit columns were available.
- Saved the cleaned dataset as `superstore_sales_cleaned.csv`.

## 4. Key Business Findings

### Overall Performance

- **Total sales:** $2,297,200.86
- **Total profit:** $286,397.02
- **Distinct orders:** 5,009
- **Overall profit margin:** 12.47%

The dataset generated approximately $2.30 million in sales and $286,397 in profit. The overall profit margin indicates that profit represented about 12.47% of total sales.

### Category Performance

Technology recorded the highest sales at $836,154.03 and the highest profit at $145,454.95.

Office Supplies generated $719,047.03 in sales and $122,490.80 in profit.

Furniture generated $741,999.80 in sales but only $18,451.27 in profit.

**Finding:** Furniture had substantial sales but comparatively low profit. This category deserves further investigation into product costs, discounting, and pricing.

### Regional Performance

- **West:** $725,457.82 in sales and $108,418.45 in profit.
- **East:** $678,781.24 in sales and $91,522.78 in profit.
- **Central:** $501,239.89 in sales and $39,706.36 in profit.
- **South:** $391,721.90 in sales and $46,749.43 in profit.

**Finding:** The West region recorded the highest sales and profit. The Central region generated less profit than the other regions, suggesting an opportunity to investigate its product mix, pricing, and discount patterns.

### Discount Analysis

The correlation between discount and profit was approximately **-0.219**, indicating a negative relationship between discount levels and profit in this dataset.

Several higher-discount groups recorded negative average profits. For example, records with a 70% discount had an average profit of approximately -$95.87.

**Finding:** Large discounts may reduce profitability. The business should review discount policies and assess whether heavily discounted products generate sufficient returns.

Correlation does not establish causation, and the relationship may also be affected by product type, order size, and other factors.

### Sub-Category Performance

- **Most profitable sub-category:** Copiers
- **Least profitable sub-category:** Tables

**Finding:** Copiers are a strong candidate for further sales and profitability analysis. Tables may require a review of pricing, costs, and discount strategies.

## 5. Visualizations Created

The project generates the following charts:

1. Sales by Category
2. Profit by Region
3. Monthly Sales Trend
4. Top Products by Sales
5. Discount vs. Profit
6. Profit by Sub-Category

These visualizations help communicate business performance and