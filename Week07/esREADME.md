# es.py readme file
#### This program reads an input file stored in the same folder as it and counts the number of strings in the file

The program without any comments: 

```python
import sys 
command_line_file = (sys.argv[1]) 

file = open(command_line_file, "r")

data = file.read(-1)
occurrences = data.count("e")

print(occurrences)

file.close()
```

The program with comments: 
```python
# https://www.informit.com/articles/article.aspx?p=2979063&seqNum=11#:~:text=To%20access%20command%2Dline%20arguments,first%20import%20the%20sys%20package.&text=You%20can%20then%20refer%20to,to%20a%20list%20named%20argv.&text=In%20either%20case%2C%20argv%20refers,arguments%2C%20all%20stored%20as%20strings.
import sys 
command_line_file = (sys.argv[1]) 

#https://www.youtube.com/shorts/V3Gahhyc3MQ - this link helped make the above section make sense to me. At first I was not understanding how the file was actually read in to be evaluated for the total number of e's, but the clip made it click for me. 
# https://www.knowledgehut.com/blog/programming/sys-argv-python-examples - Better explains the sys.argv. 
# sys.argv[1] takes the second argument from the list in the command line

# From links: https://pythonexamples.org/python-count-occurrences-of-word-in-text-file 
file = open(command_line_file, "r") # This opens the file in read-only mode - we don't need to write to a new file or append for this task 

data = file.read(-1) # read content of "file" to a string named "data". -1 is the default and indicates that the whole file is to be read (it is the defaults so does not need to be done, but have included it anyway to show how it can be used)


occurrences = data.count("e") # get number of occurrences of the substring in the string

print(f'Number of occurrences of e: {occurrences}')

file.close() # Closing file as it is good practice to do so - https://www.w3schools.com/python/python_file_open.asp
```

The first part of this task is new to this week. Usually, only the python script name goes in the command line, so understanding this was harder than it should have been. 
The first part of this was figuring out how to allow the file 'lotsofes.txt' to be read in from the command line. The bolded 'argument' from the task description was a good indication of what to look for. 
The short [YouTube clip](https://www.youtube.com/shorts/V3Gahhyc3MQ) demonstrated the use of `import sys` and `command_line_file = (sys.argv[1])` to open the correct file through the command line. Importing the sys module allows for the use of [information about the python system to be used in programs](https://realpython.com/python-modules-packages/). 
`sys.argv[]` works by [creating a list of the arguments in the command line](https://realpython.com/lessons/sysargv-in-depth/). 

`import sys` is done first to allow the use of the application within the program - allowing the use of `sys.argv[]` on the next line. 

The line `command_line_file = (sys.argv[1])` takes the second item (0 = 1st item, 1 = 2nd item) in the command line and names it as a variable `command_line_file` - in this case the command line should look like: 
"python es.py 'file_containing_es.txt'" (or in this case, 'lotsofes.txt'). Any text file could be used here, so long as its in the Week07 folder.  

The program then works by [opening the file](https://www.w3schools.com/python/python_file_handling.asp) "lotsofes.txt" from the folder "Week07" in read mode as shown - `file = open("lotsofes.txt", "r")`. As the program only counts the number of e's and does not make any changes to the contents of the file, it does not need to be opened in any other way (eg. w for write, a for append, w for writing or creating a file, etc.). 

The program then reads the file to a string using `data = file.read(-1)`. This sets up the program to allow it to count the number of occurrences of 'e' within 'file' in the next line. The new string with this data is called 'data'.  [The use of -1 in the brackets](https://www.w3schools.com/python/ref_file_read.asp) indicates that the entirety of the file is to be read (this is the default but it has been included to show its capability). This can be used to read only a certain number of bytes beginning from the start of the file, to x number of bytes into the file. 

Now that all of the bytes from the text file 'lotsofes.txt' has been read to a string named 'data' the count function can be used to determine the total number of a charater in the file, in this case it will count the number of e's. `occurrences = data.count("e")` - This names the integer value number of e's (as counted in the newly created string 'data') as `occurrences`, so that it can be printed as the output in the next line. 

With the number of e's now stored in the variable `occurrences`, the program can now use this in the printed output. This is formatted as seen in previous lectures -  `print(f'Number of occurrences of e in : {occurrences}')`