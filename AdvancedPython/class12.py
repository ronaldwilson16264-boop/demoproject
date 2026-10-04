from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def calculate_salary(self):
        salary = 30000
        return salary


class PartTimeEmployee(Employee):

    def calculate_salary(self):
        hours = 100
        rate = 200
        return hours * rate


full_time = FullTimeEmployee()
part_time = PartTimeEmployee()

print("Full Time Employee Salary:", full_time.calculate_salary())
print("Part Time Employee Salary:", part_time.calculate_salary())