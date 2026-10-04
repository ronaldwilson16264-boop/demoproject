class Company:

  def __init__(self):
    self.company_name = input("Enter company name:")
    self.location = input("Enter location:")

  def display_company(self):
    print(self.company_name, self.location)


class Employee(Company):

  def __init__(self):
    super().__init__()
    self.empid = int(input("Enter id:"))
    self.name = input("Enter name:")
    self.designation = input("Enter designation:")
    self.salary = int(input("Enter salary:"))

  def display_details(self):
    super().display_company()
    print(self.empid, self.name, self.salary, self.designation)

  def update_salary(self):
    self.salary = 1.1 * self.salary
    print("Updated Salary", self.salary)


e = Employee()
e.display_details()
e.update_salary()