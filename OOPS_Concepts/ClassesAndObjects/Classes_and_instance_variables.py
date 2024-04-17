class Employee:
    # class Variables
    no_of_leaves = 10


# Objects of class
shubham = Employee()
rahul = Employee()
print(shubham, rahul)
# output-create two different objects
# <__main__.Employee object at 0x00000177CEE0BED0> <__main__.Employee object at 0x00000177CEE0BE50>

# Object variables/instance variables
shubham.id = 101
shubham.department = "Manager"
rahul.id = 102
rahul.department = "HR"
print(shubham.id, rahul.id)
# output - value of instance variables
# 101 102

# Class variables can be accessed through class name as well as object name
print(Employee.no_of_leaves)
print(shubham.no_of_leaves)
print(rahul.no_of_leaves)
# output - 10

# Class variables can only be changed by class name
rahul.no_of_leaves = 15
print(Employee.no_of_leaves)   # 10
# rahul object will create its own variable named no_of_leaves
print(rahul.no_of_leaves)      # 15

# class has attribute __dict__ to show all properties all objects and class
print(Employee.__dict__)
print(rahul.__dict__)
print(shubham.__dict__)
# output
# {'__module__': '__main__', 'no_of_leaves': 10, '__dict__': <attribute '__dict__' of 'Employee' objects>,
# '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
# {'id': 102, 'department': 'HR', 'no_of_leaves': 15}
# {'id': 101, 'department': 'Manager'}


