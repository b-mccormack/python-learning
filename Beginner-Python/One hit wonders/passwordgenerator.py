#generate a random password

import random
import string
seed1 = random.seed()
seed2 = random.seed(seed1)
seed3 = random.seed(seed2)
passwordLength = int(input("How many characters long do you want your random password to be?: "))
count = 0
selectionList = []
passwordList = []

random.seed(seed2)
while count < passwordLength:
	selectionList.append(random.randint(1, 9))
	count = count + 1

random.seed(seed3)
for num in selectionList:
	if num <=5:
		passwordList.append(random.randint(0, 9))
	elif num >= 6 and num <= 8:
		passwordList.append(random.choice(string.ascii_letters))
	elif num == 9:
		passwordList.append(random.choice(string.punctuation))

print("Your randomly generated password is: " + ("".join(map(str, passwordList))))