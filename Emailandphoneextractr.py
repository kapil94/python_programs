####################  Email address and phone number extractor##############################################

import re
import pyperclip            # module for copying and pasting from clipboard
import mysql.connector as mysql



# Step 1: Copy text from clipboard
# Step 2: paste text by pyperclip 
# Using regex on pasted data to extract phone number and email address



##################################### Extracting phone Number ##############################################################

phonenumberRegex=re.compile(r'(\d{3})+(\-|\.)+(\d{3})+(\-|\.)+(\d{4})')


str1=pyperclip.paste()

phoneobj=phonenumberRegex.findall(str1)
phonenumber_list=[]
str2=""

# to get data from phoneobj and append it in phonenumber list
for obj in range(0,len(phoneobj)):
	for obj_name in range(0,len(phoneobj[obj])):
		str2+=phoneobj[obj][obj_name]
	phonenumber_list.append(str2)
	str2=""		


##################################### Extracting email address #############################################################

email_list=[]
emailRegex=re.compile(r'\w+\d?\@+\w+\.+[com]{3}')
emailobj=emailRegex.findall(str1)
email_list.append(emailobj)




# Instead of printing on console we can also paste phone list and email list in clipboard

print('Copied to clipboard:')
for i in range(0,len(phonenumber_list)):
	print(phonenumber_list[i])
for i in range(0,len(email_list)):
	for j in range(0,len(email_list[i])):
		print(email_list[i][j])


print(phonenumber_list)

'''
if len(phonenumber_list)>0:
	mydb=mysql.connect(
		host="127.0.0.1",
		username="root",
		password="root",
		database="mydb"
		)
	
	mycursor=mydb.cursor()
	
	mycursor.execute("CREATE TABLE IF NOT EXISTS phonenumber(s_no INT AUTO_INCREMENT,Phonenumber varchar(50),PRIMARY KEY(s_no))")
	
	sql="insert into phonenumber(Phonenumber) VALUES %s"
	
	
	t1=[]
	for i in range(0,len(phonenumber_list)):
		t1.append((phonenumber_list[i]))
		mycursor.execute(sql,tuple(t1))
		t1=[]
	
	
	mydb.commit()
'''	
	





