# bank.py
# This program takes two money amounts, adds them together and shows the result with a euro sign and decimal point between the euro and cent amounts. 
# Author: Matthew Arthur

#Step1: Get program to ask for money amounts in cents (as shown in the weekly task description on vle):

#amount1 = input("Enter amount1 (in cent): ")
#amount2 = input("Enter amount2 (in cent): ")

# This is inputting the amounts as strings. This was shown to be unreliable in the lectures so they need to be converted to floats: 


amount1 = input("Enter amount1 (in cent): ")
amount2 = input("Enter amount2 (in cent): ")

# Convert to integers and add amounts (used W3 for this - https://www.w3schools.com/python/python_howto_add_two_numbers.asp)

sum = int(amount1) + int(amount2) 

# Now that they are added together, need to convert to euro and cent amounts and output with currency symbol etc:
  
# First converting sum to a float so that it can be divided by 100 with accuracy: (Used https://www.datacamp.com/tutorial/python-data-type-conversion to see how to convert int to float)
# I am aware of the warning against using floats due to inaccurate calculations(i.e 0.2999996) but I think so long as the cent values are integers this shouldn't be a problem (hoopefully my bit of testing on the code was robust enough!). 
float(sum)

# Now using print with the f'{}' function (as seen in the videos) to divide the cent value by 100, to get the euro value:
print(f'The sum of these amounts is €{sum/100}')


