# Program to find Number is Even or Odd

a = int(input("Enter the Number to Check for Even and odd:"))
if a % 2 == 0:
    print(f"{a} is an Even Number")
else:
    print(f"{a} is an Odd Number")

print("********************************************")

# Program to Check Number is Positive or Negative

a = int(input("Enter the Number:"))
if a >= 0:
    print("Given Number is Positive")
else:
    print("Given Number is Negative")

print("*******************************")

# Program to Check For Leap Year

a = int(input("Enter the Year to be checked:"))
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")
print("******************************************")

# Program to Check Number is Positive odd ,even or negative

a = int(input("Enter the Number:"))
if a % 2 == 0:
    if a >= 0:
        print(f"{a} is Positive Even Number")
    else:
        print(f"{a} is Negative Even Number")
elif a >= 0:
    print(f"{a} is Positive Odd Number")
else:
    print(f"{a} is Negative odd Number")
print("*************************************")

# Program to find Maximum number

a = int(input("Enter the First number:"))
b = int(input("Enter the Second number:"))
c = int(input("Enter the Third number:"))
if a > b and a > c:
    print(f"{a} is the Maximum Number")
elif b > a and b > c:
    print(f"{b} is the Maximum Number")
else:
    print(f"{c} is the Maximum Number")
print("*********************************************")