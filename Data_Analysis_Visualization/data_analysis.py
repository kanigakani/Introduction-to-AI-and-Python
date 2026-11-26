import pandas as pd

# Load the dataset
data = pd.read_csv("student_performance.csv")

# Display the complete dataset
print("========== STUDENT DATASET ==========")
print(data)

# Display first five records
print("\n========== FIRST FIVE RECORDS ==========")
print(data.head())

# Display dataset information
print("\n========== DATASET INFORMATION ==========")
data.info()

# Display statistical summary
print("\n========== STATISTICAL SUMMARY ==========")
print(data.describe())


import numpy as np

print("\n========== NUMPY ANALYSIS ==========")

# Calculate subject averages
python_avg = np.mean(data["Python"])
java_avg = np.mean(data["Java"])
ds_avg = np.mean(data["Data_Science"])

print("Python Average:", python_avg)
print("Java Average:", java_avg)
print("Data Science Average:", ds_avg)

# Find highest and lowest marks
all_marks = data[["Python", "Java", "Data_Science"]].to_numpy()

print("Highest Mark:", np.max(all_marks))
print("Lowest Mark:", np.min(all_marks))

# Calculate overall average
print("Overall Average:", np.mean(all_marks))

print("\n========== DATA CLEANING ==========")

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(data.duplicated().sum())

# Remove duplicate records
data = data.drop_duplicates()

# Fill missing numerical values with column averages
numeric_columns = ["Python", "Java", "Data_Science", "Attendance"]

for column in numeric_columns:
    data[column] = data[column].fillna(data[column].mean())

# Check the cleaned dataset
print("\nCleaned Dataset:")
print(data)

print("\nMissing Values After Cleaning:")
print(data.isnull().sum())

import matplotlib.pyplot as plt

# Calculate subject averages
subjects = ["Python", "Java", "Data Science"]

averages = [
    data["Python"].mean(),
    data["Java"].mean(),
    data["Data_Science"].mean()
]

# Create bar chart
plt.figure(figsize=(8, 5))

plt.bar(subjects, averages)

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.ylim(0, 100)
plt.grid(axis="y")
plt.savefig("bar_chart.png")

plt.show()

import matplotlib.pyplot as plt

# Calculate subject averages
subjects = ["Python", "Java", "Data Science"]

averages = [
    data["Python"].mean(),
    data["Java"].mean(),
    data["Data_Science"].mean()
]

# Create bar chart
plt.figure(figsize=(8, 5))

plt.bar(subjects, averages)

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.ylim(0, 100)
plt.grid(axis="y")

plt.show()
# LINE CHART - Student Performance in Python

plt.figure(figsize=(10, 5))

plt.plot(data["Name"], data["Python"], marker="o")

plt.title("Student Performance in Python")
plt.xlabel("Student Names")
plt.ylabel("Python Marks")

plt.ylim(0, 100)
plt.xticks(rotation=45)
plt.grid()

plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()

# PIE CHART - Student Attendance

plt.figure(figsize=(8, 6))

plt.pie(
    data["Attendance"],
    labels=data["Name"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Student Attendance Distribution")

plt.savefig("pie_chart.png")
plt.show()