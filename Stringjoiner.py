def Stringjoiner(teststr1,teststr2,join_list):

	li=[]
	new_str=""
	for i in range(0,len(join_list)):
		new_str+=teststr1+join_list[i]+teststr2
		li.append(new_str)
		new_str=""
	
	return li
	

teststr1='Geeksforgeeks'
teststr2='Best'
join_list=["+", "*", "-", "$", ",", "@"]


print(Stringjoiner(teststr1,teststr2,join_list))
