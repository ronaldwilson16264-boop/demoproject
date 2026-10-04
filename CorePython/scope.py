x = 20  # global

print("outside", x)


def f():
  print("inside", x)


f()



# local


def f():
  x = 20  # local
  print("inside", x)


f()

print("outside", x)











# Non local

# def outer():
#     x = 20 # nonlocal

#     def inner():
#         y=30 # local[cite: 3]
#         print("inside inner function",x)

#     inner()
#     print("inside outer function",x)

# outer()

# #LEGB-Rule

# Built in scope
# scope of all the names declared inside python library








