# Write a function that accepts the height and width (m, n) and an optional proc s and generates a list with m
# elements.
# Each element is a string consisting of either:
# The default character (hash #) repeating n times (if no proc is given).
# The character passed in through the proc repeating n times.
# Examples
# make_rug(3, 5, '#') ➞ [
#   "#####",
#   "#####",
#   "#####"
# ]
# make_rug(3, 5, '$')  ➞ [
#   "$$$$$",
#   "$$$$$",
#   "$$$$$"
# ]
# make_rug(2, 2, 'A')  ➞ [
#   "AA",
#   "AA"
# ]

def make_rug(height, width, character):
    if not character:
        character = '#'
    output_list = ["".join([character for width in range(width)]) for height in range(height)]
    return output_list


if __name__ == "__main__":
    print(make_rug(2, 2, 'A'))
    print(make_rug(3, 5, ''))
    print(make_rug(3, 5, '$'))
    print(make_rug(5, 2, '#'))