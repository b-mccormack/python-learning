horizontalPiece = " ---"
verticalPieceLead = "| "
verticalPieceTrail = " | "
lineBreak = "\n"
player1Turn = True
player2Turn = False
turnCount = 1
player1Winner = False
player2Winner = False
p1WinCondition = bool
p2WinCondition = bool

gameBoard = [["*", "*", "*",], ["*", "*", "*"], ["*", "*", "*"]]

def didplayer1win(gameBoard, p1WinCondition):
	if gameBoard[0][0] == "X" and gameBoard[1][0] == "X" and gameBoard[2][0] == "X":
		p1WinCondition = True
	elif gameBoard[0][1] == "X" and gameBoard[1][1] == "X" and gameBoard[2][1] == "X":
		p1WinCondition = True
	elif gameBoard[0][2] == "X" and gameBoard[1][2] == "X" and gameBoard[2][2] == "X":
		p1WinCondition = True
	elif gameBoard[0][0] == "X" and gameBoard[0][1] == "X" and gameBoard[0][2] == "X":
		p1WinCondition = True
	elif gameBoard[1][0] == "X" and gameBoard[1][1] == "X" and gameBoard[1][2] == "X":
		p1WinCondition = True
	elif gameBoard[2][0] == "X" and gameBoard[2][1] == "X" and gameBoard[2][2] == "X":
		p1WinCondition = True
	elif gameBoard[0][0] == "X" and gameBoard[1][1] == "X" and gameBoard[2][2] == "X":
		p1WinCondition = True
	elif gameBoard[0][2] == "X" and gameBoard[1][1] == "X" and gameBoard[2][0] == "X":
		p1WinCondition = True
	else:
		p1WinCondition = False
	return p1WinCondition;

def didplayer2win(gameBoard, p2WinCondition):
	if gameBoard[0][0] == "O" and gameBoard[1][0] == "O" and gameBoard[2][0] == "O":
		p2WinCondition = True
	elif gameBoard[0][1] == "O" and gameBoard[1][1] == "O" and gameBoard[2][1] == "O":
		p2WinCondition = True
	elif gameBoard[0][2] == "O" and gameBoard[1][2] == "O" and gameBoard[2][2] == "O":
		p2WinCondition = True
	elif gameBoard[0][0] == "O" and gameBoard[0][1] == "O" and gameBoard[0][2] == "O":
		p2WinCondition = True
	elif gameBoard[1][0] == "O" and gameBoard[1][1] == "O" and gameBoard[1][2] == "O":
		p2WinCondition = True
	elif gameBoard[2][0] == "O" and gameBoard[2][1] == "O" and gameBoard[2][2] == "O":
		p2WinCondition = True
	elif gameBoard[0][0] == "O" and gameBoard[1][1] == "O" and gameBoard[2][2] == "O":
		p2WinCondition = True
	elif gameBoard[0][2] == "O" and gameBoard[1][1] == "O" and gameBoard[2][0] == "O":
		p2WinCondition = True
	else: 
		p2WinCondition = False
	return p2WinCondition;



print((3 * horizontalPiece) + lineBreak + verticalPieceLead + str(gameBoard[0][0]) + verticalPieceTrail + str(gameBoard[0][1]) + verticalPieceTrail + str(gameBoard[0][2]) + verticalPieceTrail \
	+ lineBreak + (3 * horizontalPiece) + lineBreak + verticalPieceLead + str(gameBoard[1][0]) + verticalPieceTrail + str(gameBoard[1][1]) + verticalPieceTrail + str(gameBoard[1][2]) + verticalPieceTrail \
	+ lineBreak + (3 * horizontalPiece) + lineBreak + verticalPieceLead + str(gameBoard[2][0]) + verticalPieceTrail + str(gameBoard[2][1]) + verticalPieceTrail + str(gameBoard[2][2]) + verticalPieceTrail \
	+ lineBreak + (3 * horizontalPiece))

print("\nLets play tic-tac-toe! Place marks by entering co-ordinates as 'row,column'\n(eg. 1,3 would place a mark in the top right)")


while turnCount <= 9 and player1Winner == False and player2Winner == False:
	if player2Turn == True and player1Winner == False and player2Winner == False:
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
				player2Winner = didplayer2win(gameBoard, p2WinCondition)					
			else:
				print("There is already a mark there. Pick another spot")
		else:
			print("That co-ordinate is not on the board. Try again.")
			
	elif player1Turn == True and player1Winner == False and player2Winner == False:
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
				player1Winner = didplayer1win(gameBoard, p2WinCondition)
			else:
				print("There is already a mark there. Pick another spot")
		else:
			print("That co-ordinate is not on the board")

if player1Winner == True:
	print("Player 1 has won the game")
elif player2Winner == True:
	print("Player 2 has won the game")
else:
	print("The game is a tie")

