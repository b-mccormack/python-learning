#Remove duplicate entries from a list, then sort in ascending order

listA = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 4, 3, 1, 5, 8, 99, 12, 45]
listB = []

for num in listA:
	if listB.count(num) < 1:
		listB.append(num)

listB.sort()

print(listB)