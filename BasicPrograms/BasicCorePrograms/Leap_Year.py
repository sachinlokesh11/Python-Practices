# Program to Check For Leap Year

a = int(input("Enter the Year to be checked:"))
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")