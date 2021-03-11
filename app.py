arr=[2,4,5,6,0,1,4,2]
counter=0
subarr=[]
for i in range(0,len(arr)-1):
    if arr[i]<arr[i+1]:
        counter=counter+1
    elif arr[i]>arr[i+1] and counter>=0:
    	counter=counter-1
        subarr.append(arr[counter])
        
        
print(subarr)
