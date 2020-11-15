import csv

inputCsv = 'C:/Git/python-projects/CIT/session14/session-14-files/task2-inputdata.csv'
outputPath = 'C:/Git/python-projects/CIT/session14/session-14-files/task2-outputdata.csv'
newHeader = ['Student Name','Total Marks']

def transformData(inputCsv,newHeader):
    outputDict = []
    with open(inputCsv) as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=',')
        lineCount = 0
        for row in csvReader:
            totalMarks = int(row['Marks in Maths']) + int(row['Marks in Science']) + int(row['Marks in English'])
            outputDict.append({newHeader[0]:row['Student Name'], newHeader[1]:totalMarks})
            lineCount += 1
    return(outputDict)

def writeCsv(data,newHeader,outputPath):
    with open(outputPath,'w+') as csvFile:
        csvWriter = csv.DictWriter(csvFile,fieldnames=newHeader)
        csvWriter.writeheader()
        csvWriter.writerows(data)

newData = transformData(inputCsv,newHeader)
writeCsv(newData,newHeader,outputPath)

