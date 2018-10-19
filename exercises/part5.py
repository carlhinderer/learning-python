# 'Learning Python', by Mark Lutz
# Part 5 Exercises


# Exercise 1
# Import Basics
#
# Write a program that counts the lines and characters in a file (similar in spirit to part of what 
#   wc does on Unix). With your text editor, code a Python module called mymod.py
#   that exports three top-level names:
#
# • A countLines(name) function that reads an input file and counts the number of lines in it (hint: 
#     file.readlines does most of the work for you, and len does the rest, though you could count with 
#     for and file iterators to support massive files too).
#
# • A countChars(name) function that reads an input file and counts the number of characters in it 
#     (hint: file.read returns a single string, which may be used in similar ways).
#
# • A test(name) function that calls both counting functions with a given input filename. Such a 
#     filename generally might be passed in, hardcoded, input with the input built-in function, or 
#     pulled from a command line via the sys.argv list shown in this chapter’s formats.py and 
#     reloadall.py examples; for now, you can assume it’s a passed-in function argument.
#
# All three mymod functions should expect a filename string to be passed in. If you type more than 
#   two or three lines per function, you’re working much too hard—use the hints I just gave!
#
# Next, test your module interactively, using import and attribute references to fetch your exports. 
#   Does your PYTHONPATH need to include the directory where you created mymod.py? Try running your 
#   module on itself: for example, test("mymod.py"). Note that test opens the file twice; if you’re 
#   feeling ambitious, you may be able to improve this by passing an open file object into the two 
#   count functions (hint:file.seek(0) is a file rewind).

import mymod
testfile = 'datafile.txt'

def exercise1():
    mymod.test(testfile)




# Exercise 2
# from/from *
#
# Test your mymod module from exercise 1 interactively by using from to load the exports directly, 
#   first by name, then using the from * variant to fetch everything.

from mymod import test

def exercise2a():
    test(testfile)

from mymod import *

def exercise2b():
    test(testfile)




# Exercise 3
# __main__
#
# Add a line in your mymod module that calls the test function automatically only when the module 
#   is run as a script, not when it is imported. The line you add will probably test the value of 
#   __name__ for the string "__main__", as shown in this chapter. Try running your module from the 
#   system command line; then, import the module and test its functions interactively. Does it still 
#   work in both modes?




# Exercise 4
# Nested imports
#
# Write a second module, myclient.py, that imports mymod and tests its functions; then run myclient
#   from the system command line. If myclient uses from to fetch from mymod, will mymod’s functions 
#   be accessible from the top level of myclient? What if it imports with import instead? Try coding 
#   both variations in myclient and test interactively by importing myclient and inspecting its 
#   __dict__ attribute.

import myclient

def exercise4():
    print(myclient.__dict__.keys())
    myclient.testmymod()




# Exercise 5
# Package imports
#
# Import your file from a package. Create a subdirectory called mypkg nested in a directory on your 
#   module import search path, copy or move the mymod.py module file you created in exercise 1 or 3 
#   into the new directory, and try to import it with a package import of the form import mypkg.mymod
#   and call its functions. Try to fetch your counter functions with a from too.
#
# You’ll need to add an __init__.py file in the directory your module was moved to make this go, but it 
#   should work on all major Python platforms (that’s part of the reason Python uses “.” as a path 
#   separator). The package directory you create can be simply a subdirectory of the one you’re working
#   in; if it is, it will be found via the home directory component of the search path, and you won’t 
#   have to configure your path. Add some code to your __init__.py, and see if it runs on each import.

import mypkg.mymod

def exercise5():
    mypkg.mymod.test(testfile)