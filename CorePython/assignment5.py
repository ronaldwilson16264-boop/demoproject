d={'a':23,'b':25,'c':28,'d':30,'e':22}
# print even values 
print("Even values in dictionary:")
for v in d.values():
    if v % 2 == 0:
        print(v,end=" ")





colors=['red','green','blue','orange','black']
# starting letter
print("starting letter is:")
for c in colors:
    print(c[0], end=" ")
print("\n")

# last letter
print("last letter is:")
for c in colors:
    print(c[-1],end=" ")
print("\n")

# reverse
print("reverse is:")
for c in colors:
    print(c[::-1],end=" ")
print("\n")

# all colors contains letter 'b'
print("colors containing letter 'b' is:")
for c in colors:
    if 'b' in c:
        print(c,end=" ")
print("\n")





# Range function
# 100-200
print("100 to 200:")
for i in range(100,201):
    print(i, end=" ")
print("\n")

# 1,2,3,4,5
print("1 to 5:")
for i in range(1,6):
    print(i, end=" ")
print("\n")

# 1,3,5,7,9,11
print("odd numbers:")
for i in range(1,12,2):
    print(i, end=" ")
print("\n")

# 2,4,6,8,10
print("even numbers:")
for i in range(2,11,2):
    print(i, end=" ")
print("\n")

# 100,200,300,400,500
print("hundreds:")
for i in range(100,501,100):
    print(i, end=" ")
print("\n")

# 5,4,3,2,1
print("reverse:")
for i in range(5,0,-1):
    print(i, end=" ")
print("\n")

# 3,6,9,12,15,18,21
print("multiples of 3:")
for i in range(3,22,3):
    print(i, end=" ")
print("\n")

# 1,4,9,16,25,36

print("squares:")
for i in range(1,7):
    print(i*i, end=" ")
print("\n")

# print all 3 digit numbers(100-999)
print("three digit numbers:")
for i in range(100,1000):
    print(i, end=" ")
print("\n")

# print all numbers divisible by 3 in the range 100-200
print("divisible by three in the range(100-200):")
for i in range(100,201):
    if i % 3 == 0:
        print(i, end=" ")
print("\n")


# 1,8,27,64,125

print("cubes:")
for i in range(1,6):
    print(i**3, end=" ")
print("\n")
