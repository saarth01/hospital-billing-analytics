# --- Data Cleaning ---

import pandas as pd
df = pd.read_csv("healthcare_dataset.csv")

# 1. Check for duplicate rows and deleting them all
print(df.duplicated().sum())
df.drop_duplicates(inplace = True)

# 2. Check for missing/blank values per column
print(df.isna().sum())

# 3. Detecting nulls
print(df.isnull().sum())

# 4. Fix Column Names (remove spaces, lowercase):
df.columns = [col.strip().lower().replace(" ","_") for col in df.columns]

# 5. Clean Text Data
df["name"] = [str(clean).strip().title() for clean in df["name"]]

# 6. Convert date columns to proper date objects
df["date_of_admission"] = pd.to_datetime(df["date_of_admission"], errors="coerce").dt.date
df["discharge_date"] = pd.to_datetime(df["discharge_date"], errors="coerce").dt.date

print(df.head())

# index=False ensures we don't save an unwanted row-number index column
# Save cleaned dataset to CSV
df.to_csv("cleaned_healthcare_dataset.csv", index=False)
print("💾 Cleaned data successfully")
