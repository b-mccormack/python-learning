# Author : Blake McCormack
# Date: 19/10/2020
# Version 1.0
#
# This program performs a regex evalutation to determine the validity of an email address

# Import the regex python module
import re

# Ask the user for an email address that they would like to check for validity
userInput = str(input('\nPlease enter an email address you would like to validate:\n'))

# Assign regular expression to a variable that can be used in a function.
emailRegex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

# Define the function that will accept a regular expression and a string to test as inputs and print whether the email address is valid or not
def check_validity(regex:str,email:str):
    if(re.search(regex,email)):
        print("That is a valid email address")
    else:
        print("Sorry, that is not a valid email address")

check_validity(emailRegex,userInput)