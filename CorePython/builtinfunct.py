# Find the count of a specific character in a string
text = "hello world"
char_count = text.count("l")
print(char_count)

# Create a dictionary where keys are letters and values are their counts
word = "banana"
letter_counts = {char: word.count(char) for char in word}
print(letter_counts)

# Create a new list with 5 random 3-digit numbers
import random
random_3digit_nums = [random.randint(100, 999) for _ in range(5)]
print(random_3digit_nums)

# Create a 5-digit OTP number
otp = random.randint(10000, 99999)
print(otp)





# Count letters, spaces, and digits using generator expressions with built-in string methods
text = "Python 3 is fun!"

letter_count = 0
space_count = 0
digit_count = 0


for char in text:
    if char.isalpha():
        letter_count += 1
    elif char.isspace():
        space_count += 1
    elif char.isdigit():
        digit_count += 1

print(f"Letters: {letter_count}")
print(f"Spaces: {space_count}")
print(f"Digits: {digit_count}")




# write a program to create a dictionary were keys are words and values are length of each word

text = "python coding is easy and fun"
word_lengths = {}

for word in text.split():
    word_lengths[word] = len(word)

print(word_lengths)





#Largest element
#Second largest element
#Smallest element
#Second smallest element

l = [34, 12, 56, 89, 90, 11]

largest  = print("Maximum:", max(l))
smallest = print("Minimum:", min(l))

l.sort()
print("sorted", l)
print("Second maximum:", l[-2])
print("Second minimum:", l[1])





# Given a list
l = [1, 1, 1, 2, 3, 3, 4, 5]

# remove duplicates from list
s = set(l)
print(s)
print("Updated List", list(s))

# Given a list
l = [1, 1, 1, 2, 3, 3, 4, 5]

# remove duplicates without set()
unique_l = []
for item in l:
    if item not in unique_l:
        unique_l.append(item)
print("Updated List without set", unique_l)

# Given two lists print common elements
l1 = [23, 45, 78, 90, 12, 74]
l2 = [45, 89, 23, 56, 34]

s1 = set(l1)
s2 = set(l2)
print("common elements", s1.intersection(s2))