# File Menu

def file_read():
    filename = input("Enter the file name: ")
    f = open(filename, "r")
    content = f.read()
    print(content)
    f.close()


def file_write():
    filename = input("Enter the file name: ")
    f = open(filename, "w")
    content = input("Enter the content: ")
    f.write(content)
    f.close()


def file_append():
    filename = input("Enter the file name: ")
    f = open(filename, "a")
    content = input("Enter the content: ")
    f.write(content)
    f.close()


def file_search():
    filename = input("Enter the file name: ")
    f = open(filename, "r")
    content = f.read()
    word = input("Enter the word: ")

    if word in content:
        print("Word found")
    else:
        print("Word not found")

    f.close()


def file_delete():
    import os

    filename = input("Enter the file name: ")
    os.remove(filename)
    print("File deleted")


while True:
    print("1. Read")
    print("2. Write")
    print("3. Append")
    print("4. Search")
    print("5. Delete")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        file_read()
    elif ch == 2:
        file_write()
    elif ch == 3:
        file_append()
    elif ch == 4:
        file_search()
    elif ch == 5:
        file_delete()
    elif ch == 6:
        exit()
    else:
        print("Invalid choice")