#import pyperclip

#s=pyperclip.paste()  // Taking data from clipboard

st="*"

#s='''Lists of animals
#Lists of aquarium life
#Lists of biologist by author abbreviation
#Lists of cultivars'''


li=s.split('\n') # splitting list on new line 

# loop to add * in from of list items and inserting into list with new values
for i in range(0,len(li)):
	st+=str(li[i])
	li.pop(i)
	li.insert(i,st)
	st='*'

# loop to copy data from list to clipboard
# find out how to convert list items into multiline string
#for i in range(0,len(li)):
	


#	pyperclip.copy(li[i])

