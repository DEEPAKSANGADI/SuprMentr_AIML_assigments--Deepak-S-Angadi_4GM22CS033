import pandas as pd
import numpy as np

df = pd.read_csv('Assignment_24_02_2026_csv_file.csv')

print("Top 5 rows of the dataset:")
print(df.head())

print("\nHighest value column:")
numeric_df = df.select_dtypes(include=[np.number])
highest_col = numeric_df.max().idxmax()
highest_value = numeric_df.max().max()
print(f"Column: {highest_col}, Value: {highest_value}")

print("\nMissing values count:")
missing = df.isnull().sum()
if missing.sum() == 0:
    print("No missing values found")
else:
    print(missing[missing > 0])

print("\n=== 5 KEY INSIGHTS ===")
print(f"1. Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"2. Total missing values: {df.isnull().sum().sum()}")
print(f"3. Duplicate rows: {df.duplicated().sum()}")
print(f"4. Data types:\n{df.dtypes}")
print(f"5. Numeric summary:\n{numeric_df.describe()}")