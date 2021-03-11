def comma_code(li):
	st=""
	for i in range(0,len(li)):
		if i==len(li)-1:
			st=st+li[i-1]+" and "+li[i]
		elif i<len(li)-2:	
			st=st+li[i]+", "
		
		
	return st
	
	
li=['Apples','Banana','Tofu','Cats','Dogs','Cows']
print(comma_code(li))
