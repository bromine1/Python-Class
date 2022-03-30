
def read_int(prompt, min, max):
    try:
        global newNum
        num = input(prompt)
        newNum = int(num)
        assert newNum >= min and newNum <= max
    except ValueError:
        print("Error: wrong input")
        read_int(prompt, min, max)
    except AssertionError:
        print(f"Error: the value is not within permitted range {min} to {max}.")
        read_int(prompt, min, max)
    return newNum




v = read_int("Enter a number from -10 to 10: \n ", -10, 10)

print("The number is:", v)
