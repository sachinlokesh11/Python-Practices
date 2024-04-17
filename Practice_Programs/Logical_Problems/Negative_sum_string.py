"""
Create a function that takes a string containing integers as well as other characters and return the sum of the
negative integers only.
Examples
negative_sum("" - 12
13 % 14 & -11
"") ➞ -23
-12 + -11 = -23
negative_sum(""
22
13 % 14 & -11 - 22
13
12
"") ➞ -33
-11 + -22 = -33
"""


def negative_sum(characters):
    my_characters = characters.split(" ")
    overall_sum = 0
    numbers = [int(character) for character in my_characters if character.lstrip("-").isdigit()]
    for value in numbers:
        if value < 0:
            overall_sum += value
    return overall_sum


print(negative_sum("-12 13 % 14 & -11"))
print(negative_sum("22 13 % 14 & -11 -22 13 12"))

