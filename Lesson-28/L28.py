from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def __init__(self,units):
        self.units=units
    @abstractmethod
    def area(self):
        print('Area Calculation!')
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self,l,b,units):
        super().__init__(units)
        self.l=l
        self.b=b
    def area(self):
        super().area()
        return self.l*self.b

## Main Program ##
# s=Shape()
r=Rectangle(5,6,'cm')
print(r.area())
