from math import sqrt
class Polygon:
    def __init__(self,*vertices):
        self.vertices=[Polygon.Point(v[0],v[1]) for v in vertices]
    @property
    def lines(self):
        allLines=[Polygon.LSeg(self.vertices[i],self.vertices[i+1]) for i in range(len(self)-1)]
        allLines.append(Polygon.LSeg(self.vertices[len(self)-1],self.vertices[0]))
        return allLines
    @property
    def area(self):
        total=0
        for i in range(len(self)-2):
            tri=Polygon.Triangle(self.vertices[0],self.vertices[i+1],self.vertices[i+2])
            total+=tri.area
        return total
    @property
    def perimeter(self):
        return sum([abs(line) for line in self.lines])
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
        def __init__(self,p1,p2,p3):
            self.p1=p1
            self.p2=p2
            self.p3=p3
        @property
        def area(self):
            a=self.p1.x*(self.p2.y-self.p3.y)
            b=self.p2.x*(self.p3.y-self.p1.y)
            c=self.p3.x*(self.p1.y-self.p2.y)
            return abs(a+b+c)/2

## Main Program ##
# poly1=Polygon((1.77,4.77), (4.27,7.97), (8.08,6.59), (7.95,2.53), (4.05,1.41))
# poly1=Polygon((1.77,4.77), (4.05,1.41), (7.95,2.53), (8.08,6.59), (4.27,7.97))
# print(poly1.perimeter)
# print(poly1.area)

# poly2=Polygon((5.09,5.80), (1.68,4.90), (1.48,1.38), (4.76,0.10), (7.00,2.83))
poly2=Polygon((5.09,5.80), (7.00,2.83), (4.76,0.10), (1.48,1.38), (1.68,4.90))
print(poly2.perimeter)
print(poly2.area)
