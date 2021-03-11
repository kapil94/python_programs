string="This is a way to learn by coding all the way"
count=0
li=[]
li=string.split(" ")
total_ord=0
new_list=[]
for i in range(0,len(li)):
	l=len(li[i])
	if l>0:
		for j in range(0,len(li[i])):
			total_ord=total_ord+ord(li[i][j])
			l=l-1
			new_list.append({li[i]:total_ord})
	else:
		totaL_ord=0

print(new_list)
