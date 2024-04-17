# JSON in python
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# Python has a built-in package called json, which can be used to work with JSON data.

# ***************** Convert from JSON to Python *******************
import json
# JSON string: MULTILINE STRING in TRIPLE quotes
data_JSON = """
    {
        "size": "Medium",
        "price": 15.67,
        "toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
        "client": {
            "name": "Jane Doe",
            "phone": "455-344-234",
            "email": "janedoe@email.com"
        }
    }
"""
print("JSON String is:", data_JSON)

# parse x:will write the data in python dictionary format in y using loads() method
# We will use the string with JSON format to create a Python dictionary that we can access, work with,
# and modify.
data_dict = json.loads(data_JSON)

# the result is a Python dictionary:
print("JSON String in Python Object is:", data_dict)

# ************  Convert from Python to JSON ************

# Python dictionary:
client = {
    "name": "Nora",
    "age": 56,
    "id": "45355",
    "eye_color": "green",
    "wears_glasses": False
}

# convert into JSON:Using dumps() method
client_JSON = json.dumps(client, indent=4)

# the result is a JSON string:
print("Python Dictionary in JSON String is:", client_JSON)


# ****************** Convert a Python object containing all the legal data types *******************
x = {
  "name": "Virat",
  "age": 27,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
# Using indent parameter to define the numbers of indents
print(json.dumps(x, indent=4))
# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))

# checking after encoding and after decoding
# Here variable hand is tuple
hand = (8, "Q")
print("Value initially is:", hand)
print("Type before encoding is:", type(hand))
# this tuple is converted to json string
encoded_hand = json.dumps(hand)
print("Type after encoding is:", type(encoded_hand))
# now json string is converted back to python object
decoded_hand = json.loads(encoded_hand)
print("Type after decoding is:", type(decoded_hand))
print("Final Value is:", decoded_hand)
# checking for equality
print("Both are equal:", hand == decoded_hand)
print("Both are equal:", hand == tuple(decoded_hand))
