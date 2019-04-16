#take a list, and write a program that prints out all the elements of the list that are less than 5

listA = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 4, 3]
listB = []
countValue = 0
comparisonValue = 0	

while countValue < len(listA): #Every time this runs, 1 is added to countValue. For as long as countValue is less than the number of entries in the list, this continues to run
	comparisonValue = listA[countValue] #Pulls a number from listA in position countValue
	if comparisonValue < 5:     #Compares the value pulled from the list to see if it is less than 5
		listB.append(comparisonValue)	#if the compared value is less than 5, it is appended to listB
	countValue = countValue + 1		#add 1 to countValue to continue the loop	

print(listB) #print listB which is all of the values from listA that are less than 5

#Ask user for a number, return only numbers from the list that are smaller than that number

userNumber = int(input("Please enter a number"))

print([number for number in listA if number < userNumber])