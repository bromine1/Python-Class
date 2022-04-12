#Python Programming II
#Monday, March 7th, 2022
#Warm-up: Learning It Coding Exercise
#Ryan Stauffer
import sys
if __name__ == "__Main__":
    print("Nope")
    sys.exit()
#Instructions:
#Step1: Create a module named Learning It with
#the ability to bring the following program into the main.py file. Change the variable names max_length and str1. Create a greeting with brief directions for user. Also change the number values for max_length and range(10).
def numerals():
    import random
    import string
    print("Generate a random alphabetical character:")
    print(random.choice(string.ascii_letters))
    print("\nGenerate a random alphabetical string:")
    MaxStringLength = 500
    randomString = ""
    for i in range(random.randint(1, MaxStringLength)):
        randomString += random.choice(string.ascii_letters)
    print(randomString)
    print("\nGenerate a random alphabetical string of a fixed length:")
    randomString = ""
    for i in range(20):
        randomString += random.choice(string.ascii_letters)
    print(randomString)


#Step2: Answer the following questions.
#1. You want to prevent your module's user from running your code as an ordinary script. How will you achieve such an effect?

#

#2. If we call a function without an argument, it uses the default value. How can you use a default parameter value? Share your example.
# a default parameter can be made with an equals, such as def num(num=1):