# Create a function that takes the age in years and returns the age in days.

# Examples
# calc_age(65) ➞ 23725

# calc_age(0) ➞ 0

# calc_age(20) ➞ 7300
# Notes
# Use 365 days as the length of a year for this challenge.
# Ignore leap years and days between last birthday and now.
# Expect only positive integer inputs.

def calculate_age_as_days(given_age):
    days_in_year = 365
    total_days_in_given_age = given_age*days_in_year
    return total_days_in_given_age


if __name__ == "__main__":
    age = int(input("Enter your age:"))
    print(calculate_age_as_days(age))
