# This program gets two numbers from the user and adds all even numbers between them
# e.g. 10 (inclusive) and 18 (exclusive) = 10 + 12 + 14 + 16  (18 is skipped/excluded)

rangeLow  = int(input("What is the lowest number you'd like to add? (inclusive) " ))
rangeHigh  = int(input("What is the highest number you'd like to add? (exclusive) " ))
rangeSum  = 0

while (rangeLow < 0):
    print("My minimum is 0 - please try again.")
    rangeLow = int(input("What is the lowest number you'd like to add? (inclusive) "))

while (rangeHigh >= 1000):
    print ("My maximum is 1000 - please try again.")
    rangeHigh = int(input("What is the highest number you'd like to add? (exclusive) "))

if (rangeLow >= rangeHigh):
    print ("The High number must be larger than Low number. I'll swap these for you.")
    temp = rangeHigh
    rangeHigh = rangeLow
    rangeLow = temp

for i in range(rangeLow, rangeHigh):
# Even numbers have 0 remainder when divided by 2 - add these numbers, throw away the odds.  The % operator gives us the remainder.
    if (i % 2 == 0):
        print("  Adding " + str(i) + " to the sum.")
        rangeSum = rangeSum + i

print("The sum of the even numbers from [" + str(rangeLow) + "] to [" + str(rangeHigh) + "] is: " + str(rangeSum))
