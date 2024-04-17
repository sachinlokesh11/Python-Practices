# Given a lottery ticket, represented by a list of 2-value lists, create a function to find out if
# you've won the jackpot.

# To do this, you must first count the "mini-wins" on your ticket. Each sublist has both a string and a number
# within it. If the character code of any of the characters in the string matches the number, you get a mini-win.
# Note you can only have one mini-win per sublist.
# Once you have counted all of your mini-wins, compare that number to the other input provided (win). If your number
# of mini-wins is more than or equal to win, return Winner!. Else, return Loser!.

# Examples
# lottery([["YYW", 70], ["WXK", 65], ["RPDI", 88]], 2)
# ➞ "Loser!"

# lottery([["KG", 80], ["NTBBVZ", 79], ["CI", 73], ["AGXMEE", 74], ["IU", 68], ["VOSP" , 84]], 1)
# ➞ "Winner!"

# lottery([["ZSAMZB", 81], ["XWWCXP", 72], ["SYBRQOHP", 88], ["HJSVV", 75]], 1)
# ➞ "Loser!"


def lottery_ticket(my_ticket, win_requires):
    min_tickets = 0
    for ticket in my_ticket:
        for ticket_number in ticket[0]:
            if ord(ticket_number) == ticket[1]:
                min_tickets += 1
                break

    return "Winner" if min_tickets >= win_requires else "Loser"


if __name__ == "__main__":
    print(lottery_ticket([["KG", 80], ["NTBBVZ", 79], ["CI", 73], ["AGXMEE", 74], ["IU", 68], ["VOSP", 84]], 1))
    print(lottery_ticket([["ZSAMZB", 81], ["XWWCXP", 72], ["SYBRQOHP", 88], ["HJSVV", 75]], 1))