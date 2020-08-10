#Make a two player rock paper scissors game. Have both players make their plays, then print a congrats for the winner


player1 = input("Player 1, do you throw rock, paper or scissors?")
if player1 == "Rock":
	player1 = "rock"

if player1 == "Scissors":
	player1 = "scissors"

if player1 == "Paper":
	player1 = "paper"


player2 = input("Player 2, do you throw rock, paper or scissors?")

if player2 == "Rock":
	player2 = "rock"

if player2 == "Scissors":
	player2 = "scissors"

if player2 == "Paper":
	player2 = "paper"

throwList = [player1, player2]

condition1 = ["rock", "scissors"]
condition2 = ["rock", "paper"]
condition3 = ["scissors", "paper"]
condition4 = ["scissors", "rock"]
condition5 = ["paper", "rock"]
condition6 = ["paper", "scissors"]
draw1 = ["paper", "paper"]
draw2 = ["rock", "rock"]
draw3 = ["scissors", "scissors"]

if (throwList == condition1) or (throwList == condition3) or (throwList == condition5):
	print("Player 1 wins")

if (throwList == condition2) or (throwList == condition4) or (throwList == condition6):
	print('Player 2 wins')

if (throwList == draw1) or (throwList == draw2) or (throwList == draw3):
	print('The game is a draw')