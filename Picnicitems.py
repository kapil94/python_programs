picnicItems={'sandwiches':4,'apples':12,'cups':4,'cookies':8000}
def printPicnic(picnicItems):
	print('Items'.ljust(10),'values'.rjust(10))
	print()
	for item,value in picnicItems.items():
		print(item.ljust(10),str(value).rjust(10))
		print('-------------------------------')
		

printPicnic(picnicItems)
