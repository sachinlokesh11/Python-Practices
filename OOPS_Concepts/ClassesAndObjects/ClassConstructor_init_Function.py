class Person:

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # Display method
    def display(self):
        print("Name:", self.name+"\n"+"ID:", self.id)


detail = Person("Shubham Singh", 105)
detail.display()