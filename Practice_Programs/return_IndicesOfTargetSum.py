# Given an array of integers nums and an integer target, return indices of the two numbers such that
# they add up to target.

# Input: nums = numbers = [2, 7, 11, 15], target = 9
# Output: [0,1]


def find_index(my_list):
    count = 0
    for x in my_list:
        y = target-x
        if y in new_list and x != y:
            index = numbers.index(y)
            return count, index
        count += 1
    return {"No Such Sum is Possible"}


if __name__ == "__main__":
    numbers = [2, 5, 4, 20, 7, 11, 15]
    target = 11
    new_list = [i for i in numbers if i <= target]
    indexes = list(find_index(new_list))
    print(indexes)





