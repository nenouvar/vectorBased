
import math
from Vector import Vector
class Circle:
    def __init__(self, center, r, theta):
        self.center = center
        self.r = r
        self.theta = theta
        self.n = len(self.center.list)
    def param(self): # vector-like object
        param = []
        x = self.center.list[0] + self.r*math.cos(self.theta)
        y = self.center.list[1] + self.r*math.sin(self.theta)
        param = [x, y]
        return Vector(param)
    def getPoints(self, n): # list of vectors
        points = []
        for i in range(n+1):
            self = Circle(self.center, self.r, 2*i*math.pi/n)
            points.append(self.param())
        return points