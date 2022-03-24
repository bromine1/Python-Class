

def mysplit(strng):
    word =""
    finalString = []
    for x in strng:
        if x.isspace():
            if not word.isspace() and len(word) != 0:
                finalString.append(word)
                word = ""
        else:
            word += x
    return finalString

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))