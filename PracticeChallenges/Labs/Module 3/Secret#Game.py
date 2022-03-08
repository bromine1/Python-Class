
#Ryan Stauffer 3.2.1.3 Labs

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
# Credit to the magician for the above
# Bottom belongs to Ryan Stauffer
while True:
    #guess number
    guess = int(input("Guess my number\n:"))
    #guess check: if true break
    if guess == 777:
        print(guess)
        break
    print("Ha ha! You're stuck in my loop!")

print("Well done, muggle! You are free now.")
exit()


