# map() takes a function and one or more iterables as arguments. The output is an iterator that returns
# the transformed items.

# The basic syntax is: map(function, iterable[, iterable1, iterable2,..., iterableN])

# This first argument to map() is a transformation function, where each original item is transformed
# into a new one. It can be any Python callable.

#                                  Example 1
# List of input numbers to transform
num = [2, 3, 6, 9, 10]

# Define a lambda function to iterate on each value of num.
cubed = map(lambda n: n ** 3, num)

# Create a list containing the cubed values
print(list(cubed))


# If you enter multiple iterables to map(), then the transformation function must take as many arguments as the
# number of iterables you pass in. Each iteration will pass one value from each iterable as an argument to the function.
#                                 Example 2
print(list(map(lambda x, y: x / y, [6, 3, 5], [2, 4, 6])))
print(list(map(lambda x, y, z: x * y + z, [6, 2], [7, 3], [8, 10])))


# We should also mention STARMAP(), which is very similar to map(). According to the Python documentation, starmap()
# is used instead of map() when the argument parameters are already grouped in tuples from a single iterable
#                              Example 3
import itertools

# Define a list of tuples
num = [(2, 3), (6, 9), (10, 12)]

# Define a lambda function to a list of tuples
multiply = itertools.starmap(lambda x, y: x * y, num)

# Create a list containing the multiplied values
print(list(multiply))
