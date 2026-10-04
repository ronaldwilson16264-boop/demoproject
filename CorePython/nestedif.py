# Write a program to check whether an entered number is positive even, positive odd, negative even, negative odd, or zero.
num = int(input("Enter an integer: "))

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
elif num < 0:
    if num % 2 == 0:
        print("The number is negative and even.")
    else:
        print("The number is negative and odd.")
else:
    print("The number is zero.")




# Write a program to check whether a number is divisible by 2 and 3, divisible by 2 and not by 3, divisible by 3 and not by 2, or not divisible by both 2 and 3.

num = int(input("Enter a number: "))

if num % 2 == 0:
    if num % 3 == 0:
        print("Divisible by 2 and 3")
    else:
        print("Divisible by 2 and not by 3")
else:
    if num % 3 == 0:
        print("Divisible by 3 and not by 2")
    else:
        print("Not divisible by 2 and 3")