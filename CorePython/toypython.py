"""
A toy vendor supplies three types of toys:

Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

The vendor gives a discount of 10% on orders for battery-based toys
if the order is for more than Rs. 1000.

On orders of more than Rs. 100 for key-based toys, a discount of 5% is given,

and a discount of 10% is given on orders for electrical charging based toys
of value more than Rs. 500.

Assume that the numeric codes 1, 2 and 3 are used for battery based toys,
key-based toys, and electrical charging based toys respectively."""

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

code = int(input("Enter product code(1 ,2, or 3):"))
amount = float(input("Enter order amount:"))

discount = 0

if code == 1:
    if amount > 1000:
        discount = amount * 0.10
elif code ==2:
    if amount > 100:
        discount = amount * 0.05
elif code ==3:
    if amount > 500:
        discount = amount * 0.10
else:
    discount = 0

net_amount = amount - discount
print("Net amount to pay:", net_amount)   