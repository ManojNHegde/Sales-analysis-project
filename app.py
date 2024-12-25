import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the data from the CSV file
file_path = "sales_data.csv"  # Update this with the actual path to your file
data = pd.read_csv(file_path)

# Step 2: Data Cleaning - Remove canceled orders
data_filtered = data[data["Status"] != "Cancelled"]

# Step 3: Analyze Sales by Category
top_categories = data_filtered.groupby("Category")["Amount"].sum().sort_values(ascending=False)

# Step 4: Analyze Sales by SKU (Individual Products)
top_products = data_filtered.groupby("SKU")["Amount"].sum().sort_values(ascending=False)

# Step 5: Visualization - Top Categories by Sales Amount
plt.figure(figsize=(10, 6))
sns.barplot(x=top_categories.index, y=top_categories.values, palette="viridis")
plt.title("Top Categories by Sales Amount")
plt.xlabel("Category")
plt.ylabel("Total Sales Amount (INR)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Step 6: Visualization - Top Products by Sales Amount
plt.figure(figsize=(10, 6))
sns.barplot(x=top_products.head(10).index, y=top_products.head(10).values, palette="viridis")
plt.title("Top Products by Sales Amount")
plt.xlabel("Product (SKU)")
plt.ylabel("Total Sales Amount (INR)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
