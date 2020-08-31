# Author : Blake McCormack
# Date: 24/08/2020
# Version 1.0
#
# This programs takes a number from a user input, and outputs the factors of that number

# Define the function findFactors which will perform the operation
def findFactors(a):
    result = []
    for i in range(1,a):      # Use a for loop with the range starting at 1 and finishing at the user-defined number
        if a % i == 0:      # Check to see if the result of modulus is 0. If so, the value of i is a factor of the user number
            result += [i]      # If i has been found to be a factor, add it to the result list
    print("The factors of", userNumber, "are:", result)

# Ask the user for a number
userNumber = int(input("\nPlease enter a whole number for which you would like to find the factors:\n"))

# Call the findFactors function using the user's number as an input
findFactors(userNumber)
