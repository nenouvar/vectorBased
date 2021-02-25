import math
class Vector:
    def __init__(self, L):
        self.list=L
        self.n=len(self.list)
    def add(self, other):
        L=[]
        for i in range(self.n):
            sum=self.list[i]+other.list[i]
            L.append(sum)
        return Vector(L)
    def sub(self, other):
        L=[]
        for i in range(self.n):
            sum=self.list[i]-other.list[i]
            L.append(sum)
        return Vector(L)
    def inn(self, other):
        sum=0
        for i in range(self.n):
            sum +=self.list[i]*other.list[i]
        return sum
    def multiply(self, t):
        L=[]
        for i in range(self.n):
            sum=self.list[i]*t
            L.append(sum)
        return Vector(L)
    def polar(self):
        r=(self.inn(self))**0.5
        theta=math.acos(self.list[0]/r)
        return [r,theta]