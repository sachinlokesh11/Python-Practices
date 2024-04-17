# In simpler terms chaining decorators means decorating a function with multiple decorators.

def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner


# First decor got called nd then decor1
@decor1
@decor
def num():
    return 10


# First decor1 got called nd then decor
@decor
@decor1
def num2():
    return 10


print(num())
print(num2())


# Output:

# 400
# 200
# The above example is similar to calling the function as –

# decor1(decor(num))
# decor(decor1(num2))
