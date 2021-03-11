import random
myBoard={'top-L':'','top-M':'','top-R':'','mid-L':'','mid-M':'','mid-R':'','low-L':'','low-M':'','low-R':''}


def printBoard(myBoard):
	print(myBoard['top-L']+'   |  '+myBoard['top-M']+'  |  '+myBoard['top-R'])
	print('---+----+---')
	print(myBoard['mid-L']+'   |  '+myBoard['mid-M']+'  |  '+myBoard['mid-R'])
	print('---+----+---')
	print(myBoard['low-L']+'   |  '+myBoard['low-M']+'  |  '+myBoard['low-R'])
	print('---+----+---')
	


printBoard(myBoard)			
			
	
for i in range(0,9):
	if turn==1 or turn%2!=0:
		pos=input('enter pos ')
		if myBoard[pos]=='':
			myBoard[pos]='0'
			if turn>=5:
				if myBoard['top-L']=='0' and myBoard['top-M']=='0' and myBoard['top-R']=='0' or myBoard['top-L']=='0' and myBoard['low-L']=='0' and myBoard['mid-L']=='0' or myBoard['top-L']=='0' and myBoard['mid-M']=='0' and myBoard['low-R']=='0' or myBoard['mid-L']=='0' and myBoard['mid-M']=='0' and myBoard['mid-R']=='0' or myBoard['low-L']=='0' and myBoard['low-M']=='0' and myBoard['low-R']=='0' or myBoard['top-R']=='0' and myBoard['mid-M']=='0' and myBoard['low-L']=='0':
					print('Player 1 wins..')
					break
			turn+=1
	elif turn%2==0:
		pos=input('enter pos ')
		if myBoard[pos]=='':
			myBoard[pos]='X'
			if turn>=6:
				if myBoard['top-L']=='X' and myBoard['top-M']=='X' and myBoard['top-R']=='X'or myBoard['top-L']=='X' and myBoard['low-L']=='X' and myBoard['mid-L']=='X' or myBoard['top-L']=='X' and myBoard['mid-M']=='X' and myBoard['low-R']=='X' or myBoard['mid-L']=='X' and myBoard['mid-M']=='X' and myBoard['mid-R']=='X' or myBoard['low-L']=='X' and myBoard['low-M']=='X' and myBoard['low-R']=='X' or myBoard['top-R']=='X' and myBoard['mid-M']=='X' and myBoard['low-L']=='X':
					print('Player 2 wins')
					break
			turn+=1
	elif turn>8:
		print('Game Draw!')
		exit()
