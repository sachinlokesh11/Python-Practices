# Write a function for picking up the numbers which are squares of positive integers from a given
# array and do a sort which is not a brute force sort or a bubble sort. Basically the complexity of the
# algorithm should be lease than O(n2)
# Example 1:
# Input: [169,145,225,211,121,183,100,111,196,214,275]
# Output: [100,121,169,196,225]
from math import sqrt


def create_newlist():
    mylist = [169, 145, 225, 211, 121, 183, 100, 111, 196, 214, 275]
    final_list = []
    for element in mylist:
        number = int(sqrt(element))
        if number*number == element:
            final_list.append(element)
    print(final_list)
    return final_list


def sort(final_list):
    for i in range(len(final_list)):
        for j in range(len(final_list) - 1 - i):
            if final_list[j] > final_list[j + 1]:
                temp = final_list[j + 1]
                final_list[j + 1] = final_list[j]
                final_list[j] = temp
    print(final_list)


if __name__ == "__main__":
    new_list = create_newlist()
    sort(new_list)


