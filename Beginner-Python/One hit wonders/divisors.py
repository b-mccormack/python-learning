#Create a program that asks user for a number, then prints a list of all the divisors of that number

userNumber = int(input("Please enter a number"))

userRange = range(1, userNumber)

divisorList = [divisor for divisor in userRange if (userNumber % divisor) == 0]

print("The divisors of this number are: " + str(divisorList))