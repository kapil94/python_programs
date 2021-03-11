tableData=[['apples','oranges','cherries','banana'],['Alice','Bob','Carol','David'],['dogs','cats','moose','goose']]

new_table=[]

def printTable(tableData,counter):
	global new_table
	for i in range(0,len(tableData)):
		new_table.append(tableData[i][counter])
		
	return new_table

counter=0

while counter<4:		
	printTable(tableData,counter)
	counter=counter+1

for i in range(0,len(new_table)):
	if i in [0,3,6,9]:
		
		print(new_table[i],end='')
	elif i in [1,4,7,10]:
		print(new_table[i].center(15),end='')
	elif i in [2,5,8,11]:
		print(new_table[i],'\n')
		
		
