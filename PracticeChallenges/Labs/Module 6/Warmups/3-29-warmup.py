#Ryan Stauffer
#Period 4
#3/29/2022
#Python Programming II Warm-up Assignment

#Instructions:
#Step 1: Review the sample pieces of code carefully using the P.R.I.M.M. method. Use this link to access these two examples.

#Step 2: Provide your prediction line by line answering the question below, "What is the expected output?".

#Step 3: Run the program to see the correct output. Were you correct?

#Step 4: Create a new programming solution with comments demonstrating your programming knowledge and critical thinking process.

#Exercise #1: What is the expected output of the following code?
#zero

try:
    print(1/0)
except ZeroDivisionError:
    print("zero")
except ArithmeticError:
    print("arith")
except:
    print("some")

#Exercise #2: What is the expected output of the following code?
#Arithmetic error

try:
    print(1/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")


#Exercise #3: What is the expected output of the following code?
#some
#Also we never learned assert, good to hear tho


def foo(x):
    assert x
    return 1/x


try:
    print(foo(0))
except ZeroDivisionError:
    print("zero")
except:
    print("some")


num = 0
try:
    1/num
except:
    print("Your math was wrong")
# Check for all errors
#Clearly tells user there was an issue
#I see no issues with this code