# operations in Stack using LinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        print(f"{data} is added to the stack")

    def pop(self):
        if self.top is None:
            print("Stack is Empty")
            return None
        else:
            print(f"{self.top.data} is removed from the stack")
            self.top = self.top.next

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.top is None:
            print("Stack is Empty")
            return None
        else:
            print("The value at top is:", self.top.data)

    def size(self):
        count = 0
        temp = self.top
        while temp:
            count += 1
            temp = temp.next
        print("Size of stack is:", count)

    def print_stack(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            while temp is not None:
                print(temp.data, "-->", end=" ")
                temp = temp.next


if __name__ == '__main__':
    stack = Stack()
    stack.push(40)
    stack.push(30)
    stack.push(20)
    stack.push(10)
    stack.print_stack()
    print()
    print(stack.is_empty())
    stack.peek()
    stack.size()
    stack.pop()
    print("Stack after Operations is:")
    stack.print_stack()



