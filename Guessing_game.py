import random

number = random.randint(1,99)
guesses = 0

print("I have chosen a number in mind from 1 to 99. Guess the number. You have 5 guesses...")
while guesses < 5:
    guess = int(input("Enter an integer from 1 to 99: "))
    print("\n")
    guesses +=1
    print("this is you %d guess." %guesses)
    if guess < number:
        print("The number is higher.")
    elif guess > number:
        print("The number is lower.")
    elif guess == number:
        break

if guess == number:
    guesses = str(guesses)
    print("You guessed the number in:", guesses + "guesses")

if guesses != number:
    number = str(number)
    print("The number was", number)