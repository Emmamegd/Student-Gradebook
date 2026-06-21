# Student Gradebook Program
# This program collects student names and grades,
# calculates averages and letter grades,
# and prints a formatted grade report.

print("=== Student Gradebook ===")

students = []
max_students = 5

# Collect student records
while len(students) < max_students:
    print(f"\nEnter information for Student #{len(students) + 1}")

    name = input("Student name: ")
    course = input("Course name: ")

    grade1 = float(input("Enter Grade 1: "))
    grade2 = float(input("Enter Grade 2: "))

    average = (grade1 + grade2) / 2

    # Decision rules for letter grades
    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"

    students.append([name, course, grade1, grade2, average, letter])

    if len(students) < max_students:
        choice = input("Add another student? (y/n): ").lower()
        if choice != "y":
            break

# Output report
print("\n=== Gradebook Report ===")
print(f"{'Name':<15}{'Course':<15}{'Grade 1':<10}{'Grade 2':<10}{'Average':<10}{'Letter'}")
print("-" * 70)

total_avg = 0
highest_avg = students[0][4]
lowest_avg = students[0][4]

for student in students:
    print(f"{student[0]:<15}{student[1]:<15}{student[2]:<10.2f}{student[3]:<10.2f}{student[4]:<10.2f}{student[5]}")
    total_avg += student[4]

    if student[4] > highest_avg:
        highest_avg = student[4]
    if student[4] < lowest_avg:
        lowest_avg = student[4]

class_average = total_avg / len(students)

# Summary
print("\n=== Summary ===")
print(f"Class Average: {class_average:.2f}")
print(f"Highest Average: {highest_avg:.2f}")
print(f"Lowest Average: {lowest_avg:.2f}")