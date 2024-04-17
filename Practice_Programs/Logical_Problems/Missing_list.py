# Create a function that takes a list of lists and return the length of the missing list.
#
# Examples
# find_missing([[1], [1, 2], [4, 5, 1, 1], [5, 6, 7, 8, 9]]) ➞ 3
#
# find_missing([[5, 6, 7, 8, 9], [1, 2], [4, 5, 1, 1], [1]]) ➞ 3
#
# find_missing([[4, 4, 4, 4], [1], [3, 3, 3]]) ➞ 2

def missing_list(input_lists):
    list_lengths = [len(individual_list) for individual_list in input_lists]
    for index in range(1, len(list_lengths)+1):
        if index not in list_lengths:
            return index


if __name__ == "__main__":
    print(missing_list([[1], [1, 2], [4, 5, 1, 1], [5, 6, 7, 8, 9]]))
    print(missing_list([[5, 6, 7, 8, 9], [1, 2], [4, 5, 1, 1], [1]]))
    print(missing_list([[4, 4, 4, 4], [1], [3, 3, 3]]))