# Create a function that finds a target number in a list of prime numbers. Implement a binary search
# algorithm in your function. The target number will be from 2 through 97. If the target is prime then return ""yes""
# else return "no".
# Examples
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# is_prime(primes, 3) ➞ "yes"
# is_prime(primes, 4) ➞ "no"


def is_prime_in_list(prime_list, search_number):
    if len(prime_list) <= 1:
        return "Yes"
    left = 0
    right = len(prime_list)-1
    mid = (left+right)/2
    if search_number > prime_list[mid]:
        left = mid
    elif search_number < prime_list[mid]:
        right = mid


if __name__ == "__main__":
    primes = []
    for number in range(2, 100):
        count = 0
        for num in range(1, number+1):
            if number%num == 0:
                count += 1
        if count == 2:
            primes.append(number)
    print(is_prime_in_list(primes, 3))
