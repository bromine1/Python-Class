#Ryan Stauffer 3-2-2022 warmup
from math import pi

# area of a circle segment in degrees
def circleSegmentArea(radius, angle):
    '''
    Returns the area of a circle
    Takes an radius and an angle
    formula used is \frac{segmet\ area}{360}\pi r^{2}
    '''
    # area of a circle segment formula: \frac{segmet\ area}{360}\pi r^{2} (Display in Tex)
    #returns as number for further processing
    return (angle/360) * pi * radius **2

print(circleSegmentArea(5, 60))

# import random
import random
# Splash text
def spalshtext():
    happenstance = {2: "A Wild Frog Approaches",
                    3: "Get off of twitter",
                    4: "Math is kind of wack bro",
                    5: "If you're seeing this you rolled a 5",
                    6: "Also try Terraria!",
                    7: "Also try Minecraft",
                    8: "You got a star!",
                    9: "Oof, that's late.",
                    10:" Sign my petition",
                    11:"Wild magic surge",
                    12:"I'm running out of references",
                    13:"Thats a little unlucky",
                    14:"DOOR STUCK, DOOR STUCK",
                    15:"Great philosopher Haga says to get out of my house",
                    16:"Happy Birthday!",
                    17:"muy, muy interesante",
                    18:"Around this time this month ~ Rachel",
                    19:"#Don't leave this line in production",
                    20:"NAT 20!!!"}

    return happenstance[random.randint(2,20)]