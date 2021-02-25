from Vector import Vector
# from Line import Line

# Vectors using lists
e0 = Vector([0, 0])
e1 = Vector([1, 0])
e2 = Vector([0, 1])

e3 = e1.add(e2).list
e4 = e1.sub(e2).list
d0 = e1.inn(e2)
d1 = e1.inn(e1)
d2 = e3.polar()
d3 = e1.multiply(2).list
print([e3,e4,d0,d1,d2,d3])

# Line using list of vectors and t
# l1 = Line([e0, e1], 2)
# print(l1.param)
# print(l1.getPoints())