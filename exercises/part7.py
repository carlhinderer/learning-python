# 'Learning Python', by Mark Lutz
# Part 7 Exercises


# Exercise 1
# try/except
#
# Write a function called oops that explicitly raises an IndexError exception when called. Then 
#   write another function that calls oops inside a try/except statement  to  catch  the  error.  
#   What  happens  if  you  change oops to raise a KeyError instead of an IndexError? Where do 
#   the names KeyError and IndexError come from? (Hint: recall that all unqualified names generally 
#   come from one of four scopes.)

def oops1():
    raise IndexError

def oops2():
    raise KeyError

def exercise1a():
    try:
        oops1()
    except IndexError:
        print('caught IndexError')

def exercise1b():
    try:
        oops2()
    except KeyError:
        print('caught KeyError')




# Exercise 2
# Exception objects and lists
#
# Change the oops function you just wrote to raise an exception you define yourself, called 
#   MyError. Identify your exception with a class (unless you’re using Python 2.5 or earlier, you 
#   must). Then, extend the try statement in the catcher function to catch this exception and its 
#   instance in addition to IndexError, and print the instance you catch.

class MyError(Exception): pass

def oops3(): 
    raise MyError

def exercise2():
    try:
        oops3()
    except IndexError:
        print('caught IndexError')
    except MyError:
        print('caught MyError')




# Exercise 3
# Error handling
#
# Write a function called safe(func, *pargs, **kargs) that runs any function with any number of 
#   positional and/or keyword arguments by using the * arbitrary arguments header and call syntax, 
#   catches any exception raised while the function runs, and prints the exception using the 
#   exc_info call in the sys module. Then use your safe function to run your oops function from 
#   exercise 1 or 2. Put safe in a module file called exctools.py, and pass it the oops
#   function interactively. What kind of error messages do you get? Finally, expand 
#   safe to also print a Python stack trace when an error occurs by calling the built-in print_exc
#   function in the standard traceback module; see earlier in this chapter, and consult the
#   Python library reference manual for usage details. We could probably code safe as a function 
#   decorator using Chapter 32 techniques, but we’ll have to move on to the next part of the book to 
#   learn fully how (see the solutions for a preview).

import sys, traceback

def safe(func, *pargs, **kargs):
    try:
        func(*pargs, **kargs)
    except:
        traceback.print_exc()
        print('Class:', sys.exc_info()[0])
        print('Instance:', sys.exc_info()[1])

def exercise3():
    safe(oops3)