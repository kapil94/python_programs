Inventory={'rope':1,'torch':6,'gold coins':42,'dagger':1,'arrow':12}


dragonLoot=['gold coins','dagger','gold coins','gold coins','ruby']

def displayInventory(Inventory):
	total_items=0
	print('Inventory:')
	# display items in Inventory
	for item in Inventory.keys():
		print(Inventory[item],'',item)
		total_items+=Inventory[item]
	print('Total no of items :',total_items)
	
	
# adding to Inventory each time a loot is done
def addtoInventory(Inventory,dragonLoot):
	count=0
	loot={}
	value=0
	# counting items in loot and adding in dictionary
	for i in range(0,len(dragonLoot)):
		count=dragonLoot.count(dragonLoot[i])
		loot[dragonLoot[i]]=count
		count=0
	# check and add looted items in Inventory
	for key in loot.keys():
		if key in Inventory.keys():
			value=loot[key]
			Inventory[key]=Inventory[key]+value
			value=0
		else:
			Inventory[key]=loot[key]
		
	
	


addtoInventory(Inventory,dragonLoot)
#addtoInventory(Inventory,dragonLoot)
displayInventory(Inventory)
