# Instructions
# The dice game Yacht is from the same family as Poker Dice, Generala and particularly Yahtzee, of which it is a precursor. In the game, five dice are rolled and the result can be entered in any of twelve categories. The score of a throw of the dice depends on category chosen.

# Scores in Yacht
# Category	Score	Description	Example
# Ones	1 × number of ones	Any combination	1 1 1 4 5 scores 3
# Twos	2 × number of twos	Any combination	2 2 3 4 5 scores 4
# Threes	3 × number of threes	Any combination	3 3 3 3 3 scores 15
# Fours	4 × number of fours	Any combination	1 2 3 3 5 scores 0
# Fives	5 × number of fives	Any combination	5 1 5 2 5 scores 15
# Sixes	6 × number of sixes	Any combination	2 3 4 5 6 scores 6
# Full House	Total of the dice	Three of one number and two of another	3 3 3 5 5 scores 19
# Four of a Kind	Total of the four dice	At least four dice showing the same face	4 4 4 4 6 scores 16
# Little Straight	30 points	1-2-3-4-5	1 2 3 4 5 scores 30
# Big Straight	30 points	2-3-4-5-6	2 3 4 5 6 scores 30
# Choice	Sum of the dice	Any combination	2 3 3 4 6 scores 18
# Yacht	50 points	All five dice showing the same face	4 4 4 4 4 scores 50

# If the dice do not satisfy the requirements of a category, the score is zero. If, for example, Four Of A Kind is entered in the Yacht category, zero points are scored. A Yacht scores zero if entered in the Full House category.

# Task
# Given a list of values for five dice and a category, your solution should return the score of the dice for that category. If the dice do not satisfy the requirements of the category your solution should return 0. You can assume that five values will always be presented, and the value of each will be between one and six inclusively. You should not assume that the dice are ordered.


# Change the values as you see fit.
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):
    points = 0
    if category == 'ONES':
        for card in dice:
            if card == 1:
                points += 1
    elif category == 'TWOS':
        for card in dice:
            if card == 2:
                points += 2
    elif category == 'THREES':
        for card in dice:
            if card == 3:
                points += 3
    elif category == 'FOURS':
        for card in dice:
            if card == 4:
                points += 4
    elif category == 'FIVES':
        for card in dice:
            if card == 5:
                points += 5
    elif category == 'SIXES':
        for card in dice:
            if card == 6:
                points += 6
    elif category == 'FULL_HOUSE':
        no_repts = set(dice)
        if (len(set(dice)) == 2) and ((dice.count(dice[0]) == 2) or (dice.count(dice[0]) == 3)):
            points += sum(dice)
    elif category == 'FOUR_OF_A_KIND':
        no_repts = set(dice)
        if (len(set(dice)) == 2) and ((dice.count(dice[0]) == 1) or (dice.count(dice[0]) == 4)):
            highest_count = 1
            highest_count_card = ''
            for card in dice:
                if dice.count(card) > highest_count:
                    highest_count = dice.count(card)
                    highest_count_card = card
            points += (highest_count * highest_count_card)
        elif len(set(dice)) == 1:
            points += dice[0] * 4
    elif category == 'LITTLE_STRAIGHT':
        if set(dice) == {1,2,3,4,5}:
            points += 30
    elif category == 'BIG_STRAIGHT':
        if set(dice) == {2,3,4,5,6}:
            points += 30
    elif category == 'CHOICE':
        points += sum(dice)
    elif category == 'YACHT':
        if len(set(dice)) == 1:
            points += 50
    
    return points
    
print(score([5, 5, 5, 5, 5], 'YACHT'))

print(score([1, 1, 1, 3, 5], 'ONES'))