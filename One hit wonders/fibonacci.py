#Ask the user how many fibonacci numbers they would like to generate, then print out the sequence

userNum = int(input("How many fibonacci numbers would you like to see? Enter a whole number"))
fibList = [1, 1]
count = 1

while count <= userNum:
		addNum = fibList[count] + fibList[count-1]
		fibList.append(addNum)
		count = count + 1

print(fibList)

