# ask the user for a string and print out whether the string is palindrome or not

userString = input("Please enter a word or phrase: ")

stringForwards = []


for x in userString:
	stringForwards.append(x)

stringBackwards = stringForwards[::-1]

if stringForwards == stringBackwards:
	print("That word is a palindrome")
else:
	print("That word is not a palindrome")
