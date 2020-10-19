# Hangman series
# Write a program that picks a random word from the SOWPODS dictionary, and has the user guess one letter at a time to find the word
# The user should have limited guesses, and upon either running out of guesses or guessing the word successfully, should have the 
# option of playing the game again.
# For extra challenge, have the program draw the figure being hanged as incorrect guesses are made.

import random

def main():
	randomNum = random.randint(0, 267751)
	openDictionary = open("sowpods.txt", "r")
	readDictionary = openDictionary.readlines()

	selectedWord = (readDictionary[randomNum])
	wordAsList = list(selectedWord)
	letterCount = len(wordAsList)
	nonLetterCharacter = "_"
	displayList = []
	playing = True
	validGuess = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
		'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	isGuessValid = True
	failedGuess = bool
	guessCount = 0

	for i in range(letterCount - 1):
		displayList.append(nonLetterCharacter)


	while playing:

		if failedGuess == True:
			print("\nSorry, that letter does not appear in the word\n")
			guessCount += 1

		print(str(" ".join(displayList)))

		if guessCount > 7:
			playing = False
			print("\nYou have run out of guesses! The word was: " + selectedWord)
			userPlayAgain = input("\nWould you like to play again? Y/N: ").upper()
			if userPlayAgain == "Y":
				main()
			else:
				exit()
			break

		failedGuess = True
		printCount = 1
		isGuessValid = True
		isLengthValid = True
		isValidLetter = False
		userGuess = [input("\nPlease guess a letter.\n").upper()]

		for i in validGuess:
			if i in userGuess[0]:
				isValidLetter = True

		if isValidLetter == False:
			print("Please enter a valid letter.")
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
					printCount += 1
					failedGuess = False
				else:
					isGuessValid = False
					
				count+=1
			

		if displayList.count("_") == 0:
			playing = False
			print("You have guessed the word! The word was: " + selectedWord)
			userPlayAgain = input("\nWould you like to play again? Y/N: ").upper()
			if userPlayAgain == "Y":
				main()
			else:
				exit()

main()