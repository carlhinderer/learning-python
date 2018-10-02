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