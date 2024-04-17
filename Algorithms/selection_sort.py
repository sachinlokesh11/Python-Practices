# Selection Sort algorithm works by repeatedly finding the minimum element from the unsorted part of the list and
#   placing it at the beginning.


def selection_sort(input_list):
    for i in range(len(input_list)):
        min_index = i
        for x in range(i+1, len(input_list)):
            if input_list[min_index] > input_list[x]:
                min_index = x
        temp = input_list[i]
        input_list[i] = input_list[min_index]
        input_list[min_index] = temp
    print(input_list)


my_list = [3, 5, 2, 6, 7, 9, 8, 1, 4]
selection_sort(my_list)