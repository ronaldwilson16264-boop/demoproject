# Inheritance


class Parent:

  def m1(self):
    print("In Parent class method m1")

  def m2(self):
    print("In Parent Class method m2")




class Child(Parent):
  pass


c = Child()


c.m1()
c.m2()