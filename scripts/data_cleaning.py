
import pandas as pd

# 1. Load Dataset
df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

# 2. Handle Missing Values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["City"] = df["City"].fillna("Unknown")

# 3. Remove Duplicate Records
df = df.drop_duplicates()

# 4. Clean Text Columns
text_columns = [
    "Order_ID",
    "Customer_ID",
    "Customer_Name",
    "Gender",
    "City",
    "Product",
    "Category"
]

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

# 5. Standardize Categorical Columns
df["Gender"] = df["Gender"].str.title()
df["City"] = df["City"].str.title()
df["Category"] = df["Category"].str.title()

# 6. Convert Order_Date to Datetime
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

# 7. Feature Engineering
df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.month_name()

# 8. Validate Sales Calculation
df["Calculated_Sales"] = (
    df["Quantity"] * df["Unit_Price"]
).round(2)

df["Sales_Difference"] = (
    df["Total_Sales"] - df["Calculated_Sales"]
).round(2)

print(
    "Sales Calculation Mismatches:",
    (df["Sales_Difference"] != 0).sum()
)

# 9. Remove Temporary Validation Columns
df.drop(
    columns=[
        "Calculated_Sales",
        "Sales_Difference"
    ],
    inplace=True
)

# 10. Final Validation
print("Missing Values:")
print(df.isnull().sum())

print("Duplicate Rows:", df.duplicated().sum())

# 11. Save Cleaned Dataset
df.to_excel(
    "Cleaned_ApexPlanet_Sales_Dataset.xlsx",
    index=False
)

print("Data cleaning completed successfully!")
print("Final Dataset Shape:", df.shape)
