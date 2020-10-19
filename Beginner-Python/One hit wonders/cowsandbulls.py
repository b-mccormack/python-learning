#Create a cows and bulls game. Generate a four digit number, for every number the user guesses correctly and in the correct position they get a cow
#For every number they guess incorrectly they get a bull. When the user guesses the correct number, the game is over.

import random
random.seed()

def compare_numbers(userListFixed, computerList):
	count1 = 0
	cowBullCount = [0, 0]
	while count1 < 4:
		if userListFixed[count1] == computerList[count1]:
			cowBullCount[1]+=1
		else:
			cowBullCount[0]+=1
		count1 = count1 + 1
	return cowBullCount

def convert(list):
	s = [str(i) for i in computerList]
	cowBullString = str("".join(s))
	return(cowBullString)

if __name__ == "__main__":
	playing = True
	guesses = 0

	computerList = []
	count = 0

	while count < 4:
		computerList.append(random.randint(0,9))
		count = count + 1

	while playing:
		userNumber = list(input("Please enter a four digit number. If you enter more, only the first four digits will be used. "))
		userListFull = []
		for i in userNumber:
			userListFull.append(i)

		userListFixed = [int(i) for i in userListFull[0:4]]

		didTheyWin = compare_numbers(userListFixed, computerList)
		guesses+=1

		print("You have " + str(didTheyWin[0]) + " cows, and " + str(didTheyWin[1]) + " bulls")

		if didTheyWin[1] == 4:
			playing = False
			print("Congrats, you won in " + str(guesses) + " guesses. The number was " + convert(list))
			break
		else:
			print("Your guess isn't quite right, try again")
