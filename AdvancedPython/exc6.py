# Ask the user to enter a password. If its length is less than 8 characters, raise
# a custom exception InvalidPasswordError with the message ("Password should be 8 characters")

class InvalidPasswordError(Exception):
  pass


# Ask the user to enter an amount and if the amount < balance, raise custom Exception
# InsufficientBalanceError with the message ("Not Enough Balance. Transaction Failed")


class InsufficientBalanceError(Exception):
  pass



try:
  password = input("Enter password: ")
  if len(password) < 8:
    raise InvalidPasswordError("Password should be 8 characters")
  else:
    print("Password accepted successfully.")
except InvalidPasswordError as e:
  print(e)





  

balance = 5000  
try:
  amount = float(input("Enter withdrawal amount: "))
  if amount < balance:  # Or amount > balance depending on your exact transaction logic
    raise InsufficientBalanceError("Not Enough Balance. Transaction Failed")
  else:
    print("Transaction successful.")
except InsufficientBalanceError as e:
  print(e)