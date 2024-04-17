# Create a function that takes in n, a, b and returns the number of positive values raised to the nth power that
# lie in the range [a, b], inclusive.
# Examples
# power_ranger(2, 49, 65) ➞ 2
# 2 squares (n^2) lie between 49 and 65, 49 (7^2) and 64 (8^2)
# power_ranger(3, 1, 27) ➞ 3
# 3 cubes (n^3) lie between 1 and 27, 1 (1^3), 8 (2^3) and 27 (3^3)
# power_ranger(10, 1, 5) ➞ 1
# 1 value raised to the 10th power lies between 1 and 5, 1 (1^10)
# power_ranger(5, 31, 33) ➞ 1
# power_ranger(4, 250, 1300) ➞ 3


def power_ranger(power, first_number, second_number):
    total_numbers = 0
    first_num = int(first_number**(1/power))
    second_num = int(second_number**(1/power))
    for index in range(first_num, second_num+1):
        if (index**power >= first_number) and (index**power <= second_number):
            total_numbers += 1
    return total_numbers


if __name__ == "__main__":
    print(power_ranger(2, 49, 65))
    print(power_ranger(3, 1, 27))
    print(power_ranger(10, 1, 5))
    print(power_ranger(5, 31, 33))
    print(power_ranger(4, 250, 1300))
