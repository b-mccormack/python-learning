#Have the user input the number, then print if the number is prime or not

userNum = int(input("Enter any number to check if it is a prime number"))

numberIsPrime = True

if userNum > 1:
	while numberIsPrime == True:
		for x in range(2, userNum):
			if userNum % x == 0:
				numberIsPrime = False
				break
		if numberIsPrime == False:
			print("That number is not prime")
		else:
			print("That number is a prime number")
			break

else:
	print("That number is not prime")

