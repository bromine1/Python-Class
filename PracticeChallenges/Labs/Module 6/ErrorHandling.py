#Ryan Stauffer
#3-28-2022
#Python Programming II Classwork/Reading
#CW 2.6.1.1. to 2.6.1.12-Errors: the programmer’s daily bread #Provide a programming example for each section. Be certain you have added the programming comments with your new found learning knowledge or prior knowledge. In addition, answer the following two reflection questions. 

#Example #1: Errors, failures, and other plagues

"""
Sometimes we get errors in our code
functions cannot except certian values, or values may be of the wrong type
"""

#Example #2: Demonstrating ZeroDivisionError
from textwrap import indent


value = 1
value /= 0

# Returns a zero division error
# Prior Knwoledge

#Example #3: Demonstrating IndexError

list = [1, 2, 3]
try:
    list[3]
except IndexError:
    ("Start with 0 numskull")

#Prior knwoeldge

#Example #4: How do you handle exceptions?
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if second_number != 0:
    print(first_number / second_number)
else:
    print("This operation cannot be done.")

print("THE END.")
#Prior knowledge

#Example #5: Exceptions: continued 2.6.1.7
try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong...")

print("3")

#Prior knowledge

#Example #6: Exceptions: continued 2.6.1.8
try:
    x = int(input("Enter a number: "))
    y = 1 / x
except:
    print("Oh dear, something went wrong...")

print("THE END.")

#Prior knowledge

#Example #7: Exceptions: continued 2.6.1.9
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")

#Prior knowledge

#Example #8: Exceptions: continued 2.6.1.10
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")

#Prior knowledge

#Example #9: Exceptions: continued 2.6.1.11
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")

print("THE END.")

#prior knowledge

#Recap and Review Questions:  
#Instructions: answer with complete sentences and support your response with learning evidence.

#1. What was the most important thing you learned from the lesson reading and coding examples? 

#For some reason I thought the exception exited the function.

#2. Why is it important? Give specific examples

#Because people put in stuff in odd and weird formatting all the time.
#You could write something accept a wide variety of inputs
#or you could force an input format, and just check for errors