# Define to find the sum of two numbers

def add():
    n1 = int(input("Enter first number:"))
    n2 = int(input("Enter second number:"))
    s = n1+n2
    print("Sum:",s)

    return
add()




# Display "Hello your name"
def hello():
    print("Hello Arun")

hello()


# Find the count of a specific character in a string
def count_character():
    string = input("Enter a string: ")
    character = input("Enter a character: ")
    count = 0

    for i in string:
        if i == character:
            count += 1

    print("Count =", count)

count_character()


# Find the factorial of a number
def factorial():
    n = int(input("Enter a number: "))
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial =", fact)

factorial()


# Check whether a number is Armstrong or not
def armstrong():
    n = int(input("Enter a number: "))
    temp = n
    sum = 0

    while n > 0:
        digit = n % 10
        sum = sum + digit ** 3
        n = n // 10

    if sum == temp:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

armstrong()



# Check whether a number is prime or not
def prime():
    n = int(input("Enter a number: "))
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        print("Prime number")
    else:
        print("Not a prime number")

prime()


# Find the factors of a number
def factors():
    n = int(input("Enter a number: "))

    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

factors()






#Argument with no return value

# Display "Hello your name"
def hello(name):
    print("Hello", name)

hello("Arun")


# Count a specific character in a string
def count_character(string, character):
    count = 0
    for i in string:
        if i == character:
            count += 1
    print("Count =", count)

count_character("malayalam", "a")


# Find factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print("Factorial =", fact)

factorial(5)


# Check Armstrong number
def armstrong(n):
    temp = n
    sum = 0

    while n > 0:
        digit = n % 10
        sum = sum + digit ** 3
        n = n // 10

    if sum == temp:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

armstrong(153)


# Check prime number
def prime(n):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        print("Prime number")
    else:
        print("Not a prime number")

prime(7)


# Find factors of a number
def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

factors(12)


# Sum of two numbers
def sum(a, b):
    print("Sum =", a + b)

sum(10, 20)


# Area of a rectangle
def area(length, width):
    print("Area =", length * width)

area(10, 5)



# Simple interest
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    print("Simple Interest =", si)

p = int(input("Enter principal: "))
r = int(input("Enter rate: "))
t = int(input("Enter time: "))

simple_interest(p, r, t)


#String and character count
def count_character(string, character):
    count = 0

    for i in string:
        if i == character:
            count += 1

    print("Count =", count)

string = input("Enter a string: ")
character = input("Enter a character: ")

count_character(string, character)

