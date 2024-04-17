# Prime Factors of a Given Number
number = int(input("Enter the Number to find its Prime Factors:"))
factors = []
prime_factors = []
for i in range(1, number+1):
    if number % i == 0:
        factors.append(i)
        flag = 0
        if i > 1:
            for check in range(2, i):
                if i % check == 0:
                    flag = 1
        if flag == 0 and i >1:
            prime_factors.append(i)


print(f"Factors of {number} are:{factors}")
print(f"Prime Factors of {number} are:{prime_factors}")
