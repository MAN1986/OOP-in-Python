from functools import total_ordering
@total_ordering
class Student:
    'This class defines a Student for Mechatronics Department'
    _department='Mechatronics'
    _offSubjects=['Mech','LA','ES','CP-II','MOM','Proj']
    _allStudents=[]
    def __init__(self,fName,lName,reg):
        self.fName=fName
        self.lName=lName
        self.reg=reg
        self.email=f'{self.reg.lower()}@uet.edu.pk'
        self._courses=['Proj']
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
            if s not in Student._offSubjects:
                raise ValueError(f'{s} is not offered!')
            if s in Student._offSubjects and s not in self._courses:
                self._courses.append(s)
    ## Class Methods ##
    @classmethod
    def notRegSub(cls):
        a=set()
        for std in cls._allStudents:
            s=set(std._courses)
            a.update(s)
        return list(set(cls._offSubjects).difference(a))
    @classmethod
    def withoutGroupMembers(cls):
        return list(filter(lambda s: s._groupMember==None,cls._allStudents))
    
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
        elif(self._groupMember!=other):
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





            











