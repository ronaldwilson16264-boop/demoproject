# write a program that takes a number as input from user and finds the factorial of that number 
# using math.factorial().use a try -except block to handle the value error if user inputs a 
# number/character input 
import math

try:
    num = int(input("Enter a number: "))
    print("Factorial:", math.factorial(num))

except ValueError:
    print("Invalid input. Please enter a number.")
 
#Write a Python program to create a simple calculator that performs addition, subtraction, multiplication, 
#and division based on user choice. Handle invalid inputs and division by zero using exception handling. 
 
while True:

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Calculator exited.")
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", a + b)

        elif choice == 2:
            print("Result:", a - b)

        elif choice == 3:
            print("Result:", a * b)

        elif choice == 4:
            try:
                print("Result:", a / b)
            except ZeroDivisionError:
                print("Cannot divide by zero.")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input. Please enter a number.")

# write a program to open a file (text file) in read mode 
# if the file does not exist catch the file exception print the error message file does not 
# exist 
try:

    f = open("k.txt", "r")

    content = f.read()
    print(content)

    f.close()

except FileNotFoundError:
    print("File does not exist.")
 
#Given a Dictionary 
# 
# d={"name':"arun","age":23,"place":"ekm"} 
# Write a program to ask the user to enter a key and display its value. 
# Handle KeyError if key does not exist   do this



d = {"name": "arun", "age": 23, "place": "ekm"}

try:
    key = input("Enter a key: ")
    print("Value:", d[key])

except KeyError:
    print("Key does not exist.")



# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial(). use a try-except block to handle the value error if user inputs a
# number/character input
import math

try:
  n = int(input("Enter a number"))
  r = math.factorial(n)
  print("Factorial", r)

except:
  print("Invalid Input")