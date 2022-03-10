#Nature of Strings Classwork
#Ryan Stauffer
#Example #1
multiline = '''Line #1
Line #2'''

print(len(multiline))
#len of 15 because of newline character , \n


#Example #2
str1 = 'a'
str2 = 'b'
str3 = 'c'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)
print ('c'* 8)
#shortcut variants of the above operators are also applicable for strings (+= and *=).

#Already Known - +=, *=

#Example #3 Lesson 2.2.1.4
# Demonstrating the ord() function.

char_1 = 'c'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

#Example 4 

#Converts to unicode number

# Demonstrating the chr() function.

print(chr(97))
print(chr(945))

# Converts from unicode

#Example #5
# Indexing strings.

the_string = 'silly walks now'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

#Prints each item in the string

#Example #6
# Slices

#Prior Knowledge
alpha = "abcdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

#Example #7

# Boolean statement on weather something is in a string
# case sensative
#order sensative
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

#Example #8
#alphabet = "abcdefghijklmnopqrstuvwxyz"


alphabet.append("a") #illegal
alphabet.insert(3, 1) #illegal
del(alphabet[3]) #illegal
del(alphabet) # success
alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"
#prior knowledge, can be added lke tuples
print(alphabet)

#another example using
spring_break = "noschool"

spring_break = "fun" + spring_break
spring_break = spring_break + "amazing"

print(spring_break)


#Example #9

#Min gets the lowest value
#Value is based on the ascii/unicode table

# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))

# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2] #used the square brackets to prevent the space from being overlooked on your screen.
print(min(t))

#Example #10

# Returns the largest value in the string on the Ascii table
#uppercase, then lowercase


# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))

# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

#Example #11

#prior knowledge

# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))#index is not a function
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

#Example #12

#Returns a string as a list type
#I Think it works with any iterable?
# Allows us to work with it as a string
#.join() would be the reversal of this
#probably a different method to do this as well

# Demonstrating the list() function:
print(list("abcabcefgefg"))

# Demonstrating the count() method:
print("abcabcefgefg".count("b"))
print('abcabcefgefg'.count("g"))
print('abcabcefgefg'.count("a"))