from math import sqrt
class Polygon:
    def __init__(self,*vertices):
        self.vertices=[Polygon.Point(v[0],v[1]) for v in vertices]
    @property
    def lines(self):
        pass  #Retun list of all line segments of Polygon
    @property
    def area(self):
        if(self.shape=='Complex'):
            raise TypeError('Area of Complex Polygon is out of scope!')
        else:
            pass # Shoelace Algorithm
    @property
    def perimeter(self):
        pass # Complete Perimiter Calculations
    @property
    def shape(self):
        pass
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
        
    class LSeg:
        def __init__(self,p1,p2):
            self.p1=p1
            self.p2=p2
        def __abs__(self):
            return self.p1.dist(self.p2)
