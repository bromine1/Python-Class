from time import sleep
def add():
    try:
        print("\nPlease give 2 numbers to be added\n")
        x = float(input("The first number\n:"))
        y = float(input("The second number\n:"))
    except ValueError:
        print("\n\nOne of those wasn't a number, please try again")
        sleep(1)
        add()
    except:
        print("Something went wrong, please try again")
        sleep(1)
        add()
    return x + y 
print(add())
exit()

