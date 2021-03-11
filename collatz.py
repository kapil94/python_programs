def collatz(num):
	
	if num%2==0:
		print(num//2)
		return num//2
	else:
		print(3*num+1)
		return 3*num+1
		

try:
	num=int(input())
	returned_value=0
	returned_value=collatz(num)
	
	while returned_value>1:
		returned_value=collatz(returned_value)
		if returned_value==1:
			break	
			
except ValueError:
	print('Expected integer value got anything else')
	

