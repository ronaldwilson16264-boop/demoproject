try:
  num1 = int(input("Enter number"))
  num2 = int(input("Enter number"))
  r = num1 / num2
  print("Result", r)

except ZeroDivisionError:
  print("Zero division error")

except ValueError:
  print("valueErrot")

except:  # general code if any exception other than above two
  print("Error")