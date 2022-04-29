class Fib:
    def __init__(self, nn):
        print("__init__") #Label for when object starts
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):#decorator __iter__ outlines the interface between the function and __next__
        print("__iter__") #Label for when the iterator starts: function here runs and handles iterator
        return self #This line is kind of magic but self is just the iterator

    def __next__(self): #Decorator __next__ outlines the iteration
        print("__next__") #Runs every iteration			
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration #Error to stop iterating
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


class Class: #Generator functions can be referenced in classes
    def __init__(self, n):
        self.__iter = Fib(n) #reference the class as a function, store it

    def __iter__(self):#__iter__ is still needed to handle the constructed generator function
        print("Class iter")
        return self.__iter; #reference the stored object


object = Class(8)

for i in object:
    print(i)

#yield
#yield makes a function a generator object
#it is no longer a function and *cannot* be referenced explicitly
#yield saves the state of the function, rather than exiting and restarting it
def fun(n):
    for i in range(n):
        yield i


for v in fun(5):
    print(v)

#Generators can be used in List Comprehension
def powers_of_2(n): #generator statement
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = [x for x in powers_of_2(5)]#  list comprehension
#The content of the list is the value that the generator function returns
print(t)

#the list() function can also convert a generator output to a list
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = list(powers_of_2(3))# Convert statement
print(t)

# the *in* keyword allows you to compare against the contents of a list
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for i in range(20): # for the numbers one through 20
    if i in powers_of_2(4): # If the number is in the contents of powers of 2, up to the 4th power
        print(i) #print the item


#you can make generator objects, but generator functions are much cleaner
def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)


#List Comprehension
#For method of making a list, 3 lines
list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

#Comprehension method, 1 line
#Lets break it down
#list is equal to val with modification for each val in the return of something
list_2 = [10 ** ex for ex in range(6)]

print(list_1)
print(list_2)

#One line conditionals

#expression if statement, else other expression
the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)
#If the remainder of x and 2 is 0, return one. Otherwise return 0
print(the_list)

#Comprehension can be mixed with one line conditionals
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
#for each number in 1-10, if the number divided by 2 is 0, return 1. Otherwise return 0

the_generator=(1 if x % 2 == 0 else 0 for x in range(10))
#Only difference between comprehending a list and making a generator is brackets v parenthases
#Comprehensions make a list and check against it, which means iteration
#generators continuously make values as they are called


#Lambda functions
# lambda parameters: expression
two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y #functions are given names

for a in range(-2, 3):
    print(sqr(a), end=" ") #parameter passed to lambda function is a
    print(pwr(a, two())) #Two parameters passed, the value of a and the value the lambda function 'two' returns

#Why use lambda functions?
#Lambda functions can be anonymous, or they don't need namespace
#If we only use it once, we only need to define it once
def print_function(args, fun): #args is a list, fun is a function
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)
#evaluates the lambda function for each number in the range

#map
#map (function, list/generator/comprehension)
#map returns an interator that applies the function to every output of an item
#map the inputs to a function and return the outputs
list_1 = [x for x in range(5)] #literally just range 5
list_2 = list(map(lambda x: 2 ** x, list_1)) #apply 2^x for every number in range 5, store it in a list
print(list_2) #print the list

for x in map(lambda x: x * x, list_2): #square every number in list 2
    print(x, end=' ')
print()

#filter()
#filter(function that evaluates true, list)
#like map, but only returns the value if a function returns true
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)
#gets 5 random numbers from -1 to 10 and evaluates if they are positive and even. If so, they are returned

#closure
#due to scope, variables cease to exist when a function is done executing
try:
    def outer(par):
        loc = par
    
    var = 1
    outer(var)
    
    print(var)
    print(loc)
except:
    print("Intended eroneous value")

#loc is out of scopre, we can't access it.
#If we create a function inside another function, and return that function,
#it returns a copy of that function
#That function has a copy of all of it's variables at execution
def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun()) #note that fun is executed as a function, it needs those parenthases

#closures need arguments if they have them, same as any other function
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))
