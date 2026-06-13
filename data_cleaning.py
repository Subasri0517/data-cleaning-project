import pandas as pd

# Load dataset
df = pd.read_csv("raw_data.csv")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing age with average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Validate emails
df = df[df["Email"].str.contains("@", na=False)]

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("Data Cleaning Completed Successfully!")
