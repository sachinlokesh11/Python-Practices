# Polymorphism in Python

# What is Polymorphism?
# The literal meaning of polymorphism is the condition of occurrence in different forms.

# Polymorphism is a very important concept in programming.
# It refers to the use of a single type entity (method, operator or object) to represent
# different types in different scenarios.
from math import pi

# Example 1: Polymorphism in addition operator
num1 = 1
num2 = 2
print(num1+num2)

str1 = "Python"
str2 = "Programming"
print(str1+" "+str2)

# Function Polymorphism in Python
# Example 2: Polymorphic len() function
print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))

# Output
#
# 9
# 3
# 2


# Class Polymorphism in Python
# Example 3: Polymorphism in Class Methods
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


# Polymorphism and Inheritance
# Example 4: Method Overriding
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())

# Output
#
# Circle
# I am a two-dimensional shape.
# Squares have each angle equal to 90 degrees.
# 153.93804002589985


# Note: Method Overloading, a way to create multiple methods with the same name
# but different arguments, is not possible in Python.