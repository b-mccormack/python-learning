# Author : Blake McCormack
# Date: 19/10/2020
# Version 1.0
#
# This program performs a regex evalutation to determine the validity of an email address

# Import the regex python module
import re

userInput = str(input('\nPlease enter an email address you would like to validate:\n'))

emailRegex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

if(re.search(emailRegex,userInput)):
    print("Valid Email")
else:
    print("Invalid Email")