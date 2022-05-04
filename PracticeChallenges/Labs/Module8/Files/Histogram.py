from os import strerror
import re



file = 'PracticeChallenges/Labs/Module8/Files/samplefile.txt'
def countCharacter(text):
    latinNum = {chr(letter):0 for (letter) in range(ord('a'), ord('z'))}  # Dictionary Comprehension of the alphabet
    for line in text:
        for character in line: #count characters
            if character.isalpha():
                latinNum[character.lower()] += 1 #add them to the dictionary
    return latinNum

try:
    with open(file, 'r', encoding='utf_8') as text:
        histList = countCharacter(text)
except IOError as e:
    exit(f"error {strerror(e.errno)}")


histogram = lambda x, y: f"{x} 🠖 {y}"

writeFile = re.split(".txt$", file)

with open(f"{writeFile[0]}.hist.txt", "w") as text:
    for key in sorted(histList.keys(), key=lambda x: histList[x], reverse=True):
        if histList[key] > 0:
            print(histogram(key,histList[key]))
            text.write(f"{histogram(key,histList[key])}\n")
