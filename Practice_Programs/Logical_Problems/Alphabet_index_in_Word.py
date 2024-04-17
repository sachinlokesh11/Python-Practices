# 4.Given a name, return the letter with the highest index in alphabetical order, with its corresponding index,
# in the form of a string. You are prohibited to use max() nor is reassigning a value to the alphabet list allowed.

# Examples
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
# "v", "w", "x", "y", "z"]

# alphabet_index(alphabet, "Flavio") ➞ "22v"

# alphabet_index(alphabet, "Andrey") ➞ "25y"
# alphabet_index(alphabet, "Oscar") ➞ "19s"

def alphabet_index(alphabet, word):
    highest_index = 0
    alpha = ''
    for alphabets in word:
        index = alphabet.index(alphabets.lower())
        if index > highest_index:
            highest_index = index
            alpha = alphabets
    return str(highest_index+1)+alpha


if __name__ == "__main__":
    my_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                 "v", "w", "x", "y", "z"]
    print(alphabet_index(my_alphabet, "Flavio"))
    print(alphabet_index(my_alphabet, "Andrey"))
    print(alphabet_index(my_alphabet, "Oscar"))