# Author : Blake McCormack
# Date: 31/08/2020
# Version 1.0
#
# This program is designed to be a simple inventory management system for a small accounting firm

import time

staffDetails = {'Jane Doe' : ['0400111222','Accountant','95000'],\
    'John Doe' : ['0400123123','Lawyer','110000'], 'Sam Daniels' : ['0401987567','Accountant','97000'],\
    'Steve McKinley' : ['0402735244','Human Resources','62000'], 'Bruce Fletcher' : ['0423846247','Office Manager','106000'],\
    'Leah Smith' : ['0463855233','Accountant','107500'], 'Karen Bucket' : ['0432574836','Business Owner','154000'],\
    'Jessica Lovatt' : ['0427946139','Accountant','102000'], 'Matthew Hewitt' : ['0427946725','Manager','101000'],\
    'Keiran Potter' : ['0428947363','Accountant','104700']}



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
    print('This is staffPayRates')
    print(staffDetails['Some Person'][2])

def gadgetList():
    print('This is gadgetList')

def gadgetCosting():
    print('This is gadgetCosting')


main()