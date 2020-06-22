from myClasses import Student

std1=Student('Anwar','Ali','MCT-UET-01') 
std2=Student('Akbar','Khan','MCT-UET-02')
std3=Student('Hamza','Akhtar','MCT-UET-03')

# offSubjects=['Mech','LA','ES','CP-II','MOM','Proj']
std1.registerSubject('CP-II','MOM')
std2.registerSubject('Mech','ES','MOM')
std3.registerSubject('CP-II')

print(Student.test(3))



