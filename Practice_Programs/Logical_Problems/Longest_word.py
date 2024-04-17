# Write a function that will return the longest word in a sentence. In cases where more than one word is found,
# return the first one.

# Examples
# find_longest("A thing of beauty is a joy forever.") ➞ "forever"
#
# find_longest("Forgetfulness is by all means powerless!") ➞ "forgetfulness"
#
# find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel.") ➞
# "strengths"
# Notes
# Special characters and symbols don't count as part of the word.


def find_longest_word(sentence):
    my_words = sentence.split()
    if len(my_words) <= 1:
        return my_words[0]
    longest_word = find_longest_word(" ".join(my_words[1:]))
    return longest_word if len(longest_word) > len(my_words[0]) else my_words[0]


if __name__ == "__main__":
    print(find_longest_word("A thing of beautyyyyyyy is a joy forever"))
    print(find_longest_word("Forgetfulness is by all means powerless!"))
    print(find_longest_word('"Strengths" is the longest and most commonly used word that contains only a single vowel.'))

