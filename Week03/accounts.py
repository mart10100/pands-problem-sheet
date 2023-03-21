# accounts.py
# This program reads an input 10-difit account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# Author: Matthew Arthur 

# First thoughts on how to approach the problem: 
# ask for input of bank account number, make sure its a string
# slice out the last 4 digits and add t the end of 6 x's ? Principles to do this taken from w3 schools - https://www.w3schools.com/python/python_strings_slicing.asp

bank_num = input(str("Please enter a 10 digit account number: ")) # acount number is now stored

# Create 6 x's merged with sliced bank account number: 

print(f'XXXXXX{bank_num[6:]}')

# The additional task of "Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)"

# (The easiest and most straightforward way  to do it would be to just print something like " the last 4 digits of the account number are: XXXX", done by printing as above , just without the 6 X's. Let's try something a bit more convuluted for the fun of it!)

# To me, this sounds like only the last 4 digits are to be shown regadless of input string length. This leaves the question, "how many X's are to be included?" 
# To give the same number of X's minus 4 (for the shown digits) could try to get the bank a/c number length as and work this into the 

# Given this assumption, the best opion I think would be to use the following: 

long_bank_num = input(str("Please enter an account number of any length"))

long_bank_num_length = len(long_bank_num) # 

num_of_xs = long_bank_num_length - 4



#print(f'')