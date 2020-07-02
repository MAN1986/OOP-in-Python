class Student:
    def __init__(self,fName,lName,reg):
        self.fName=fName
        # self.set_fName(fName)
        self.lName=lName
        # self.set_lName(lName)
        self.reg=reg
    def get_fName(self):
        return self._fName
    def set_fName(self,newname):
        if(Student.validName(newname)):
            self._fName=newname
        else:
            raise ValueError('Name must contain alphabets only and atleast two of those!')
    fName=property(get_fName,set_fName)
    
    
    def get_lName(self):
        return self._lName
    def set_lName(self,newname):
        if(Student.validName(newname)):
            self._lName=newname
        else:
            raise ValueError('Name must contain alphabets only and atleast two of those!')
    lName=property(get_lName,set_lName)
    
    def get_reg(self):
        return self.reg
    def set_reg(self,newreg):
        self.reg=newreg

    @staticmethod
    def validName(newname):
        if(isinstance(newname,str) and len(newname)>=2 and newname.isalpha()):
            return True
        else:
            return False

