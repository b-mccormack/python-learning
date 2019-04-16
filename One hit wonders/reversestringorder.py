#Reverse the words in a sentence

userSentence = input("Please enter a sentence you want to see written in backwards word order: ")
splitString = userSentence.split()
stringList = list(splitString)
reverseStringList = stringList[::-1]
print(" ".join(reverseStringList))