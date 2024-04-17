# Given a singly-linked list of integers, delete its head node, and advance the head pointer to point at the
# next node in line.
#
# Input : 1 -> 2 —> 3 —> 4 —> None
# Output: 2 —> 3 —> 4 —> None
#
# Input : 1 —> None
# Output: None
#
# Input : None
# Output: None


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

    def delete_head(self):
        if self.head is None:
            print("LinkedList is Empty")
            return
        self.head = self.head.next
        print("Head Node is Deleted Successfully ")

    def print_list(self):
        if self.head is None:
            print("LinkedList is Empty")
        temp = self.head
        while temp is not None:
            print(temp.data, "-->", end=' ')
            temp = temp.next


if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.add_element(20)
    linkedList.add_element(14)
    linkedList.add_element(17)
    linkedList.add_element(23)
    linkedList.print_list()
    print()
    flag = True
    while flag:
        choice = int(input("Enter 1 to delete further 2 to exist\n"))
        match choice:
            case 1:
                linkedList.delete_head()
                linkedList.print_list()
                print()
            case 2:
                flag = False


