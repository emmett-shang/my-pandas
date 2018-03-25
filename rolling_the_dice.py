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
    print(random.randint(min,max))
    print(random.randint(min,max))

    roll_again = input("Do you want to roll the dice again?")