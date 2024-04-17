# "Create a function that takes a list lst and a number n and returns a list of two integers whose product is
# that of the number n.
# Examples
# two_product([1, 2, 3, 4, 13, 5], 39) ➞ [3, 13]
# two_product([11, 2, 7, 3, 5, 0], 55) ➞ [5, 11]
# two_product([100, 12, 4, 1, 2], 15) ➞ None"


def two_product(input_list, number):
    output_list = []
    for element in input_list:
        second_element = number/element
        if second_element in input_list:
            output_list.extend([element, int(second_element)])
            return output_list
    return "None"


if __name__ == "__main__":
    print(two_product([1, 2, 3, 4, 13, 5], 39))
    print(two_product([11, 2, 7, 3, 5, 0], 55))
    print(two_product([100, 12, 4, 1, 2], 15))
