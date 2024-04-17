# Condition and statements in python
# if statement
if 10 > 5:
    print("Condition is true")
print("************************************")

# if..else statement
x = 10
y = 20
if x > y:
    print("Condition is true")
else:
    print("Condition is false")
print("************************************")

# if..elif statement(checks for second condition if first is false)
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
print("*************************************")

# Nested if
x = 41
if x > 10:
  print("Number is above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
print("**********************************")

# Pass Statement
x = 40
y = 50
if x < y:
     pass
print("Pass successfully")
print("***************************************")

# ifelse using ternary operator
a = 330
b = 330
print("A is greater") if a > b else print("Both are equal") if a == b else print("B is greater")