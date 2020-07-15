from math import sqrt
from numbers import Real
from functools import total_ordering
@total_ordering
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,newx):
        if(isinstance(newx,Real)):
            self._x=newx
        else:
            raise TypeError('x coordinate must be a number')
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,newy):
        if(isinstance(newy,Real)):
            self._y=newy
        else:
            raise TypeError('y coordinate must be a number')
    def reset(self):
        self.move(0,0)
    def move(self,newx,newy):
        self.x=newx
        self.y=newy
    def movX(self,newx):
        self.x=newx
    def movY(self,newy):
        self.x=newy
    def __repr__(self):
        return f'({self.x},{self.y})'
    def __abs__(self):
        return sqrt(self.x**2+self.y**2)
    def __neg__(self):
        return Point(-self.x,-self.y)
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
    
    def __sub__(self,other):
        # return Point(self.x-other.x,self.y-other.y)
        return self+(-other)
    
    def __mul__(self,other):
        if(isinstance(other,Real)):
            return Point(self.x*other,self.y*other)
        if(isinstance(other,Point)):
            return self.x*other.x+self.y*other.y
    __rmul__=__mul__
    
    def __truediv__(self,num):
        return self*(1/num)
    
    def __eq__(self,other):
        return abs(self)==abs(other)
    def __lt__(self,other):
        return abs(self)<abs(other)
    def __iter__(self):
        yield self.x
        yield self.y
    
