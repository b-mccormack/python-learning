# Write a program that takes a user input in the form "row,column" and places their piece in the relevant location.


gameBoard = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]

player1Turn = True
player2Turn = False
turnCount = 1

print("Lets play tic-tac-toe! Place pieces by entering co-ordinates as row,column (eg. 1,3 would place a mark in the top right")

while turnCount <= 8:
	
	if player2Turn == True:
		player2Input = input("Player 2, please place your piece: ")
		player2InputList = player2Input.split(",")
		player2Row = int(player2InputList[0]) - 1
		player2Column = int(player2InputList[1]) - 1
		if player2Row <= 2 and player2Column <=2:
			if gameBoard[player2Row][player2Column] == 0:
				gameBoard[player2Row][player2Column] = "O"
				turnCount+=1
				player2Turn = False
				player1Turn = True
				print(gameBoard[0])
				print(gameBoard[1])
				print(gameBoard[2])
			else:
				print("There is already a mark there. Pick another spot")
		else:
			print("That co-ordinate is not on the board. Try again.")
			
	if player1Turn == True:
		player1Input = input("Player 1, please place your piece: ")
		player1InputList = player1Input.split(",")
		player1Row = int(player1InputList[0]) - 1
		player1Column = int(player1InputList[1]) - 1
		if player1Row <= 2 and player1Column <= 2:
			if gameBoard[player1Row][player1Column] == 0:
				gameBoard[player1Row][player1Column] = "X"
				turnCount+=1
				player1Turn = False
				player2Turn = True
				print(gameBoard[0])
				print(gameBoard[1])
				print(gameBoard[2])
			else:
				print("There is already a mark there. Pick another spot")
		else:
			print("That co-ordinate is not on the board")



print("The board is full")