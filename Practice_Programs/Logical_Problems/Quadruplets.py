# Given an unsorted integer array, find all quadruplets (i.e., four elements tuple) having a given sum.

# Input : nums = [2, 7, 4, 0, 9, 5, 1, 3], target = 7
# Output: {(0, 1, 2, 4)}

# Since the input can contain multiple quadruplets that sum to a given target, the solution should return a set
# containing all the quadruplets.

# Input : nums = [2, 7, 4, 0, 9, 5, 1, 3], target = 20
# Output: {(0, 4, 7, 9), (1, 3, 7, 9), (2, 4, 5, 9)}
# Note: The order of elements doesn't matter in a quadruplet, and any permutation is allowed in the output.
# For example, the output set can contain quadruplets [9, 1, 7, 3] and [9, 3, 7, 1], but system treats them the same.


def quadruplets(input_list, target_sum):
    output_list = []
    for element in input_list:
        for new_element in input_list:
            if input_list.index(new_element) != input_list.index(element):
                for value in input_list:
                    if input_list.index(value)!=input_list.index(new_element) and input_list.index(value)!=input_list.index(element):
                        for data in input_list:
                            if input_list.index(data) != input_list.index(new_element) and input_list.index(data) != input_list.index(element) and input_list.index(data) != input_list.index(value):
                                if (element+new_element+value+data) == target_sum:
                                    result = (element,new_element,value,data)
                                    new_result = list(result)
                                    new_result.sort()
                                    final_result = tuple(new_result)
                                    if final_result not in output_list:
                                        output_list.append(final_result)

    return set(output_list)


if __name__ == "__main__":
    print(quadruplets([2, 7, 4, 0, 9, 5, 1, 3], 20))
    print(quadruplets([2, 7, 4, 0, 9, 5, 1, 3], 7))

