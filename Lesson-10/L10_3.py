class Student:
    def __init__(self,fName,lName,reg):
        self.fName=fName
        self.lName=lName
        self.reg=reg
        self.fullName=f'{self.fName} {self.lName}'
    @property
    def fullName(self):
        self.fullName=f'{self.fName} {self.lName}'
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
            raise ValueError('Name must contain alphabets only and atleast two of those!')

    @property
    def lName(self):
        return self._lName
    @lName.setter
    def lName(self,newname):
        if(Student.validName(newname)):
            self._lName=newname
        else:
            raise ValueError('Name must contain alphabets only and atleast two of those!')
    
    @property
    def reg(self):
        return self._reg
    @reg.setter
    def reg(self,newreg):
        if(isinstance(newreg,str) and str(newreg).startswith('MCT-UET-')):
            self._reg=newreg
        else:
            raise ValueError('Reg. No. must start with MCT-UET-')

    @staticmethod
    def validName(newname):
        if(isinstance(newname,str) and len(newname)>=2 and newname.isalpha()):
            return True
        else:
            return False
