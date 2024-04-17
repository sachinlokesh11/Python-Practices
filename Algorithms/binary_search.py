import logging


def search_element(mylist, left, right):
    mid = int((left + right) / 2)
    return mylist[mid], mid


def binary_search():
    """
    This function binary search the element in the list
    :return: None
    """
    try:
        my_list = [8, 3, 9, 15, 65, 2, 30, 13]
        my_list.sort()
        print("Sorted list:", my_list)
        user_input = int(input("Enter an element to search: "))
        left = 0
        right = len(my_list) - 1
        check = 0
        for i in range(0, len(my_list)):
            element = search_element(my_list, left, right)
            mid = element[1]
            if user_input == element[0]:
                check = 1
                print(f"Element is at index {mid}")
                break
            elif user_input < my_list[mid]:
                right = mid
            else:
                left = mid

        if check == 0:
            print("Element is not Present in Given List")
    except Exception as ex:
        logging.exception("Exception : ", ex)


if __name__ == '__main__':
    flag = True
    while flag:
        choice = int(input("1.Find Element\n2.Exit\n"))
        match choice:
            case 1:
                binary_search()
            case 2:
                flag = False
