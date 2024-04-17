# To check for Armstrong Number
number = int(input("Enter the three  digit Number:"))
sum_ = 0
check_number = number
while check_number > 0:
    last_digit = check_number % 10
    sum_ += last_digit**3
    check_number //= 10

if sum_ == number:
    print(f"{number} is an Armstrong Number")
else:
    print(f"{number} is not an Armstrong Number")