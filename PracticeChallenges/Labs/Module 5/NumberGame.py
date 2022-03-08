import random
# Ryan Stauffer NumberGame
def guesser():
    # Error handling
    try:
        guess = int(input("Please guess a number between 1 and 5"))
    except:
        print("Only whole integers please")
        # Calls Function again
        guesser()
    if guess < 1 or guess > 5:
        print("That isn't between 1 and 5")
        guesser()
        # Get random number and check it
    if random.randrange(1,6) == guess:
        print("You guessed the number!")
    else:
        print("That wasn't the number")
        guesser()
