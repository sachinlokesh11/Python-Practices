# Create a function that groups a list of numbers based on a size parameter.
# The size represents the maximum length of each sub-list.
#
# [1, 2, 3, 4, 5, 6], 3
# [[1, 3, 5], [2, 4, 6]]
# # Divide list into groups of size 3.
# [1, 2, 3, 4, 5, 6], 2
# [[1, 4], [2, 5], [3, 6]]
# # Divide list into groups of size 2.
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4
# [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9]]
# # "Leftover" lists are okay.
# Examples
# group([1, 2, 3, 4], 2) ➞ [[1, 3], [2, 4]]
# group([1, 2, 3, 4, 5, 6, 7], 4) ➞ [[1, 3, 5, 7], [2, 4, 6]]
# group([1, 2, 3, 4, 5], 1) ➞ [[1], [2], [3], [4], [5]]
# group([1, 2, 3, 4, 5, 6], 4) ➞ [[1, 3, 5], [2, 4, 6]]
from math import ceil


def group_list(input_list, list_size):
    print("Input List:", input_list, "Size we want:", list_size)
    total_lists = ceil(len(input_list)/list_size)
    my_list = [input_list[index::total_lists] for index in range(0, total_lists)]
    return my_list


if __name__ == "__main__":
    print("Output List: ", group_list([1, 2, 3, 4, 5, 6], 2))
    print("Output List: ", group_list([1, 2, 3, 4, 5, 6, 7], 4))
    print("Output List: ", group_list([1, 2, 3, 4, 5, 6], 3))
    print("Output List: ", group_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4))
    print("Output List: ", group_list([1, 2, 3, 4], 2))
    print("Output List: ", group_list([1, 2, 3, 4, 5], 1))