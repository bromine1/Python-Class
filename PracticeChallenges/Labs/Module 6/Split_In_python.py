def mysplit(strng):
    word =""
    finalString = []
    #Initialize Variables
    #I miss strongtyping sometimes
    for x in strng:
        if x.isspace():
            if not word.isspace() and len(word) != 0: #Check the word to make sure it isn't an empty item
                finalString.append(word)
                word = "" # reset the variable
        else:
            word += x # add the letter to word
    return finalString # return the string

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))