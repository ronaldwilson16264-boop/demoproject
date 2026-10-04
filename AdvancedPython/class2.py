
#Define a class Named Employee with attributes empid, name, age, place, salary, designation and methods getsalary() and showpersonaldetails() create an Employee Object and call the methods..


class Employee:

  def __init__(self):
    print("Enter Employee Details")
    self.empid = int(input("Enter the ID"))
    self.name = input("Enter name")
    self.age = int(input("Enter age"))
    self.place = input("Enter place")
    self.salary = int(input("Enter salary"))
    self.designation = input("Enter designation")

  def getsalary(self):
    print("Salary", self.salary)

  def showpersonaldetails(self):
    print("Name", self.name, "Age", self.age, "Place", self.place)


e = Employee()

e.getsalary()
e.showpersonaldetails()