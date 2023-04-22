# plottask.py
# This program displays a histogram of a normal distribution of 1000 values with a mean of 5 and a standard deviation of 2, and a plot of the function h(x) = x**3 in the range [0,10], all on one set of axis. 
# Author: Matthew Arthur

# First thoughts: 
# Need to import numpy for the random values, and matplotlib for showing the plot. 

import matplotlib.pyplot as plt
import numpy as np

# First part of task: histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2. 

stdev_plot = np.random.normal(5,2,1000) # https://www.w3schools.com/python/matplotlib_histograms.asp shows how to generate normal distribution, and the syntax. 

plt.hist(stdev_plot)

# Second part of task: plot of the function h(x) = x**3 in the range [0,10], all on one set of axis. 

x_points = np.array(range(1,11)) # Range of 1 to 11 used to ensure that 10 is included. This was not clear to me whether 10 was to be included in the program, so I made the call to include and state that this is what I intended. 
y_points = x_points**3

plt.plot(x_points, y_points)

plt.title("Task 8 - Plot of Normal distribution \n and function h(x) = x**3")
plt.xlabel("X - axis") # Creating labels for the axes - https://www.w3schools.com/python/matplotlib_labels.asp
plt.ylabel("Y - axis")
plt.legend(["h(x) = x**3","normal dist."]) # https://www.tutorialspoint.com/manually-add-legend-items-python-matplotlib

plt.show()