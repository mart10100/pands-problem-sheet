# es.py
# This program reads in  a text file, counts the number of 'e's in the file and outputs the number. 
# Author: Matthew Arthur

# First thoughts: Need to get a text file fromsomewhere - either make it and add to the folder, or get one online or something simnilar. 
# Once file is available, need to read in file ashown in lecture. Will then need to use some function (maybe built in?) 

# W3 schools link to use .count() https://www.w3schools.com/python/ref_list_count.asp

# https://www.informit.com/articles/article.aspx?p=2979063&seqNum=11#:~:text=To%20access%20command%2Dline%20arguments,first%20import%20the%20sys%20package.&text=You%20can%20then%20refer%20to,to%20a%20list%20named%20argv.&text=In%20either%20case%2C%20argv%20refers,arguments%2C%20all%20stored%20as%20strings.
import sys 
command_line_file = (sys.argv[1]) 

#https://www.youtube.com/shorts/V3Gahhyc3MQ - this clip made this section make sense to me. At first I was not understanding how the file was actually read in to be evaluated for the total number of e's, but for some eason this clip made it click in my mind 

# From link: https://pythonexamples.org/python-count-occurrences-of-word-in-text-file
file = open(command_line_file, "r") # This opens the file in read-only mode - we don't need to write to a new file or append for this task 

data = file.read(-1) # read content of "file" to a string named "data". -1 is the default and indicates that the whole file is to be read (it is the defaults so does not need to be done, but have included it anyway to show how it can be used)

occurrences = data.count("e") # get number of occurrences of the substring in the string

print(occurrences)

file.close() # Closing file as it is good practice to do so - https://www.w3schools.com/python/python_file_open.asp
