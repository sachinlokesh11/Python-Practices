# Write a program to sort a list using bubble sort


def bubble_sort(my_list):
    for x in range(len(my_list)-1, 0, -1):
        for y in range(x):
            if my_list[y] > my_list[y+1]:
                temp = my_list[y]
                my_list[y] = my_list[y+1]
                my_list[y+1] = temp
    return my_list


if __name__ == "__main__":
    my_list = [19, 2, 31, 45, 6, 11, 121, 27]
    print(bubble_sort(my_list))
