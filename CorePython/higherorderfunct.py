#create a new list of cubes
l = [1, 2, 3, 4]
print(list(map(lambda x: x**3, l)))

#create a new list of square roots
l = [25, 36, 81, 100]
print(list(map(lambda x: x**0.5, l)))

#create a new list of lengths
colors = ['red', 'green', 'blue', 'yellow', 'black']
print(list(map(lambda x: len(x), colors)))

#create a new list of first characters
print(list(map(lambda x: x[0], colors)))

#create a new list of last characters
print(list(map(lambda x: x[-1], colors)))

#create a new list of reverse of each element
print(list(map(lambda x: x[::-1], colors)))



#Given a list l=[23,78,12,56]
l = [23, 78, 12, 56]

#Add 10 to each element in the given sequence
print(list(map(lambda x: x + 10, l)))

#given a list of dictionaries
l = [
    {'empid': 100, 'name': 'arun', 'salary': 20000, 'email': 'arun@gmail.com'},
    {'empid': 101, 'name': 'amal', 'salary': 25000, 'email': 'amal@gmail.com'},
    {'empid': 102, 'name': 'anu', 'salary': 30000, 'email': 'anu@gmail.com'}
]

#create a new list of emails
print(list(map(lambda x: x.get('email'), l)))

#create a new list of names
print(list(map(lambda x: x.get('name'), l)))

#create a new list of salaries
print(list(map(lambda x: x.get('salary'), l)))







# Filter elements greater than 50
l = [23, 65, 89, 12, 20, 33, 85, 40]

# Normal Code
new = []
for i in l:
    if i > 50:
        new.append(i)
print("Filter > 50 (Normal Code):", new)

# Comprehension
new = [i for i in l if i > 50]
print("Filter > 50 (Comprehension):", new)

# Filter
print("Filter > 50 (Lambda):", list(filter(lambda x: x > 50, l)))
print("-" * 50)



# Filter even values less than 50

# Normal Code
new = []
for i in l:
    if i < 50 and i % 2 == 0:
        new.append(i)
print("Filter even < 50 (Normal Code):", new)

# Comprehension
new = [i for i in l if i < 50 and i % 2 == 0]
print("Filter even < 50 (Comprehension):", new)

# Filter
print("Filter even < 50 (Lambda):", list(filter(lambda x: x < 50 and x % 2 == 0, l)))
print("-" * 50)




# Filter elements whose length is greater than 5
fruits = ['apple', 'orange', 'pineapple', 'grapes', 'avocado']

# Normal Code
new = []
for i in fruits:
    if len(i) > 5:
        new.append(i)
print("Fruits len > 5 (Normal Code):", new)

# Comprehension
new = [i for i in fruits if len(i) > 5]
print("Fruits len > 5 (Comprehension):", new)

# Filter
print("Fruits len > 5 (Lambda):", list(filter(lambda x: len(x) > 5, fruits)))



