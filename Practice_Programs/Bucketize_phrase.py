# Write a function that divides a phrase into word buckets, with each bucket containing n or fewer characters.
# Only include full words inside each bucket.
# Examples
# bucketize("she sells sea shells by the sea", 10)
# ➞ ["she sells", "sea shells", "by the sea"]
# bucketize("the mouse jumped over the cheese", 7)
# ➞ ["the", "mouse", "jumped", "over", "the", "cheese"]
# bucketize("fairy dust coated the air", 20)
# ➞ ["fairy dust coated", "the air"]
# bucketize("a b c d e", 2)
# ➞ ["a", "b", "c", "d", "e"]

# bucketize("she sells sea shells by the sea", 10)
def bucketize(given_phrase, max_characters):
    words = given_phrase.split(" ")
    my_bucket = []
    previous = ""
    for word in words:
        if len(word)+len(previous)+1 <= max_characters:
            previous += " "+word
        else:
            my_bucket.append(previous)
            previous = word
    my_bucket.append(previous)
    return my_bucket


if __name__ == "__main__":
    print(bucketize("she sells sea shells by the sea", 10))
    print(bucketize("the mouse jumped over the cheese", 7))
    print(bucketize("fairy dust coated the air", 20))
    print(bucketize("a b c d e", 2))
