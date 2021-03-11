num = int(input("Enter a number: "))

# initialize sum
prod = 1

# find the sum of the cube of each digit
temp = num
while temp != 0:
   rem = temp % 10
   prod = prod ** rem
   temp //= 10
   
   print(prod)
