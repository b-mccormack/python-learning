gameBoard = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]

horizontalPiece = " ---"
verticalPieceLead = "| "
verticalPieceTrail = " | "
lineBreak = "\n"
		
print((3 * horizontalPiece) + lineBreak + verticalPieceLead + str(gameBoard[0][0]) + verticalPieceTrail + str(gameBoard[0][1]) + verticalPieceTrail + str(gameBoard[0][2]) + verticalPieceTrail \
	+ lineBreak + (3 * horizontalPiece) + lineBreak + verticalPieceLead + str(gameBoard[1][0]) + verticalPieceTrail + str(gameBoard[1][1]) + verticalPieceTrail + str(gameBoard[1][2]) + verticalPieceTrail \
	+ lineBreak + (3 * horizontalPiece) + lineBreak + verticalPieceLead + str(gameBoard[2][0]) + verticalPieceTrail + str(gameBoard[2][1]) + verticalPieceTrail + str(gameBoard[2][2]) + verticalPieceTrail \
	+ lineBreak + (3 * horizontalPiece))


