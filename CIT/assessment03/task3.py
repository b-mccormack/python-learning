# Author : Blake McCormack
# Date: 31/08/2020
# Version 1.0
#
# This program is designed to be a simple inventory management system for a small accounting firm

staffDetails = {'Some Person' : ['0400111222','Accountant','95000']}

# Define the main function which will be called when the application starts
def main():
    print("\nWelcome to the WIDGET inventory management system\n")
    menuText = "\nPlease select from the following menu options:\n\n\
        1 = Enter staff details\n\
        2 = See staff pay rates\n\
        3 = See a list of required IT hardware\n\
        4 = See the costing for IT hardware\n\
        5 = Exit\n\n\
        Please enter your selection: "
    menuSelection = str(input(menuText))
    if menuSelection == '1':
        addStaffDetails()
    elif menuSelection == '2':
        staffPayRates()
    elif menuSelection == '3':
        gadgetList()
    elif menuSelection == '4':
        gadgetCosting()
    elif menuSelection == '5':
        exit()
    else:
        print("\nError: You did not enter a valid menu selection. Please enter a number between 1 and 4")
        main()

def addStaffDetails():
    print('This is addStaffDetails')

def staffPayRates():
    print('This is staffPayRates')
    print(staffDetails['Some Person'][2])

def gadgetList():
    print('This is gadgetList')

def gadgetCosting():
    print('This is gadgetCosting')


main()

