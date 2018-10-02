# 'Learning Python', by Mark Lutz
# Part 4 Exercises


# Exercise 1
# The basics
#
# At the Python interactive prompt, write a function that prints its single
# argument to the screen and call it interactively, passing a variety of object types:
# string, integer, list, dictionary. Then, try calling it without passing any argument.
# What happens? What happens when you pass two arguments?

def print_argument(arg):
	print(arg)




# Exercise 2
# Arguments
#
# Write a function called adder in a Python module file. The function
# should accept two arguments and return the sum (or concatenation) of the two.
# Then, add code at the bottom of the file to call the adder function with a variety of
# object types (two strings, two lists, two floating points), and run this file as a script
# from the system command line. Do you have to print the call statement results to
# see results on your screen?

def adder(addend1, addend2):
	return addend1 + addend2

def test_adder():
	# Add 2 strings
	str1, str2 = 'abc', 'def'
	print(adder(str1, str2))

	# Add 2 lists
	list1, list2 = ['abc', 123], ['def', 456]
	print(adder(list1, list2))

	# Add 2 floating points
	fp1, fp2 = 1.5, 2.75
	print(adder(fp1, fp2))




# Exercise 3
# varargs
#
# Generalize the adder function you wrote in the last exercise to compute
# the sum of an arbitrary number of arguments, and change the calls to pass more
# or fewer than two arguments. What type is the return value sum? (Hints: a slice
# such as S[:0] returns an empty sequence of the same type as S, and the type built-in 
# function can test types; but see the manually coded min examples in Chapter 18
# for a simpler approach.) What happens if you pass in arguments of different
# types? What about passing in dictionaries?

def varargs_adder(*args):
  sum = args[0] if args else None
  for arg in args: sum += arg
  return sum

def test_varargs_adder():
  # No arguments
  print(varargs_adder())

  # One argument
  str = 'abc'
  print(varargs_adder(str))

  # Two arguments
  int1, int2 = 35, 25
  print(varargs_adder(int1, int2))

  # Arguments of different types
  try:
      print(varargs_adder(str, int1))
  except:
      print('Trying to add different types together threw an error.')

  dict1 = {'a': 1, 'b': 2, 'c': 3}
  dict2 = {'d': 4, 'e': 5}
  try:
      print(varargs_adder(dict1, dict2))
  except:
      print('Trying to add 2 dictionaries threw an eror.')




# Exercise 4
# Keywords
#
# Change the adder function from exercise 2 to accept and sum/concatenate three arguments: 
# def adder(good, bad, ugly).
#
# Now, provide default values for each argument, and experiment with calling the function 
# interactively. Try passing one, two, three, and four arguments. Then, try passing keyword arguments. 
# Does the call adder(ugly=1, good=2) work? Why? Finally, generalize the new adder to accept and 
# sum/concatenate an arbitrary number of keyword arguments. This is similar to what you did in 
# exercise 3, but you’ll need to iterate over a dictionary, not a tuple. (Hint: the dict.keys
# method returns a list you can step through with a for or while, but be sure to wrap it in a 
# list call to index it in 3.X; dict.values may help here too.)

def default_args_adder(good=1, bad=2, ugly=3):
	return good + bad + ugly

def test_default_args_adder():
    # Test passing in all 3
    print(default_args_adder(1, 2, 3))

    # Passing keyword arguments
    print(default_args_adder(ugly=1, good=2))

def keyword_args_adder(**args):
	keys = list(args.keys())
	sum = args[keys[0]]
	for key in keys[1:]: sum += args[key]
	return sum

def test_keyword_args_adder():
	# Test single argument
	sum = keyword_args_adder(a=1)
	print(sum)

	# Test multiple arguments
	sum = keyword_args_adder(a=1, b=2, c=10)
	print(sum)




# Exercise 5
# Dictionary tools
#
# Write a function called copyDict(dict) that copies its dictionary
# argument. It should return a new dictionary containing all the items in its argument. 
# Use the dictionary keys method to iterate (or, in Python 2.2 and later, step
# over a dictionary’s keys without calling keys). Copying sequences is easy (X[:]
# makes a top-level copy); does this work for dictionaries, too? As explained in this
# exercise’s solution, because dictionaries now come with similar tools, this and the
# next exercise are just coding exercises but still serve as representative function
# examples.

def copy_dict(dict):
	copy = {}
	for key in dict.keys(): copy[key] = dict[key]
	return copy

def test_copy_dict():
	# Copy empty dictionary
	d1 = {}
	print(copy_dict(d1))

	# Copy dictionary with single item
	d2 = {'a': 1}
	print(copy_dict(d2))

	# Copy dictionary with multiple items
	d3 = {'a':1, 'b':2, 'c':3}
	print(copy_dict(d3))




# Exercise 6
# Dictionary tools
# 
# Write a function called addDict(dict1, dict2) that computes the
# union of two dictionaries. It should return a new dictionary containing all the items
# in both its arguments (which are assumed to be dictionaries). If the same key appears in 
# both arguments, feel free to pick a value from either. Test your function
# by writing it in a file and running the file as a script. What happens if you pass lists
# instead of dictionaries? How could you generalize your function to handle this case,
# too? (Hint: see the type built-in function used earlier.) Does the order of the arguments 
# passed in matter?

def add_dict(dict1, dict2):
    for key in dict2.keys(): dict1[key] = dict2[key]
    return dict1

def test_add_dict():
	# Add 2 empty dictionaries
    d1, d2 = {}, {}
    print(add_dict(d1, d2))

	# Add empty dictionary to non-empty
    d1 = {}
    d2 = {'a': 1, 'b': 2}
    print(add_dict(d1, d2))

	# Add dictionaries with overlapping keys
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'c':10, 'd': 20}
    print(add_dict(d1, d2))




# Exercise 7
# More argument-matching examples
#
# First, define the following six functions (either
# interactively or in a module file that can be imported):

def f1(a, b): print(a, b)            # Normal args
def f2(a, *b): print(a, b)           # Positional varargs
def f3(a, **b): print(a, b)          # Keyword varargs
def f4(a, *b, **c): print(a, b, c)   # Mixed modes
def f5(a, b=2, c=3): print(a, b, c)  # Defaults
def f6(a, b=2, *c): print(a, b, c)   # Defaults and positional varargs

# Now, test the following calls interactively, and try to explain each result; in some
# cases, you’ll probably need to fall back on the matching algorithm shown in Chapter 18.
# Do you think mixing matching modes is a good idea in general? Can you
# think of cases where it would be useful?
#
# >>> f1(1, 2)
# 1 2
#
# >>> f1(b=2, a=1)
# 1 2
#
# >>> f2(1, 2, 3)
# 1 (2, 3)
#
# >>> f3(1, x=2, y=3)
# 1 {'x':2, 'y': 3}
#
# >>> f4(1, 2, 3, x=2, y=3)
# 1 (2, 3) {'x': 2, 'y': 3}
#
# >>> f5(1)
# 1 2 3
#
# >>> f5(1, 4)
# 1 4 3
#
# >>> f6(1)
# 1 2 ()
#
# >>> f6(1, 3, 4)
# 1 3 (4,)
#




# Exercise 8
# Primes revisited
#
# Recall the following code snippet from Chapter 13, which simplistically determines whether a 
# positive integer is prime:
#
#     x = y // 2                          # For some y > 1
#     while x > 1:
#         if y % x == 0:                  # Remainder
#             print(y, 'has factor', x)
#             break                       # Skip else
#         x -= 1
#     else:                               # Normal exit
#         print(y, 'is prime')
#
# Package this code as a reusable function in a module file (y should be a passed-in
# argument), and add some calls to the function at the bottom of your file. While
# you’re at it, experiment with replacing the first line’s // operator with / to see how
# true division changes the / operator in Python 3.X and breaks this code (refer back
# to Chapter 5 if you need a reminder). What can you do about negatives, and the
# values 0 and 1? How about speeding this up? Your outputs should look somethinglike this:
#
# 13 is prime
# 13.0 is prime
# 15 has factor 5
# 15.0 has factor 5.0

def print_whether_prime(y):
    x = y // 2
    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            break
        x -= 1
    else:
        print(y, 'is prime')


def test_print_whether_prime():
    print_whether_prime(13)
    print_whether_prime(13.0)
    print_whether_prime(15)
    print_whether_prime(15.0)