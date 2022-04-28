#Rstauff
#Python 2 Warmup April 26th 2022
import math
try:
    print(math.sqrt(-9))
except ValueError:
    print("inf")
else:
    print("fine")
finally:
    print("the end")

#Prints:
# inf
# the end


import math
class NewValueError(ValueError):

    def __init__(self, name, color, state):
        self.data = (name, color, state)

try:
    raise NewValueError("Enemy warning", "Red alert", "High readiness")
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end='! ')

#Prints:
# ENemy Warning! Red ALert! High Readiness!