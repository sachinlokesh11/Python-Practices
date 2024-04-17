# Program to find the length of last word in  given string


intro = "My name is Shubham Singh studying in Bridgelabz  "

words = intro.split(" ")
last_word = words.pop()
length = len(last_word)
print(f"The last word is \"{last_word}\" with length {length}")