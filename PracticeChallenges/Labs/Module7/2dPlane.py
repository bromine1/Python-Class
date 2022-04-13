#RS
#period 4
#4/13/22

from math import sqrt


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return sqrt((self.__x - x)**2 + (self.__y - y)**2)

    def distance_from_point(self, point):
        pointX = point.getx()
        pointY = point.gety()
        return sqrt((self.__x - pointX)**2 + (self.__y - pointY)**2)

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))