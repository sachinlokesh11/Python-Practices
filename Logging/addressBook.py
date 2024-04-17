import logging

# Create logger
logger = logging.getLogger(__name__)

# Set Logging Level
logger.setLevel(logging.DEBUG)

# Set Format
formatter = logging.Formatter("%(levelname)s: %(name)s: %(message)s")

# Add file handler
file_handler = logging.FileHandler("addressBook.log")

# Set format to file handler
file_handler.setFormatter(formatter)

# now add handler to logger
logger.addHandler(file_handler)


class AddressBook:
    def __init__(self, first_name, last_name, number, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email
        self.location = location

    def full_name(self):
        logger.info({f"FullName: {self.first_name} {self.last_name}"})

    def address(self):
        logger.info({f"Address: {self.number}, {self.email},  {self.location}"})


emp1 = AddressBook("Shubham", "Singh", 7584833939, "shubh@gmail.com", "SRE")
emp2 = AddressBook("Rahul", "Singh", 7584833939, "rahul@gmail.com", "Dehradun")
emp3 = AddressBook("Raj", "Singh", 7583433939, "raj@gmail.com", "Delhi")


emp1.full_name(), emp1.address()
emp2.full_name(), emp2.address()
emp3.full_name(), emp2.address()




