# *********************  Custom Exception   *********************
# Custom Exception is a user Defined Exception class to handle Error in our code
# Syntax For Custom Exception class
class CustomExceptionError(Exception):
    """ my custom exception class """


try:
    raise CustomExceptionError('This is my custom exception')
except CustomExceptionError as ex:
    print(ex)


# Demonstration for custom Exception
class Error(Exception):
    """Base class for other exceptions"""
    pass


class To_small_value_exception(Error):
    """This exception will be raised when the keyed in value is too small"""
    pass


class To_large_value_exception(Error):
    """ This exception will be raised when the keyed in value is too large"""
    pass


Check_value = 10

try:
    Input_Number = int(input("Enter a number: "))
    if Input_Number < Check_value:
        raise To_small_value_exception
    elif Input_Number > Check_value:
        raise To_large_value_exception
except To_small_value_exception:
    print("Value is very small")
except To_large_value_exception:
    print("Value is very large")
print("Value is acceptable!!.")
