import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def calc_sum(x, y):
    return x+y


def calc_multiply(x, y):
    return x*y


def calc_subtract(x, y):
    return x - y


def calc_division(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y