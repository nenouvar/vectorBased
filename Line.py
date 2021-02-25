
from Vector import Vector
class Line:
    def __init__(self, vectors, t):
        self.t = t
        self.vectors = vectors
        self.param = vectors[0].add(vectors[1].multiply(self.t))
    def getPoints(self, n): # list of vectors
        points = []
        for i in range(-n, n, 1):
            points.append(Line(self.vectors, i).param)
        return points