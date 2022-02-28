import random
def guesser():
    try:
        guess = int(input("Please guess a number between 1 and 5"))
    except:
        print("Only whole integers please")
        guesser()
    if guess < 1 or guess > 5:
        print("That isn't between 1 and 5")
        guesser()
    if random.randrange(1,6) == guess:
        print("You guessed the number!")
    else:
        print("That wasn't the number")
        guesser()
