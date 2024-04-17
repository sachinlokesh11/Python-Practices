#                            Properties of first class functions:
# A function is an instance of the Object type.
# You can store the function in a variable.
# You can pass the function as a parameter to another function.
# You can return the function from a function.
# You can store them in data structures such as hash tables, lists, …


#                             What is a custom decorator?
# Basically, a decorator takes a function as an argument, makes some in-place modifications on the function and
# returns a new modified function based off the function it received as an argument.

#                          When to Use a Decorator in Python
# You'll use a decorator when you need to change the behavior of a function without modifying the function itself.
# A few good examples are when you want to add logging, test performance, perform caching, verify permissions,
# and so on.
# You can also use one when you need to run the same code on multiple functions.

#                             Decorator
# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.


#                             Syntax for Decorator:

# @gfg_decorator
# def hello_decorator():
#     print("Gfg")
#
#  '''
#  Above code is equivalent to -
#
#     def hello_decorator():
#         print("Gfg")
#
#     hello_decorator = gfg_decorator(hello_decorator)
#     '''

#                   Custom Decorator Example 1 using Method 1

# defining a decorator
def hello_decorator(func):

    def inner_function():           # wrapper function
        print("Hello, this is before function execution using Method 1")

        # calling the actual function now inside the wrapper function.
        func()

        print("This is after function execution using Method 1")

    return inner_function


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function using Method 1")


# passing 'function_to_be_used' inside the decorator to control its behaviour
variabe_to_store_function = hello_decorator(function_to_be_used)

# calling the function
variabe_to_store_function()


#                   Custom Decorator Example 1 using Method 2

# defining a decorator
def hello_decorator2(func):

    def inner_function2():           # wrapper function
        print("Hello, this is before function execution using Method 2")

        # calling the actual function now inside the wrapper function.
        func()

        print("This is after function execution using Method 2")

    return inner_function2


@hello_decorator2
def function_to_be_used2():
    print("This is inside the function using Method 2")


# calling the function
function_to_be_used2()

#                             Return type function with *args, **kwars


def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


# getting the value through return of the function
print("Sum =", sum_two_numbers(25, 35))