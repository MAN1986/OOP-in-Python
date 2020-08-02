from math import sqrt
class Polygon:
    def __init__(self,*vertices):
        self.vertices=[Polygon.Point(v[0],v[1]) for v in vertices]
    @property
    def lines(self):
        pass  #Retun list of all line segments of Polygon
    @property
    def area(self):
        pass # Use triangle class
    @property
    def perimeter(self):
        pass
    def __len__(self):
        return len(self.vertices)
    class LSeg:
        def __init__(self,p1,p2):
            self.p1=p1
            self.p2=p2
        def __abs__(self):
            return self.p1.dist(self.p2)
        def __repr__(self):
            return f'{self.p1}--{self.p2}'
    class Point:
        def __init__(self,x,y):
            self.x=x
            self.y=y
        def dist(self,other):
            return sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        def __repr__(self):
            return f'({self.x},{self.y})'
    class Triangle:
        pass

## Main Program ##
# p1=Point(1,3)
# p2=Point(2,5)
# # l1=LSeg(p1,p2)
# l1=LSeg(p1,(2,5))
# print(l1)
# print(abs(l1))
poly1=Polygon((0,0),(2,4),(5,6),(3,4))
print(len(poly1))
print(poly1.vertices)



# @property
#         def p1(self):
#             return self._p1
#         @p1.setter
#         def p1(self,p1):
#             if isinstance(p1,Point):
#                 self._p1=p1
#             elif isinstance(p1,tuple) and len(p1)==2:
#                 self._p1=Point(p1[0],p1[1])
#             else:
#                 raise TypeError
#         @property
#         def p2(self):
#             return self._p2
#         @p2.setter
#         def p2(self,p2):
#             if isinstance(p2,Point):
#                 self._p2=p2
#             elif isinstance(p2,tuple) and len(p2)==2:
#                 self._p2=Point(p2[0],p2[1])
#             else:
#                 raise TypeError
