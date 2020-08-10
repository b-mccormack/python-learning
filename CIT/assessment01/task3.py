# Author : Blake McCormack
# Date: 10/08/2020
# Version 1.0
#
# Rock Paper Scissors game
# Two players

# Ask the players for their names
print("Welcome to Rock, Paper, Scissors!")
print("Let's Begin ...")
name1 = input("Player 1: What's your name?")
name2 = input("Player 2: What's your name?\n")

print("Hello " + name1 + " and " + name2)
print(name2 + ": Close your eyes!")

# Ask the players to make their choice of throw
choice1 = input(name1 + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ")
print("Great choice! Now - cover your answer and ask " + name2 + " to choose. \n\n\n")
choice2 = input(name2 + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ")

# Put the player's choices into a list for evaluation
throwList = [choice1, choice2]

# Define all the possible outcomes in their own lists
condition1 = ["r", "s"]
condition2 = ["r", "p"]
condition3 = ["s", "p"]
condition4 = ["s", "r"]
condition5 = ["p", "r"]
condition6 = ["p", "s"]
draw1 = ["p", "p"]
draw2 = ["r", "r"]
draw3 = ["s", "s"]

# Evaluate which list matches with the player's throws and determine win/loss/draw condition accordingly
if (throwList == condition1) or (throwList == condition3) or (throwList == condition5):
	print("\nCongratulations " + name1 + ", you win!\n")

if (throwList == condition2) or (throwList == condition4) or (throwList == condition6):
	print("\nCongratulations " + name2 + ", you win!\n")

if (throwList == draw1) or (throwList == draw2) or (throwList == draw3):
	print("\nThe game is a draw!\n")

print("Thanks for playing Rock, Paper, Scissors")