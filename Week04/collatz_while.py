# collatz_while.py
# This program takes a positive integer, if its even it divides it by two. If its odd it multiplies it by three and adds one. It continues to do this until the output is 1. 
# Author: Matthew Arthur 

# First thoughts: A while loop could work for this. I will first try this. 

number = int(input("Please enter a positive integer: "))


while (number % 2 != 0 and number > 1): # number is odd and greater than 1
    print(int(number))
    number = ((number * 3) + 1)
    while (number % 2 == 0 and number > 1): # number is even and greater than 1
        print(int(number))
        number = (number / 2)
if (number) == 1 : print(int(number)) # Added to stop even input number from outputting twice in output set of numbers.  

# I had to repeat this with the two while statements switched around for an even input. 

while (number % 2 == 0 and number > 1): # number is even and greater than 1
        print(int(number))
        number = (number / 2)
        print(int(number))
        while (number % 2 != 0 and number > 1): # number is odd and greater than 1
             print(int(number))
             number = ((number * 3) + 1)           