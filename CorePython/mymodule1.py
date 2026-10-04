from Shapes import circle
from Shapes import rectangle

r = float(input("Enter radius: "))

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))

print("Circle area:", circle.area(r))
print("Circle perimeter:", circle.perimeter(r))

print("Rectangle area:", rectangle.area(l, b))
print("Rectangle perimeter:", rectangle.perimeter(l, b))