# Author : Blake McCormack
# Date: 17/08/2020
# Version 1.0
#
# This program takes a number and prints out its times table from 1 to 9

userNumber = int(input("Please enter a number\n"))

print("The times table for this number is:")

# Create a for loop with a range that will result in values of "i" of 1 to 12
for i in range(1,13):
    # For each pass of the loop multiple the user number by "i"
    print(str(i) + "x", "=", i * userNumber)