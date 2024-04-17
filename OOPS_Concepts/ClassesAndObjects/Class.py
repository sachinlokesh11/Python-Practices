#  The class is the replica or blueprint of the object.
# A class consist of mainly four thing attribute, constructor ,method and property.

# Working with Class and Instance Variables Together

class Vehicle:
    #class variables
    vehicle_type= "bike"
    wheel= 2
    #Constructor with instance variables bike_name and max_speed
    def __init__(self, bike_name, max_speed):
        self.bike_name= bike_name
        self.max_speed= max_speed
    # Method with instance variable tyre_size
    def tyre_description(self, tyre_size):
        print("Tyre Size is:", tyre_size)

bike_ = Vehicle("Bullet",120)
bike_.tyre_description(40)
print("Type of Bike:", bike_.bike_name)
print("Maximum Speed of Bike is:", bike_.max_speed)