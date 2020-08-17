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
class LabDirector(Instructor):
    def __init__(self,fName,lName,pay,desig,lab,*labEmp):
        super().__init__(fName,lName,pay,desig)
        self.lab=lab
        self.labEmp=list(labEmp)
    def assignCourse(self,*subj):
        super().assignCourse(*subj)
        for ins in self.labEmp:
            ins.assignCourse(*subj)
    def addLabEmployee(self,ins):
        self.labEmp.append(ins)
    def dropLabEmployee(self,ins):
        self.labEmp.remove(ins)

class AdminStaff(Employee):
    raise_amount=1.15
    allAdminStaff=[]
    def __init__(self,fName,lName,pay,team=None):
        super().__init__(fName,lName,pay)
        self.team=team
        self.tasks=[]
        AdminStaff.allAdminStaff.append(self)
    def assignTask(self,*task):
        self.tasks=list(set(self.tasks+list(task)))
class AdminOfficer(AdminStaff):
    def __init__(self,fName,lName,pay,team):
        super().__init__(fName,lName,pay,team)
    @property
    def teamMembers(self):
        return list(filter(lambda s: s.team==self.team,AdminStaff.allAdminStaff))


## Main Program ##
i1=Instructor('Ahsan','Naeem',100000,'AP')
i2=Instructor('Rzi','Abbas',95000,'Lect')
i3=Instructor('Misbah','Rehman',90000,'Lect')
i4=Instructor('Shujat','Ali',85000,'TF')

# labDir1=LabDirector('Mohsin','Rizwan',120000,'AP','Embedded Systems',i1,i2)
# print(labDir1.labEmp)
# labDir1.assignCourse('Robotics')
# print(labDir1.courses)
# print(i1.courses)
# print(i2.courses)

as1=AdminStaff('Imran','Hanif',90000,'Exam')
as2=AdminStaff('Saqib','Majeed',105000,'Dues')
as3=AdminStaff('Inam','Haider',110000,'Exam')

off1=AdminOfficer('Naveed','Aslam',120000,'Exam')
print(off1.teamMembers)















