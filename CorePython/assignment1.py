##1Given a string
s = "I am learning Python"

# Find the length of the string
length_s = len(s)
# Find the reverse of the string
reverse_s = s[::-1]
print("Reverse:",reverse_s)
# find the last character of the strings
last_char = s[-1]
print("Last character:",last_char)
#find the 13th character
thirteenth_char = s[12]
print("13th character:",thirteenth_char)
#print the characters from 2nd index to 15 th index
character = s[2:16]
print("characters from 2nd to 15th index:",character)
#combines the string s with word "programming"
combined_string = s + "programming"
print("combined string:",combined_string)


# #2.Given a list
l = ['Guitar', 'Piano', 'Violin', 'Drums', 'Flute']
# Add a new item 'Veena' to the list
l.append('veena')
print("updated list:",l)


# #3Declare a list of 5 food items
food_items = ['pizza','burger','pasta','soup','salad']
#Add new fooditem to the list
food_items.append('idli')
#change the second food item
food_items[1] = 'sandwich'
#print the updated list
print("updated food items:",food_items)
#print the last food 
print("last food item:",food_items[-1])
#print the number of food items
print("number of food items:",len(food_items))



# #4.Given a string 
s="python is a programming language"
#Remove the first 10 characters and print the remaining
remaining_string = s[10:]
print("after removing 10 characters:",remaining_string)
#print the last 5 characters
last_five = s[-5:]
print("last five characters",last_five)
