#  Lambda Functions are anonymous function means that the function is without a name.
# 'def' keyword is used to define a normal function in Python. Similarly,
# the 'lambda' keyword is used to define an anonymous function in Python.
# Syntax:
# lambda arguments: expression

# **************** Demonstration OF Lambda Expression***********************
text = 'My Name is Shubham'

# lambda returns a function object
rev_upper = lambda string: string.upper()[::-1]
print(f"\"{text}\" in Reverse is \"{rev_upper(text)}\"")
# ***************************************************************************


#  Difference Between Lambda functions and def defined function
# using function defined ,using def keyword
def cube(y):
    return y*y*y

print("Using function defined with `def` keyword, cube is:", cube(5))


# ******************** using the lambda function **************************
cube = lambda y: y*y*y

print("Using Lambda function, cube is:", cube(5))

# ****************** Demonstration 2 *************************
even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]

# iterate on each lambda function
# and invoke the function to get the calculated value
for item in even_list:
    print(item())

# Example of lambda function using if-else
Max = lambda a, b: a if (a > b) else b

print(Max(101, 92))

# ***************Using lambda() Function with filter()***************************
# The filter() function in Python takes in a Lambda function and a list as arguments.
# filter() function only keeps elements where it produces True.
# To filter odd numbers
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

# ***************** Using lambda() Function with map() ***********************
# The function is called with a lambda function and a list and a new list is returned
# which contains all the lambda modified items returned by that function for each item
# Multiply all elements of a list by 2 using lambda and map() function
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x * 2, li))
print(final_list)

# ************************ Using lambda() Function with reduce() *************
# The function is called with a lambda function and an iterable and a new reduced result is returned.
# Finding total sum of list elements
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum_ = reduce((lambda x, y: x + y), li)
print(sum_)
