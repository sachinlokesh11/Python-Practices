# "Given a list of integers representing the color of each sock, determine how many pairs of socks with matching
# colors are there. For example, there are 7 socks with colors [1, 2, 1, 2, 1, 3, 2]. There is one pair of color 1 and
# one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.
# Create a function that returns an integer representing the number of matching pairs of socks that are available.
# Examples
# sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) ➞ 3

def sock_merchant(given_socks):
    total_pairs = 0
    socks_color = []
    for socks in given_socks:
        if socks in socks_color:
            total_pairs += 1
            socks_color.remove(socks)
        else:
            socks_color.append(socks)
    return total_pairs


if __name__ == "__main__":
    print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))