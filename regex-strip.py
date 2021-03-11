import re

def regex_strip(text,stripped_text):
	if len(stripped_text)==0:
		textRegex=re.compile(r'\s')
		text=text.replace(textRegex.search(' ').group(),'')
		return text
	else:
		textRegex=re.compile(stripped_text)
		if textRegex.search(stripped_text)==None:
			return stripped_text+" not found in :"+text
		else:
			text=text.replace(textRegex.search(stripped_text).group(),'')
			return text


regex_strip('Geeks for Geeks','')
regex_strip('Geeks for Geeks','Geeks')

