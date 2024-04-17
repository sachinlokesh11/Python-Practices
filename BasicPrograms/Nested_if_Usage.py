# Program to Find Maximum number using Nested if and if else statements

a = int(input("Enter the first Number:"))
b = int(input("Enter the second Number:"))
c = int(input("Enter the Third Number:"))
if a > b:
    if b > c:
        print(f"{a} is Maximum")
    elif a > c:
        print(f"{a} is Maximum")
    else:
        print(f"{c} is Maximum")
elif b > a:
    if a > c:
        print(f"{b} is Maximum")
    elif b > c:
        print(f"{b} is Maximum")
    else:
        print(f"{c} is Maximum")
else:
    print(f"{c} is Maximum")
print("**************************************")

# Program to find teenager or not

age = int(input("Enter the Age:"))
if age >= 18:
    if age <= 30:
        print("Person is a teenager")
    else:
        print("You are not a teenager")
elif age > 0:
    print("You are a Kid")
else:
    print("Invalid Input")
print("**********************************************")

# Program to Check Number Even Number Between 20 and 50

number = int(input("Enter the Number:"))
if number > 20:
    if number < 50:
        if number % 2 == 0:
            print("Number is Even between the given range")
        else:
            print("Number is Odd between the given range")
    else:
        print("Number is not Between given range")
else:
    print("Number is not Between given range")
print("******************************************************")

# Program to Find Number Present in List or not
myList = [10, 33, -30, 45, 65]
newList = [23, 45, -30, 5]
x = int(input("Enter the Number:"))
if(x in myList):
    if(x in newList):
        print("Number is present in Both the list")
    else:
        print("Number is Present is First list only")
elif(x in newList):
    print("Number is Present in second list only")
else:
    print("Number is not present in any list")
print("********************************************")

# Program to Check Account balance
amount = int(input("Enter the amount:"))
if amount > 0:
    if amount < 3000:
        print("Less than Minimum amount")
    else:
        print("Sufficient Amount balance")
else:
    print("Your Account is empty")