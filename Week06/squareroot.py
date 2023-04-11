# squareroot.py
# This program takes a positive floating point number as an inoput and outputs an approximation of its square root. 
# Author: Matthew Arthur

def squareroot(number): # Need to create the function to take the inputs, processes, and outputs as square root. 
    x = float(number)

    root = x / 2  # need to guess an initial approximation for the root of the input number. As all numbers (except 2 and 3) have square roots smaller than half

    approximation = 0.000001 # As limit approaches zero -> 0.000001 is close enough to zero for me!

    while abs(root**2 - x) > approximation: # var "root" is the unknown square root. abs used as this allows negative values for (root**2 - x) to be calculatged
        #Therefore, root**2 = number -> for equation f(root) = root**2 - number = 0 (or 0.000001 in the difference in this case with the approximation). 
        root = (root + (x / root)) / 2 # the while loop keeps the 

    return root


number = float(input("Please enter a positive number: "))

while number < 0: 
    number = float(input("That is a negative number, please input a positive number: "))

answer = squareroot(number),2



print (f'The square root of {number} is {answer}.')
