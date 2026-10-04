class Company:
    def _init(self):
        self.companyname=input("Enter company name")
        self.location=input("Enter location")

    def displaycompany(self):
        print(self.companyname,self.location)


class Employee(Company):
    def _init(self):
        super().init()
        self.empid=int(input("Enter id"))
        self.name=input("Enter name")
        self.designation=input("Enter designation")
        self.salary=int(input("Enter salary"))

    def displaydetails(self):
        super().displaycompany()
        print(self.empid,self.name,self.salary,self.designation)
    def updatesalary(self):
        self.salary=1.1*self.salary
        print("Updated Salary",self.salary)

e=Employee()
e.displaydetails()
e.updatesalary()