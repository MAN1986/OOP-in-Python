class Student:
    'This class defines a Student for Mechatronics Department'
    department='Mechatronics'
    offSubjects=['Mech','LA','ES','CP-II','MOM','Proj']
    allStudents=[]
    def __init__(self,fName,lName,reg):
        self.fName=fName
        self.lName=lName
        self.reg=reg
        self.email=f'{self.reg.lower()}@uet.edu.pk'
        self.courses=['Proj']
        self.groupMember=None
        Student.allStudents.append(self)
    @property
    def fullName(self):
        return f'{self.fName} {self.lName}'
    def __repr__(self):
        return f'{self.lName}-{self.reg[-2:]}'
    
    def registerSubject(self,*sub):
        for s in sub:
            if s not in Student.offSubjects:
                raise ValueError(f'{s} is not offered!')
            if s in Student.offSubjects and s not in self.courses:
                self.courses.append(s)
    def setGroupMember(self,other):
        if(self.groupMember!=None):
            raise ValueError(f'{self} already has {self.groupMember} as group member')
        elif(other.groupMember!=None):
            raise ValueError(f'{other} already has {other.groupMember} as group member')
        else:
            self.groupMember=other
            other.groupMember=self
    def dropGroupMember(self,other):
        if(self.groupMember==None and other.groupMember==None):
            return
        elif(self.groupMember!=other):
            raise ValueError(f'{self} is not group member of {other}.')
        else:
            self.groupMember=None
            other.groupMember=None
    @classmethod
    def notRegSub(cls):
        a=set()
        for std in cls.allStudents:
            s=set(std.courses)
            a.update(s)
        return list(set(cls.offSubjects).difference(a))
    @classmethod
    def withoutGroupMembers(cls):
        return list(filter(lambda s: s.groupMember==None,cls.allStudents))
    




            











