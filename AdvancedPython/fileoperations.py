# # #write a program to read a text file and displays the number of lines in a file

file = open("k.txt", "r")

lines = file.readlines()

print("Number of lines:", len(lines))

file.close()

# # #write a program to display the number of words in a file

file = open("k.txt", "r")

text = file.read()

words = text.split()

print("Number of words:", len(words))

file.close()

# # #write a program to update the second line in a file

file = open("k.txt", "r")
lines = file.readlines()
new_line = input("Enter the new second line: ")
lines[1] = new_line + "\n"
file.close()
file = open("k.txt", "w")
file.writelines(lines)
file.close()
print("Second line updated successfully.")


# # #write a program to display the last 5 lines in a file
file = open("k.txt", "r")
lines = file.readlines()
print("Last 5 lines:")
for line in lines[-5:]:
    print(line, end="")

file.close()


# #program to search a particular word in a file
file = open("k.txt", "r")
text = file.read()
word = input("Enter the word to search: ")
if word in text:
    print("Word found")
else:
    print("Word not found")

file.close()


# #find the number of letters,digits,and spaces in a file

file = open("k.txt", "r")

text = file.read()

letters = 0
digits = 0
spaces = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("Letters:", letters)
print("Digits:", digits)
print("Spaces:", spaces)

file.close()

#reverse the lines in a file
file = open("k.txt", "r")
lines = file.readlines()
for line in lines[::-1]:
    print(line, end="")

file.close()



# A file totalstudents.txt contains the names of all students in a class,
# and a file passedstudents.txt contains the names of students who passed.txt the exam.
# Write a Python program to:
# Read the names from both files.
# # Find the students who did not pass.
# # Write their names to a new file named failed_students.txt, one name per line.
# #