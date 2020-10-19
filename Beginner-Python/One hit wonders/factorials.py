

def main():
    userNumber = int(input("\nPlease enter an integer that you would like to know the factorial of: "))
    
    factorialCount = 1
    for i in range(1, (userNumber+1)):
        factorialCount*=i
    print("\n" + str(userNumber) + "! is: " + str(factorialCount))

    goAgain = input("\nWould you like to choose another number? Y/N: ")
    if goAgain.upper() == "Y":
        main()
    else:
        exit()

main()