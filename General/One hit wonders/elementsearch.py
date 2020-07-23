# Write a function that takes an ordered list of numbers, and another number. The function decides whether or not the given number is inside the list and returns (then prints)
# an appropriate boolean


list1 = [2, 6, 8, 11, 11, 11, 21, 22, 23, 24, 29, 31, 40, 44, 45, 49, 50, 51, 58, 60, 64, 65, 66, 82, 84, 88, 88, 89, 93, 97]
print(list1)
userNumber = int(input("Please enter a two digit number to see if it is in the list"))
isInList = False

for i in list1:
	if i == userNumber:
		isInList = True
	

if isInList == True:
	print("Your number is in the list")
else:
	print("That number does not appear in the list")
