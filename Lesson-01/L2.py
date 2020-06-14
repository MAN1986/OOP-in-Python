class Student:
    def __init__(self,fName,lName,reg):
        self.fName=fName
        self.lName=lName
        self.reg=reg
        self.email=f'{self.reg.lower()}@uet.edu.pk'
    def welcome(self):
        return f'Welcome {self.fName} {self.lName}'

## Main Program ##
std1=Student('Anwar','Ali','MCT-UET-01') # Object Instantiated and Initialzed
std2=Student('Akbar','Khan','MCT-UET-02')

print(std1.welcome())
print(std2.welcome())
