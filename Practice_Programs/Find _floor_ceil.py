# Given a sorted integer array, find the floor and ceiling of a given number in it. For a given number x,
# floor(x) is the largest integer in the array less than or equal to x, and ceil(x) is the smallest integer in the
# array greater than or equal to x.
#
# The solution should return the (floor, ceil) pair. If the floor or ceil doesn't exist, consider it to be -1.
#
# Input: nums[] = [1, 4, 6, 8, 9], x = 2
# Output: (1, 4)
# Explanation: The floor is 1 and ceil is 4
#
# Input: nums[] = [1, 4, 6, 8, 9], x = 6
# Output: (6, 6)
# Explanation: The floor is 6 and ceil is 6
#
# Input: nums[] = [-2, 0, 1, 3], x = 4
# Output: (3, -1)
# Explanation: The floor is 3 and ceil doesn't exist


def floor_ceil(nums, number):
    output = []
    floor = [i for i in nums if i < number]
    ceil = [j for j in nums if j > number]
    if floor:
        result = floor[0]
        for x in range(len(floor)):
            for j in range(len(floor)):
                if floor[j] > result:
                    result = floor[j]
        output.append(result)
    else:
        output.append(-1)

    if ceil:
        result = ceil[0]
        for x in range(len(ceil)):
            for j in range(len(ceil)):
                if ceil[j] < result:
                    result = ceil[x]
        output.append(result)
    else:
        output.append(-1)
    print(tuple(output))


if __name__ == "__main__":
    nums = [-2, 0, 1, 3]
    flag = True
    while flag:
        choice = int(input("\nEnter 1 to check, 2 to exit\n"))
        match choice:
            case 1:
                number = int(input("Enter the Number: "))
                if number in nums:
                    print("Floor and ceil of number is: ", (number, number))
                else:
                    floor_ceil(nums, number)
            case 2:
                flag = False
