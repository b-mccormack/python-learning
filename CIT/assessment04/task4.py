# Author : Blake McCormack
# Date: 19/10/2020
# Version 1.0
#
# This program checks in an input string starts or ends with a vowel

# Import the regex python module
import re

# Ask the user for a string that they would like to check
userInput = str(input('\nWelcome! This program will check if a string starts and ends with a vowel.\nPlease enter the string you would like to test:\n'))

# Assign regular expression to a variable that can be used in a function.
regex = '^[aeiou].*[aeiou]$'

# Define the function that will accept a regular expression and a string to test as inputs and print whether the string matches the regex
def check_validity(regex:str,testString:str):
    if(re.search(regex,testString)):
        print("That string starts and ends with a vowel!")
    else:
        print("Sorry, that does not start and end with a vowel")

check_validity(regex,userInput)