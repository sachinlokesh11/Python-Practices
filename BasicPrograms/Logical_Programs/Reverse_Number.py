# Find Reverse of a number
number = int(input("Enter the Number:"))
reverse_number = 0
while number > 0:
    remainder = number % 10
    reverse_number = reverse_number*10 + remainder
    number = int(number/10)

print(f"Reverse of a Number is {reverse_number}")
