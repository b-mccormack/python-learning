# Author : Blake McCormack
# Date: 10/08/2020

# This program generates a random number and then invites
# the user to try and guess what that number is

import random

# Define the range within which the random number will be generated
minGuess = 1
maxGuess = 6

# Ask the user for their name and their guess
name = input("What is your name?\n")
print("\nHi", name + "!")
print("Enter a number between:", minGuess, "and", maxGuess)
guess = int(input("What is your guess?\n"))

# Generate a random number and tell the user if they won or lost
secretNumber = random.randint(minGuess,maxGuess)
if (guess != secretNumber):
    print("\nSorry, that was not the correct number\nThe correct number was", secretNumber)
else:
    print("Congratulations, you got it right! The number was", secretNumber)

print("\nThank you for playing Guess the Number\n")