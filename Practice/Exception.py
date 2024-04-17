# Try-Except
# The try block lets us test a block of code for errors.
# The except block lets us handle the error.

# Syntax for Try-Except(Exception Handling)
try:
  print(x)
except:
  print("An exception occurred")

# Syntax for Try-Except with many Exception
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except SyntaxError:
  print("Something else went wrong")

# Using Else in Exception Handling
# Else will execute if no error occurs
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# Try-Except using Finally
# This block, if specified, will be executed regardless if the try block raises an error or not

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# Raise Exception

x = 5
while x >= 0:
    print(x)
    x -= 1
raise Exception("Sorry, no numbers below zero")