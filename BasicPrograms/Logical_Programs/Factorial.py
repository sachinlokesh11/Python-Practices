# To find factorial of a number
number = int(input("Enter the Number:"))
factorial = 1
i = number
while i > 0:
    factorial *= i
    i -= 1

print(f"Factorial of {number} is :{factorial}")