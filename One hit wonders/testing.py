sample = "Testing the new line feature. \nThis is a new line"
print(sample)



#Calculate the percentage of pay packet spent on coffee
wages = float(input("How much were you paid?"))
numberCoffees = int(input("How many coffees did you have?"))
priceCoffees = float(input("How much did each coffee cost?"))
coffeeSpending = float(numberCoffees * priceCoffees)
coffeeBudgetPercentage = (coffeeSpending / wages) * 100
print("The percentage of your wage spent on coffee is " + str(coffeeBudgetPercentage) + str("%"))



#Calculate the year someone turns 100
userName = str(input("What is your name?"))
userAge = int(input("What is your age in whole numbers"))
currentYear = int(input("What is the current year?"))
birthdayYet = input("Have you had your birthday this year, yes or no?")

yearsToGo = int(100 - userAge)
yearTurn100 = int(yearsToGo + currentYear)

if birthdayYet == "No" or "no":
        print(str(userName) + str(", you will turn 100 in the year ") + str((yearTurn100 - 1)))
else:
        print(str(userName) + str(", you will turn 100 in the year ") + str(yearTurn100))
        
#print multiple copies of result
numberCopies = int(input("Please enter a number between 1 and 20"))

if birthdayYet == "No" or "no":
        for numberCopies in range(numberCopies):
        	print((str(userName) + str(", you will turn 100 in the year ") + str((yearTurn100 - 1))))
else:
        for numberCopies in range(numberCopies):
        	print(numberCopies * (str(userName) + str(", you will turn 100 in the year ") + str(yearTurn100)))
