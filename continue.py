attempt=1
flag=True
while flag:
	name=input()
	if name!='Joe':
		print('Wrong user!! Try again')
		continue
	print('Hi!! Joe pls enter your password:')
	password=input()
	if password!='swordfish':
		
		print('Wrong password, attempt no',str(attempt),'Pls enter again..')
		attempt=attempt+1
		
		if attempt>3:
			print('Password attempt exhausted!!')
			break
		
	else:	
		print('Hi Joe you are logged in')
		flag=False
