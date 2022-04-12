# Ryan Stauffer Warmup 3-10
# Example 1 The len() function used for strings returns a number of characters contained by the arguments. The snippet outputs what?

word = 'new lesson, fun times'
print(len(word))
#Guess: 20
#I forgot to count the comma, its 21

# Example 2 Any string can be empty. What's its length?

empty = ''
print(len(empty))
#GUess: 0
#I was right

# Example 3 Don't forget that a backslash (\) used as an escape character is not included in the string's total length. Therefore, what's its output?

i_am = 'I\'m what I say I\am'
print(len(i_am))
#Guess: I'm what I say Iam

# So Strings are basically iterables? Makes sense