# Write a function that picks a random word from the SOWPODS dictionary (sowpods.txt)

# The below counted how many lines were in sowpods.txt (there are 267751). This was to define the range for random number generation
#reading = True
#openDictionary = open("sowpods.txt", "r")
#currentWord = ""
#count = 0
#readDictionary = openDictionary.readlines()

#while reading == True:
#	currentWord = readDictionary[count]
#	count+=1
#	if currentWord == "ZZZS":
#		reading = False
#print(count)

import random

randomNum = random.randint(0,267751)

openDictionary = open("sowpods.txt", "r")

readDictionary = openDictionary.readlines()

print(readDictionary[randomNum])