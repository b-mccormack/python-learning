# Check if someone has won tic tac toe

# If a game of tic tac toe is represented like so:
# game = [[1, 2, 0],
		# [2, 1, 0],
		# [2, 1, 1]]
# where 0 means an empty square, 1 means player 1 put their token in that space, and 2 is player 2's token
# write a program that determines which player has won, if any

gameBoard = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]

rows = 3
columns = 3
player1Winner = False
player2Winner = False

player1BoardCheck = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
player2BoardCheck = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

player1Wins1 = [[1, 0, 0], [1, 0, 0], [1, 0, 0]] # positions [0][0] [1][0] [2][0]
player1Wins2 = [[0, 1, 0], [0, 1, 0], [0, 1, 0]] # positions [0][1] [1][1] [2][1]
player1Wins3 = [[0, 0, 1], [0, 0, 1], [0, 0, 1]] # positions [0][2] [1][2] [2][2] 
player1Wins4 = [[1, 1, 1], [0, 0, 0], [0, 0, 0]] # positions [0][0] [0][1] [0][2]
player1Wins5 = [[0, 0, 0], [1, 1, 1], [0, 0, 0]] # positions [1][0] [1][1] [1][2]
player1Wins6 = [[0, 0, 0], [0, 0, 0], [1, 1, 1]] # positions [2][0] [2][1] [2][2]
player1Wins7 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]] # positions [0][0] [1][1] [2][2]
player1Wins8 = [[0, 0, 1], [0, 1, 0], [1, 0, 0]] # positions [0][2] [1][1] [2][0]

player2Wins1 = [[2, 0, 0], [2, 0, 0], [2, 0, 0]]
player2Wins2 = [[0, 2, 0], [0, 2, 0], [0, 2, 0]]
player2Wins3 = [[0, 0, 2], [0, 0, 2], [0, 0, 2]]
player2Wins4 = [[2, 2, 2], [0, 0, 0], [0, 0, 0]]
player2Wins5 = [[0, 0, 0], [2, 2, 2], [0, 0, 0]]
player2Wins6 = [[0, 0, 0], [0, 0, 0], [2, 2, 2]]
player2Wins7 = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
player2Wins8 = [[0, 0, 2], [0, 2, 0], [2, 0, 0]]

for i in range(columns):
	for j in range(rows):
		if gameBoard[i][j] == 1:
			player1BoardCheck[i][j] = 1 
		else:
			player1BoardCheck[i][j] = 0

for i in range(columns):
	for j in range(rows):
		if gameBoard[i][j] == 2:
			player2BoardCheck[i][j] = 2
		else:
			player2BoardCheck[i][j] = 0


