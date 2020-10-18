horizontalPiece = " ---"
verticalPieceLead = "| "
verticalPieceTrail = " | "
lineBreak = "\n"
player1Turn = True
player2Turn = False
turnCount = 1
player1Winner = False
player2Winner = False

gameBoard = [["*", "*", "*",], ["*", "*", "*"], ["*", "*", "*"]]

print((3 * horizontalPiece) + lineBreak + verticalPieceLead + str(gameBoard[0][0]) + verticalPieceTrail + str(gameBoard[0][1]) + verticalPieceTrail + str(gameBoard[0][2]) + verticalPieceTrail \
					+ lineBreak + (3 * horizontalPiece) + lineBreak + verticalPieceLead + str(gameBoard[1][0]) + verticalPieceTrail + str(gameBoard[1][1]) + verticalPieceTrail + str(gameBoard[1][2]) + verticalPieceTrail \
					+ lineBreak + (3 * horizontalPiece) + lineBreak + verticalPieceLead + str(gameBoard[2][0]) + verticalPieceTrail + str(gameBoard[2][1]) + verticalPieceTrail + str(gameBoard[2][2]) + verticalPieceTrail \
					+ lineBreak + (3 * horizontalPiece))

print("\nLets play tic-tac-toe! Place pieces by entering co-ordinates as 'row,column'\n(eg. 1,3 would place a mark in the top right)")

while player1Winner == False and player2Winner == False and turnCount <=9:
	if gameBoard[0][0] == "X" and gameBoard[1][0] == "X" and gameBoard[2][0] == "X":
		player1Winner = True
	elif gameBoard[0][1] == "X" and gameBoard[1][1] == "X" and gameBoard[2][1] == "X":
		player1Winner = True
	elif gameBoard[0][2] == "X" and gameBoard[1][2] == "X" and gameBoard[2][2] == "X":
		player1Winner = True
	elif gameBoard[0][0] == "X" and gameBoard[0][1] == "X" and gameBoard[0][2] == "X":
		player1Winner = True
	elif gameBoard[1][0] == "X" and gameBoard[1][1] == "X" and gameBoard[1][2] == "X":
		player1Winner = True
	elif gameBoard[2][0] == "X" and gameBoard[2][1] == "X" and gameBoard[2][2] == "X":
		player1Winner = True
	elif gameBoard[0][0] == "X" and gameBoard[1][1] == "X" and gameBoard[2][2] == "X":
		player1Winner = True
	elif gameBoard[0][2] == "X" and gameBoard[1][1] == "X" and gameBoard[2][0] == "X":
		player1Winner = True
	elif gameBoard[0][0] == "O" and gameBoard[1][0] == "O" and gameBoard[2][0] == "O":
		player2Winner = True
	elif gameBoard[0][1] == "O" and gameBoard[1][1] == "O" and gameBoard[2][1] == "O":
		player2Winner = True
	elif gameBoard[0][2] == "O" and gameBoard[1][2] == "O" and gameBoard[2][2] == "O":
		player2Winner = True
	elif gameBoard[0][0] == "O" and gameBoard[0][1] == "O" and gameBoard[0][2] == "O":
		player2Winner = True
	elif gameBoard[1][0] == "O" and gameBoard[1][1] == "O" and gameBoard[1][2] == "O":
		player2Winner = True
	elif gameBoard[2][0] == "O" and gameBoard[2][1] == "O" and gameBoard[2][2] == "O":
		player2Winner = True
	elif gameBoard[0][0] == "O" and gameBoard[1][1] == "O" and gameBoard[2][2] == "O":
		player2Winner = True
	elif gameBoard[0][2] == "O" and gameBoard[1][1] == "O" and gameBoard[2][0] == "O":
		player2Winner = True
	
	elif player2Turn == True:
		player2Input = input("Player 2, please place your 'O': ")
		player2InputList = player2Input.split(",")
		player2Row = int(player2InputList[0]) - 1
		player2Column = int(player2InputList[1]) - 1
		if player2Row <= 2 and player2Column <=2:
			if gameBoard[player2Row][player2Column] == "*":
				gameBoard[player2Row][player2Column] = "O"
				turnCount+=1
				player2Turn = False
				player1Turn = True
				print((3 * horizontalPiece) + lineBreak + verticalPieceLead + str(gameBoard[0][0]) + verticalPieceTrail + str(gameBoard[0][1]) + verticalPieceTrail + str(gameBoard[0][2]) + verticalPieceTrail \
					+ lineBreak + (3 * horizontalPiece) + lineBreak + verticalPieceLead + str(gameBoard[1][0]) + verticalPieceTrail + str(gameBoard[1][1]) + verticalPieceTrail + str(gameBoard[1][2]) + verticalPieceTrail \
					+ lineBreak + (3 * horizontalPiece) + lineBreak + verticalPieceLead + str(gameBoard[2][0]) + verticalPieceTrail + str(gameBoard[2][1]) + verticalPieceTrail + str(gameBoard[2][2]) + verticalPieceTrail \
					+ lineBreak + (3 * horizontalPiece))
			else:
				print("There is already a mark there. Pick another spot")
		else:
			print("That co-ordinate is not on the board. Try again.")
			
	elif player1Turn == True:
		player1Input = input("Player 1, please place your 'X': ")
		player1InputList = player1Input.split(",")
		player1Row = int(player1InputList[0]) - 1
		player1Column = int(player1InputList[1]) - 1
		if player1Row <= 2 and player1Column <= 2:
			if gameBoard[player1Row][player1Column] == "*":
				gameBoard[player1Row][player1Column] = "X"
				turnCount+=1
				player1Turn = False
				player2Turn = True
				print((3 * horizontalPiece) + lineBreak + verticalPieceLead + str(gameBoard[0][0]) + verticalPieceTrail + str(gameBoard[0][1]) + verticalPieceTrail + str(gameBoard[0][2]) + verticalPieceTrail \
					+ lineBreak + (3 * horizontalPiece) + lineBreak + verticalPieceLead + str(gameBoard[1][0]) + verticalPieceTrail + str(gameBoard[1][1]) + verticalPieceTrail + str(gameBoard[1][2]) + verticalPieceTrail \
					+ lineBreak + (3 * horizontalPiece) + lineBreak + verticalPieceLead + str(gameBoard[2][0]) + verticalPieceTrail + str(gameBoard[2][1]) + verticalPieceTrail + str(gameBoard[2][2]) + verticalPieceTrail \
					+ lineBreak + (3 * horizontalPiece))
			else:
				print("There is already a mark there. Pick another spot")
		else:
			print("That co-ordinate is not on the board")

if gameBoard[0][0] == "X" and gameBoard[1][0] == "X" and gameBoard[2][0] == "X":
	player1Winner = True
elif gameBoard[0][1] == "X" and gameBoard[1][1] == "X" and gameBoard[2][1] == "X":
	player1Winner = True
elif gameBoard[0][2] == "X" and gameBoard[1][2] == "X" and gameBoard[2][2] == "X":
	player1Winner = True
elif gameBoard[0][0] == "X" and gameBoard[0][1] == "X" and gameBoard[0][2] == "X":
	player1Winner = True
elif gameBoard[1][0] == "X" and gameBoard[1][1] == "X" and gameBoard[1][2] == "X":
	player1Winner = True
elif gameBoard[2][0] == "X" and gameBoard[2][1] == "X" and gameBoard[2][2] == "X":
	player1Winner = True
elif gameBoard[0][0] == "X" and gameBoard[1][1] == "X" and gameBoard[2][2] == "X":
	player1Winner = True
elif gameBoard[0][2] == "X" and gameBoard[1][1] == "X" and gameBoard[2][0] == "X":
	player1Winner = True
elif gameBoard[0][0] == "O" and gameBoard[1][0] == "O" and gameBoard[2][0] == "O":
	player2Winner = True
elif gameBoard[0][1] == "O" and gameBoard[1][1] == "O" and gameBoard[2][1] == "O":
	player2Winner = True
elif gameBoard[0][2] == "O" and gameBoard[1][2] == "O" and gameBoard[2][2] == "O":
	player2Winner = True
elif gameBoard[0][0] == "O" and gameBoard[0][1] == "O" and gameBoard[0][2] == "O":
	player2Winner = True
elif gameBoard[1][0] == "O" and gameBoard[1][1] == "O" and gameBoard[1][2] == "O":
	player2Winner = True
elif gameBoard[2][0] == "O" and gameBoard[2][1] == "O" and gameBoard[2][2] == "O":
	player2Winner = True
elif gameBoard[0][0] == "O" and gameBoard[1][1] == "O" and gameBoard[2][2] == "O":
	player2Winner = True
elif gameBoard[0][2] == "O" and gameBoard[1][1] == "O" and gameBoard[2][0] == "O":
	player2Winner = True

if player1Winner == True:
	print("Player 1 has won the game")
elif player2Winner == True:
	print("Player 2 has won the game")
else:
	print("The game is a tie")
