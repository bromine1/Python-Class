class mom:
    eyeColor = "green"
    def walk(self):
        print("i'm walking")

class child(mom):
    pass

jimmy = child()

print(jimmy.eyeColor)
jimmy.walk()

