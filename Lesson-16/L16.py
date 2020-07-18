from enum import Enum
class Desig(Enum):
    Prof='Professor'
    AssocProf='Associate Professor'
    AP='Assistant Professor'
    Lect='Lecturer'
    TF='Teaching Fellow'
class Instructor:
    def __init__(self,fName,lName,desig:Desig):
        self.fName=fName
        self.lName=lName
        self.desig=desig
        self.courses=[]
    def __repr__(self):
        return f'{self.fName} {self.lName} - {self.desig}'
    @property
    def desig(self):
        return self._desig.value
    @desig.setter
    def desig(self,newdesig):
        if(isinstance(newdesig,Desig)):
            newdesig=newdesig.name
        if(newdesig in Desig.__members__):
            self._desig=Desig[newdesig]
        else:
            raise ValueError(f'{newdesig} is not a valid Designation!')
## Main Program ##
i1=Instructor('Ali','Raza',Desig.AssocProf)
print(i1.desig)






# print(type(Desig.Prof))
# print(isinstance(Desig.AssocProf,Desig))
# print(repr(Desig.Prof))
# print(Desig.AssocProf.value)
# print(Desig.__members__)
# print(Desig['Lect'].value)
