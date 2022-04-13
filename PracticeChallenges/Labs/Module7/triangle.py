from math import sqrt

class Point:
    def __init__(self, x=0.0, y=0.0): #initialize data
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return sqrt((self.__x - x)**2 + (self.__y - y)**2) #Distance formula

    def distance_from_point(self, point):
        pointX = point.getx()
        pointY = point.gety()
        return sqrt((self.__x - pointX)**2 + (self.__y - pointY)**2) #distance formula


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3): # get points
        self.one = vertice1
        self.two = vertice2
        self.three = vertice3

    def perimeter(self): #Find distance between points
        one = self.one.distance_from_point(self.two)
        two = self.one.distance_from_point(self.three)
        three = self.two.distance_from_point(self.three)
        return one + two + three #return them

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
