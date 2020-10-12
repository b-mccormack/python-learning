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
        1 = Enter new staff member details, or edit existing ones\n\
        2 = See staff pay rates\n\
        3 = See a list of required IT hardware\n\
        4 = See the costing for IT hardware\n\
        5 = Exit\n\n\
        Please enter your selection: "
    menuSelection = str(input(menuText))
    if menuSelection == '1':
        staffDetailsMenu()
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

# Function for the sub menu to choose whether to add a new staff member or edit an existing one
def staffDetailsMenu():
    optionText = "\nPlease select from the following options:\n\n\
        1 = Add a new staff member\n\
        2 = Change details of an existing staff member\n\
        3 = Return to main menu\n\n\
        Please enter your selection: "
    userSelection = str(input(optionText))
    if userSelection == '1':
        addStaffMember()
    elif userSelection == '2':
        editStaffMember()
    elif userSelection == '3':
        main()
    else:
        print("You did not enter a valid menu selection. Please enter a number between 1 and 3")
        time.sleep(3)
        staffDetailsMenu()

# Function for adding a new staff member
def addStaffMember():
    newName = str(input("\nPlease enter the full name of the new staff member you wish to add: "))
    newPhoneNumber = str(input("Please enter the phone number of the new staff member: "))
    newRole = str(input("Please enter the job role of the new staff member: "))
    newSalary = str(input("Please enter the salary of the new staff member: "))
    print("The details you have entered are:\nName:",newName,"\nPhone number:",newPhoneNumber,"\nJob role:",newRole,"\nSalary:",newSalary,"\n\n")
    commitData = str(input("Is this information correct? y/n"))
    if commitData == 'y' or commitData == 'Y':
        staffDetails[newName] = [newPhoneNumber,newRole,newSalary]
        returnToMenu = str(input("The staff member's details have been added. Enter 1 to return to the main menu or 2 to exit:\n"))
        if returnToMenu == '1':
            main()
        else:
            exit()
    else:
        startAgain = str(input("Would you like to enter the details again? y/n\n"))
        if startAgain == 'y' or startAgain == 'Y':
            addStaffMember()
        else:
            main()

# Function for editing the data for an existing staff member
def editStaffMember():
    staffName = str(input("Please enter the name of the staff member you wish to edit (case sensitive):\n"))
    if staffName in staffDetails:
        print("\nYou have selected staff member" + str(staffName) + ". Please enter a selection for the data you wish to modify:\n")
        editField = str(input("1: Phone number\n2: Job role\n3: Salary\n4: Return to main menu\n"))
        if editField == '4':
            exit()
        elif editField not in ['1','2','3']:
            print("You did not enter a valid number. Please try again.")
            time.sleep(3)
            editStaffMember()
        newValue = str(input("Please enter the new value for this field: "))
        confirmData = str(input("The new value you have entered is: " + str(newValue) + " - is this correct? y/n: "))
        if confirmData == 'y' or confirmData == 'Y':
            if editField == '1':
                staffDetails[staffName][0] = newValue
            elif editField == '2':
                staffDetails[staffName][1] = newValue
            elif editField == '3':
                staffDetails[staffName][2] = newValue
            print("The staff member's details are now:",staffDetails[staffName])
            time.sleep(3)
            main()
        else:
            editStaffMember()
    else:
        tryAgain = str(input("\nThat staff member could not be found. Enter 1 to try again, or 2 to return to the main menu:\n"))
        if tryAgain == '1':
            editStaffMember()
        else:
            main()

# Function that totals the salaries of all staff members that currently exist in the staffDetails dictionary
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

# Function that outputs the number of hardware devices required based on how many staff members exist
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

# Function that outputs the total cost of the hardware devices required by the company
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