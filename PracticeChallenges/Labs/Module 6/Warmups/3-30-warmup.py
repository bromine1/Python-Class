#Ryan Stauffer
#4
#3/30/2022
#Python Programming II Warm-up Assignment

#Instructions:
#Step 1: Review the sample pieces of code carefully using the P.R.I.M.M. method. Use the link provided on Canvas to access the programming examples.

#Step 2: Provide the missing code. Then answer, "What is the expected output?".

#Step 3: Run the program to see the correct output. Were you correct?

#Step 4: Make sure you use comments demonstrating your programming knowledge and critical thinking process for each (all) example.

#Coding Exercise #1: 
#1. Assuming we want to ask the user to enter an integer number. If we use an input(), the input will be a string, which we have to cast into an integer. If the input isn't a valid integer, we will generate (raise) a ValueError. This shows  in the following code below:

# n = int(input("Please enter a number: "))

#With the aid of exception handling, we can write robust code for reading an integer from input:

#Will take an unput and exit a loop if no error occurs
while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print("Great, you successfully entered an integer!")


#Coding Exercise #2: 
#2. We want to ask the user to enter a number. What missing pieces of code could you enter?
# A check for a valueerror
#A break statement
while True: 
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
            print("Oops!  That wasn't a valid number.  Please try again...")

#Coding Exercise #2: 
#3. We want to ask the user to enter a number. What missing pieces of code could you enter?
#Better error codes
#Fstring
#try statement and volatile statement swap
#Handling run-time error: division by zero

def this_fails():   
    try:
        x = 1/0
    except ZeroDivisionError as err:#2) as err: 
        print(f'Handling run time error: {err}')

this_fails()