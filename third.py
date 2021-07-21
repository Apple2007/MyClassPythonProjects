# Functions Example
def firstFunction():
    print("This is the first function")
firstFunction()
# Return Value Examples
def secondFunction(num):
    return num*num
print(secondFunction(4))
# Function that takes in postitive number and returns the nearest even number greater than or equal to n
def nearestEven(n):
    if n%2 == 0:
        return n
    else:
        return n+1
print(nearestEven(2008))