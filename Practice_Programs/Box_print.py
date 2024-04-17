# Create a function that creates a box based on dimension n.
# Examples
# make_box(5) ➞ [
#   "#####",
#   "#   #",
#   "#   #",
#   "#   #",
#   "#####"
# ]
#
# make_box(3) ➞ [
#   "###",
#   "# #",
#   "###"
# ]
#
# make_box(2) ➞ [
#   "##",
#   "##"
# ]
#
# make_box(1) ➞ [
#     "#"
# ]

def make_box(input_dimension):
    for i in range(input_dimension):
        for j in range(input_dimension):
            if i == 0 or i == input_dimension-1 or j == 0 or j == input_dimension-1:
                print("#", end="")
            else:
                print(" ", end="")
        print()


dimension = 5
make_box(dimension)
