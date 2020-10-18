# Hangman series
# Write a program that, using the word 'EVAPORATE', asks users to guess letters one at a time and displays them as they are guessed

selectedWord = "EVAPORATE"
wordAsList = list(selectedWord)
letterCount = len(wordAsList)
nonLetterCharacter = "_"
displayList = []
playing = True
validGuess = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
isGuessValid = True
failedGuess = bool
guessUsed = bool
guessCount = 0

for i in range(letterCount):
	displayList.append(nonLetterCharacter)



while playing:

	if failedGuess == True:
		print("\nSorry, that letter does not appear in the word\n")

	print(str(" ".join(displayList)))

	if guessUsed == True:
		guessCount+=1
	
	if guessCount > 7:
		playing = False
		print("\nYou have run out of guesses!")
		break

	guessUsed = False
	failedGuess = True
	printCount = 1
	isGuessValid = True
	isLengthValid = True
	isValidLetter = False
	successfulGuess = False
	userGuess = [input("\nPlease guess a letter. Use capital letters only\n")]

	for i in validGuess:
		if i in userGuess[0]:
			isValidLetter = True

	if isValidLetter == False:
		print("Please enter a valid letter. Remember, capitals only")
		isGuessValid = False
	elif len(userGuess) > 1:
		isLengthValid = False
	elif isLengthValid == False:
		print("Please enter one letter only")
		isGuessValid = False

	while isGuessValid == True:
		count = 0
		for i in wordAsList:
			if userGuess[0] == i:
				displayList[count] = userGuess[0]
				if printCount == 1:
					print("\nYour letter does appear in the word!\n")
				printCount+=1
				failedGuess = False
				guessUsed = True
			else:
				isGuessValid = False
				guessUsed = True
			count+=1
		

	if displayList.count("_") == 0:
		playing = False
		print("You have guessed the word! The word was: " + str("".join(displayList)))