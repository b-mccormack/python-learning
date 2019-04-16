#Generate a random number between 1 and 9. Have the user input a number, then tell them if they guessed too high, too low or correctly

import random
randomNum = random.randint(1, 9)

guessCorrect = False

while guessCorrect == False:
	userGuess = int(input("Try to guess the computer's number. Enter a whole number between 1 and 9"))
	if userGuess == randomNum:
		print("You guessed correctly!")
		guessCorrect = True
	else:
		if userGuess > randomNum:
				print("Your guess was too high, try again")
		if userGuess < randomNum:
				print("Your guess was too low, try again")