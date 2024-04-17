# Searching element in a given list , if present return true else false

def linear_search(values, search_for):
    search_at = 0
    search_res = False
# Match the value with each data element
    while search_at < len(values) and search_res is False:
        if values[search_at] == search_for:
            search_res = True
        else:
            search_at = search_at + 1
    return search_res


my_list = [64, 34, 25, 12, 22, 11, 90]

print(linear_search(my_list, 12))
print(linear_search(my_list, 91))