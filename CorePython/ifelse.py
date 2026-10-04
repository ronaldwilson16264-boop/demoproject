# Write a program to check whether the entered number is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")



# Check if two entered numbers are equal
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 == num2:
  print("The numbers are equal.")
else:
  print("The numbers are not equal.")



# Check if two entered words are equal
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if word1 == word2:
  print("The words are equal.")
else:
  print("The words are not equal.")




# Find the maximum of two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
  print(f"{num1} is the maximum.")
elif num2 > num1:
  print(f"{num2} is the maximum.")
else:
  print("Both numbers are equal.")




# Check whether the entered character is a vowel or not
char = input("Enter a character: ").lower()

if char in "aeiou":
  print(f"'{char}' is a vowel.")
else:
  print(f"'{char}' is not a vowel.")




# Check whether the entered country name contains the word 'land'
country = input("Enter a country name: ").lower()

if "land" in country:
  print("The country name contains 'land'.")
else:
  print("The country name does not contain 'land'.")




# Write a python program to check whether the entered number is 3 digit or not
n = int(input("Enter a number: "))

if n > 99 and n <= 999:
    print(f"{n} is a three digit number")
else:
    print(f"{n} is not a three digit number")


# Check whether the entered string is a palindrome
s = input("Enter a string: ")

if s == s[::-1]:
  print(f"'{s}' is a palindrome.")
else:
  print(f"'{s}' is not a palindrome.")



# Check whether a number is present in the given list
l = [23, 67, 12, 90]
num = int(input("Enter a number to search: "))

if num in l:
  print(f"{num} is present in the list.")
else:
  print(f"{num} is not present in the list.")





# Check whether a key is present in a dictionary
d = {101: "Arun", 102: "Amal", 103: "Anu"}
key = int(input("Enter a key to search: "))

if key in d:
  print(f"Key {key} is present in the dictionary (Value: '{d[key]}').")
else:
  print(f"Key {key} is not present in the dictionary.")



# Write a program to check whether the given password is strong/weak (if length less than 8 then the password is weak)
password = input("Enter the password: ")

if len(password) < 8:
    print("The password is weak.")
else:
    print("The password is strong.")

    