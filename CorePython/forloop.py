# Print numbers from 1 to 10
for i in range(1, 11):
    print(i)


# Print even numbers from 1 to 10
for i in range(2, 11, 2):
    print(i)


# Question: Print odd numbers from 1 to 10
for i in range(1, 11, 2):
    print(i)


# Question: Print numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)


# Find the sum of numbers from 1 to 10

total = 0
for i in range(1, 11):
    total += i
print(total)


# Print all elements of a list
numbers = [10, 20, 30, 40, 50]
for i in numbers:
    print(i)


# Print even numbers from a list

numbers = [10, 23, 45, 60, 72]
for i in numbers:
    if i % 2 == 0:
        print(i)


# Find the largest number in a list
numbers = [10, 45, 23, 78, 34]
largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print(largest)


# Count vowels in a string
word = "python programming"
count = 0

for i in word:
    if i in "aeiou":
        count += 1

print(count)


# Find the sum of digits
number = 12345
total = 0

for i in str(number):
    total += int(i)

print(total)




# 0, 1, 2, 3, 4
for i in range(5):
    print(i)

# 1, 2, 3, 4, 5
for i in range(1, 6):
    print(i)

# 2, 4, 6, 8, 10
for i in range(2, 11, 2):
    print(i)

# 1, 3, 5, 7, 9
for i in range(1, 10, 2):
    print(i)

# 5, 10, 15, 20, 25
for i in range(5, 26, 5):
    print(i)

# 3, 6, 9, 12, 15
for i in range(3, 16, 3):
    print(i)

# 10, 20, 30, 40, 50
for i in range(10, 51, 10):
    print(i)

# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
for i in range(10, 0, -1):
    print(i)

# 10, 8, 6, 4, 2
for i in range(10, 1, -2):
    print(i)

# 9, 7, 5, 3, 1
for i in range(9, 0, -2):
    print(i)

# 1, 4, 7, 10, 13
for i in range(1, 14, 3):
    print(i)

# 2, 7, 12, 17
for i in range(2, 18, 5):
    print(i)

# 100, 200, 300, 400, 500
for i in range(100, 501, 100):
    print(i)

# 100, 90, 80, 70, 60, 50
for i in range(100, 49, -10):
    print(i)

# -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
for i in range(-5, 6):
    print(i)

# -1, -2, -3, -4, -5
for i in range(-1, -6, -1):
    print(i)

# 1, 4, 9, 16, 25
for i in range(1, 6):
    print(i ** 2)

# 1, 8, 27, 64, 125
for i in range(1, 6):
    print(i ** 3)