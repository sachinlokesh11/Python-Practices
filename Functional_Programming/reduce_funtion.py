# The REDUCE() function implements a technique called FOLDING or reduction. It takes an existing function,
# applies itcumulatively to all the items in iterable, and returns a single final value.

# The basic syntax is: functools.reduce(function, iterable[, initializer])

#                              Example 1
# importing reduce() function from functools module
from functools import reduce
input_list = [12, 4, 10, 15, 6, 5]
print("The sum of all list items:")
sums = reduce(lambda x, y: x+y, input_list)
print(sums)

#                              Example 2
my_nums = [2, 4, 3, 1, 9]
multiply = reduce(lambda x, y: x*y, my_nums)
print("The Product of all list items:", multiply)
