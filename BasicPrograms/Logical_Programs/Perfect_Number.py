# To check for a Perfect Number
perfect_number = int(input("Enter the Number:"))
total_sum = 0
for i in range(1, perfect_number):
    if perfect_number % i == 0:
        total_sum += i


if total_sum == perfect_number:
    print(f"{perfect_number} is a perfect Number")
else:
    print(f"{perfect_number} is not a perfect Number")

