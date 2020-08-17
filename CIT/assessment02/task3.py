# Author : Blake McCormack
# Date: 17/08/2020
# Version 1.0
#
# This script takes an input for a number of blocks
# It then calculates the height of the 2D pyramid that can be contructed with those blocks

blockInventory = int(input("Please enter the number of blocks you have:\n"))

# Define the initial height of the pyramid as 0
pyramidHeight = 0
# Create a variable to use for both calculating if there are any blocks left over and to use for the loop condition
# without changing the value of blockInventory. This is set to 1 initially because the loop requires a value
# greater than 0, the number is irrelevant as long as it is positive
blockPivot = 1

# This while loop adds 1 to the pyramid height in each pass.
# Then, the number of blocks to build that height of pyramid is calculated according to
# the formula x = n(n+1)/2 and this is subtracted from blockInventory
# This value is assigned to blockPivot, and if it drops below 0 we know we have run out of blocks and the loop exits
while blockPivot > 0:
    pyramidHeight += 1
    blockPivot = blockInventory - ((pyramidHeight*(pyramidHeight+1))/2)

# If blockPivot is equal to 0 we had exactly the correct number of blocks for the pyramid
# If it is less than 0, we ran out of blocks before the last level of the pyramid was complete
# In this case we need to subtract 1 from the pyramid height before outputting it
if blockPivot < 0:
    pyramidHeight -= 1


print("The highest pyramid you can build is", pyramidHeight, "blocks high")