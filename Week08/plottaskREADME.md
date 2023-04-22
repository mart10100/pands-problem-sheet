#Task 8 - plottask.py ReadMe 
####This program uses numpy and matplotlib to generate plots of a normal distribution and of the function h(x)=x^3^
####Author: Matthew Arthur

**First thoughts:** 
This task will firslty need the modules numpy and matplotlib.pyplot, to make use of random number generation (needed for the points to be used in the normal distribution) and for displaying the data from both as plots. 

**The script without any comments:**
```python
import matplotlib.pyplot as plt
import numpy as np

stdev_plot = np.random.normal(5,2,1000) 

plt.hist(stdev_plot)

x_points = np.array(range(1,11))  
y_points = x_points**3

plt.plot(x_points, y_points)

plt.title("Task 8 - Plot of Normal distribution \n and function h(x) = x**3")
plt.xlabel("X - axis") 
plt.ylabel("Y - axis")
plt.legend(["h(x) = x**3","normal dist."], loc = 0) 

plt.show()
```


**The script with comments by line:**

Importing the modules, and naming them plt and np respectively, using  'as' (as done in the lecture videos) for ease of reading the program. 
```python
import matplotlib.pyplot as plt 
import numpy as np
```

First part of task: histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2. 

```python
stdev_plot = np.random.normal(5,2,1000) 
```
The information of the plot is stored in the variable 'stdev_plot' to make it easier to call it in the next line. The numpy module (np) randomly picks values as per a normal distribution. [The syntax follows whats shown in the lecture/in the link](https://www.w3schools.com/python/matplotlib_histograms.asp ), with 5, 2, and 1000 being the mean, standard deviation, and dataset size. 
<br>
```python
plt.hist(stdev_plot)
```
This line uses matplotlib.pyplot (saved as plt) to create a histogram from the previously defined variable 'stdev_plot'. This is stored but needs to be shown, which can be done later.   
<br>

Second part of task: plot of the function h(x) = x^3^ in the range [0,10], all on one set of axis. 
```python
x_points = np.array(range(1,11))
``` 
['Array'](https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp) from the numpy (np) module is used to store the numbers from 1 to [Range](https://www.w3schools.com/python/ref_func_range.asp) of 1 to 11 used to ensure that 10 is included. These are assigned to the variable x_points, as inputs to the function 'h(x) = x^3^' and for the x-axis of the plot. This was not clear to me whether 10 was to be included in the program, so I made the call to include and state that this is what I intended. 
<br>
```python
y_points = x_points**3
```
The variable 'y_points' [cubes](https://www.w3schools.com/python/python_operators.asp) the inputs (1-10 inclusive) so that the plot can be built using both of these values. 
<br> 
```python
plt.plot(x_points, y_points)
```
The matplotlib.pyplot module is used here, and the syntax shows the variables 'x_points' and 'y_points' being assigned as x and y values for the the plot, respectively. The default is to use a line, so this will look different to the normal distribution (histogram) The line defaulted to be a different colour to the histogram, making it clear to see. The colour can be changed if required by using `color="red"`` after the x and y data is given. This is also just stored and not shown, as there is still some formatting to be done to the plot to make it look nice. 
<br>
```python
plt.title("Task 8 - Plot of Normal distribution \n and function h(x) = x**3")
plt.xlabel("X - axis") # Creating labels for the axes - https://www.w3schools.com/python/matplotlib_labels.asp
plt.ylabel("Y - axis")
plt.legend(["h(x) = x**3","normal dist."], loc = 0) # https://www.tutorialspoint.com/manually-add-legend-items-python-matplotlib
```
These have been included toether for commenting as they are all quite similar, in that they are formatting the appearance of the plot and not actually representing any data. 
[The title and axis labels](https://www.w3schools.com/python/matplotlib_labels.asp) are called using the matplotlib.pyplot module. No unites were included in the labelling of the axis. A line break was included in the title to keep it condensed. 
[The legend was added](https://www.tutorialspoint.com/manually-add-legend-items-python-matplotlib) in the top right corner, out of the way of plot elements. This is the default location, but as shown, this can be changed using `loc=x` to move it around the plot as needed. 
<br>
```python
plt.show()
```
The final line of the program is what shows the combined plots with the assigned formatting. They are combined as it is not called out after the histogram to show it, so they are overlayed on one plot. The program does not stop closing until the plot window has been closed. 