# operations in Queue using LinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.rear is None:
            self.front = self.rear = Node(data)
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next
        print("Value is added")

    def dequeue(self):
        if self.front is None:
            return "Queue is Empty"
        else:
            self.front = self.front.next
            print("Element is removed")

    def is_empty(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print("Queue is not Empty")

    def size(self):
        count = 0
        temp = self.front
        while temp:
            count += 1
            temp = temp.next
        return count

    def print_queue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            while temp is not None:
                print(temp.data, "-->", end=" ")
                temp = temp.next


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(20)
    queue.enqueue(10)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.dequeue()
    print(queue.size())
    queue.is_empty()
    queue.print_queue()


