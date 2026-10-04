from abc import ABC, abstractmethod


class Shape(ABC):

  @abstractmethod
  def get_area(self):
    pass

  @abstractmethod
  def get_perimeter(self):
    pass


class Rectangle(Shape):

  def __init__(self):
    self.length = int(input("Enter length: "))
    self.breadth = int(input("Enter breadth: "))

  def get_area(self):
    print("Area", self.length * self.breadth)

  def get_perimeter(self):
    print("Perimeter", 2 * (self.length + self.breadth))


class Square(Shape):

  def __init__(self):
    self.side = int(input("Enter side: "))

  def get_area(self):
    print("Area", self.side**2)

  def get_perimeter(self):
    print("Perimeter", 4 * self.side)



r = Rectangle()
r.get_area()
r.get_perimeter()

s = Square()
s.get_area()
s.get_perimeter()