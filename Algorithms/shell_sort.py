# ShellSort is a variation of insertion sort
# Also called Diminishing increment sort
# working - By Breaking the original list into a smaller sublists,each sublist is sorted using the insertion sort


def shell_sort(my_list):
    gap = len(my_list) // 2
    while gap > 0:
        for i in range(gap, len(my_list)):
            current_element = my_list[i]
            pos = i

            # Sort the sub list for this gap
            while pos >= gap and current_element < my_list[pos - gap]:
                my_list[pos] = my_list[pos - gap]
                pos = pos-gap
            my_list[pos] = current_element
    # Reduce the gap for the next element
        gap = gap//2


input_list = [19, 2, 31, 45, 30, 11, 121, 27]
shell_sort(input_list)
print(input_list)
