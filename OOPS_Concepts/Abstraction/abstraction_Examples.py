# ************** Example 1 *******************
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):

    def move(self):
        print("I can walk and run")


class Snake(Animal):

    def move(self):
        print("I can crawl")


class Dog(Animal):

    def move(self):
        print("I can bark")


class Lion(Animal):

    def move(self):
        print("I can roar")


# Creating object for Class Human
R = Human()
R.move()
# Creating object for Class Snake
K = Snake()
K.move()
# Creating object for Class Dog
R = Dog()
R.move()
# Creating object for Class Lion
K = Lion()
K.move()


# ************************ Example 2 ***********************************
class Employee(ABC):

    @abstractmethod
    def present(self):
        pass


class PartTimeEmployee(Employee):

    def present(self):
        print("Employee is Present For Part Time")


class FullTimeEmployee(Employee):

    def present(self):
        print("Employee is Present For Full Time")


# Creating Object For Derived class
p1 = PartTimeEmployee()
p1.present()

p2 = FullTimeEmployee()
p2.present()


# ******************* Example 3 ************************************
class Addition(ABC):

    @abstractmethod
    def add(self, a, b):
        pass


class Math(Addition):
    def add(self, a, b):
        c = a + b
        return c


addition = Math()
result = addition.add(5, 9)
print("Sum of two numbers is:", result)
