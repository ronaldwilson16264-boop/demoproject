#Define a class Named Student with attributes rollno, name, mark1, mark2, mark3 and method display() to display roll no and total mark of a student create 2 student objects and call the methods

class Student:

  def __init__(self):
    print("Enter Student Details")
    self.rollno = int(input("Enter roll no: "))
    self.name = input("Enter name: ")
    self.mark1 = int(input("Enter mark1: "))
    self.mark2 = int(input("Enter mark2: "))
    self.mark3 = int(input("Enter mark3: "))

  def display(self):
    total = self.mark1 + self.mark2 + self.mark3
    print("Roll No:", self.rollno, "Total Mark:", total)



s1 = Student()
s2 = Student()

s1.display()
s2.display()