import csv
import json

students = [
    [1, "Rahul", "CSE", 80, 75, 90],
    [2, "Sneha", "AI", 70, 60, 85],
    [3, "Rohan", "CSE", 65, 76, 92]
]

# Writing data into CSV file
with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Roll No.", "Name", "Branch",
        "Mathematics", "Python", "C++"
    ])

    writer.writerows(students)


# Reading data from CSV file
with open("student.csv", "r") as file:
    data = csv.DictReader(file)

    for row in data:
        m1 = int(row["Mathematics"])
        m2 = int(row["Python"])
        m3 = int(row["C++"])

        total = m1 + m2 + m3
        percentage = (total / 300) * 100

    print("Roll No.:", row["Roll No."])
    print("Name:", row["Name"])
    print("Branch:", row["Branch"])
    print("Total:", total)
    print("Percentage:", percentage)
    print("----------------------")