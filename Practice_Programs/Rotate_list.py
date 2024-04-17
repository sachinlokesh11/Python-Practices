# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
#      1-->2-->3-->4-->5
#      5-->1-->2-->3-->4   for k = 1
#      4-->5-->1-->2-->3   for k = 2
# Output: [4,5,1,2,3]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def return_last(self):
        if self.head is None:
            print("LinkedList is Empty")
        temp = self.head
        while temp.next.next:
            temp = temp.next
        return temp.next.data

    def delete_last(self):
        if self.head is None:
            print("LinkedList is Empty")
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def print_list(self):
        if self.head is None:
            print("LinkedList is Empty")
        temp = self.head
        while temp is not None:
            print(temp.data, "-->", end=' ')
            temp = temp.next


if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.add_element(5)
    linkedList.add_element(4)
    linkedList.add_element(3)
    linkedList.add_element(2)
    linkedList.add_element(1)
    linkedList.print_list()
    print()
    flag = True
    while flag:
        choice = int(input("Enter 1 to Rotate, 2 to Exit:\n"))
        match choice:
            case 1:
                rotation = int(input("Enter how many times you want to rotate list: "))
                for x in range(rotation):
                    last_element = linkedList.return_last()
                    linkedList.delete_last()
                    linkedList.add_element(last_element)
                    linkedList.print_list()
                    print()
            case 2:
                flag = False


