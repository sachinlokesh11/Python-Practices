# John is playing a dice game. The rules are as follows.
# Roll two dice.
# Add the numbers on the dice together.
# Add the total to your overall score.
# Repeat this for three rounds.
# But if you roll DOUBLES, your score is instantly wiped to 0 and your game ends immediately!
# Create a function that takes in a list of tuples as input, and return John's score after his game has ended.
# Examples
# dice_game([(1, 2), (3, 4), (5, 6)]) ➞ 21
# dice_game([(1, 1), (5, 6), (6, 4)]) ➞ 0
# dice_game([(4, 5), (4, 5), (4, 5)]) ➞ 27
import random


def calculate_scorecard(dice_numbers):
    print(dice_numbers)
    overall_score = 0
    for numbers in dice_numbers:
        if numbers[0] == numbers[1]:
            return 0
        overall_score += sum(numbers)
    return overall_score


if __name__ == "__main__":
    numbers_on_dice = [tuple([random.randrange(1, 7), random.randrange(1, 7)]) for rounds in range(1, 4)]
    print(calculate_scorecard(numbers_on_dice))