# Keep track of when our friends' birthdays are, and be able to find that information based on their name
# Create a dictionary (in your file) of names and birthdays. When you run your progra it should ask the user to enter a name,
# and return the birthday of that person back to them. 

bday_dictionary = {
    "Blake": "14-11-1991",
    "Jebus": "25-12-0000",
    "Albert": "14-03-1879",
    "Ned": "01-06-1855",
    "Marie": "07-11-1867"
}

def main():

    userNameReq = input("Please enter the name of the person whose birthday you want to look up: \n")

    if userNameReq in bday_dictionary:
        print(str(userNameReq) + "'s birthday is: " + bday_dictionary[userNameReq])
        continueInput = input("Would you like to look up another birthday? Y/N: ").upper()
        if continueInput == "Y":
            main()
        else:
            quit()
        
    else:
        continueInput2 = input("That name does not appear in the dictionary. Would you like to try again? Y/N: ").upper()
        if continueInput2 == "Y":
            main()
        else:
            quit()

main()