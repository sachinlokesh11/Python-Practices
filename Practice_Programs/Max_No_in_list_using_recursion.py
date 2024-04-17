# Create a function that finds the highest integer in the list using recursion.

# Examples
# find_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99
# find_highest([0, 12, 4, 87]) ➞ 87
# find_highest([8]) ➞ 8

def max_number_in_list(input_list):
    if len(input_list) <= 1:
        return input_list[0]
    max_number = max_number_in_list(input_list[1:])
    return max_number if max_number > input_list[0] else input_list[0]


if __name__ == "__main__":
    print("The Largest number in given list is: ", max_number_in_list([-1, 3, 5, 106, 6, 99, 12, 2]))
