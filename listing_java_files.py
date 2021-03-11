import os # Module for file operation in python
import re # Module for regular expression in python


try:

	path='/home/kapil/Desktop/new'
	
	javafiles=re.compile(r'\w+\.+java$')
	
	for i in range(0,len(os.listdir(path))):	# os.listdir(path) - here list of files on a path is returned
		if javafiles.search(os.listdir(path)[i]): # from list of files returned it is checked if they are java files
			print(os.listdir(path)[i])
			
except FileNotFoundError:
	print('File doesn\'t exist!!')
