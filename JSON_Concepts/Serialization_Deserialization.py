# using dump() and Load() method for serialization and deserialization
import json

data = {
  "name": "Sachin",
  "age": 27,
  "married": True,
  "divorced": False,
  "children": ("Khushi", "Neeraj"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# Serialization of person_details json file
with open("person_detail.json", "w") as write_file:
    json.dump(data, write_file, indent=4)
    print("Data is added Successfully")

# Deserialization of person_details json file
with open("person_detail.json", "r") as read_file:
    y = json.load(read_file)
    print(y)

# Deserialization of Pizza json file
with open("Pizza.json", "r") as read:
    data = json.load(read)
    print(data)

# Now we can perform modifications in json file data which get stored in variable data
print(len(data))
print(data["orders"])
print(data["orders"][0]["toppings"])

for order in data["orders"]:
    del order["client"]

print(data["orders"])

# Writing this modified dictionary to new json file created at a time
with open("new_Pizza.json", "w") as write:
    json.dump(data, write, indent=4)
    print(data)



