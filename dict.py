"""
def isValid(s):
	mydict={}
	mylist=[]
	count=0
	second_count=0
	third_count=0
	fourth_count=0
	flag=True
	for i in range(0,len(s)):
		count=s.count(s[i])
		mydict[s[i]]=count
	
	for key in mydict:
		mylist.append({key:mydict[key]})
	
	for i in range(0,len(mylist)-1):
		for key in mylist[i]:
			for new_key in mylist[i+1]:
				if mylist[i][key]!=mylist[i+1][new_key] and mylist[i][key]>mylist[i+1][new_key]:
					second_count=mylist[i][key]
					second_count=second_count-1
					third_count=third_count+1 
				
					if third_count==1:
						mylist[i][key]=second_count
					
						if mylist[i][key]!=mylist[i+1][new_key]:
							flag=False
					else:
						flag=False
				elif mylist[i][key]!=mylist[i+1][new_key] and mylist[i][key]<mylist[i+1][new_key]:
					second_count=mylist[i+1][new_key]
					second_count=second_count-1
					fourth_count=fourth_count+1	
				
					if fourth_count==1:
						mylist[i+1][new_key]=second_count
					
						if mylist[i][key]!=mylist[i+1][new_key]:
							flag=False
					else:
						flag=False


	return flag					
						

isValid('aabbccddeefghi')

if isValid('aabbccddeefghi'):
	print('Yes')
else:
	print('No')
"""


def isValid(s):
	mydict={}
	mylist=[]
	
	count_occ=0
	
	for i in range(0,len(s)):
		count_occ=s.count(s[i])
		mydict[s[i]]=count_occ
	
	for key in mydict:
		mylist.append({key:mydict[key]})
	
	freq=0
	freq=mylist[0][s[0]]
	count=0
	
	for i in range(1,len(mylist)):
		for key in mylist[i]:
			if freq!=mylist[i][key]:
				
				count=count+1
				
	if count>1:
		return "NO"
		
	elif count==1:
		return "YES"
		
	else:
		return "YES"	
		
print(isValid('abcdefghhgfedecba'))
print(isValid('aabbccddeefghi'))
print(isValid('aabbcd'))
print(isValid('aabcd'))

