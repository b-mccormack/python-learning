horizontalPiece = " ---"
verticalPiece = "|   "
lineBreak = "\n"

userSize = int(input("Please enter the grid size for the game board (e.g. for 3x3, just enter '3'): "))
count = 0

if userSize > 19:
	print("Fuck you Evan")
else: 
	while count < userSize:
		print(userSize * horizontalPiece)
		print((userSize + 1) * verticalPiece)
		count+=1
	print (userSize * horizontalPiece)


