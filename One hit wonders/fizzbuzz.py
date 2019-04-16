# Write a program that prints the numbers 1 - 100
# For multiples of 3, also print "Fizz"
# For multiples of 5, also print "Buzz"
# For multiples of both 3 and 5, print "FizzBuzz"

def main():
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        else:
            print(str(i))
main()