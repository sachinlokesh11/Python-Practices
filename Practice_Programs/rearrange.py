# Given an integer array, in-place rearrange it such that it contains positive and negative numbers at
# alternate positions. Assume that all values in the array are non-zero.
#
# • In case the multiple rearrangement exists, the solution can return any one of them.
#
# Input : [9, -3, 5, -2, -8, -6, 1, 3]
# Output: [9, -3, 5, -2, 1, -8, 3, -6] or [5, -2, 9, -6, 1, -8, 3, -3] or any other valid combination..
#
# • If the array contains more positive or negative elements, the solution should move them to the end
# Input : [9, -3, 5, -2, -8, -6]
# Output: [5, -2, 9, -6, -3, -8] or [-2, 5, -6, 9, -3, -8] or any other valid combination..
#
# Input : [5, 4, 6, -1, 3]
# Output: [5, -1, 4, 6, 3] or [-1, 5, 4, 6, 3] or any other valid combination..

input_data = [9, -3, 5, -2, -8, -6, 1, 3, -6, -8, -3, -5]
output_data = []
positive_num = [x for x in input_data if x > 0]
negative_num = [y for y in input_data if y < 0]

if len(positive_num) == len(negative_num):
    for i in range(len(positive_num)):
        output_data.append(positive_num[i])
        output_data.append(negative_num[i])
elif len(positive_num) > len(negative_num):
    for i in range(len(negative_num)):
        output_data.append(positive_num[i])
        output_data.append(negative_num[i])
    left_indexes = len(positive_num) - len(negative_num)
    remaining_values = []
    for i in range(1, left_indexes+1):
        remaining_values.append(positive_num[-i])
    output_data.extend(remaining_values)
else:
    for i in range(len(positive_num)):
        output_data.append(positive_num[i])
        output_data.append(negative_num[i])
    left_indexes = len(negative_num) - len(positive_num)
    remaining_values = []
    for i in range(1, left_indexes + 1):
        remaining_values.append(negative_num[-i])
    output_data.extend(remaining_values)

print("\nGiven Input Data is:", input_data)
print("\nAfter Rearranging it in required format, we have:", output_data)


