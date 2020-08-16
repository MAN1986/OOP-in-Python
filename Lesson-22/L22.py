class Employee:
    raise_amount=1.1 #10% annual raise in income
    total_emp=0
    def __init__(self,fName,lName,pay):
        self.fName=fName
        self.lName=lName
        self.pay=pay
        self.email=f"{self.fName.lower()}.{self.lName.lower()}@uet.edu.pk"
        Employee.total_emp+=1
    def raise_pay(self):
        self.pay*=self.raise_amount
    def __repr__(self):
        return f'{self.fName} {self.lName}'
class Instructor(Employee):
    def __init__(self,fName,lName,pay,desig):
        # Employee.__init__(self,fName,lName,pay)
        super().__init__(fName,lName,pay)
        self.desig=desig
        self.courses=[]
    def assignCourse(self,*subj):
        self.courses=list(set(self.courses+list(subj)))
        
class AdminStaff(Employee):
    raise_amount=1.15
    def __init__(self,fName,lName,pay,team=None):
        super().__init__(fName,lName,pay)
        self.team=team
        self.tasks=[]
    def assignTask(self,*task):
        self.tasks=list(set(self.tasks+list(task)))


## Main Program ##
i1=Instructor('Ahsan','Naeem',100000,'AP')
i1.assignCourse('CP2','CP2','Mech')
i1.raise_pay()
print(i1.pay)

as1=AdminStaff('Imran','Hanif',90000,'Exam')
as1.assignTask('exam-1','exam-2')
as1.raise_pay()
print(as1.pay)
# print(as1.tasks)

# print(i1.courses)
# print(i1.desig)
# print(isinstance(i1,Employee))
# help(i1)
# print(Instructor.__mro__)


# print(hasattr(i1,'raise_pay'))
# print(hasattr(as1,'raise_pay'))

# print(hasattr(i1,'assignCourse'))
# print(hasattr(as1,'assignCourse'))
