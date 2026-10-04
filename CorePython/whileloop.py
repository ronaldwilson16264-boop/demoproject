# Write a program to print the first 10 integers using a while loop.

num = 1

while num <= 10:
    print(num)
    num += 1

# Write a program to print the first 10 even numbers.
i = 2
while i <= 20:
    print(i,end=",")
    i += 2

# 1, 4, 7, 10, 13, 16
i = 1
while i <= 16:
    print(i, end=",")
    i += 3


# 10, 20, 30, 40, 50, 60, 70, 80
i = 10
while i <= 80:
    print(i, end=",")
    i += 10


# 3, 6, 9, 12, 15, 18, 21
i = 3
while i <= 21:
    print(i, end=",")
    i += 3


# 5, 4, 3, 2, 1
i = 5
while i >= 1:
    print(i, end=",")
    i -= 1



# Print all 4-digit numbers (1000 to 9999)
i = 1000
while i <= 9999:
    print(i, end=",")
    i += 1


# Print 3-digit numbers that are divisible by 3
i = 100
while i <= 999:
    if i % 3 == 0:
        print(i, end=",")
    i += 1


# Print 4-digit numbers that contain the digit '3'
i = 1000
while i <= 9999:
    if '3' in str(i):
        print(i, end=",")
    i += 1


# print the numbers that are divisible by 3 and 5 in the range (1, 100) 
i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
    i += 1


# program to print the square numbers sequence: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 
i = 1
while i <= 10:
    print(i ** 2, end=",")
    i += 1


# print all 3-digit numbers that contain the digit '3'
i = 100
while i <= 999:
    if '3' in str(i):
        print(i, end=",")
    i += 1

# program to print all 2-digit numbers where both digits are even 
i = 10
while i <= 99:
    d1 = i // 10
    d2 = i % 10
    if d1 % 2 == 0 and d2 % 2 == 0:
        print(i, end=",")
    i += 1