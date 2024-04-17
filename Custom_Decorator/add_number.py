# Add two numbers using custom decorator

def enter_numbers(func):                                        # step3
    number1 = int(input("Enter the first number: "))            # step4
    number2 = int(input("Enter the second number: "))           # step5

    def operations():                                           # step6, step9
        # call original function
        func(number1, number2)                                  # step10
        print("Numbers are Added")                              # step14
    return operations                                           # step7


# Decorate ordinary function
@enter_numbers                                                  # step2, step8
def add_numbers(a, b):                                          # step11
    c = a+b                                                     # step12
    print("Sum of Numbers is:", c)                              # step13


# call the decorated function
add_numbers()                                                   # step1


# enter_numbers function ko as a decorator use karenge to wo execute ho jata hai bs uske andar ka wrapper function
# tab execute hota hai jab decorator k function ko call karenge...phi ye wraper function add_numbers funciotn ko call
# karta hai
