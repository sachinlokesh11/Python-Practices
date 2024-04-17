# Python Operators:

# 1-Arithmatic Operators(addition,subtraction,multiplication,division,modulus,Exponential,floor division)
# Program to perform Arithmatic Operations
a = 20
b = 3
# Addition
add = a + b
# Subtraction
sub = a - b
# Multiplication
mult = a * b
# Division
div = a / b
# Modulus
mod = a % b
# Exponential
power = a ** b
# floor division
floorDiv = a // b
print("Addition of two Numbers:{}", add)
print("Result after Subtraction:{}", sub)
print("Product of two numbers:{}", mult)
print("Quotient after division :{}", div)
# will give remainder
print("Remainder :{}", mod)
print("Result:{}", power)
# rounds the result down to the nearest whole number
print("Round Off Value after division:{}", floorDiv)
print("------------------------------------------------")

# 2-Assignment Operators
# Program to perform Assignment Operators
a = 10
# Assign value
b = a
print(b)

# Add and assign value
b += a
print(b)
# Subtract and assign value
b -= a
print(b)
# multiply and assign
b *= a
print(b)

# divide and assign value
b /= a
print(b)
print("---------------------------------------------")

# 3-Comparison Operators(greater than,less than,equal to,not equal to,greater than equal to,less than equal to)
# Program to Perform Comparison Operators
a = 13
b = 33

# Greater than
print(b > a)

# Less than
print(a > b)

# Equal to
print(a == b)

# Not Equal to
print(a != b)

# Greater than Equal to
print(b >= a)

# Less than Equal to
print(a <= b)
print("-----------------------------------")

# 4-Logical Operators(And,Or,Not)
# Program to Perform Logical Operators
# Examples of Logical Operator
a = 23
b = 17

# And operator
print(a < 25 and b > 10)

# Or Operator
print(a > 10 or b < 15)

# Not operator
print(not(a > 9))
print("--------------------------")

# 5- Identity Operators(is,is not)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# returns True because z is the same object as x
print(x is z)

# returns False because x is not the same object as y, even if they have the same content
print(x is y)

# returns true because x is not the same object as y, even if they have the same content
print(x is not y)

# difference betweeen "is" and "==": this comparison returns True because x is equal to y
print(x == y)
print("----------------------------------------")

# 6- Membership Operators(to check whether value is present in sequence or not - in,not in)
# Program to Perform membership operations
x = 24
y = 20
my_list = [10, 20, 30, 40, 50]

# 'not in' operator
if (x not in my_list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in my_list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

print("-----------------------------")

# 7-Bitwise Operators(binary Comparison)
# Program to Perform Bitwise Operations
a = 10
b = 4

# Bitwise AND
print(a & b)

# Bitwise OR
print(a | b)

# Bitwise NOT
print(~a)

# Bitwise XOR
print(a ^ b)

# Bitwise right shift
print(a >> 2)

# Bitwise left shift
print(a << 2)