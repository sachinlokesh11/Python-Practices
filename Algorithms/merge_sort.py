# Merge sort

def merge_sort(list):
    if len(list) > 1:

        middle = len(list) // 2
        left_list = list[:middle]
        right_list = list[middle:]

        merge_sort(left_list)
        merge_sort(right_list)
        i = j = k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i += 1
            else:
                list[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("List Before Sorting :\n", unsorted_list)
merge_sort(unsorted_list)
print("List After Sorting :\n", unsorted_list)