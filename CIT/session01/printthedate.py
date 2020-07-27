
print("This program will output the date in the format dd/mm/yyyy")

day = int(input("Please enter the day of the month:\n"))
if len(str(day)) < 2:
    day = "0" + str(day)
elif day > 31:
    print("Error: there can not be a day of the month higher than 31")
    exit()
elif len(str(day)) > 2:
    print("Error: you have entered too many digits")
    exit()

month = int(input("Please enter the month (a1s a number from 1 to 12):\n"))
if (len(str(month)) < 2):
    month = "0" + str(month)
elif month > 12:
    print("Error: there can not be a month higher than 12")
    exit()
elif (len(str(month)) > 2):
    print("Error: you have entered too many digits")
    exit()

year = (input("Please enter the year (as a four digit number):\n"))
if (len(str(year)) < 4):
    print("Error: you have not entered enough digits")
    exit()
elif (len(str(year)) > 4):
    print("Error: you have entered too many digits")

print(str(day) + "/" + str(month) + "/" + str(year))

