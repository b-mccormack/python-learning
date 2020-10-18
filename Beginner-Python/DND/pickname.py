import random

openFirstNames = open("firstnames.txt", "r")
readFirstNames = openFirstNames.readlines()
numLines1 = sum(1 for line in open('firstnames.txt'))
randomNum1 = random.randint(0,(numLines1 - 1))
firstName = readFirstNames[randomNum1]


openLastNames = open("lastnames.txt", "r")
readLastNames = openLastNames.readlines()
numLines2 = sum(1 for line in open('lastnames.txt'))
randomNum2 = random.randint(0,(numLines2 - 1))
lastName = readLastNames[randomNum2]

print("Your dwarf name is " + str(firstName) + " " + str(lastName))