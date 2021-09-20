import StudentClass as sc

studentid = 1001
name = 'Blake'
dob = '3/26/2000'
classification = 'junior'

blake = sc.Student(studentid,name, dob,classification)

blake.calc_age

blake.register()

print('Student age is:',blake.get_age())

print('Student can register between:',blake.get_registration())