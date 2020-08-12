Year = int(input("What is your birth year?: "))
Birthday = input("Have you had your birthday yet? (yes/no): ")
if Birthday == "yes" or Birthday == "Yes" or Birthday == "Yeah" or Birthday == "yeah" or Birthday == "y" or Birthday == "Y":
    ageYes = 2020 - Year
    print("Happy birthday! You are now " + str(ageYes))
elif Birthday == "no" or Birthday == "No" or Birthday == "nah" or Birthday == "Nah" or Birthday == "n" or Birthday == "N":
    ageNo = 2020 - Year
    print("I hope you have a good birthday! You are currently " + str(ageNo))
else:
    print("Please answer with a yes or no. My code isnt that advance...")