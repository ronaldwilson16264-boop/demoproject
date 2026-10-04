# Write a program to display a number if it is divisible by 3

num = int(input("Enter a number: "))

if num % 3 == 0:
    print(num)

# Write a program to display a number if it is divisible by 7 and 5

num = int(input("Enter a number: "))

if num % 7 == 0 and num % 5 == 0:
    print(num)

# Write a program to display a name if name contains letter 'n'

name = input("Enter a name: ")

if 'n' in name:
    print(name)

# Write a program to display a name if name starts with letter 'A'

name = input("Enter a name: ")

if(name[0]=="A" or  name[0]=="a"):
    print(name)