# List Comprehension in Python
# List comprehension offers a shorter syntax when we want to create a new list based on the values of an existing list.

# Without List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# with List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# Syntax for newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits if "a" in x]

print(newlist)


# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# ************************* Dictionary Comprehension **************************
#  A dictionary comprehension takes the form {key: value for (key, value) in iterable}
# Python code to demonstrate dictionary comprehension

# Lists to represent keys and values
keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]
# zip returns object
print(zip(keys, values))
# dict comprehension
myDict = {k: v for (k, v) in zip(keys, values)}

# We can use below too
# myDict = dict(zip(keys, values))

print(myDict)

# Python code to demonstrate dictionary creation using list comprehension
myDict = {x: x**2 for x in [1, 2, 3, 4, 5]}
print(myDict)

# Nested dictionary comprehension
string = "ABC"

# using dictionary comprehension
dic = {
  x: {y: x + y for y in string} for x in string
}

print(dic)

