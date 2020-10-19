#Testing whether a user inputted number is odd or even
#Extra task = check if divisible by 4, if so return a different message

userNumber = int(input("Please enter any whole number"))

evenCheck = userNumber % 2
divisibleBy4 = userNumber % 4

if divisibleBy4 == 0:
	print("Your number is divisible by 4")
else:
		if evenCheck > 0:
			print("Your number is odd")
		else:
			print("Your number is even") 

#Ask user for two numbers, one number to check and one to divide by. If the number being checked divides evenly into the other number, 
#tell that to the user. Otherwise print another message

num = int(input("Please enter a number to check"))
check = int(input("Please enter a number to divide by"))
divisibleCheck = num % check

if divisibleCheck == 0:
	print(str(num) + " divides evenly into " + str(check))
else:
	print(str(num) + " does not divide evenly into " + str(check))