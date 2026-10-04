class Category:

  def __init__(self):
    self.category_name = input("Enter category:")

  def show_category(self):
    print("Category name", self.category_name)


class Product(Category):

  def __init__(self):
    super().__init__()
    self.product_name = input("Enter product name:")
    self.price = int(input("Enter Price:"))
    self.quantity = int(input("Enter quantity:"))

  def total_price(self):
    print("Total price", self.price * self.quantity)


p = Product()
p.total_price()
p.show_category()