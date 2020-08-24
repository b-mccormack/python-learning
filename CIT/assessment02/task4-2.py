# Author : Blake McCormack
# Date: 17/08/2020
# Version 1.0
#
# This script asks the user for a number range, and prints the sum of all the odd numbers in that range

print("\nThis script will sum all the odd numbers in a given range.")
lowerNum = int(input("Please enter the lower number of the range:\n"))
upperNum = int(input("\nPlease enter the upper number of the range:\n"))

sumOdd = 0

# Use the user's number for the range in a for loop. One is added to upperNum as "i" will only reach the upper range number minus one
for i in range(lowerNum,(upperNum+1)):
    # This checks if i is divisible by 2; if so it is an even number and is skipped
    if i % 2 == 0:
        continue
    sumOdd += i

print("\nThe sum of all the odd numbers in the given range is:", sumOdd)