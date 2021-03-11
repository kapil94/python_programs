import re 


################################### To check if password is strong or not ###############################

def strong_Password(password):
	passwordRegex=re.compile(r'(([A-Z]+[a-z]+)|([a-z]+[A-Z]+))+\d?(([0-9]+[!@#$%^&*()_+=-]+)|([!@#$%^&*()_+=-]+[0-9]+))')
	passobj=passwordRegex.search(password)
		
	if passobj==None:
		return 'Password is not compliant with rules !!'
	
	elif len(passobj.group())>=8 and len(passobj.group())<=10:
		return "Strong password"
		
	elif len(passobj.group())>10:
		return "Password length should be less than 10"
		
print(strong_Password('Abc123'))
print(strong_Password('Abcd1234'))
print(strong_Password('Abcd1234@'))
print(strong_Password('abcd1234@'))
print(strong_Password('abcdA1234@'))
print(strong_Password('abcdA@1234'))

