class Person:

  def __init__(self):  # __init__ used to create and initialize
    # object attributes/properties

    self.name = input("Enter name")
    self.age = int(input("Enter age"))

  def show(self):  
    print(self.name, self.age)


# dynamic input

p1 = Person() 

p2 = Person()  

p1.show()

p2.show()