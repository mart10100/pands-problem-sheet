# squareroot.py
#### This program takes a positive floating point number as an inoput and outputs an approximation of its square root. 
#### Author: Matthew Arthur

**First thoughts:** 
 - This will need some research into the [Newton method](https://www.youtube.com/watch?v=WuaI5G04Rcw&ab_channel=AndrewLiang) (as suggested) as it's been a while!
  - Looking at this the program will need to run a while loop as the limit approaches zero, where the updated value is reused and updated until the input value and its square root are approximately equal - I have an allowed difference of 0.000001 for this program. 
 - Once this is done, the approximate end value of the for loop in the sqrt function can be used to take in an input number, is passed through the function and read out in a clear and concise manner. 
  - I have put all the code together in one chunk and then broken it down line by line to explain better what is going on for each part. 

 **The whole code in bulk:**

```python
def squareroot(number):  
    x = float(number) 

    root = x / 2

    approximation = 0.000001 

    while abs(root**2 - x) > approximation: 
        root = (root + (x / root)) / 2 
    return root


number = float(input("Please enter a positive number: "))

while number < 0: 
    number = float(input("That is a negative number, please input a positive number: "))

answer = squareroot(number)

print (f'The square root of {number} is {answer}.')
```

**Broken down:**

Task does not specify integer only, so need to use a float:
```python
def sqrt(number):  
    x = float(number) 
```

`root = x / 2`:
Nearly all numbers have roots that are less than half (except 2 and 3) of their value. This is not required, but it should cut down on the number of iterations the while loop will have to go through before getting the approximate root, speeding up the code. 

Using absolute zero was causing issues for some numbers. I took the hint from the task outline (aand online readings) to approximate to some small near-zero value. 0.000001 seemed small enough!
`approximation = 0.000001`

The while loop is what gets the approximated value from the input value. It uses the fact that some unkown value ("root") when squared is equal to x, the input value. 

(root ** 2) = x
(root ** 2) - x = x - x
(root ** 2) - x = 0

This is mainpulated as above and used in the while loop. The root cannot be equal to zero (the exact root) as this can lead to infinite iterations, so instead the approximate zero is used. The absolute value is used so that the program functions correctly in the case of a number below 3 being used. For 1/2/3, the first iteration of `root**2 - x` results in negative numbers, which are smaller than `approximation`. Without the absolute value this ends the while loop and outputs incorrect numbers. 
`while abs(root**2 - x) > approximation:`

The line below updates the value of `root` for the next iteration of the loop. Uses the Newton method. (No subscript )

root^2^ = x 
f(root) = (root^2^) - x = 0
f'(root) = 2*root = 0
[Newton's method:](https://en.wikipedia.org/wiki/Newton%27s_method) 
x~1~ = (x~0~ - (f(x~0~)/f'(x~0~))) (where x~1~ is the second iteration of the while loop)
Applying this to our case: 

root = root - (f(root) / f'(root)())
    simplifies to
root = (root + (x / root)) / 2
which, with each iteration, brings the approximate root closer and closer to the actual root. Return root is self explanatory, it takes the newly calculated root value and inputs it to the start of the while loop. 
  
    root = (root + (x / root)) / 2

        return root


The next part of the program works by taking an input to be used as the inital `number` to calculate the square root from. 

    number = float(input("Please enter a positive number: "))

The program also includes another while loop that repeatedly asks for a positive number until this is input, as shown in previous weeks. 

    while number < 0: 
        number = float(input("That is a negative number, please input a positive number: "))

Here the defined function squareroot() with input `number` is named answer, for more correct formatting in the final printout. 
    
    answer = squareroot(number)

    print (f'The square root of {number} is {answer}.')



**Limitations of this program:**
- This program by nature is not accurate, only an approximation of the square root value. The using sqrt() would be a lot more straightforward and accurate. 
- The program does not output the exact same as detailed in the task description, but with multiple decimals. This could be easily altered using the round function. 