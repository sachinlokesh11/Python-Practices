# Program to find Number is Even or Odd
check_number = lambda x: print(f"{x} is an Even Number") if x % 2 == 0 else print(f"{x} is a Odd Number")

check_number(int(input("Enter the number:")))

# Find Head or tail by flipping coin
flip_coin = lambda check: print("Its a Head") if check == 0 else print("Its Tail")

import random
flip_coin(random.randrange(0, 2))

# Program to Check For Leap Year
check_leap_year = lambda year: print(f"{year} is a leap year") if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else print(f"{year} is not a leap year")

check_leap_year(int(input("Enter the year:")))

# Program to find Maximum number
maximum_number = lambda a, b: print(f"{a} is the Maximum Number") if a > b else print(f"{b} is the Maximum Number")

maximum_number(45, 39)

# Program to use for loop with lambda expression
mylist = [4, 2, 13, 21, 5]

newlist = []

# run for loop to iterate over list
for i in mylist:
    temp = lambda i: i ** 2   # lambda function to make square of number
    newlist.append(temp(i))  # newlist = list(map(lambda v: v ** 2, mylist))
print("New List After squaring elements in list are:", newlist)

# map() function
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

list1 = list(map(lambda x: x['name'], dict_a))  # Output: ['python', 'java']
print(list1)
list2 = list(map(lambda x: x['points'] * 10, dict_a))  # Output: [100, 80]
print(list2)
list3=list(filter(lambda x: x['name'] != 'python', dict_a))
print(list3)