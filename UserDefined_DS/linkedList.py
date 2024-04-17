# Linked list operations in Python


# Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        print("Value inserted at beginning")

    # Insert at the end
    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            print("Linkedlist is Empty.\nValue is added")
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        print("Value is Inserted successfully at the end")

        # Insert after a node

    def insert_at(self, index, new_data):
        new_node = Node(new_data)
        if index == 0:
            self.insert_at_beginning(new_data)
            return

        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                new_node.next = temp.next
                temp.next = new_node
                break
            count += 1
            temp = temp.next

    # Search an element
    def search_element(self, element):

        temp = self.head

        while temp is not None:
            if temp.data == element:
                print(f"{element} is present in Linkedlist")
                return True
            temp = temp.next
        print(f"{element} is not present in Linkedlist")
        return False

    # Deleting a node
    def delete_from(self, position):
        if self.head is None:
            print("LinkedList is Empty")
            return

        if position == 0:
            self.head = self.head.next
            return

        count = 0
        temp = self.head
        while temp:
            if count == position-1:
                temp.next = temp.next.next
                break
            count += 1
            temp = temp.next

    # Print the linked list
    def printList(self):
        if self.head is None:
            print("LinkedList is Empty")
            return
        temp = self.head
        while temp:
            print(str(temp.data) + " ", end="")
            temp = temp.next


if __name__ == '__main__':

    llist = LinkedList()
    llist.insert_at_end(1)
    llist.insert_at_beginning(2)
    llist.insert_at_beginning(3)
    llist.insert_at_end(4)
    llist.insert_at(2, 5)

    print('linked list:')
    llist.printList()

    print("\nAfter deleting an element:")
    llist.delete_from(3)
    llist.printList()

    print()
    llist.search_element(3)
