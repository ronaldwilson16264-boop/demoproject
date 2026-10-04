class Hospital:

  def __init__(self):
    self.hos_name = input("Enter Hospital name: ")
    self.location = input("Enter location: ")
    self.phone = int(input("Enter Phone: "))

  def display_hospital(self):
    print("Hospital Name", self.hos_name)


class Department:

  def __init__(self):
    self.department_name = input("Enter department name: ")
    self.doctor_name = input("Enter Doctor name: ")

  def display_department(self):
    print(
        "Department name", self.department_name, "Doctor name", self.doctor_name
    )


class Patient(Hospital, Department):

  def __init__(self):
    Hospital.__init__(self)
    Department.__init__(self)
    # patient properties
    self.patient_name = input("Enter Patient name: ")
    self.age = int(input("Enter age: "))
    self.gender = input("Enter gender: ")
    self.admission_date = input("Enter admission date: ")
    self.bedno = input("Enter Bed number: ")
    self.discharge_date = ""

  def full_summary(self):
    print("Hospital Details")
    Hospital.display_hospital(self)
    print("Department Details")
    Department.display_department(self)
    print("Patient Details")
    print("Patient name", self.patient_name)
    print("Age", self.age)
    print("Gender", self.gender)
    print("Admission Date", self.admission_date)
    print("Bed number", self.bedno)
    if self.discharge_date == "":
      print("Not yet Discharge")
    else:
      print("Discharge date", self.discharge_date)

  def set_discharge(self):
    self.discharge_date = input("Enter Discharge date: ")


p = Patient()
p.full_summary()
p.set_discharge()
p.full_summary()