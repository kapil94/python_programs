def similarString(teststr1,teststr2,K):
	count1=0
	count2=0
	mydict1={}
	mydict2={}
	
	for i in range(0,len(teststr1)):
		count1=teststr1.count(teststr1[i])
		mydict1[teststr1[i]]=count1
	
	for i in range(0,len(teststr2)):
		count2=teststr2.count(teststr2[i])
		mydict2[teststr2[i]]=count2
		
	max_val1=[]
	max_val2=[]
	for key in mydict1:
		max_val1.append(mydict1[key])
	
	for key in mydict2:
		max_val2.append(mydict2[key])
		
	if K>=abs(max(max_val1)-max(max_val2)):
		return True
	else:
		return False
		

if similarString('aaaaa','aabbccd',1):
	print('Similar strings')
else:
	print('Not similar')
