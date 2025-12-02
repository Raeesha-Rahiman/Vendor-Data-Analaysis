# Vendor Performance Analysis
# Overview
This project aims to analyze and report on vendor performance using a complete data pipeline built with Python, MySQL, and Power BI. The project includes data extraction, transformation and analysis, and the creation of an interactive report for deep insights into vendor efficiency and compliance.



## 🎯 Objectives
Assess and compare vendor performance on key metrics.
Identify top and low-performing vendors using visual analytics.
Generate actionable insights to improve procurement and supply chain decisions.

- ## 🗂️ Dataset Description
| Table Name | Description |
|-------------|--------------|
| **purchases** | Purchase transactions including purchase date, vendor, brand, quantity, and amount. |
| **purchase_prices** | Actual vs purchase price for each vendor-brand combination. |
| **vendor_invoice** | Vendor-level invoice summary including freight and total cost. |
| **sales** | Sales transactions with brand, sales quantity, selling price, and revenue. |

## 🧰 Tools & Technologies
SQL (Common Table Expressions, Joins, Filtering)
Python (Pandas, Matplotlib, Seaborn, SciPy)
Power BI (Interactive Visualizations)

## Project Structure 
```

📂 Vendor-Data-Analysis
│
├── 📁 data/
│   ├── purchases.csv
│   ├── purchase_prices.csv
│   ├── vendor_invoice.csv
│   └── sales.csv
│
├── 📁 sql/
│   ├── data_ingestion.sql
│   ├── data_cleaning_etl.sql
│   └── kpi_calculation_queries.sql
│
├── 📁 notebooks/
│   └── vendor_performance_analysis.ipynb  ← main Jupyter notebook
│
├── 📁 visuals/
│   ├── vendor_sales_vs_freight.png
│   ├── top_brands_chart.png
│   └── PowerBI_Dashboard.pbix
│
├── requirements.txt
└── README.md
```

## 🔄 Workflow Description

| Step | Stage | Tool | Description |
|------|--------|------|--------------|
| **1. Data Loading** | Data files (CSV) were imported into SQL database | **SQL (MySQL / SQLite / PostgreSQL)** | Loaded all raw data tables 
| **2. Data Connection** | SQL–Python link created | **Python (SQLAlchemy)** | Created a **database engine** in Jupyter Notebook to connect Python with SQL for querying and ingestion. |
| **3. Data Ingestion & ETL** | Transformation & Cleaning | **SQL** | Cleaned duplicates, handled null values, calculated freight %, and joined tables for unified dataset. |
| **4. Data Analysis** | Exploratory Data Analysis (EDA) | **Python + SQL in Jupyter** | Used `pandas`, `numpy`, and SQL queries for descriptive statistics and trend analysis. |
| **5. Hypothesis Testing** | Statistical validation | **Python (scipy.stats)** | Performed hypothesis testing to evaluate if **freight costs significantly affect sales performance**. |
| **6. Visualization & Dashboard** | Business insights | **Power BI** | Designed an interactive dashboard highlighting vendor sales, freight %, and profitability comparison. |
| **7. Reporting** | Documentation | **Markdown (README)** | Summarized insights, findings, and recommendations in this GitHub report. |



## 📊 Key Insights

1. **Top Vendors by Sales and Purchases**  
   - Vendor A and Vendor B contribute the highest sales and purchase volumes.  
   - These vendors are critical for revenue generation and procurement efficiency.

2. **Brand Performance**  
   - Brand X and Brand Y consistently achieve the highest sales across multiple vendors.  
   - Highlighting top brands helps focus inventory and marketing strategies.

3. **Freight Cost Analysis**  
   - Vendors with higher freight percentages often show lower net profitability.  
   - Optimizing freight cost can directly improve margins.

4. **Profitability Trends**  
   - Vendor-brand combinations with high sales but low freight show the best profitability.  
   - This analysis identifies which vendors to prioritize for scale-up.

5. **Statistical Insights (Hypothesis Testing)**  
   - Freight cost has a measurable impact on sales performance (p-value < 0.05).  
   - Data-driven decisions can be made to negotiate freight rates or adjust pricing strategies.
  

# Dashboard 

<img width="926" height="552" alt="vendor performance dashboard" src="https://github.com/user-attachments/assets/0610d3ef-748f-4d55-aa5e-98a47e52b2b7" />


## Author
**Raeesha Rahiman**  
Aspiring Data Analyst | Skilled in SQL, Python, and Power BI  
📍 Abu Dhabi 


---
