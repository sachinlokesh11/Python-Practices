class Parent:

    def singer(self):
        print("I am a Singer")


# define class that derive from SuperClass(Parent)
class Son(Parent):
    def dancer(self):
        print("I am a Dancer")


# define class that derive from DerivedClass1(Son)
class Grandson(Son):

    def guitarist(self):
        print("I can Play Guitar")


# create an object of DerivedClass2(Grandson)
d2 = Grandson()

d2.singer()  # Output: "I am a Singer"

d2.dancer()  # Output: "I am a Dancer"

d2.guitarist()  # Output: "I can Play Guitar"
