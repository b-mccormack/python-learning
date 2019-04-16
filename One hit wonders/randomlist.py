#generate two random lists to then compare and produce a list of all the values that overlap

import random

listA = []
listB = []
countValueA = 0
countValueB = 0
userSeedA = int(input("Please enter a random whole number, as many digits as you like"))
random.seed(userSeedA)
while countValueA < 100:
		listA.append(random.randint(0, 1000))
		countValueA = countValueA + 1

userSeedB = int(input("Please enter another random whole number, different to the first"))
random.seed(userSeedB)

while countValueB < 100:
		listB.append(random.randint(0, 1000))
		countValueB = countValueB + 1

listC = [common for common in listA if common in listB]

print("The list of common numbers between the two lists is: " + str(listC))

