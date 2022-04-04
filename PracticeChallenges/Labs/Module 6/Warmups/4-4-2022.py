#Get values

a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
    # Try division
    division = a/b
    print(division)
except ZeroDivisionError as err:
    #Except a zero division
    print(f"Please enter valid values. {err}")
else:
    #Confirm to user that values are valid
    print("Both values were valid")
finally:
    #Confirm to user that values are finished
    print("Finally")

#1. Code is structured more with errors than perviously
#2I haven't seen finally before, but it makes sense why it exists
#Else also makes a decent amount of sense for the programs
#3. answered in PRIMM in code
#4 Code doesnt do anything to prevent a zero division error, or stop the program
#Only one line in the output says theres an error, then it continues as usual