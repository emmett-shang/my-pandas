import random

"""
http://www.pythonforbeginners.com/code-snippets-source-code/game-rolling-the-dice
"""

min = 1
max = 6

roll_again = 'yes'

while roll_again == 'yes' or roll_again == 'y':
    print("rolling the dice...")
    print("the values are...")
    dice_1 = random.randint(min, max)
    print(dice_1)

    dice_2 = random.randint(min, max)
    print(dice_2)

    print("the difference between the numbers are = ...")

    print(abs(dice_1 - dice_2))

    roll_again = input("Do you want to roll the dice again?")
