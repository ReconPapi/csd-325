
import json

# Print student list
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Load JSON file

with open('Student.json', 'r') as file:
    students = json.load(file)

print("\nOriginal Student List:")
print_students(students)

# Add new student
new_student = {
    "F_Name": "Robert",
    "L_Name": "Ruiz",
    "Student_ID": 246810,
    "Email": "thisemailisfake.bellevue.edu"
}

students.append(new_student)

print("\nUpdated Student List:")
print_students(students)

# Print .json file was updated
with open("Student.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nJSON file updated.")