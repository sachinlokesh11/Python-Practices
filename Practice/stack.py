# Simple python program to perform push and pop operation in a stack


stack = []


def push_element():
    element = input("Enter the Element To be Added: ")
    stack.append(element)
    print("Element Added is:", element)
    print(stack)


def pop_element():
    if not stack:
        print("Stack is Empty")
    else:
        a = stack.pop()
        print("Removed Element is:", a)
        print(stack)


if __name__ == "__main__":
    while True:
        print("Select the operation 1.Push 2.Pop 3.Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            push_element()
        elif choice == 2:
            pop_element()
        elif choice == 3:
            break
        else:
            print("Enter the valid option")

