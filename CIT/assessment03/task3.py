# Author : Blake McCormack
# Date: 31/08/2020
# Version 1.0
#
# This program is designed to be a simple inventory management system for a small accounting firm

import time

# Create a dictionary containing existing staff details
staffDetails = {'Jane Doe' : ['0400111222','Accountant','95000'],\
    'John Doe' : ['0400123123','Lawyer','110000'], 'Sam Daniels' : ['0401987567','Accountant','97000'],\
    'Steve McKinley' : ['0402735244','Human Resources','62000'], 'Bruce Fletcher' : ['0423846247','Office Manager','106000'],\
    'Leah Smith' : ['0463855233','Accountant','107500'], 'Karen Bucket' : ['0432574836','Business Owner','154000'],\
    'Jessica Lovatt' : ['0427946139','Accountant','102000'], 'Matthew Hewitt' : ['0427946725','Manager','101000'],\
    'Keiran Potter' : ['0428947363','Accountant','104700']}

# Defining the equipment amounts required per staff member
staffPerRouter = 10
staffPerServer = 5
staffPerSwitch = 5
staffPerLaptop = 1
totalStaff = len(staffDetails) # Value equal to the number of entries in the dictionary

# Working out the number of hardware devices required here to avoid duplicating code in the gadgetList and gadgetCosting functions
numberRouters = totalStaff // staffPerRouter
numberServers = totalStaff // staffPerServer
numberSwitches = totalStaff // staffPerSwitch
numberLaptops = totalStaff // staffPerLaptop

# Define the main function which will be called when the application starts
def main():
    print("\nWelcome to the WIDGET inventory management system")
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
        print("\nError: You did not enter a valid menu selection. Please enter a number between 1 and 5")
        time.sleep(3)
        main()

def addStaffDetails():
    print(staffDetails['Jane Doe'][1])

def staffPayRates():
    print('\nThe yearly salaries for staff members are as follows:\n')
    salarySum = 0
    for i in staffDetails: # Iterate through each staff member in the dictionary and print the name and salary in each pass
        salarySum += int(staffDetails[i][2]) # Add the currently selected staff member's salary to the running total
        print(i + " = $" + str(staffDetails[i][2]))
    print("\nThe total value of all staff salaries is $" + str(salarySum)) # Print the complete total value of the staff salaries
    # Menu selection for the user to return to main or exit
    userContinue = input(str("\nWould you like to return to the menu? y/n\n"))
    if userContinue == 'y' or userContinue == 'Y':
        main()
    else:
        exit()

def gadgetList():
    print("The total hardware required for the company is as follows:")
    print("\nRouters = " + str(numberRouters))
    print("Servers = " + str(numberServers))
    print("Switches = " + str(numberSwitches))
    print("Laptops = " + str(numberLaptops))
    # Menu selection for the user to return to main or exit
    userContinue = input(str("\nWould you like to return to the menu? y/n\n"))
    if userContinue == 'y' or userContinue == 'Y':
        main()
    else:
        exit()

def gadgetCosting():
    # Define the costs for each hardware device
    routerCost = 3500
    serverCost = 6750
    switchCost = 2200
    laptopCost = 1680
    # Multiply each cost by the number of units required to get a subtotal per device type, and add each subtotal to get a grand total
    totalHardwareCost = (routerCost*numberRouters)+(serverCost*numberSwitches)+(switchCost*numberSwitches)+(laptopCost*numberLaptops)
    print("\nThe total cost for all required IT hardware for the company is $" + str(totalHardwareCost))
    # Menu selection for the user to return to main or exit
    userContinue = input(str("\nWould you like to return to the menu? y/n\n"))
    if userContinue == 'y' or userContinue == 'Y':
        main()
    else:
        exit()

main()