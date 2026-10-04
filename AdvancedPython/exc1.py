#Sum of two numbers
try:
  num1 = int(input("Enter number:"))
  num2 = int(input("Enter number:"))
  s = num1 + num2

except:
  print("Invalid number")

#optional
else:
  print("Sum", s)

finally:
  print("done")