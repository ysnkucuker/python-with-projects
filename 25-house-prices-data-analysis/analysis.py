import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1️⃣ Load dataset
df = pd.read_csv("data/train.csv")

# 2️⃣ Basic dataset information
print("Dataset information:")
print(df.info())

print("\nStatistical summary:")
print(df.describe())

# 3️⃣ Missing value analysis
print("\nMissing values per column:")
missing = df.isnull().sum().sort_values(ascending=False)
missing = missing[missing > 0]
print(missing.head(10))

# 4️⃣ Handle missing values
# Fill numerical column with mean
df["LotFrontage"] = df["LotFrontage"].fillna(df["LotFrontage"].mean())


# Drop columns with too many missing values
df.drop(columns=["Alley", "PoolQC", "Fence", "MiscFeature"], inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum().sum())

# 5️⃣ Price statistics
average_price = df["SalePrice"].mean()
median_price = df["SalePrice"].median()
std_price = df["SalePrice"].std()

print(f"\nAverage house price: {average_price:.2f}")
print(f"Median house price: {median_price:.2f}")
print(f"Standard deviation of prices: {std_price:.2f}")

# 6️⃣ Relationship between house quality and price
plt.figure()
plt.scatter(df["OverallQual"], df["SalePrice"])
plt.xlabel("Overall Quality Score")
plt.ylabel("Sale Price")
plt.title("House Quality vs Sale Price")
plt.show()

# 7️⃣ House age analysis
df["HouseAge"] = df["YrSold"] - df["YearBuilt"]

plt.figure()
plt.hist(df["HouseAge"], bins=30)
plt.xlabel("House Age")
plt.ylabel("Number of Houses")
plt.title("Distribution of House Ages")
plt.show()

# 8️⃣ Neighborhood-based price analysis
price_by_neighborhood = (
    df.groupby("Neighborhood")["SalePrice"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(8, 5))
price_by_neighborhood.plot(kind="barh")
plt.xlabel("Average Sale Price")
plt.title("Average House Prices by Neighborhood")
plt.show()

print("\nAnalysis completed successfully.")
