# Check if someone has won tic tac toe

# If a game of tic tac toe is represented like so:
# game = [[1, 2, 0],
		# [2, 1, 0],
		# [2, 1, 1]]
# where 0 means an empty square, 1 means player 1 put their token in that space, and 2 is player 2's token
# write a program that determines which player has won, if any

gameBoard = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
player1Winner = False
player2Winner = False

# winning combination positions (if all are 1 or all are 2, the respective player has won)
# [0][0] [1][0] [2][0]
# [0][1] [1][1] [2][1]
# [0][2] [1][2] [2][2] 
# [0][0] [0][1] [0][2]
# [1][0] [1][1] [1][2]
# [2][0] [2][1] [2][2]
# [0][0] [1][1] [2][2]
# [0][2] [1][1] [2][0]

while player1Winner == False and player2Winner == False:
	if gameBoard[0][0] == 1 and gameBoard[1][0] == 1 and gameBoard[2][0] == 1:
		player1Winner = True
	elif gameBoard[0][1] == 1 and gameBoard[1][1] == 1 and gameBoard[2][1] == 1:
		player1Winner = True
	elif gameBoard[0][2] == 1 and gameBoard[1][2] == 1 and gameBoard[2][2] == 1:
		player1Winner = True
	elif gameBoard[0][0] == 1 and gameBoard[0][1] == 1 and gameBoard[0][2] == 1:
		player1Winner = True
	elif gameBoard[1][0] == 1 and gameBoard[1][1] == 1 and gameBoard[1][2] == 1:
		player1Winner = True
	elif gameBoard[2][0] == 1 and gameBoard[2][1] == 1 and gameBoard[2][2] == 1:
		player1Winner = True
	elif gameBoard[0][0] == 1 and gameBoard[1][1] == 1 and gameBoard[2][2] == 1:
		player1Winner = True
	elif gameBoard[0][2] == 1 and gameBoard[1][1] == 1 and gameBoard[2][0] == 1:
		player1Winner = True
	elif gameBoard[0][0] == 2 and gameBoard[1][0] == 2 and gameBoard[2][0] == 2:
		player2Winner = True
	elif gameBoard[0][1] == 2 and gameBoard[1][1] == 2 and gameBoard[2][1] == 2:
		player2Winner = True
	elif gameBoard[0][2] == 2 and gameBoard[1][2] == 2 and gameBoard[2][2] == 2:
		player2Winner = True
	elif gameBoard[0][0] == 2 and gameBoard[0][1] == 2 and gameBoard[0][2] == 2:
		player2Winner = True
	elif gameBoard[1][0] == 2 and gameBoard[1][1] == 2 and gameBoard[1][2] == 2:
		player2Winner = True
	elif gameBoard[2][0] == 2 and gameBoard[2][1] == 2 and gameBoard[2][2] == 2:
		player2Winner = True
	elif gameBoard[0][0] == 2 and gameBoard[1][1] == 2 and gameBoard[2][2] == 2:
		player2Winner = True
	elif gameBoard[0][2] == 2 and gameBoard[1][1] == 2 and gameBoard[2][0] == 2:
		player2Winner = True
	else:
		print("Oops, something went wrong")
		break

if player1Winner == True:
	print("Player 1 has won the game")
elif player2Winner == True:
	print("Player 2 has won the game")
else:
	print("Nobody has won the game")
