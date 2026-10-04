import math

try:
    num = int(input("Enter a number: "))
    print("Factorial:", math.factorial(num))

except ValueError:
    print("Invalid input. Please enter a number.")