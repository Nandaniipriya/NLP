''''
Question 1: You are given a dataset containing information about customer transactions, 
including CustomerID, TransactionDate, and TransactionAmount. 
Write a Python script to perform the following tasks:
a) Identify the top 5 customers who spent the most (TransactionAmount) over the entire period.
b) Plot a bar chart showing the spending of these top 5 customers.

'''
import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "CustomerID": [101, 102, 103, 101, 104, 105, 102, 103, 101],
    "TransactionDate": [
        "2024-01-01", "2024-01-02", "2024-01-03",
        "2024-02-01", "2024-02-02", "2024-02-03",
        "2024-03-01", "2024-03-02", "2024-03-03"
    ],
    "TransactionAmount": [200, 150, 300, 400, 500, 250, 100, 450, 300],
}

# Step 1: Create DataFrame
df = pd.DataFrame(data)
df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])

# Step 2: Calculate total spending per customer
total_spending = df.groupby("CustomerID")["TransactionAmount"].sum()

# Step 3: Get the top 5 customers by spending
top_customers = total_spending.nlargest(5)

# Step 4: Plot the spending of top 5 customers
plt.figure(figsize=(8, 5))
top_customers.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Top 5 Customers by Spending", fontsize=14)
plt.xlabel("CustomerID", fontsize=12)
plt.ylabel("Total Spending", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()


  