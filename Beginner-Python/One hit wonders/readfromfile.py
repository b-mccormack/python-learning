# Using the supplied list of names in Training-Names.txt, count how many of each name is in the file and print the results.

openFile = open('Training-Names.txt', 'r')
namesBigString = openFile.read()
namesList = namesBigString.split("\n")

LeaCount = 0
DarthCount = 0
LukeCount = 0

for i in namesList:
	if i == "Lea":
		LeaCount+=1
	elif i == "Darth":
		DarthCount+=1
	elif i == "Luke":
		LukeCount+=1

print("Lea appears " + str(LeaCount) + " times, Darth appears " + str(DarthCount) + " times, and Luke appears " + str(LukeCount) + " times")