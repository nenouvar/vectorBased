class Line:
    def __init__(self, vectors, t):
        self.t = t
        self.vectors = vectors
    def getPoints(self, n): # list of vectors
        points = []