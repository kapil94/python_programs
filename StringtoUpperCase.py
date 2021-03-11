def StringtoUppercase(testlist,K):
	text=""
	for i in range(0,len(testlist)):
					
		if len(testlist[i])>K:
			text+=testlist[i]
			testlist.pop(i)
			testlist.insert(i,text.upper())
			text=""
				
	
	return testlist
	
testlist=["gfg","is","best","for","geeks"]
K=3
print(StringtoUppercase(testlist,K))
