class Computer:
    def __init__(self):
        self.__max_price = 20000

    def selling_price(self):
        return f"Selling Price of computer is {self.__max_price}"

    def change_price(self, price):
        self.__max_price = price


comp = Computer()
print(comp.selling_price())
comp._max_price = 30000        # # will not change price by object name
print(comp.selling_price())    # 20000
comp.change_price(30000)       # will change price using class method
print(comp.selling_price())    # 30000


