# 'Learning Python', by Mark Lutz
# Part 6 Exercises


# Exercise 1
# Inheritance
#
# Write a class called Adder that exports a method add(self, x, y) that prints a 
#   “Not Implemented” message. Then, define two subclasses of Adder that implement the add method:
#     ListAdder
#       With an add method that returns the concatenation of its two list arguments
#     DictAdder
#       With an add method that returns a new dictionary containing the items in both
#       its two dictionary arguments (any definition of dictionary addition will do)
#
# Experiment by making instances of all three of your classes interactively and calling
#   their add methods.  Now, extend your Adder superclass to save an object in the instance 
#   with a constructor (e.g., assign self.data a list or a dictionary), and overload the 
#   + operator with an __add__ method to automatically dispatch to your add methods (e.g., 
#   X + Y triggers X.add(X.data,Y)). Where is the best place to put the constructors and
#   operator overloading methods (i.e., in which classes)? What sorts of objects can
#   you add to your class instances?
#
# In practice, you might find it easier to code your add methods to accept just one real 
#   argument (e.g., add(self,y)), and add that one argument to the instance’s current data (e.g., 
#   self.data + y). Does this make more sense than passing two arguments to add? Would you say 
#   this makes your classes more “object-oriented”?

class Adder:
    def __init__(self, initialval):
        self.val = initialval
    def add(self, x, y):
        raise NotImplementedError('Must be defined in subclass!')
    def __add__(self, other):
        return self.add(self.val, other)
    def __radd__(self, other):
        return self.add(other, self.val)

class ListAdder(Adder):
    def add(self, x, y):
        return x + y

class DictAdder(Adder):
    def add(self, x, y):
        result = {}
        for key in x.keys(): result[key] = x[key]
        for key in y.keys(): result[key] = y[key]
        return result




# Exercise 2
# Operator overloading
# 
# Write a class called MyList that shadows (“wraps”) a Python list: it should overload most list operators 
#   and operations, including +, indexing, iteration, slicing, and list methods such as append and 
#   sort. See the Python reference manual or other documentation for a list of all possible methods to support. 
#   Also, provide a constructor for your class that takes an existing list (or a MyList instance) and copies its 
#   components into an instance attribute. Experiment with your class interactively. Things to explore:
#
#     a. Why is copying the initial value important here?
#     b. Can you use an empty slice (e.g., start[:]) to copy the initial value if it’s a MyList instance?
#     c. Is there a general way to route list method calls to the wrapped list?
#     d . Can you add a  MyList and a regular list? How about a list and a MyList instance?
#     e. What type of object should operations like + and slicing return? What about indexing operations?
#     f. If you are working with a reasonably recent Python release (version 2.2 or later), you may implement 
#          this sort of wrapper class by embedding a real list in a standalone class, or by extending the 
#          built-in list type with a subclass. Which is easier, and why?

class MyList(list):
    def __init__(self, listval):
        self.listval = list(listval)           # Copy value to avoid changing mutable object
    def __getitem__(self, offset):
        return self.listval[offset]
    def __add__(self, other):
        return MyList(self.listval + other)
    def __radd__(self, other):
        return MyList(other + self.listval)
    def __mul__(self, other):
        return MyList(self.listval * other)
    def __len__(self):
        return len(self.listval)
    def __getslice__(self, low, high):
        return MyList(self.listval[low:high])
    def __repr__(self):
        return self.listval.repr()
    def append(self, node):
        self.listval.append(node)




# Exercise 3
# Subclassing
#
# Make a subclass of MyList from exercise 2 called MyListSub, which extends MyList to print a message to 
#   stdout before each call to the + overloaded operation and counts the number of such calls. 
#   MyListSub should inherit basic method behavior from MyList. Adding a sequence to a MyListSub
#   should print a message, increment the counter for + calls, and perform the superclass’s method.
#   Also, introduce a new method that prints the operation counters to stdout, and experiment with your 
#   class interactively. Do your counters count calls per instance, or per class (for all instances of the 
#   class)? How would you program the other option? (Hint: it depends on which object the count members are 
#   assigned to: class members are shared by instances, but self members are per-instance data.)

class MyListSub(MyList):
    def __init__(self, listval):
        self.addcount =  0
        MyList.__init__(self, listval)
    def __add__(self, other):
        self.addcount += 1
        print('Incrementing add counter, new value: %s' % self.addcount)
        MyList.__add__(self, other)




# Exercise 4
# Attribute methods
#
# Write a class called Attrs with methods that intercept every attribute qualification (both fetches and 
#   assignments), and print messages listing their arguments to stdout. Create an Attrs instance, and experiment 
#   with qualifying it interactively. What happens when you try to use the instance in expressions? Try adding, 
#   indexing, and slicing the instance of your class. (Note: a fully generic approach based upon __getattr__
#   will work in 2.X’s classic classes but not in 3.X’s new-style classes—which are optional in 2.X—for reasons 
#   noted in Chapter 28, Chapter 31, and Chapter 32, and summarized in the solution to this exercise.)

# Note: this code only works for 2.X, since all methods will use '__getattr__' and '__setattr__'.
#   In 3.X, we must override each individual method.
class Attrs:
    def __getattr__(self, name):
        print('getattr: %s' % name)
    def __setattr__(self, name, value):
        print('setattr: Name: %s, Value: %s' % (name, value))




# Exercise 5
# Set objects
#
# Experiment with the set class described in “Extending Types by Embedding”. Run commands to do the 
#   following sorts of operations:
#
#     a. Create two sets of integers, and compute their intersection and union by using & and | 
#          operator expressions.
#     b. Create a set from a string, and experiment with indexing your set. Which methods in the class 
#          are called?
#     c. Try iterating through the items in your string set using a for loop. Which methods run this 
#          time?
#     d. Try computing the intersection and union of your string set and a simple Python string. Does 
#          it work?
#     e. Now, extend your set by subclassing to handle arbitrarily many operands using the *args 
#          argument form. (Hint: see the function versions of these algorithms in Chapter 18.) Compute 
#          intersections and unions of multiple operands with your set subclass. How can you intersect 
#          three or more sets, given that & has only two sides?
#     f. How would you go about emulating other list operations in the set class? (Hint: __add__
#          can catch concatenation, and __getattr__ can pass most named list method calls like append
#          to the wrapped list.)

from exercises.setwrapper import Set

def exercise5a():
     set1 = Set(['a', 'b', 'c'])
     set2 = Set(['c', 'd', 'e'])

     # Union and Intersection
     print(set1 & set2)
     print (set1 | set2)

     # From a string
     set3 = Set('spam')
     print('S[0]: %s' % set3[0])
     print('S[-1]: %s' % set3[-1])
     print('S[0:2]: %s' % set3[0:2])

     # Iterate
     for c in set3: print(c)

     # Union and Intersection of strings
     set4 = 'clam'
     print(set3 & set4)
     print(set3 | set4)

class SetWithMultiples(Set):
    def intersect(self, *others):
        res = []
        for item in self.data:
            for set in list(others): 
                if not item in set: break
            else:
                res.append(item)
        return Set(res)

    def union(self, *others):
        res = list(self.data)
        for set in others:
            for item in list(set):
                if not item in res:
                    res.append(item)
        return Set(res)

def exercise5b():
    S1 = {'a', 'b', 'c'}
    S2 = {'c', 'd', 'e'}
    S3 = {'c', 'f', 'g', 'h'}
    setwithmults = SetWithMultiples(S1)
    u = setwithmults.union(S2, S3)
    print('Union', u)
    i = setwithmults.intersect(S2, S3)
    print('Intersection', i)




# Exercise 6
# Class tree links
# 
# In “Namespaces: The Whole Story” in  Chapter 29 and in “Multiple Inheritance:  ‘Mix-in’  Classes”  in 
#   Chapter  31,  we  learned  that  classes  have  a __bases__ attribute that returns a tuple of their 
#   superclass objects (the ones listed in parentheses in the class header). Use __bases__ to extend the 
#   lister.py mix-in classes we wrote in Chapter 31 so that they print the names of the immediate
#   superclasses of the instance’s class. When you’re done, the first line of the string representation 
#   should look like this (your address will almost certainly vary):
#   <Instance of Sub(Super, Lister), address 7841200>

class SuperclassLister:
    def listsupers(self):
        supers = []
        for klass in self.__class__.__bases__: supers.append(klass.__name__)
        print('Supers: ', supers)

class Superclass:
    def supermethod(): pass

class Subclass(Superclass, SuperclassLister):
    def superclasses(self):
        SuperclassLister.listsupers(self)

def exercise6():
    sub = Subclass()                                                                                                                                                
    sub.listsupers()




# Exercise 7
# Composition
#
# Simulate a fast-food ordering scenario by defining four classes:
#   Lunch
#     A container and controller class
#   Customer
#     The actor who buys food
#   Employee
#     The actor from whom a customer orders
#   Food
#     What the customer buys
#
# To get you started, here are the classes and methods you’ll be defining:
#   class Lunch:
#       def __init__(self)               # Make/embed Customer and Employee
#       def order(self, foodName)        # Start a Customer order simulation
#       def result(self)                 # Ask the Customer what Food it has
# 
#   class Customer:
#       def __init__(self)                        # Initialize my food to None
#       def placeOrder(self, foodName, employee)  # Place order with an Employee
#       def printFood(self)                       # Print the name of my food
#
#   class Employee:
#       def takeOrder(self, foodName)    # Return a Food, with requested name
#
#   class Food:
#       def __init__(self, name)         # Store food name

class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()
    def order(self, foodName):
        self.customer.placeOrder(foodName, self.employee)
    def result(self):
        self.customer.printFood()

class Customer:
    def __init__(self):
        self.food = None
    def placeOrder(self, foodName, employee):
        self.food = employee.takeOrder(foodName)
    def printFood(self):
        print(self.food.name)

class Employee:
    def takeOrder(self, foodName):
        return Food(foodName)

class Food:
    def __init__(self, name):
        self.name = name

def exercise7():
    lunch = Lunch()
    lunch.order('hamburger')
    lunch.order('hot dog')
    print(lunch.result())




# Exercise 8
# Zoo  animal  hierarchy
#
# Code a set of six class statements to model this taxonomy with Python inheritance. Then, add a 
#   speak method to each of your classes that prints a unique message, and a reply method in your 
#   top-level Animal superclass that simply calls self.speak to invoke the category-specific message 
#   printer in a subclass below (this will kick off an independent inheritance search from self). 
#   Finally, remove the speak method from your Hacker class so that it picks up the default above it.

class Animal:
    def reply(self):
        self.speak()
    def speak(self):
        print("I'm an animal!")

class Mammal(Animal):
    def speak(self):
        print("I'm a mammal!")

class Cat(Mammal):
    def speak(self):
        print('Meow')

class Dog(Mammal):
    def speak(self):
        print('Woof')

class Primate(Mammal):
    def speak(self):
        print("I'm a primate!")

class Hacker(Primate): pass

def exercise8():
    for animal in [Animal(), Mammal(), Cat(), Dog(), Primate(), Hacker()]:
        animal.reply()




# Exercise 9
# The Dead Parrot Sketch
#
# Code a set of Python classes to implement this structure with composition. Code your Scene
#   object to define an action method, and embed instances of the Customer, Clerk, and Parrot
#   classes (each of which should define a line method that prints a unique message). The 
#   embedded objects may either inherit from a common superclass that defines line and simply 
#   provide message text, or define line themselves.

class Customer:
    def speak(self): print("I'd like to buy a bird.")

class Clerk:
    def speak(self): print("I've got a parrot here you'll love!")

class Parrot:
    def speak(self): print("Squawk!!!")

class Scene:
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def play(self):
        for actor in [self.customer, self.clerk, self.parrot]: actor.speak()

def exercise9():
    scene = Scene()
    scene.play()