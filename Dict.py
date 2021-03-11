birthdays=[]
details={}

for i in range(0,2):
	name=input('Enter name:')
	dob=input('Enter date of birth:')
	
	if name=='' or dob=='':
		print('Either name or dob is empty')
		break
	else:	
		details={'Name':name,'D.o.b':dob}
	
		birthdays.insert(i,details)
	
if len(birthdays)!=0:
	print(birthdays)
