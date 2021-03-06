#Ryan Stauffer
#3-22-22
#Python Programming II Classwork Codealong
#CW 2311-to-23117-String-methods practice


#Example #1
# Demonstrating the capitalize() method:
print("fixed that grammer mistake.".capitalize())

#Capitalize capitalizes the first character in a string

#Example #2
# Demonstrating the center() method:
print('[' + 'alpha'.center(10, "*") + ']')

#Attempts to center a string within a given number of characters. Not wrapped around, but in a given amount. Takes that value as an integer, and the seperators between the ends takes a string, defaults to whitespace

#Example #3
# Demonstrating the endswith() method:
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")
if "epsilOn".endswith("on"):
    print("yes")
else:
    print("no")
#Checks if the given characters end with the exact end of the string


#Example #4
# Demonstrating the find() method:

print("The incredibles".find("incredible"))
#Finds strings in string, crazy, huh
#slower than in
# can take an index position to start at as a second argument
#just use regex lol


#Example #5
# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())



#Example #6
# Example 6.1: Demonstrating the isapha() method:
print("Moooo".isalpha())
print('Mu40'.isalpha())

#checks if a string is just letters

# Example 6.2: Demonstrating the isdigit() method:
print('2018'.isdigit())
print("Year2019".isdigit())

#checks if a string is just numbers

#Example #7
# Example 7.1: Demonstrating the islower() method:
print("Moooo".islower())
print('moooo'.islower())

#checks if a string is just lowercase

# Example 7.2: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("\t".isspace())
#checks if a string is ONLY whitespace
#need to add third example to this one

#Should we be doing jyupiter notebooks here?
#It just seems like a decent way of presenting these

# Example 7.3: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print("SHOUTING".isupper())
#need to add third example to this one


#Example #8
# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))

#Joins a list together using a string as a seperator

#Example #9
# Demonstrating the lower() method:

print("I AM WHISPERING".lower())
#Makes all characters lowercase

#Example #10
# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")
#Removes LEADING whitespace

#can take a string as an argument, takes those inputs as outputs

#Example #11
# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("I Love Wordpress".replace("Wordpress","Typescript"))
print("Apple juice".replace("", "Am I Interrupting"))
#Using the first argument as blank interrupts everywhere
print("I don't think I can".replace("don't ",""))
#Using a blank string replacement deletes the item



#need to add third example to this one
#Replaces a given string with a different string
#I wonder if theres a way to use regex with this

#Example #12
# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))
print("Buffalo Buffalo Buffalo".rfind("buffalo"))
print("Buffalo Buffalo Buffalo".rfind("Buffalo",7))

#need to add last two examples to this one
#like find, but from the back



#Example #13
# Demonstrating the rstrip() method:
print("[" + " upsilon ".rstrip() + "]")
print("Lets GOOOOOOOOOOOOooooooooooo".rstrip("o"))
#Like strip, but starting from -1 and stepping -1
#need to add last example to this one

#Example #14
# Demonstrating the split() method:
print("phi       chi\npsi".split())
print("Monday, Tuesday, Wednesday, Thursday".split())
#Splits a string into a list by using whitespace as seperators

#Example #15
# Demonstrating the startswith() method:
print("omega".startswith("meg"))
print("omega".startswith("om"))
#Like endswith, but at the start

print()

# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")
#Lstrip and Rstrip combined
#Removes leading and trailing whitespace


#Example #16
# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())
#Swaps the cases of the characters. Lowercanse becomes uppercase, uppercase becomes lowercase

print("i KNOW THAT i KNOW NOTHING.".swapcase())

# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())
#Makes every word uppercase

# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())
#makes every character uppercase

