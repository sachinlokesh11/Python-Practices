# Iterators in Python
# An iterator is an object that can be iterated upon, meaning that we can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the
# methods __iter__() and __next__().

# defining tuple
mytuple = ("apple", "banana", "cherry")

# creating iterator from tuple
myit = iter(mytuple)

# getting all the elements of iterator
print(next(myit))
print(next(myit))
print(next(myit))

# getting all the elements of iterator using for loop
myList = [2, 6, 4, 9]
iterator = iter(myList)
for element in iterator:
    print(element)

# custom Iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Custom Iterator using StopIterator
# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
# To prevent the iteration to go on forever, we can use the StopIteration statement.

# will stop after 10 numbers
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 10:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)