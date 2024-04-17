# Program to check whether a given number is Palindrome or not
number = int(input("Enter the Number:"))
reverse = 0
temp_number = number
while temp_number > 0:
    remainder = temp_number % 10
    reverse = reverse*10 + remainder
    temp_number //= 10

if number == reverse:
    print(f"{number} is a Palindrome")
else:
    print(f"{number} is not a Palindrome")

