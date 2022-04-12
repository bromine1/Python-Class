from typing import final


user_word = input("Input a word to have it's vowels eaten.\n:")
word_without_vowels = ""
#Capitalize for formatting
user_word = user_word.upper()
for letter in user_word:
    #check if not in vowels, print the letter if it isn't
    if letter in ["A", "E", "I", "O" , "U"]:
        continue
    else:
        word_without_vowels+=letter

print(word_without_vowels)
exit()