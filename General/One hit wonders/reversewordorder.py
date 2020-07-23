#Have a user enter a word, then return that word backwards

userWord = input('Please enter a word you would like to see spelled backwards')

wordList = list(userWord)

backwardsWordList = wordList[::-1]

backwardsWord = "".join(backwardsWordList)
print("Your word spelled backwards is: " + backwardsWord)

