import math
import os
import random
import re
import sys


def sockMerchant(n,arr):
	
	mydict={}
	count=0
	new_count=0
	
	if n>=1 and n<=100:
		
		ar.sort()
	
		for i in range(0,len(ar)):
			count=ar.count(ar[i])
			mydict[ar[i]]=count
		
		
		for key in mydict:
			while mydict[key]!=0:
				if mydict[key]==1:
					break
				elif mydict[key]%2!=0:
					mydict[key]=mydict[key]-1
				else:
					mydict[key]=mydict[key]-2
					new_count=new_count+1
			
	return new_count
	

n=int(input())
ar=list(map(int,input().rstrip().split()))

print(sockMerchant(n,ar))
