# Count of 3-digit numbers that contain digit '3'
count = 0
for num in range(100, 1000):
    if '3' in str(num):
        count += 1
print("Task 1:", count)



# Count of numbers divisible by 7 or 3 in the range(200, 300)
count = 0
for num in range(200, 300):
    if num % 3 == 0 or num % 7 == 0:
        count += 1
print("Task 2:", count)



# Count of odd numbers divisible by 5 in the range(1, 100)
count = 0
for num in range(1, 100):
    if num % 5 == 0 and num % 2 != 0:
        count += 1
print("Task 3:", count)



# Count of all palindrome numbers in the range(1, 1000)
count = 0
for num in range(1, 1000):
    if str(num) == str(num)[::-1]:
        count += 1
print("Task 4:", count)




# Count of numbers divisible by 3 in the range(1, 50)
count = 0
for num in range(1, 50):
    if num % 3 == 0:
        count += 1
print("Task 5:", count)










# Task 1: Sum of first 5 numbers (1 to 5)
sum_1 = 0
i = 1
while i <= 5:
    sum_1 += i
    i += 1
print("1. Sum of first 5 numbers:", sum_1)

# Task 2: Sum of numbers divisible by 3 in range(1, 50)
sum_2 = 0
i = 1
while i < 50:
    if i % 3 == 0:
        sum_2 += i
    i += 1
print("2. Sum of numbers divisible by 3 (1-50):", sum_2)

# Task 3: Sum of all 3 digit numbers (100 to 999)
sum_3 = 0
i = 100
while i < 1000:
    sum_3 += i
    i += 1
print("3. Sum of all 3-digit numbers:", sum_3)

# Task 4: Sum of first 10 even numbers
sum_4 = 0
count = 0
i = 2
while count < 10:
    sum_4 += i
    i += 2
    count += 1
print("4. Sum of first 10 even numbers:", sum_4)















# Task 1: Product of series 1, 2, 3, 4, 5
prod_1 = 1
i = 1
while i <= 5:
    prod_1 *= i
    i += 1
print("1. Product of series 1,2,3,4,5:", prod_1)

# Task 2: Product of first 10 odd numbers (1, 3, 5, ..., 19)
prod_2 = 1
count = 0
i = 1
while count < 10:
    prod_2 *= i
    i += 2
    count += 1
print("2. Product of first 10 odd numbers:", prod_2)

# Task 3: Product of numbers that contain digit '3' in the range(1, 50)
prod_3 = 1
i = 1
while i < 50:
    if '3' in str(i):
        prod_3 *= i
    i += 1
print("3. Product of numbers containing digit '3' (1-50):", prod_3)

# Task 4: Factorial of a number entered by user
num = int(input("4. Enter a number for factorial: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print("Factorial:", fact)

# Task 5: Multiplication table of a number (up to 10)
num_table = int(input("5. Enter a number for multiplication table: "))
i = 1
while i <= 10:
    print(f"{num_table} x {i} = {num_table * i}")
    i += 1







# Sum of digits of a number entered by user 
num = int(input("Enter a number: "))
sum_digits = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp //= 10

print(f"The sum of the digits of {num} is: {sum_digits}")