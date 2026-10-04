#Define a class named Book with attributes title, author, price, pages, language and methods gettitle(), getauthor(), getprice(), settitle(), setauthor(), setprice().

class Book:

  def getprice(self):
    print(self.price)

  def settitle(self):
    self.title = input("Enter the new title")
    self.gettitle()

  def setauthor(self):
    self.author = input("Enter the new author ")
    self.getauthor()

  def setprice(self):
    self.price = int(input("Enter new price"))
    self.getprice()



b = Book()
b.gettitle()

b.settitle()
