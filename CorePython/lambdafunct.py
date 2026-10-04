# Sum of 2 numbers
s = lambda n1, n2: n1 + n2
print(s(7, 8))

# product of 3 numbers
s = lambda n1, n2, n3: n1 * n2 * n3
print(s(7, 8, 9))

# length of a string
s = lambda n: len(n)
print(s("hello"))

# square root of a number
s = lambda n: n ** 0.5
print(s(16))

# first letter of a string
s = lambda n: n[0]
print(s("hello"))

# last letter of a string
s = lambda n: n[-1]
print(s("hello"))

# name value from dictionary
s = lambda a: a.get('name')
d = {'name': 'arun', 'age': 23, 'salary': 30000}
print(s(d))

# salary value from dictionary
s = lambda a: a.get('salary')
print(s(d))

# add 10 to a number
s = lambda n: n + 10
print(s(23))