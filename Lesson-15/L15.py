class Author:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.books=[]
    def __repr__(self):
        return f'{self.name}-{self.age}'
class Book:
    def __init__(self,title,year,authors=None):
        self.title=title
        self.year=year
        if(authors is None):
            self.authors=[]
        else:
            self.authors=authors
    @property
    def authors(self):
        return self._authors
    @authors.setter
    def authors(self,newauthors):
        for a in newauthors:
            if(not isinstance(a,Author)):
                raise TypeError
            else:
                a.books.append(self)
        self._authors=newauthors
    def __repr__(self):
        return f'{self.title}-{self.year}'

## Main Program ##
auth1=Author('Ahsan Naeem',34)
auth2=Author('Rzi Abbas',30)
auth3=Author('Misbah-ur-Rehman',30)
print(f'{auth1}={auth1.books}')
print(f'{auth2}={auth2.books}')  
print(f'{auth3}={auth3.books}') 
b1=Book('Python Programming',2020,[auth1,auth2])
b2=Book('OOP in Python',2020,[auth1,auth3])
print('_______________')
print(f'{auth1}={auth1.books}')
print(f'{auth2}={auth2.books}')  
print(f'{auth3}={auth3.books}') 
print('_______________')
print(b1.authors)



#https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
