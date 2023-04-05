# accounts.py
### This program reads an input 10-digit account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
### Author: Matthew Arthur 

#### First thoughts on how to approach the problem: 
- Ask for input of bank account number, make sure its a string
- Slice out the last 4 digits and add to the end of 6 x's. Principles to do this taken from [w3 schools](https://www.w3schools.com/python/python_strings_slicing.asp)

`bank_num = input(str("Please enter a 10 digit account number: "))`

 acount number is now stored in bank_num variable. 

#### Create 6 x's merged with sliced bank account number: 

`print(f'XXXXXX{bank_num[6:]}')`

A limitation of the above program is that it does not recognise how long the bank account number is. 
For this reason, something like the program I wrote below might be more suitable as it keeps all but the last four digits hidden with x's (that is if the bank account number is longer than 4 digits). 





### The additional task of "Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)"

- To me, this sounds like only the last 4 digits are to be shown regadless of input string length. This leaves the question, "how many X's are to be included?" 
- To give the same number of X's minus 4 (for the shown digits) could try to get the bank a/c number length as and work this into the formula when printing the bank account number with x's and just the last 4 digts showing. See below: 

Given this assumption, the best opion I think would be to use the following: 

```long_bank_num = input(str("Please enter an account number of any length: "))

long_bank_num_length = len(long_bank_num)  

num_of_xs = int(long_bank_num_length - 4)

hidden_numbers = (num_of_xs * "x")

merged_number = (hidden_numbers + (long_bank_num[-4:])) 

#print(merged_number)
```
- The idea here was to get the number of digits in the bank account number, as this was needed to determine how many X's were needed to be shown (As the code states - number of X's is the total number of digits minus the 4 visible digits). 
- the variable `hidden_numbers` was created so that it can be merged with the visible numbers. It creates the required amount of x's needed. 

- Used the info from [w3 Schools](https://www.w3schools.com/python/python_strings_slicing.asp) to slice the `long_bank_num` string from the end rather than the beginning. 

Another way it could have been formatted is as following: 

`print(f'{hidden_numbers}{long_bank_num[-4:]}')`

- I went with creating the merged_number variable as if the code was ever to be extended or modified it may be useful to have the partially hidden account number available to use. 
- A limitation of the above is when an account number is 4 digits or shorter. For `long_bank_num[-4:]`, this means that the all last 4 digits of the string are visible, as they are all included in `[-4:]`. As far as I am aware banks need account numbers longer than 4 digits, so in this case, it should not be a problem. 
- Now knowing about while loops, another useful addition would be to add a message to retry if the wrong number of digits were input. 