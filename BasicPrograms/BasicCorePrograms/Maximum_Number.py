# Program to find Maximum number

a = int(input("Enter the first number:"))
b = int(input("Enter the Second number:"))
c = int(input("Enter the third number:"))
if a > b and a > c:
    print(f"{a} is the Maximum Number")
elif b > a and b > c:
    print(f"{b} is the Maximum Number")
else:
    print(f"{c} is the Maximum Number")