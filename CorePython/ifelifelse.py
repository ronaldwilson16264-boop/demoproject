# write a program to check whether the number is positive negetive or zero
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Write a program to find the largest among three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print(f"The largest number is {largest}.")



# write a program to calculate Electricity bill based on the following criteria.
#Units consumed Rates per unit
#<= 100 unit 0
#100-200 5 Rs/unit
#200-300 10 Rs/unit
#Above 300 15Rs/unit

units = int(input("Enter the number of units consumed: "))
bill = 0

if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 5
elif units <= 300:
    bill = (100 * 5) + (units - 200) * 10
else:
    bill = (100 * 5) + (100 * 10) + (units - 300) * 15

print(f"The total electricity bill is: Rs. {bill}")



# Check whether the entered number is a 2-digit, 3-digit, or 4-digit number
num = int(input("Enter an integer: "))

if 10 <= abs(num) <= 99:
    print("The entered number is a 2-digit number.")
elif 100 <= abs(num) <= 999:
    print("The entered number is a 3-digit number.")
elif 1000 <= abs(num) <= 9999:
    print("The entered number is a 4-digit number.")
else:
    print("The number is not a 2, 3, or 4-digit number.")



# Basic calculator program
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /, %, //): ")

if op == '+':
    print(f"Result: {num1 + num2}")
elif op == '-':
    print(f"Result: {num1 - num2}")
elif op == '*':
    print(f"Result: {num1 * num2}")
elif op == '/':
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
elif op == '%':
    print(f"Result: {num1 % num2}")
elif op == '//':
    print(f"Result: {num1 // num2}")
else:
    print("Invalid operator!")



# Print the number of days in a month
l1 = ['january', 'March', 'May', 'july', 'August', 'October', 'December']
l2 = ['April', 'june', 'September', 'November']
l3 = ['February']

month = input("Enter month: ")

if month in l1:
    print(f"{month} has 31 days")
elif month in l2:
    print(f"{month} has 30 days")
elif month in l3:
    print(f"{month} has 28 or 29 days")
else:
    print("Invalid month")


# Print grades based on criteria
marks = float(input("Enter the marks: "))

if 91 <= marks <= 100:
    print("Grade A")
elif 81 <= marks <= 90:
    print("Grade B")
elif 71 <= marks <= 80:
    print("Grade C")
elif 61 <= marks <= 70:
    print("Grade D")
elif marks < 61:
    print("Grade E")
else:
    print("Invalid marks entered.")


# Write a program to calculate the discount on a purchase based on the following criteria:
#Purchase amount up to Rs. 1000: No discount (0%)
#Purchase amount between Rs. 1001 and Rs. 5000: 5% discount
#Purchase amount between Rs. 5001 and Rs. 10000: 10% discount
#Purchase amount above Rs. 10000: 20% discount

amount = float(input("Enter the total purchase amount: Rs. "))

if amount <= 1000:
    discount = 0
elif amount <= 5000:
    discount = 5
elif amount <= 10000:
    discount = 10
else:
    discount = 20

final_amount = amount - (amount * discount / 100)
print(f"Discount applied: {discount}%")
print(f"Final amount to pay: Rs. {final_amount:.2f}")

