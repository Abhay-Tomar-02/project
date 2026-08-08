import pandas as pd

# 1. Load the CSV file
df = pd.read_csv(r"A:\Pythoncodes\employee.csv")

# Display the dataset
print("Employee Dataset:")
print(df)

# 2. Calculate average salary
average_salary = df["Salary"].mean()
print("\nAverage Salary:", average_salary)

# 3. Count employees in each department
department_count = df["Department"].value_counts()
print("\nEmployees in Each Department:")
print(department_count)

# 4. Filter employees above salary threshold
threshold = 50000

high_salary = df[df["Salary"] > threshold]

print("\nEmployees with Salary Above", threshold)
print(high_salary)

# 5. Export filtered results to a new CSV
high_salary.to_csv("high_salary_employees.csv", index=False)

print("\nResults exported to high_salary_employees.csv")