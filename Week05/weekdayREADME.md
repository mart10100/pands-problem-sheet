# weekday.py
#### This program tells you if it is a weekday or not.
#### Author: Matthew Arthur

**First thoughts:** 
 -Will need to import some sort of calendar. Possibly assign days to the dates. 
 -Will need to make two lists or possibly a dictionary to assign what weekdays and weekdend days are. 
 -May need an if loop saying something like if mon-fri, then ... , if sat/sun, then yay

The following code was my first thought process on how to tackle it. As shown this did not work, but have left it in to try and show my thought process (for better or worse!) 

```python
import datetime # https://www.w3schools.com/python/python_datetime.asp

today = datetime.datetime.now() # https://www.w3schools.com/python/trypython.asp?filename=demo_datetime_strftime_a2

current_day = today.strftime("%A")    # https://www.w3schools.com/python/trypython.asp?filename=demo_datetime_strftime_a2
    # This converts today into a readable form
```

Now need to create a directory of days to class as eitherr weekday or weekend

```python
weekdays = ["Monday", "Tuesday",  "Wednesday", "Thursday", "Friday"] - not sure if need to define before

day = datetime.datetime.today().weekday()

print (day)

day_type = {
  "weekdays" : ["Monday", "Tuesday",  "Wednesday", "Thursday", "Friday"],
  "weekends" : ["Saturday", "Sunday"]
}

if current_day, day_type == "weekdays"
    print ("Yes, unfortunately today is a weekday.")
else day_type == "weekends": 
    print ("It is the weekend, yay!")
```
---
After some research the following was found [online](https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python) when the above was not working. It is much more simple than what I was going for and uses a date object to number the days from 0 to 6 starting on Monday. This allows an elif statement to be used, with < 5 returning a weekday and anything larger being the weekend. With the datetime module imported this allows todays date to be used, and to the elif loop uses this to print the correct output. 

```python
import datetime

weekno = datetime.datetime.today().weekday() # Days of the week are in list from Monday (0) to Sunday (6).(https://docs.python.org/3/library/datetime.html#datetime.date.weekday)

if weekno < 5:
    print ("Yes, unfortunately today is a weekday.")
    # 0 (Monday) to 5 (Exclusive of 5 - Saturday) are weekdays
else:  
    print ("It is the weekend, yay!")
```

This seems to be the most straightforward code, despite not using dictionaries (as covered in this week - I think this is what confused megit ). 