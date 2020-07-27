from myClasses import Student,Subj,Instructor,Desig,Department
std1=Student('Anwar','Ali','MCT-UET-01') 
std2=Student('Akbar','Khan','MCT-UET-02')
std3=Student('Hamza','Akhtar','MCT-UET-03')
std4=Student('Faisal','Iqbal','MCT-UET-04')

std1.registerSubject('CP2','Mech',Subj.MOM)
std2.registerSubject('ES','Mech','MOM')
std3.registerSubject('ES','LA','MOM','Mech','CP2')
std4.registerSubject('LA','Mech','MOM')

i1=Instructor('Ali','Raza','AP')
i2=Instructor('Ahsan','Naeem',Desig.AP)
i3=Instructor('Rzi','Abbas','Lect')
i4=Instructor('Misbah','Rehman','Lect')
i5=Instructor('Shujat','Ali','TF')
i6=Instructor('Mohsin','Rizwan','AP')

i1.assignCourse('Mech')
i2.assignCourse('CP2')
i3.assignCourse(Subj.MOM)
i4.assignCourse('ES','Proj')
i5.assignCourse('LA')
i6.assignCourse('Proj')

# for ins in Instructor.allInsts:
#     print(f'{ins}\t{ins._courses}')

# for item in Department.subjInst.items():
#     print(item)

# for item in Department.subjStd.items():
#     print(item)
Department.createGroups()
for std in Student._allStudents:
    print(std,std._groupMember)
