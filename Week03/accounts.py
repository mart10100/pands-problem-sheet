# accounts.py
# This program reads an input 10-difit account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# Author: Matthew Arthur 



bank_num = input(str("Please enter a 10 digit account number: ")) # acount number is now stored

print(f'XXXXXX{bank_num[6:]}') # 6 x's merged with sliced bank account number. Account number shown from 7th number to the end. 


# The additional task of "Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)"

# To me, this sounds like only the last 4 digits are to be shown regadless of input string length. This leaves the question, "how many X's are to be included?" 
# To give the same number of X's minus 4 (for the shown digits) could try to get the bank a/c number length as and work this into theformula when printing the bank account number with x's and just the last 4 digts showing. See below.. 
# Given this assumption, the best opion I think would be to use the following: 

long_bank_num = input(str("Please enter an account number of any length: "))

long_bank_num_length = len(long_bank_num)  

num_of_xs = int(long_bank_num_length - 4)

hidden_numbers = str(num_of_xs * "x")

merged_number = (hidden_numbers + (long_bank_num[-4:])) # Used the info from here to get the sliced string: https://www.w3schools.com/python/python_strings_slicing.asp

print(merged_number)

#print(f'{hidden_numbers}{long_bank_num[-4:]}')

#A limitation of the above is when an account number is 4 digits or shorter.