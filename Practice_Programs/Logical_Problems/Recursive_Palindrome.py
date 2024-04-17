# Write a function that recursively determines if a string is a palindrome.

# Examples
# is_palindrome("abcba") ➞ True

# is_palindrome("b") ➞ True
#
# is_palindrome("") ➞ True

# is_palindrome("ad") ➞ False
# Note
# An empty string counts as a palindrome.

def check_palindrome(input_string):
    if len(input_string) < 1:
        return True
    if input_string[0] == input_string[-1]:
        return check_palindrome(input_string[1:-1])
    return False


if __name__ == "__main__":
    print(check_palindrome(""))
    print(check_palindrome("b"))
    print(check_palindrome("ad"))
    print(check_palindrome("abcba"))
