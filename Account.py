class Account:
	
	def Login_details(self,acc_no,mPin):
		self.acc_no=acc_no
		self.mPin=mPin
		
	def __Account_details(self):
		return "account no is {} and mPin is {}".format(self.acc_no,self.mPin)
	
	

account_details=Account()
acc_no=int(input())
mPin=int(input())
account_details.Login_details(acc_no,mPin)
try:
	print(account_details.__Account_details())
except AttributeError:
	print("Pvt method is not accessed like that")
