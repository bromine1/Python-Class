class mom:
    hairColor = "Brown"

class dad:
    hairColor = "Black"

class child(mom, dad):
    pass

Jimmy = child()
print(Jimmy.hairColor)

