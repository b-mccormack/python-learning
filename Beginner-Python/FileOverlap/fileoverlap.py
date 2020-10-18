# Given two text files that have lists of numbers in them, find the numbers that are overlapping.
# One text file has a list of all prime numbers, under 1000, the other has a list of happy numbers up to 1000

openPrimeNumbers = open("primenumbers.txt", "r")
openHappyNumbers = open("happynumbers.txt", "r")
primeString = openPrimeNumbers.read()
happyString = openHappyNumbers.read()
primeList = primeString.split("\n")
happyList = happyString.split("\n")

combinedList = []

for i in primeList:
	if i in happyList:
		combinedList.append(i)

print(combinedList)