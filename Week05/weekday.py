# weekday.py
# This program tells you if it is a weekday or not.
# Author: Matthew Arthur

# First thoughts: Will need to import some sort of calendar. Possibly assign days to the dates. 
# Will need to make two lists or possibly a dictionary to assign what weekdays and weekdend days are. 
# May need an if loop saying something like if mon-fri, then ... , if sat/sun, then 

# import datetime # https://www.w3schools.com/python/python_datetime.asp

#today = datetime.datetime.now() # https://www.w3schools.com/python/trypython.asp?filename=demo_datetime_strftime_a2

#current_day = today.strftime("%A")    # https://www.w3schools.com/python/trypython.asp?filename=demo_datetime_strftime_a2
    # This converts today into a readable form

# Now need to create a directory of days to class as eitherr weekday or weekend

# weekdays = ["Monday", "Tuesday",  "Wednesday", "Thursday", "Friday"] - not sure if need to define before

# day = datetime.datetime.today().weekday()

# print (day)

# day_type = {
 #  "weekdays" : ["Monday", "Tuesday",  "Wednesday", "Thursday", "Friday"],
 #  "weekends" : ["Saturday", "Sunday"]
#}

#if current_day, day_type == "weekdays"
#    print ("Yes, unfortunately today is a weekday.")
#else day_type == "weekends": 
#    print ("It is the weekend, yay!")

# Found online when the above was not working: https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python

import datetime

weekno = datetime.datetime.today().weekday() # Days of the week are in list from Monday (0) to Sunday (6). 

if weekno < 5:
    print ("Yes, unfortunately today is a weekday.")
    # 0 (Monday) to 5 (Exclusive of 5 - Saturday) are weekdays
else:  
    print ("It is the weekend, yay!")




# Seems to be the most straightforward code, despite not using dictionaries


