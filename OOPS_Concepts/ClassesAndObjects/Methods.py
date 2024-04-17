# Type of methods in Class are:
# - Instance methods
# - Class methods
# - Static methods

class MyClass:
    def instancemethod(self):
        print(self.name)
        print(self.age)
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def check_age(age):
        if age >= 18:
            return True
        else:
            return False


age = 20
name = "sachin"
id = 101
if MyClass.check_age(age):
    v1 = MyClass()


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return 'Pizza({})'.format(self.ingredients)

    @classmethod
    def margherita(cls):
        return cls(['sweetcorn', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['sweetcorn', 'tomatoes', 'ham'])


a = Pizza.margherita()
print(a)
a = Pizza.prosciutto()
print(a)

# Example
import math


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return ('Pizza({}, '
                '{})').format(self.radius, self.ingredients)

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


p = Pizza(4, ['sweetcorn', 'tomatoes'])
Pizza(4, ['sweetcorn', 'tomatoes'])
print(p.area())