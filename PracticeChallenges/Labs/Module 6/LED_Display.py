#Ryan Stauffer LED Display Lab

#I did look up a hint to the lab and got the following:
# Hints taken from https://stackoverflow.com/a/58721716
#Keep them on one line
#use 3 dimensional lists



def nums(num):
    numbers = {
        #Map each number line by line
        #Array will essentially be rotated right 90 degrees, placing numbers correctly
        
        #Line:  1      2      3      4      5
        '0': ("***", "* *", "* *", "* *", "***"),
        '1': (" * ", " * ", " * ", " * ", " * " ),
        '2': ("***", "  *", "***", "*  ", "***" ),
        '3': ("***", "  *", "***", "  *", "***"),
        '4': ("* *", "* *", "***", "  *", "  *"),
        '5': ("***", "*  ", "***", "  *", "***"),
        '6': ("*  ", "*  ", "***", "* *", "***"),
        '7': ("***", "  *", "  *", "  *", "  *"),
        '8': ("***", "* *", "***", "* *", "***"),
        '9': ("***", "* *", "***", "  *", "  *"),
    }
    numberString = [numbers[nums] for nums in str(num)] #Creates a 3 dimensional list with each number
    for n in range (5): # used for choosing which line is being printed
        print(" ".join(part[n] for part in numberString)) # prints a line of the number. part in partstring selects the number
        #part[n] selects the line from the selected number

nums(123)
nums(9081726354)
