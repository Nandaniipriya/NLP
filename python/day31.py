"""
Question:
You are given a dataset containing information about employees. Each entry is a dictionary representing a record for an employee, 
and the dataset is stored in a dictionary of lists, where each list holds a list of records.
"""
data = {
    "Employee_ID": [1, 2, 3, 4, 5, 6, 7],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"],
    "Department": ["HR", "Engineering", "Engineering", "HR", "Finance", "Finance", "Engineering"],
    "Salary": [50000, 75000, 80000, 60000, 85000, 90000, 95000],
    "Experience_Years": [5, 3, 8, 4, 12, 10, 6]
}
import pandas as pd

# Dataset as a dictionary
data = {
    "Employee_ID": [1, 2, 3, 4, 5, 6, 7],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"],
    "Department": ["HR", "Engineering", "Engineering", "HR", "Finance", "Finance", "Engineering"],
    "Salary": [50000, 75000, 80000, 60000, 85000, 90000, 95000],
    "Experience_Years": [5, 3, 8, 4, 12, 10, 6]
}

# Step 1: Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Step 2: Find the average salary for each department
avg_salary_by_dept = df.groupby("Department")["Salary"].mean()

# Step 3: Find the department with the highest average salary
highest_avg_salary_dept = avg_salary_by_dept.idxmax()

# Step 4: Sort employees by their years of experience and get the top 3
top_experience_employees = df.sort_values("Experience_Years", ascending=False).head(3)

# Display the results
print("Average salary by department:\n", avg_salary_by_dept)
print("\nDepartment with the highest average salary:", highest_avg_salary_dept)
print("\nTop 3 employees with the most experience:\n", top_experience_employees)
