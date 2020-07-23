# Modify the birthdaydictionaries.py file to load the birthday dictionary from a JSON file on the disk. 
# Bonus: Ask the user for another name and birthday and add these details to the JSON file.

import json

def main():
    with open("birthdays.json", "r") as f:
        birthday = json.load(f)

    userNameReq = input("\nPlease enter the name of the person whose birthday you want to look up: \n")

    if userNameReq in birthday:
        print("\n" + str(userNameReq) + "'s birthday is: " + "{}".format(birthday[userNameReq]))
        continueInput = input("\nWould you like to look up another birthday? Y/N: ").upper()
        if continueInput == "Y":
            main()
        else:
            userOption()
        
    else:
        continueInput2 = input("\nThat name does not appear in the dictionary. Would you like to try again? Y/N: ").upper()
        if continueInput2 == "Y":
            main()
        else:
            userOption()

def addData():
    newName = input("\nPlease enter the name of the person to add: ")
    newDate = input("\nPlease enter " + str(newName) + "'s birthday in the format dd-mm-yyyy: ")
    doubleCheck = input("\nYou are adding " + str(newName) + "'s birthday as " + str(newDate) + ". Is this correct? Y/N: ").upper()
    if doubleCheck == "Y":
        newDataEntry = {
            str(newName): str(newDate)
        }
        with open("birthdays.json") as h:
            loadedData = json.load(h)
        loadedData.update(newDataEntry)
        with open("birthdays.json", "w") as g:
            json.dump(loadedData, g)
        print("\n" + str(newName) + "'s birthday has been added to the dictionary")
        userOption()

    else:
        continueCheck = input("\nDo you want to add another birthday to the dictionary? Y/N: ").upper()
        if continueCheck == "Y":
            addData()
        else:
            userOption()

def userOption():
    userSelection = input("\nPlease choose what you would like to do. Enter the number corresponding to your desired option\n1) Look up a birthday\n2) Add a new birthday to the dictionary\n3) Quit the program\n")
    if userSelection == "1":
        main()
    elif userSelection == "2":
        addData()
    elif userSelection == "3":
        exit()
    else:
        print("\nPlease enter a valid option")
        userOption()

userOption()