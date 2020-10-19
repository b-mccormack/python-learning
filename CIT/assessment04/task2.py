# Author : Blake McCormack
# Date: 19/10/2020
# Version 1.0
#
# This program acts as a gradebook for students

# Define the dictionaries that contain marks for the students
dictBob = { 'name':'bob', 'assignments':[15,16,14,20], 'presentations':[8,6,7,9], 'lab tasks':[18,15,16,20] }
dictJane = { 'name':'jane', 'assignments':[45,52,50,55], 'presentations':[9,7,8,10], 'lab tasks':[28,25,26,30] }

# Put the student's names into a list and print it
studentList = [dictBob['name'],dictJane['name']]
print("\nThe students currently in the system are: " + str(studentList) + "\n")

# Use dictionary keys to print the values of the students' marks
print("The marks for student " + str(dictBob['name']) + " are:\nAssignments: " + str(dictBob['assignments']) + "\nPresentations: " + \
    str(dictBob['presentations']) + "\nLab tasks: " + str(dictBob['lab tasks']) + "\n")
print("The marks for student " + str(dictJane['name']) + " are:\nAssignments: " + str(dictJane['assignments']) + "\nPresentations: " + \
    str(dictJane['presentations']) + "\nLab tasks: " + str(dictJane['lab tasks']) + "\n")

# Define the get_average function to get the weighted final results for a student
def get_average(dictionary):
    assignmentResult = average(dictionary['assignments']) / 60
    presentationResult = average(dictionary['presentations']) / 10
    labTaskResult = average(dictionary['lab tasks']) / 30
    assignmentWeight = 60
    presentationWeight = 10
    labTaskWeight = 30
    weightedAssignmentResult = assignmentResult * assignmentWeight
    weightedPresentationResult = presentationResult * presentationWeight
    weightedLabTaskResult = labTaskResult * labTaskWeight
    finalResult = weightedAssignmentResult + weightedPresentationResult + weightedLabTaskResult
    return(finalResult)

# Define the function to determine the average of a list of numbers
def average(numbers):
    total = (sum(numbers))
    total = float(total)
    result = total / len(numbers)
    return(result)


get_average(dictJane)