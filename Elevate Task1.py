import pandas as pd

# Load dataset
df = pd.read_csv(r"D:\Campaign.csv", sep="\t")

print("Original Shape:", df.shape)

# =========================
# 1. Check Missing Values
# =========================
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing Income values with median
df['Income'] = df['Income'].fillna(df['Income'].median())

# =========================
# 2. Remove Duplicates
# =========================
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

df.drop_duplicates(inplace=True)

# =========================
# 3. Standardize Text Columns
# =========================
df['Education'] = df['Education'].str.title()
df['Marital_Status'] = df['Marital_Status'].str.title()

# =========================
# 4. Convert Date Format
# =========================
df['Dt_Customer'] = pd.to_datetime(
    df['Dt_Customer'],
    format='%d-%m-%Y'
)

# =========================
# 5. Rename Columns
# =========================
df.columns = (
    df.columns
    .str.lower()
    .str.replace(" ", "_")
)

# =========================
# 6. Check Data Types
# =========================
print("\nData Types:")
print(df.dtypes)

# =========================
# 7. Remove Impossible Ages
# =========================
current_year = 2026

df['age'] = current_year - df['year_birth']

df = df[(df['age'] >= 18) & (df['age'] <= 100)]

# =========================
# 8. Save Cleaned Dataset
# =========================
df.to_csv(r"D:\customer_personality_cleaned.csv", index=False)

print("\nFinal Shape:", df.shape)
print("Dataset Cleaned Successfully!")