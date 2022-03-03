import sys
# Get pathing to work on my end
sys.path.append("Practice challenges\Labs\Module 5\Calculator\Functions\shapes")
#import module
from shapes import quadArea,trigArea,circleArea
#get data points
l = 2
w = 2
h = 2
r = 3

# functions return data as integers for further processing
print (quadArea(l,w))
print (trigArea(l,h))
print(circleArea(r))