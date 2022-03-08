#Ryan Stauffer 3.2.1.10
# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Input a word to have it's vowels eaten.\n:")
#Capitalize for formatting
user_word = user_word.upper()
for letter in user_word:
    #check if not in vowels, print the letter if it isn't
    if letter in ["A", "E", "I", "O" , "U"]:
        continue
    else:
        print(letter)
exit()