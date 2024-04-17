# Given an unsorted integer array, find a pair with the given sum in it.
#
# • Each input can have multiple solutions. The output should match with either one of them.
#
# Input : nums[] = [8, 7, 2, 5, 3, 1], target = 10
# Output: (8, 2) or (7, 3)
#
# • The solution can return pair in any order. If no pair with the given sum exists, the solution should return
# an empty tuple.
#
# Input : nums[] = [5, 2, 6, 8, 1, 9], target = 12
# Output: ()


def find_pair(my_list):
    pairs = []
    count = 0
    check = 0
    for x in my_list:
        count += 1
        y = target-x
        new_count = 0
        for i in my_list:
            new_count += 1
            if i == y and new_count != count:
                my_tuple = (x, i)
                pairs.append(my_tuple)
                check = 1
                my_list.remove(x)

    if check == 1:
        return pairs
    return ()


if __name__ == "__main__":
    numbers = [5, 2, 6, 8, 1, 9]
    target = 10
    new_list = [i for i in numbers if i <= target]
    pair = find_pair(new_list)
    print(pair)
