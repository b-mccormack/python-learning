# Author : Blake McCormack
# Date: 10/08/2020
# Version 1.0
#
# This program will ask the user what their birth year is, and if they have had a birthday yet this year
# It will write an output with their current age, and wish them a happy birthday past or present depending on whether it has passed or not

currentYear = 2020

# Ask the user what their birth year was and if they have had their birthday yet this year
birthYear = int(input("Please enter your birth year as a four digit number:\n"))
birthdayYet = str(input("\nHave you had your birthday yet this year? Type 'y' or 'n':\n"))

# Assign different variables for the user's current age and the birthday message to print according to their answer
if (birthdayYet == 'y'):
    currentAge = currentYear - birthYear
    birthdayMessage = "Happy Birthday!"
else:
    currentAge = currentYear - birthYear - 1
    birthdayMessage = "I hope you have a good birthday!"

print("Your current age is:", currentAge)
print(birthdayMessage)
