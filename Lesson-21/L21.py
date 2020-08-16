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
    pass
class AdminStaff(Employee):
    pass

## Main Program ##
i1=Instructor('Ahsan','Naeem',100000)
# print(type(i1))
# print(isinstance(i1,Instructor))
# print(isinstance(i1,Employee))
# print(Employee.total_emp)
# print(i1.pay)
# i1.raise_pay()
# print(i1.pay)
# e1=Employee('Hamza','Latif',90000)
# print(isinstance(e1,Instructor))
# print(isinstance(e1,Employee))
a1=AdminStaff('Adeel','Munir',80000)
print(isinstance(a1,Instructor))
print(isinstance(a1,AdminStaff))
print(isinstance(a1,Employee))
