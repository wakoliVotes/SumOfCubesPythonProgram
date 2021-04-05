#This program takes a positive integer n, and returns the sum of all the squared values
# A square is a number multiplied by itself, hence, twice
def sumOfCubes(number):
    sum = 0
    for m in range (1, int(number) + 1):
        sum += m*m      
    return sum

# This phase calls upon allowing user input from the keyboard
# The input function is applied

number = input("Kindly enter an Integer :: ")
print("You Entered: ", number)
print("The sum of Cubes for " + number + " in this case is::  ", sumOfCubes(number))