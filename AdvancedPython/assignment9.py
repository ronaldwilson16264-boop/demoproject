#Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.



class Student:
    def __init__(self,rollno,name,marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks
    def display(self):
        print("Roll no:",self.rollno)
        print("Name:",self.name)
        print("Marks:",self.marks)

students =[]

while True:
    print("\n1.Add Student")
    print("2.Update Marks")
    print("3.Display All Student Details")
    print("4.Search student By Roll Number")
    print("5.Delete Student")
    print("6.Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        rollno = int(input("Enter roll number:"))
        name = input("Enter name:")
        marks = float(input("Enter marks:"))
        s = Student(rollno,name,marks)
        students.append(s)

        print("Student added successfully")




    elif choice == 2:
            rollno = int(input("Enter roll number:"))
            for s in students:
                 if s.rollno == rollno:
                      marks = float(input("Enter new marks"))
                      s.marks = marks
                      print("Marks updated successfully")
                      break
            else:
                 print("Student not found")





    elif choice == 3:
                for s in students:
                    s.display()




    elif choice == 4:
                rollno = int(input("Enter roll number:"))
                for s in students:
                    if s.rollno == rollno:
                          s.display()
                          break
                else:
                      print("Student not found")

    elif choice == 5:
                rollno = int(input("Enter roll number:"))
                for s in students:
                    if s.rollno == rollno:
                          students.remove(s)
                          print("Student deleted successfully")
                          break
                else:
                          print("student not found")

    elif choice == 6:
          print("program exited")
          break
    else:
          print("Invalid choice")
    