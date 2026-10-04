# Ask the user to enter a number. If the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"
try:
  num = int(input("Enter number:"))
  if num <= 0:
    raise ValueError("Number must be Positive")
  else:
    print(num)

except ValueError as e:
  print(e)