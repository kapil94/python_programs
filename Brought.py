allGuests={'Alice': {'apples': 5, 'pretzels': 12}, 'Bob': {'ham sandwiches': 3, 'apples': 2}, 'Carol': {'cups': 3, 'apple pies': 1}}

	
	
def totalBrought(allGuests,item):
	total_item=0
	for guest in allGuests.keys():
		if item in allGuests[guest].keys():
			total_item+=allGuests[guest][item]
			
	return total_item
	

print('Total no of apples brought by guests is :',str(totalBrought(allGuests,'apples')))
print('Total no of pretzels brought by guests is :',str(totalBrought(allGuests,'pretzels')))
print('Total no of ham sandwiches brought by guests is :',str(totalBrought(allGuests,'ham sandwiches')))
print('Total no of cups brought by guests is :',str(totalBrought(allGuests,'cups')))
print('Total no of apple pies brought by guests is :',str(totalBrought(allGuests,'apple pies')))	
