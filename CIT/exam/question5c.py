# Mark to Grade Conversion Program
# Date:   16/11/2020
# Version 0.1 (Beta)
# Author: Blake McCormack


mark = int(input("Enter the mark: "))

if (mark < 0 or mark > 100):
    print("The mark must be between 0 and 100")
else:
    if (mark >= 90 and mark <= 100):
        grade = "High Distinction"

    elif (mark >= 80 and mark < 90):
        grade = "Distinction"

    elif (mark >= 50 and mark < 80):
        grade = "Credit"

    elif (mark < 50 and mark >= 0):
        grade = "Fail"

    print("The grade is:", grade)
