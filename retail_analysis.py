import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

# Clean
df.dropna(inplace=True)

# Revenue by product
product_sales = df.groupby("Item_Type")["Item_Outlet_Sales"].sum()

print(product_sales)

# Plot
product_sales.sort_values().plot(kind="barh")
plt.title("Sales by Product Type")
plt.show()

# Save summary
product_sales.to_csv("sales_summary.csv")
