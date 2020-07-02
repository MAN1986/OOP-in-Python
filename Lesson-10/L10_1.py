class Student:
    def __init__(self,fName,lName,reg):
        self.fName=fName
        self.lName=lName
        self.reg=reg

## Main Program ##
std1=Student('Anwar','Ali','MCT-UET-01') 
std2=Student('Akbar','Khan','MCT-UET-02')
att='fName'
setattr(std1,att,'Ahmad')
print(getattr(std1,att))

print(getattr(std1,'uni','UET'))
