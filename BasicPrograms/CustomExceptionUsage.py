# Custom Exception Example1
class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg = arg
class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg


age = int(input("Enter Age:"))
if age > 60:
    raise TooOldException("Your age already crossed marriage age...no chance of getting marriage")
elif age < 18:
    raise TooYoungException("Plz wait some more time you will get best match soon!!!")
else:
    print("You will get match details soon by email!!!")

# Custom Exception Example2
class AdditionError(Exception):
    pass


try:
    a = 10
    b = 20
    c = a
    if c != 30:
        raise AdditionError("Syntax for Addition is wrong")
except AdditionError as ex:
    print(ex)

# Custom Exception Example3

class Error(Exception):
   pass


class Not_Positive_exception(Error):
  """ This exception will be raised when the number is not positive """
  pass

try:
   Input_Number = int(input("Enter a number: "))
   if Input_Number <= 0:
     raise Not_Positive_exception
   else:
       print("Number is Positive")
except Not_Positive_exception:
  print("Number is not positive")

# Custom Exception Example4
class ZeroDivisionException(Exception):
    def __init__(self,arg):
        self.arg = arg

a = int(input("Enter the number:"))
if a == 0:
    raise ZeroDivisionException("Cannot Divide by zero")
else:
    c = int(25/a)
    print(c)

#  Custom Exception Example5
class TextException(Exception):
    pass

text = "Hello Boys , what doing"
if "Shubham" not in text:
    raise TextException("Word is not present ")
else:
    print("Word is Present")




