# Multiply two numbers using custom decorator

def enter_numbers(func):                                        # step2
    number1 = int(input("Enter the first number: "))            # step3
    number2 = int(input("Enter the second number: "))           # step4

    def operation():                                            # step5, step8
        # call original function
        func(number1, number2)                                  # step9
        print("Numbers are Multiplied")                         # step13
    return operation                                            # step6


#  define ordinary function
def multiply_numbers(a, b):                                     # step10
    c = a*b                                                     # step11
    print("Product of Numbers is:", c)                          # step12


# decorate the ordinary function
multiply_numbers = enter_numbers(multiply_numbers)              # step1

# call the decorated function
multiply_numbers()                                              # step7
