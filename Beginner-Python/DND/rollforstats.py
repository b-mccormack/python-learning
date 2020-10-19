# Goal: write a program that has the player roll for stats, then assign those stats to their desired skills

import random

def main():
    statValueListRaw = []
    statValueListCut = []
    statValueListFinal = []

    def rawStatsRoll():
        randomList = []
        for i in range(0, 6):
            for h in range(0, 4):
                randomList.append(random.randint(1, 6))
            statValueListRaw.append(randomList)
            randomList = []
        cutStatsRoll()

    def cutStatsRoll():
        for i in statValueListRaw:
            tempList = i
            tempList.sort()
            del tempList[0]
            statValueListCut.append(tempList)
        finalStatsRoll()

    def finalStatsRoll():
        for i in statValueListCut:
            statValueListFinal.append(sum(i))
        printStats()

    def printStats():
        print("\nYour rolled values for stats are: \n1) " + str(statValueListFinal[0]) + "\n2) " + str(statValueListFinal[1]) 
            + "\n3) " + str(statValueListFinal[2]) + "\n4) " + str(statValueListFinal[3]) + "\n5) " + str(statValueListFinal[4]) + "\n6) " + str(statValueListFinal[5]))
        menuOptions()

    def menuOptions():
        userSelection = str(input("\nWould you like to roll again? Y/N: "))
        if userSelection.upper() == 'Y':
            main()
        else:
            exit()

    rawStatsRoll()

main()