# ApexPlanet Task 1 - Data Wrangling

## Project Overview

This project focuses on data immersion, data quality assessment, cleaning, transformation, and preparation of a sales dataset for analysis.

## Objective

The objective of this task is to acquire, understand, clean, transform, and prepare the provided dataset for analysis.

## Dataset

The dataset contains sales transaction information, including:

- Order ID
- Order Date
- Customer ID
- Customer Name
- Age
- Gender
- City
- Product
- Category
- Quantity
- Unit Price
- Total Sales

## Data Quality Assessment

The dataset was checked for:

- Missing values
- Duplicate records
- Inconsistent formatting
- Outliers
- Sales calculation mismatches

## Data Cleaning & Transformation

The following steps were performed:

- Checked and handled data quality issues
- Standardized date-related fields
- Checked numerical columns for outliers
- Verified sales calculations
- Created Year, Month, and Month Name fields
- Prepared the final dataset for analysis

## Project Files

```text
ApexPlanet-Task-1-Data-Wrangling/
│
├── data/
│   ├── Raw Data.xlsx
│   └── Cleaned_ApexPlanet_Sales_Dataset.xlsx
│
├── documentation/
│   └── Data_Dictionary.xlsx
│
├── notebook/
│   └── Data_Wrangling.ipynb
│
├── scripts/
│   └── data_cleaning.py
│
└── README.md

## Results

The final cleaned dataset contains 1,000 records and 15 columns.

Sales calculation mismatches found: **0**

## Tools Used

- Python
- Pandas
- Jupyter Notebook / Google Colab
- Microsoft Excel
- GitHub
