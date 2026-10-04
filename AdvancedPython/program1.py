file = open("total_students.txt", "r")
total_students = [student.strip() for student in file.readlines()]
file.close()
file = open("passed_students.txt", "r")
passed_students = [student.strip() for student in file.readlines()]
file.close()
file = open("failed_students.txt", "w")
for student in total_students:
    if student not in passed_students:
        file.write(student + "\n")

file.close()