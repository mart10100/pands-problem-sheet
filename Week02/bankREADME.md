# Bank README.md file
### This program takes two money amounts, adds them together and shows the result with a euro sign and decimal point between the euro and cent amounts. 
#### Author: Matthew Arthur

Get program to ask for money amounts in cents (as shown in the weekly task description on vle):

```python
amount1 = int(input("Enter amount1 (in cent): "))
amount2 = int(input("Enter amount2 (in cent): "))`

#This is inputting the amounts as strings. They cannot be added as strings so they need to be converted to integers: 

`sum = (amount1 + amount2)
```

Convert to integers and add amounts ([W3 schools was used for this](https://www.w3schools.com/python/python_howto_add_two_numbers.asp))

Now that they are added together, need to convert to euro and cent amounts and output with currency symbol etc:
- First converting sum to a float so that it can be divided by 100 with accuracy: (Used [this data camp link](https://www.datacamp.com/tutorial/python-data-type-conversion) to see how to convert int to float).

- I am aware of the warning against using floats due to inaccurate calculations (i.e 0.2999996) but I think so long as the cent values are integers this shouldn't be a problem (hoopefully my bit of testing on the code was robust enough!). 

```python
float(sum)

# Now using print with the f'{}' function to divide the cent value by 100, to get the euro value:

`print(f'The sum of these amounts is €{"%.2f" % (sum/100)}')
```

The '"%.2f" %' means to [format the floating point to a given number of decimals](https://www.freecodecamp.org/news/2f-in-python-what-does-it-mean/#:~:text=So%20%25.2f%20means%20to%20round%20up%20to%20two%20decimal%20places.), in this case it is to 2. 
