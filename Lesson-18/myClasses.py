from functools import total_ordering
from enum import Enum
from random import shuffle
class Subj(Enum):
    Mech='Mechanism'
    LA='Linear Algebra'
    ES='Embedded Systems'
    CP2='Computer Programming-II'
    MOM='Mechanics of Material'
    Proj='Design Project'
class Desig(Enum):
    Prof='Professor'
    AssocProf='Associate Professor'
    AP='Assistant Professor'
    Lect='Lecturer'
    TF='Teaching Fellow'
class Instructor:
    allInsts=[]
    def __init__(self,fName,lName,desig:Desig):
        self.fName=fName
        self.lName=lName
        self.desig=desig
        self._courses=[]
        Instructor.allInsts.append(self)
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
    def assignCourse(self,*sub):
        for s in sub:
            if isinstance(s,Subj):
                s=s.name
            if s not in Subj.__members__:
                raise ValueError(f'{s} is not offered!')
            if Subj[s].value not in self._courses:
                self._courses.append(Subj[s].value)
                if Department.subjInst.get(s) is None:
                    Department.subjInst[s]=[self]
                else:
                    Department.subjInst[s].append(self)
@total_ordering
class Student:
    'This class defines a Student for Mechatronics Department'
    _department='Mechatronics'
    _allStudents=[]
    def __init__(self,fName,lName,reg):
        self.fName=fName
        self.lName=lName
        self.reg=reg
        self.email=f'{self.reg.lower()}@uet.edu.pk'
        self._courses=[Subj.Proj.value]
        self._groupMember=None
        self.fullName=f'{self.fName} {self.lName}'
        Student._allStudents.append(self)

    ## Getters and Setters
    @property
    def fullName(self):
        return f'{self.fName} {self.lName}'
    @fullName.setter
    def fullName(self,newname):
        f,l=newname.split(' ')
        self.fName=f
        self.lName=l
        self._fullName=newname    
    @property
    def fName(self):
        return self._fName
    @fName.setter
    def fName(self,newname):
        if(Student.validName(newname)):
            self._fName=newname
        else:
            raise ValueError('Name should contain alphabet only and at least 2 of those!')    
    @property
    def lName(self):
        return self._lName
    @lName.setter
    def lName(self,newname):
        if(Student.validName(newname)):
            self._lName=newname
        else:
            raise ValueError('Name should contain alphabet only and at least 2 of those!')
    @property
    def reg(self):
        return self._reg
    @reg.setter
    def reg(self,newreg):
        if(isinstance(newreg,str) and str(newreg).startswith('MCT-UET-')):
            self._reg=newreg
        else:
            raise ValueError('Reg must start as MCT-UET-')

    ## Static Methods ##
    @staticmethod
    def validName(name):
        if(isinstance(name,str) and len(name)>=2 and name.isalpha()):
            return True
        else:
            return False
    ## Instance Methods ##
    def registerSubject(self,*sub):
        for s in sub:
            if isinstance(s,Subj):
                s=s.name
            if s not in Subj.__members__:
                raise ValueError(f'{s} is not offered!')
            if Subj[s].value not in self._courses:
                self._courses.append(Subj[s].value)
                if Department.subjStd.get(s) is None:
                    Department.subjStd[s]=[self]
                else:
                    Department.subjStd[s].append(self)
    ## Class Methods ##
    @classmethod
    def notRegSub(cls):
        a=set()
        m=[e.value for e in Subj]
        for std in cls._allStudents:
            s=set(std._courses)
            a.update(s)
        return list(set(m).difference(a))
    @classmethod
    def withoutGroupMembers(cls):
        return list(filter(lambda s: s._groupMember is None,cls._allStudents))
    
    ## Magic Methods ##
    def __repr__(self):
        return f'{self.lName}-{self.reg[-2:]}'
    def __add__(self,other):
        if(self._groupMember is not None):
            raise ValueError(f'{self} already has {self._groupMember} as group member')
        elif(other._groupMember is not None):
            raise ValueError(f'{other} already has {other._groupMember} as group member')
        else:
            self._groupMember=other
            other._groupMember=self
    def __sub__(self,other):
        if(self._groupMember is None and other._groupMember is None):
            return
        elif(self._groupMember is not other):
            raise ValueError(f'{self} is not group member of {other}.')
        else:
            self._groupMember=None
            other._groupMember=None
    def __lt__(self,other):
        return len(self)<len(other)
    def __eq__(self,other):
        return len(self)==len(other)
    def __len__(self):
        return len(self._courses)
    def __iter__(self):
        yield self.fName
        yield self.lName
        yield self.reg
        for c in self._courses:
            yield c
class Department:
    subjInst={}
    subjStd={'Proj':Student._allStudents}
    @staticmethod
    def createGroups():
        shuffle(Student._allStudents)
        l=len(Student._allStudents)
        for i in range(0,l,2):
            if(i!=l-1):
                Student._allStudents[i]+Student._allStudents[i+1]



            











