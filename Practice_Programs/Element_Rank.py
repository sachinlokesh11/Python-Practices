# Given an array of distinct integers, in-place replace each array element by its corresponding rank in the
# array. The minimum array element has the rank 1; the second minimum element has a rank of 2, and so on.
#
# Input : [10, 8, 15, 12, 6, 20, 1]
# Output: [4, 3, 6, 5, 2, 7, 1]
#
# Input : [0, 1, -1]
# Output: [2, 3, 1]

def selection_sort(my_list):
    input_list = list(my_list)
    for i in range(len(input_list)):
        min_index = i
        for x in range(i+1, len(input_list)):
            if input_list[min_index] > input_list[x]:
                min_index = x
        temp = input_list[i]
        input_list[i] = input_list[min_index]
        input_list[min_index] = temp
    return input_list


def find_rank(my_list, initial_list):
    i = 1
    final_list = list(my_list)
    for x in my_list:
        index = initial_list.index(x)
        final_list[index] = i
        i += 1
    print(final_list)


if __name__ == "__main__":
    unsorted_list = [10, 8, 15, 12, 6, 20, 1]
    print(unsorted_list)
    sorted_list = selection_sort(unsorted_list)
    find_rank(sorted_list, unsorted_list)