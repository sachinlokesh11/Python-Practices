import random


def gambling(initial_stake):
    """
    Description: Checks if the gambler loses or wins
    Parameter:Initial Amount
    Return:win_flag: If Gambler wins, it returns win_flag = 1 & if loses, it returns win_flag = 0
    """
    win_flag = 0
    while (initial_stake > 0) and (initial_stake <= goal_money):
        bet = random.randint(0, 1)
        if bet == WIN_NUMBER:
            initial_stake += BET_MONEY
        else:
            initial_stake -= BET_MONEY
    if initial_stake >= goal_money:
        win_flag = 1
    return win_flag


if __name__ == "__main__":
    WIN_NUMBER = 1
    BET_MONEY = 1
    starting_stake = int(input("Enter the starting stake of Gambler: "))
    goal_money = int(input("Enter the goal money of Gambler: "))
    games_played = int(input("Enter the number of times, Gambler wants to play: "))

    win_count = lose_count = 0
    for i in range(1, games_played+1):
        result = gambling(starting_stake)
        if result == 1:
            win_count += 1
        else:
            lose_count += 1

    print(f"Gambler wins {win_count} times & percentage of win & loss are "
          f"{(win_count/games_played)*100} and {(lose_count/games_played)*100} respectively.")
