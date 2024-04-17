# Insertion Sort

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        next_element = my_list[i]
        j = i-1
        while my_list[j] > next_element and j >= 0:
            my_list[j+1] = my_list[j]
            print(my_list)
            j = j - 1
        my_list[j+1] = next_element
    print(my_list)


unsorted_list = [3, 5, 2, 6, 7, 9, 8, 1, 4]
insertion_sort(unsorted_list)