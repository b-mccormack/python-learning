# The user has a number in their head. The program guesses a number, and the user inputs whether their number is higher, lower, or the correct number
# The program then adjusts accordingly and guesses again if necessary until it wins. It then prints how many guesses it took.

import random

playing = True
highNumber = 100
lowNumber = 0
numberGuesses = 0

print("Think of a number between 0 and 100. The computer will try to guess it, and you need to enter higher (h), lower (l) or coreect (c) accordingly.")

while playing == True:

	computerGuess = random.randint(lowNumber,highNumber)
	print("The computer guesses the number " + str(computerGuess))
	
	userInput = input("Is your number higher, lower or correct? ")
	if userInput == "higher" or userInput == "Higher" or userInput == "h" or userInput == "H":
		lowNumber = (computerGuess + 1)
		numberGuesses+=1
				
	elif userInput == "lower" or userInput == "Lower" or userInput == "l" or userInput == "L":
		highNumber = (computerGuess - 1)
		numberGuesses+=1
				
	elif userInput == "correct" or userInput == "Correct" or userInput == "c" or userInput == "C":
		playing = False
		print("The computer guessed that your number was " + str(computerGuess) + " in " + str(numberGuesses) + " guesses.")

	else:
		print("error")
		playing = False