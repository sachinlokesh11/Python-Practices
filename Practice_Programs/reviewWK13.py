# 1.Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
# If the number is a multiple of 3 the output should be "Fizz".
# If the number given is a multiple of 5, the output should be "Buzz".
# If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
# If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples
# below.
# The output should always be a string even if it is not a multiple of 3 or 5.

# Examples
# fizz_buzz(3) ➞ "Fizz"

# fizz_buzz(5) ➞ "Buzz"

# fizz_buzz(15) ➞ "FizzBuzz"

def multiple_of_3(num):
    return True if num % 3 == 0 else False


def multiple_of_5(num):
    return True if num % 5 == 0 else False


def check_multiple(input_number):
    if multiple_of_3(input_number):
        if multiple_of_5(input_number):
            return "FizzBuzz"
        return "Fizz"
    if multiple_of_5(input_number):
        return "Buzz"
    return input_number


print(check_multiple(21))


# 2.Write a function that takes a list of numbers and returns a list with two elements:
# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.
# Example
# sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# # 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9
#
# sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])
#
# sum_odd_and_even([0, 0]) ➞ [0, 0])
#
# Notes
# Count 0 as an even number.

def sum_odd_and_even(input_list):
    output_list = [sum([odd_number for odd_number in input_list if odd_number % 2 == 0])]
    odd_sum = [sum([even_number for even_number in input_list if even_number % 2 != 0])]
    output_list.append(odd_sum[0])
    return output_list


my_list = [-1, -2, -3, -4, -5, -6]
print(sum_odd_and_even(my_list))