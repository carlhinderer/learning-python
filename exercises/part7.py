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