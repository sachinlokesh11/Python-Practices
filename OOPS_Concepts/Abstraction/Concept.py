
# Abstraction in python is defined as a process of handling complexity by
# hiding unnecessary information from the user.
# When we want to provide a common interface for different implementations of a component, we use an abstract class.

# Python program showing abstract base class work

# ABC is super base class for every abstract class
from abc import ABC, abstractmethod


class Polygon(ABC):

    # Decorator
    @abstractmethod
    def no_of_sides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def no_of_sides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def no_of_sides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def no_of_sides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def no_of_sides(self):
        print("I have 4 sides")


# Driver code
# Creating Object for Triangle class
R = Triangle()
R.no_of_sides()
# Creating Object for Quadrilateral class
K = Quadrilateral()
K.no_of_sides()
# # Creating Object for Pentagon class
R = Pentagon()
R.no_of_sides()
# # Creating Object for Hexagon class
K = Hexagon()
K.no_of_sides()