# collatz_elif.py
# This program takes a positive integer, if its even it divides it by two. If its odd it multiplies it by three and adds one. It continues to do this until the output is 1. 
# Author: Matthew Arthur 

number = int(input("please enter a positive integer: "))

if (number % 2) == 0: 
    print(number / 2)

elif (number % 2) != 0:
    print((number * 3) + 1)

else: 
    number = 1
    print("1")