
text1 = 'C:/Git/python-projects/CIT/session14/session-14-files/text1.txt'
text2 = 'C:/Git/python-projects/CIT/session14/session-14-files/text2.txt'

firstFile = open(text1,'r')
secondFile = open(text2,'r')
firstFileContent = firstFile.read()
secondFileContent = secondFile.read()
firstFileList = firstFileContent.split("\n")
secondFileList = secondFileContent.split("\n")

combinedList = []

for i in firstFileList:
	if i in secondFileList:
		combinedList.append(i)

print(combinedList)