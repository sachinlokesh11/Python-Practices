# The self parameter is a reference to the current instance of the class, and is used to access variables that
# belongs to the class.
#  We can call it whatever name we like, but it has to be the first parameter of any function in the class:

# Use the words myparameter and abc instead of self:

class Person:

  def __init__(myparameter, name, age):
    myparameter.name = name
    myparameter.age = age


  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Shubham", 26)
p1.myfunc()

# We can modify object properties
p1.age = 25
print(p1.age)

# We can delete object properties
del p1.age
# delete object
del p1


# Pass Statement

class Person:
  pass

# having an empty class definition like this, would raise an error without the pass statement