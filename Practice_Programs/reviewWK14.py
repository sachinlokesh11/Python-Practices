# 1.1.Write a function that sorts the positive numbers in ascending order, and keeps the negative numbers untouched.

# Examples
# pos_neg_sort([6, 3, -2, 5, -8, 2, -2]) ➞ [2, 3, -2, 5, -8, 6, -2]

# pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]) ➞ [1, 2, 3, -1, 4, 5, -1, 6]

# pos_neg_sort([-5, -5, -5, -5, 7, -5]) ➞ [-5, -5, -5, -5, 7, -5]

# pos_neg_sort([]) ➞ []

# Notes
# If given an empty list, you should return an empty list.
# Integers will always be either positive or negative (0 isn't included in the tests).

# 1.2 Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits
# are rearranged.
#
# Examples
# rearranged_difference(972882) ➞ 760833
# 988722 - 227889 = 760833
#
# rearranged_difference(3320707) ➞ 7709823
# # 7733200 - 23377 = 7709823
#
# rearranged_difference(90010) ➞ 90981
# # 91000 - 19 = 90981


def sort_numbers1(input_list):
    pos_num = [num for num in input_list if num > 0]
    neg_num = [num for num in input_list if num < 0]
    for index in range(len(pos_num)-1, 0, -1):
        for new_index in range(index):
            if pos_num[new_index] > pos_num[new_index+1]:
                temp = pos_num[new_index]
                pos_num[new_index] = pos_num[new_index+1]
                pos_num[new_index+1] = temp
    x = y = 0
    for i in range(len(input_list)):
        if input_list[i] > 0:
            input_list[i] = pos_num[x]
            x += 1
        else:
            input_list[i] = neg_num[y]
            y += 1
    return input_list


def sort_numbers2(input_list):
    for i in range(len(input_list)):
        min_index = i
        if input_list[min_index] > 0:
            for x in range(i+1, len(input_list)):
                if input_list[x] > 0:
                    if input_list[min_index] > input_list[x]:
                        min_index = x
            temp = input_list[i]
            input_list[i] = input_list[min_index]
            input_list[min_index] = temp
    return input_list


def rearranged_difference(number):
    my_number = [num for num in number]
    for index in range(len(my_number) - 1, 0, -1):
        for new_index in range(index):
            if my_number[new_index] < my_number[new_index+1]:
                temp = my_number[new_index]
                my_number[new_index] = my_number[new_index+1]
                my_number[new_index+1] = temp
    reverse_num = my_number[::-1]
    max_num = int("".join(my_number))
    min_num = int("".join(reverse_num))
    difference = max_num-min_num

    return difference


if __name__ == "__main__":
    options = int(input("1.Sort numbers with negative numbers untouched\n2.Find Difference between maximum  "
                        "and minimum number\n"))
    match options:
        case 1:
            print("Using First Method:")
            print(sort_numbers1([6, 3, -2, 5, -8, 2, -2]))
            print(sort_numbers1([-5, -5, -5, -5, 7, -5]))
            print(sort_numbers1([6, 5, 4, -1, 3, 2, -1, 1]))
            print(sort_numbers1([]))
            print("Using Second Method:")
            print(sort_numbers2([6, 3, -2, 5, -8, 2, -2]))
            print(sort_numbers2([-5, -5, -5, -5, 7, -5]))
            print(sort_numbers2([6, 5, 4, -1, 3, 2, -1, 1]))
            print(sort_numbers2([]))
        case 2:
            print(rearranged_difference("972882"))
            print(rearranged_difference("3320707"))
            print(rearranged_difference("90010"))
