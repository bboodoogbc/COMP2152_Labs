
# Solution for Week02 lab 2
# Name: Billy Boodoo
# Student number: 100867472
# Submission
# Link: https://github.com/bboodoogbc/COMP2152_Labs.git

# "Rock, Paper, Scissors" Game

import random

choice = ['Rock', 'Paper', 'Scissors']

playerChoice = input("Enter your choice - 1.Rock, 2.Paper, 3.Scissors: ")
# print(playerChoice)

playerChoice = int(playerChoice)
# print(type(playerChoice))

# Input check
if playerChoice < 1 or playerChoice > 3:
    print("Invalid choice! Please select a number between 1 and 3.")
else:
    # Develop the game logic through if/elif/else statements
    computerChoice = random.randint(1, 3)

    if playerChoice == computerChoice:
        print("It's a tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("You win! Rock crushes Scissors.")
    elif playerChoice == 2 and computerChoice == 1:
        print("You win! Paper covers Rock.")
    elif playerChoice == 3 and computerChoice == 2:
        print("You win! Scissors cut Paper.")
    else:
        print("You Lose! Computer wins!")

    