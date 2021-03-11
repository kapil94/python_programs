import re

def regex_strip(text,stripped_text):
	if len(stripped_text)==0:
		textRegex=re.compile(r'^\s+\w+\s$')
		if textRegex.search(text):
			text=text.replace(textRegex.search(' ').group(),'')
			return text
		else:
			return text
	else:
		text_Regex=re.compile(stripped_text)
		textobj=text_Regex.search(text)
		
		if textobj==None:
			return stripped_text+" not found in :"+text
		else:
			text=text.replace(text_Regex.search(stripped_text).group(),'')
			return text


print(regex_strip('Geeks for Geeks',''))
print(regex_strip('Geeks for Geeks','Geeks'))
print(regex_strip(' Geeks for Geeks',''))
print(regex_strip('Geeks for Geeks','geehdks'))

