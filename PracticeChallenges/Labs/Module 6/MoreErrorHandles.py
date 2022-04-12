#Ryan Stauffer
#Period 4
#3-29-2022
#Python Programming II Classwork/Lesson Readings
#CW PE2: 2.7.1.1. to 2.7.1.8-Anatomy of Exceptions Instructions: Provide a programming example for each section. Be certain you have added the programming comments with your new found learning knowledge or prior knowledge. In addition, answer the following two reflection questions. 

#Example #1 Ciso NetAcad 2.7.1.2

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Oooppsss...")

print("THE END.")

#Example #2 Ciso NetAcad 2.7.1.3
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")

#Example #3 Ciso NetAcad 2.7.1.4 
def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

bad_fun(0)

print("THE END.")

#Example #4 Ciso NetAcad 2.7.1.5 (raise)
"""
Returns a division error

Division errors count as Arithmetic Errors
Except arithmetic errors is raised
"""
def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")

#Example #5 Ciso NetAcad 2.7.1.6 (raise)
#Raise raises the error it is a part of
def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise


try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")


#Example #6 Ciso NetAcad 2.7.1.7 (assert)

#Assert returns an error if it is false
#The ultimate code temper tantrum
#THis returns an error if a value isn't greater than 0


import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)

#Recap and Review Questions:  
#Instructions: answer with complete sentences and support your responses with learning evidence.
#1. What was the most important thing you learned from the lesson reading and coding examples? 
"""
Raising can be nested, and the assert statement works for one-line destructive try statements

"""

#2. Why is it important? Give specific reasons and examples.
"""
Sometimes you don't need to handle an error, you just need to return one upon a condition
Assert is really nice for that.

"""