# Constructors in Class
# Types Of Constructors are:
# 1-Default Constructor-The default constructor is a simple constructor that does not accept any arguments.
class Vehicle:
    #default constructor
    def __init__(self):
         pass

    # parameter constructor
    def __init__(self, bike_name, top_speed):
        self.bike_name = bike_name
        self.top_speed = top_speed


bike_1 = Vehicle('bullet', 130)
bike_2 = Vehicle('honda', 129)
print("Bike Name:", bike_1.bike_name, "," "Bike Maximum Speed:", bike_1.top_speed)
print("Bike Name:", bike_2.bike_name, "," "Bike Maximum Speed:", bike_2.top_speed)
