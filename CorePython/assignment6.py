# # # Q1.Define a function that takes 2 numbers and returns their product

def multiply(a,b):
    return a * b

result = multiply(3,4)
print("Product:",result)

# # Q2.Define a function that takes a string and returns number of vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count
result = count_vowels("malayalam")
print("Vowels:",result)

# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle
def area_rectangle(l,b):
    return l * b
result = area_rectangle(10,5)
print("Area:",result)



# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]

l=[45,78,90,12,35]
def even_number(ls):
    even_list = []
    for num in ls:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
result = even_number(l)
print("Even numbers:",result)


# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]
l = [123, 345, 111, 678, 134, 809]
def digit_list(ls):
    result = []
    for num in ls:
        s = 0
        for i in range(3):
            digit = num % 10
            s += digit
            num = num // 10
        result.append(s)
    return result

result = digit_list(l)
print("Sum of digits:",result)


#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list
# l=[12,34,78,12,67,34,90,23]
l=[12,34,78,12,67,34,90,23]

def unique_list(ls):
    new_list = []
    for num in ls:
        if num not in new_list:
            new_list.append(num)
    return new_list

result = unique_list(l)
print("unique list:",result)


#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]

list1=[12,34,56,78,90]
list2=[90,34,11,57,45]

def common_elements(l1,l2):
    common = []
    for num in l1:
        if num in l2:
            common.append(num)
    return common


result = common_elements(list1,list2)
print("Common elements:",result)


