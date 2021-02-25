
from Vector import Vector
class Line:
    def __init__(self, vectors, t):
        self.t = t
        self.vectors = vectors
    def param(self):
        v = Vector([0, 0])
        v1 = v.add(self.vectors[0])
        v2 = self.vectors[1].multiply(self.t)
        return v1.add(v2)
    def getPoints(self, n): # list of vectors
        points = []
        for i in range(-n, n, 1):
            points.append(Line(self.vectors, i))
        return points