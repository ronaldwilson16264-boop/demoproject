# *
for i in range(1):
    print("*")


# * * * * *
for i in range(5):
    print("*", end=" ")


# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()


# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()


# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


#     *
#    * *
#   * * *
#  * * * *
# * * * * *
for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(i):
        print("* ", end="")
    print()


# * * * * *
#  * * * *
#   * * *
#    * *
#     *
for i in range(5, 0, -1):
    print(" " * (5 - i), end="")
    for j in range(i):
        print("* ", end="")
    print()


# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# 1
# 2 3
# 4 5 6
# 7 8 9 10
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


# A
# A B
# A B C
# A B C D
for i in range(1, 5):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()