
file = 'PracticeChallenges/Labs/Module8/Files/samplefile.txt'
def countCharacter(text):
    latinNum = {chr(k):0 for (k) in range(ord('a'), ord('z'))}  # Dictionary Comprehension of the alphabet
    for line in text:
        for character in line: #count characters
            if character.isalpha():
                latinNum[character.lower()] += 1 #add them to the dictionary
    return latinNum

with open(file, 'r', encoding='utf_8') as text:
    histList = countCharacter(text)
    for x in histList.items():
        if x[1] > 0:
            print(f"{x[0]} 🠖 {x[1]}")
