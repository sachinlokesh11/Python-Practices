my_string = "My name is shubham singh. I live in saharanpur, Uttar Pradesh. I have 10 friends."
my_list = my_string.split(". ")
for sentence in my_list:
    print(sentence)
mystring_lowercase = my_string.lower()

# count_a = count_e = count_i = count_o = count_u = 0
# for char in mystring_lowercase:
#     if char == "a":
#         count_a += 1
#         vowels_dictionary.update({"a": count_a})
#     elif char == "e":
#         count_e += 1
#         vowels_dictionary.update({"e": count_e})
#     elif char == "i":
#         count_i += 1
#         vowels_dictionary.update({"i": count_i})
#     elif char == "o":
#         count_o += 1
#         vowels_dictionary.update({"o": count_o})
#     elif char == "u":
#         count_u += 1
#         vowels_dictionary.update({"u": count_u})
vowels_list = ["a", "e", "i", "o", "u"]
vowels_dictionary = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
for char in mystring_lowercase:
    if char in vowels_list:
        vowels_dictionary[char] += 1


print(vowels_dictionary)


