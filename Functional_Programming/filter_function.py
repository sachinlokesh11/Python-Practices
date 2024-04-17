# A filtering operation processes an iterable and extracts the items that satisfy a given operation. It can be
# performed with Python’s FILTER() built-in function.
# Accepts only single iterable and single function argument

# The basic syntax is: filter(function, iterable)

#                               Example 1
# List of numbers
num = [12, 37, 34, 26, 9, 250, 451, 3, 10]

# Define lambda function to filter even numbers
even = list(filter(lambda x: x % 2 == 0, num))

# Print the even numbers
print(even)

# The above example uses filter() to check whether numbers are even. If this condition is met and returns True, the
# even number "goes through the filter".

#                                Example 2
# creating a function that returns the eligibility ages for voting from the list
input_list = [3, 20, 18, 6, 14, 25, 19]
eligibility_list = filter(lambda x: x >= 18, input_list)
# converting into a list
print("Eligibility ages for voting from the input list:", list(eligibility_list))
