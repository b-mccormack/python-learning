# Author : Blake McCormack
# Date: 31/08/2020
# Version 1.0
#
# Program to multiply two 2x2 matrices

X = [[5, 6],
    [2,5]]
Y = [[7,10],
    [10,6]]
R = [[0,0],
    [0,0]]

# Define the function multiplyMatrices that will perform the operation
def multiplyMatrices(a,b):
    for i in range(len(a)):      # Iterate through the rows of X matrix
        for j in range(len(b[0])):     # Iterate through the columns of Y matrix
            for k in range(len(b)):     # Iterate through the rows of Y matrix
                R[i][j] += a[i][k] * b[k][j]    # On each pass, the result is added to the result matrix R
    for r in R:
        print(r)

multiplyMatrices(X,Y)