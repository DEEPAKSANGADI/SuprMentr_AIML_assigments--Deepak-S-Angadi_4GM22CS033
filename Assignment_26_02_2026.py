import pandas as pd
import numpy as np

data = {
    'Name': ['John', 'jane', 'JOHN', 'John', np.nan, 'Bob'],
    'Email': ['john@email.com', 'jane@email.com', 'john@email.com', 'john@email.com', 'bob@email.com', 'bob@email.com'],
    'Age': [25, 30, np.nan, 25, 35, 28],
    'Salary': [50000, 60000, 55000, 50000, np.nan, 65000]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)
print("\n" + "="*50 + "\n")


df['Age'].fillna(df['Age'].mean(), inplace=True)  # Fill with mean
df['Salary'].fillna(df['Salary'].median(), inplace=True)  # Fill with median
df['Name'].fillna('Unknown', inplace=True)  # Fill with default value

print("After handling missing values:")
print(df)
print("\n" + "="*50 + "\n")


df.drop_duplicates(inplace=True)

print("After removing duplicates:")
print(df)
print("\n" + "="*50 + "\n")

df['Name'] = df['Name'].str.strip().str.title()
df['Email'] = df['Email'].str.strip().str.lower()

print("After standardizing text:")
print(df)

print("\n" + "="*50)
print("WHY DATA CLEANING MATTERS:")
print("="*50)
print("""
1. ACCURACY: Clean data ensures reliable analysis and predictions
2. CONSISTENCY: Standardized format allows proper comparison
3. COMPLETENESS: Handling missing values prevents biased results
4. EFFICIENCY: Removes redundant data, improving performance
5. TRUST: Quality data builds confidence in insights and decisions
6. COMPLIANCE: Clean data helps meet regulatory requirements
""")