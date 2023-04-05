# Collatz.py 
### This program takes an input positive integer and outputs successive values calculated based on whether or not it is odd or even. 
### Author: Matthew Arthur. 

#### Task: At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one. 

Initial thoughts: 
For this task I am thinking that either a while or elif loop (or possibly a combination?) will be required to complete the series of outputs. 

**While loop** - please see the file collatz.py for the code, the others are rough work. 
```python
number = int(input("Please enter a positive integer: "))


while (number % 2 != 0 and number > 1): # number is odd and greater than 1
    print(int(number))
    number = ((number * 3) + 1)
    while (number % 2 == 0 and number > 1): # number is even and greater than 1
        print(int(number))
        number = (number / 2)
if (number) == 1 : print(int(number)) # Added to ensure that 1 is uncluded in output numbers, without this line the output stops at 2. The if statement stops an even input number from outputting twice in output set of numbers. 

# I had to repeat this with the two while statements switched around for an even input. 

while (number % 2 == 0 and number > 1): # number is even and greater than 1
        print(int(number))
        number = (number / 2)
        print(int(number)) # This line ensures that 1 is included in the output numbers, without it the output set stops at 2. 
        while (number % 2 != 0 and number > 1): # number is odd and greater than 1
             print(int(number))
             number = ((number * 3) + 1)    
```
Initially in the above code only the first half was included, but this only worked for odd numbers. I thought that the input would continue through to the second while loop but instead, this only prints the input value. To overcome this, i repested the code with the while loops reversed. This now works as desired. 

Despite the code working as requested in the task, there are some issues with it. Firstly, the duplication of the code seems a bit clunky and long winded. At the time of writing the code, this was the only way I knew to do this. Now, after having googled it and covered functions in the following weeks, using a function seems like a more suitable approach. Here is some [code I found while researching](https://www.webucator.com/article/collatz-conjecture-in-python/) which makes more sense for this task:

```python 
def collatz(num): # defines the function as collatz and the argument as num
    while num != 1: # sets out while loop for when num is not 1
        print(num) # print the number
        if num % 2 == 0: # if the number is even: 
            num = int(num / 2) # divide the number by 2
        else:
            num = int(3 * num + 1) # if not, multiply by 3 and add 1. 
    else:
        print(num) # when number is equal to one, just print it. 


def main(): # second funtion that uses collatz function and prints it out after asking for an input
    num = int(input('Input an integer: ')) # retrieves a number input for the argument 
    collatz(num)
main()
```
This combines while, elif, and functions to create a more simplified code. It is easier to read and easier to make changes to (if this were necessary). 
