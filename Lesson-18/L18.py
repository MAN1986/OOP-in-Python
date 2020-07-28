import csv,copy
from myClasses import Student,Subj,Instructor,Desig,Department
with open('studentsDetail.csv','r') as ifile:
    dataReader=csv.DictReader(ifile)
    for line in dataReader:
        # print(line)
        f,l=line['Name'].split(' ')
        s=Student(f,l,line['Reg'])
        for item in line.items():
            if(item[1]=='YES'):
                s.registerSubject(item[0])
# print(Student._allStudents)
# for i in range(10):
#     print(Student._allStudents[i]._courses)
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

# print(Department.subjStd['CP2'])
for s in Subj:
    f=f'{s.name}.csv'
    with open(f,'w',newline='') as ofile:
        dataWriter=csv.writer(ofile)
        for s in Department.subjStd[s.name]:
            dataWriter.writerow([s._reg])
Department.createGroups()
with open('ProjectGroups.csv','w',newline='') as ofile:
    dataWriter=csv.writer(ofile)
    dataWriter.writerow(['Member-1','Member-2'])
    allStds=copy.deepcopy(Student._allStudents)
    for s in allStds:
        if s._groupMember is not None:
            dataWriter.writerow([s._reg,s._groupMember._reg])
            allStds.remove(s._groupMember)
        else:
            dataWriter.writerow([s._reg])
