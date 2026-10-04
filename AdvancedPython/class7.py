class Person:

  def __init__(self):
    self.name = input("Enter name:")
    self.age = int(input("Enter age:"))

  def show(self):
    print("Name:", self.name, "Age:", self.age)


class Student(Person):

  def __init__(self):
    super().__init__()
    self.rollno = int(input("Enter roll number:"))
    self.course = input("Enter course:")
    self.mark = int(input("Enter mark:"))

  def show(self):
    super().show()
    print("Roll No:", self.rollno, "Mark:", self.mark, "Course:", self.course)

  def updatemark(self):
    self.mark = int(input("Enter new mark:"))

s = Student()
s.show()
s.updatemark()
