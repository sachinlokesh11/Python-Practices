# "Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence
# is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.
# Examples
# consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True
# consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False
# consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False
# consecutive_combo([44, 46], [45]) ➞ True"


def consecutive_combo(input_array1, input_array2):
    input_array1.extend(input_array2)
    final_array = list(input_array1)
    min_num = min(final_array)
    for index in range(len(final_array)-1):
        if min_num+1 not in final_array:
            return False
        min_num += 1
    return True


if __name__ == "__main__":
    print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
    print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
    print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 11]))
    print(consecutive_combo([44, 46], [45]))