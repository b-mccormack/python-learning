
userInput = str(input("Please enter your home country:\n"))
hashTable = {'Australia' : 'Sydney', 'New Zealand' : 'Auckland', 'Indonesia' : 'Jakarta', 'Japan' : 'Tokyo',\
    'USA' : 'Los Angeles', 'England' : 'London', 'Russia' : 'Moscow', 'China' : 'Shanghai', 'Brazil' : 'Rio de Janeiro'}

print("I bet you were born in: " + hashTable[userInput])