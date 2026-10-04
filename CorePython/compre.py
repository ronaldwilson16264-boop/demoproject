# List comprehension
l = [1, 2, 3, 4]
# Squares
new = [i**2 for i in l]
print(new)  # [1, 4, 9, 16]

# Cubes
new = [i**3 for i in l]
print(new)  # [1, 8, 27, 64]

# Constant value
new = [5 for i in l]
print(new)  # [5, 5, 5, 5]






l = [1, 2, 3, 4, 5, 6]
# Create a new list with even numbers
evens = [i for i in l if i % 2 == 0] # in each iteration adds i if i is divisible by 2
print(evens)

# Create a new list with odd numbers
odds = [i for i in l if i % 2 != 0] # in each iteration adds i if i is not divisible by 2
print(odds)








colors = ["red", "green", "blue", "yellow"]

# Create a new list with the first letter of each color
first_letters = [color[0] for color in colors]
print(first_letters)

# Create a new list with the length of each color
color_lengths = [len(color) for color in colors]
print(color_lengths)








# Set comprehension


# Given a list with duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]

# Create a set with unique squares (duplicates are automatically removed)
unique_squares = {x**2 for x in numbers}
print(unique_squares)

# Create a set with unique even numbers using a condition
even_set = {x for x in numbers if x % 2 == 0}
print(even_set)

# Given a list of words with duplicates
words = ["apple", "banana", "apple", "cherry", "banana"]

# Create a set with the first letter of each unique word
unique_first_letters = {word[0] for word in words}
print(unique_first_letters)

# Create a set with the unique lengths of each word
word_lengths = {len(word) for word in words}
print(word_lengths)






# Dictionary comprehension

# Given a list of numbers
numbers = [1, 2, 3, 4, 5]

# Create a dictionary mapping each number to its square
squares_dict = {x: x**2 for x in numbers}
print(squares_dict)

# Create a dictionary mapping only even numbers to their cubes with a condition
even_cubes = {x: x**3 for x in numbers if x % 2 == 0}
print(even_cubes)

# Given a list of words
words = ["apple", "banana", "cherry"]

# Create a dictionary mapping each word to its length
word_lengths = {word: len(word) for word in words}
print(word_lengths)

# Create a dictionary mapping each word to its first letter
first_letter_map = {word: word[0] for word in words}
print(first_letter_map)