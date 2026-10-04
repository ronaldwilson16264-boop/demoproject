l = [23, 45, 12, 78, 90, 51, 75]

# Print all numbers
for i in l:
    print(i)

# Print all even numbers
for i in l:
    if i % 2 == 0:
        print(i)

# Print those numbers that are divisible by 5
for i in l:
    if i % 5 == 0:
        print(i)

# Stops the loop if i > 50
for i in l:
    if i > 50:
        break
    print(i)

# Skips all even numbers
for i in l:
    if i % 2 == 0:
        continue
    print(i)

# Print the first even number whose value is greater than 50
for i in l:
    if i > 50 and i % 2 == 0:
        print(i)
        break