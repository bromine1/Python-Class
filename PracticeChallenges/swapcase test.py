

text = input("Input some text: ")



def swapcase1(text):
    from random import randint
    ltext = list(text) 
    print(ltext)
    for x in range(len(ltext)):
        ltext[x].swapcase()
    return "".join(ltext)


print(swapcase1(text))