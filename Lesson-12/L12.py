from myClasses import Student
std1=Student('Anwar','Ali','MCT-UET-01') 
std2=Student('Akbar','Khan','MCT-UET-02')
std3=Student('Hamza','Akhtar','MCT-UET-03')
std4=Student('Faisal','Iqbal','MCT-UET-04')

std1.registerSubject('CP-II','MOM')
std2.registerSubject('Mech','ES','MOM')
std3.registerSubject('CP-II','LA')
std4.registerSubject('Mech','LA','MOM','ES')

# std1+std2
# std2-std1
# print(std1._groupMember)

# Student._allStudents.sort()
# print(Student._allStudents)
# print(min(Student._allStudents))

# print(std2>std1)
# print(std2<=std1)
# print(len(std1))

for i in std2:
    print(i)
