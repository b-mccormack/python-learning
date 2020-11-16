# Mark to Grade Conversion Program
# Date:   16/11/2020
# Version 0.1 (Beta)
# Author: Blake McCormack


mark = int(input("Enter the mark: "))

if (mark >= 90):
    grade = "High Distinction"

elif (mark >= 80 and mark < 90):
    grade = "Distinction"

elif (mark >= 50 and mark < 80):
    grade = "Credit"

elif (mark < 50):
    grade = "Fail"

print("The grade is:", grade)
