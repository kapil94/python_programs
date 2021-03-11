import random

messages = ['It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']

print('What do you desire to ask?')
print('press 1 to continue and 0 to exit')

try:
	num=int(input())
	if num==0:
		print('Bye!! ;)')
		exit()
	elif num==1:
		print('And ball says',messages[random.randint(0,len(messages)-1)])
	else:
		print('Invalid number!! enter either 0 or 1')
		while True:
			num=int(input())
			
			if num==0:
				print('Bye!! ;)')
				break
			elif num==1:
				print('And ball says',messages[random.randint(0,len(messages)-1)])
				break
			else:
				print('Invalid number!! enter either 0 or 1')
except ValueError:
	print('Invalid input!!')	
