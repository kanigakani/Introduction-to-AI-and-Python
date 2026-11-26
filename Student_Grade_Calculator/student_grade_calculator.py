# STUDENT GRADE CALCULATOR

print("================================")
print("      STUDENT GRADE CALCULATOR")
print("================================")

# Get student details
name = input("Enter Student Name: ")

# Get marks for five subjects
print("\nEnter marks for five subjects (out of 100):")

subject1 = float(input("Subject 1: "))
subject2 = float(input("Subject 2: "))
subject3 = float(input("Subject 3: "))
subject4 = float(input("Subject 4: "))
subject5 = float(input("Subject 5: "))

# Calculate total and average
total = subject1 + subject2 + subject3 + subject4 + subject5
average = total / 5

# Calculate grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Check pass or fail
if all(0 <= mark <= 100 for mark in
       [subject1, subject2, subject3, subject4, subject5]):

    print("\n========== RESULT ==========")
    print("Student Name:", name)
    print("Total Marks:", total, "/ 500")
    print("Average:", average, "%")
    print("Grade:", grade)

    if all(mark >= 35 for mark in
           [subject1, subject2, subject3, subject4, subject5]):
        print("Result: PASS")
    else:
        print("Result: FAIL")

else:
    print("Invalid marks! Enter marks between 0 and 100.")