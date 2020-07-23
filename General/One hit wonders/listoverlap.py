#take two lists, and write code that returns a list containing only the elements that are common between the two lists

ListA = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ListB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

combinedList = [common for common in ListA if (common in ListB)]

print(str(combinedList))