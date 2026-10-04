# Read


f = open("k.txt", "r")


# read()
# returns file content as string format


# readlines()
# returns file content as list format


s = f.read()


# s=f.readlines()


print(s)
print(type(s))


f.close()