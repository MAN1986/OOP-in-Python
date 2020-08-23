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
        if(self.shape=='Complex'):
            raise TypeError('Area of Complex Polygon is out of scope!')
        else:
            x=[v.x for v in self.vertices]
            y=[v.y for v in self.vertices]
            sum1=sum(i*j for i,j in zip(x,y[1:]+y[:1]))
            sum2=sum(i*j for i,j in zip(x[1:]+x[:1],y))
            return abs(sum1-sum2)/2
    @property
    def perimeter(self):
        return sum([abs(line) for line in self.lines])
    @property
    def shape(self):
        for i in range(2,len(self)):
            for j in range(2,i+1):
                if (i==len(self)-1 and i==j):
                    break
                if Polygon.LSeg.intersect(self.lines[i],self.lines[i-j]):
                    return 'Complex'
        z=list(zip(self.vertices,self.vertices[1:],self.vertices[2:]))
        z.append((self.vertices[-2],self.vertices[-1],self.vertices[0]))
        signs1=[Polygon.Point.zCrossProduct(a,b,c)>=0 for a,b,c in z]
        signs2=[Polygon.Point.zCrossProduct(a,b,c)<=0 for a,b,c in z]
        if(all(signs1) or not any(signs1)):
            return 'Convex'
        if(all(signs2) or not any(signs2)):
            return 'Convex'
        return 'Concave'
        # Check Intrsections as discussed in Algorithm
        # if(any intersetion):
            #return Complex
        # if (all cross product>=0 or all cross products <=0):
            #return 'Convex'
        # return 'Concave'
        
    def __len__(self):
        return len(self.vertices)
    def __iter__(self):
        return (p for p in self.vertices)

    class Point:
        def __init__(self,x,y):
            self.x=x
            self.y=y
        def dist(self,other):
            return sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        def __repr__(self):
            return f'({self.x},{self.y})'
        @staticmethod
        def zCrossProduct(a,b,c):
            return (a.x-b.x)*(b.y-c.y)-(a.y-b.y)*(b.x-c.x)
        
    class LSeg:
        def __init__(self,p1,p2):
            self.p1=p1
            self.p2=p2
        def __abs__(self):
            return self.p1.dist(self.p2)
        @staticmethod
        def ccw(A,B,C):
            return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

        def intersect(self,other):
            return Polygon.LSeg.ccw(self.p1,other.p1,other.p2) != Polygon.LSeg.ccw(self.p2,other.p1,other.p2) and Polygon.LSeg.ccw(self.p1,self.p2,other.p1) != Polygon.LSeg.ccw(self.p1,self.p2,other.p2)

## Main Program ##
# poly1=Polygon((0.65,0.92), (5,0), (6,2), (4,3), (3,2), (4,-2), (-1,-3))
# print(poly1.shape)

# poly2=Polygon((1.77,4.77), (4.27,7.97), (8.08,6.59), (7.95,2.53), (4.05,1.41))
# print(poly2.shape)
# print(poly2.perimeter)
# print(poly2.area)    

# poly3=Polygon((3,4), (5,11), (12,8), (9,5), (5,6))
# print(poly3.shape)
# print(poly3.perimeter)
# print(poly3.area)

######################
# poly=Polygon((0.65,0.92), (5,0), (6,2), (4,3), (3,2), (4,-2), (-1,-3))
# poly=Polygon((0.65,0.92), (-1,-3), (4,-2), (3,2), (4,3), (6,2), (5,0))
# # print(poly.area)
# print(poly.shape)

# poly=Polygon((0.5,3), (5.5,3), (1,0), (3,5), (5,0))
# # poly=Polygon((0.5,3), (5,0), (3,5), (1,0), (5.5,3))
# # print(poly.area)
# print(poly.shape)
# # print(poly.perimeter)

# poly=Polygon((1.7,0), (3,1), (4.3,0), (3.75,1.6), (4.9,2.4), (3.4,2.4), (3,3.6), (2.7,2.4), (1.1,2.4), (2.3,1.6))
# # poly=Polygon((1.7,0), (2.3,1.6), (1.1,2.4), (2.7,2.4), (3,3.6), (3.4,2.4), (4.9,2.4), (3.75,1.6), (4.3,0), (3,1))
# print(poly.area)
# print(poly.shape)
# print(poly.perimeter)

poly=Polygon((0,0),(0,1),(0,2),(2,2),(4,2),(4,1),(4,0),(2,0))
print(poly.area)
print(poly.perimeter)
print(poly.shape)
