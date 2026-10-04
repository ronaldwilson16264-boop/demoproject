# Inheritance


class Parent:

  def m1(self):
    print("In Parent class method m1")

  def m2(self):
    print("In Parent Class method m2")


# p=Parent()
# p.m1()
# p.m2()


class Child(Parent):

  def m3(self):
    print("in child class m3")


c = Child()


c.m1()
c.m2()
c.m3()