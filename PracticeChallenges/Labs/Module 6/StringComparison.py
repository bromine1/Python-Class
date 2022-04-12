#Ryan Stauffer
#3-25-22
#Python Programming II Classwork Codealong
#CW 2.4.1.1. to 2.4.1.5-Strings in Action
#Provide a programming example in each section. Be certain you have added the programming comments with your new found learning knowledge. 

#Example #1
# Demonstrating comparing strings

"Prior Knowledge" #Example for how I am commenting here 

#Example #2
# Demonstrating comparing strings con't with digits
#Even if a string contains digits only, it's still not a number. It's interpreted as-is, like any other regular string, and its (potential) numerical aspect is not taken into consideration in any way.

"Prior Knowledge"


# Test examples here.
#Comparing strings con't
#Comparing strings against numbers is generally a bad idea.
print ('10' == '010')
print ('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' < '80')

print ('10' == 10)
print ('10' != 10)
print ('10' == 1)
print ('10' != 1)
print ('10' > 10)

"""
Comparing numbers comapres them how strings are comapred regularly
works off of the ascii table/binary
"""
#Example #3
# Demonstrating the sorted() function:
# first_greek = ['omega', 'alpha', 'pi', 'gamma']
# first_greek_2 = sorted(first_greek)

# print(first_greek)
# print(first_greek_2)

# print()

# # Demonstrating the sort() method:
# second_greek = ['omega', 'alpha', 'pi', 'gamma']
# print(second_greek)

# second_greek.sort()
# print(second_greek)

VideoMedia = ["Fullmetal ALchemist Brotherhood", "She-ra", "Ducktales", "SpaceBalls", "Monty Python and the holy grail"]
print(f"The sorted list for my favorite movies: \n{sorted(VideoMedia)}, and the unsorted list: \n {VideoMedia}")
snacks = ["Potato Chips", "Salsa", "Chocolate coverd espresso beans", "Applesauce", "bannanas"]
print (snacks)
snacks.sort()
print(f"I sorted your snacks for you. \n {snacks} \n I hope those werent organised already")

"""
Sorts based on the alphabet
sorted() is a function that returns an output that is a sorted list
.sort() is a method that changes the data in a list object to be sorted
"""
# Its funny how confused I was at the distinction here until I learned
#why things were the way they were.


#Example #4 
# Demonstrating strings vs. numbers
#The reverse transformation (string-number) is possible when and only when the string represents a valid number. If the condition is not met, expect a ValueError exception.
"Prior knowledge"
#Use the int() function if you want to get an integer, and float() if you need a floating-point value.
