class Bird:
	def intro(self):
		print("There are different types of birds")
	def flight(self):
		print("Most of the birds can fly but some cannot..")

class Sparrow(Bird):
	def intro(self):
		print("This is sparrow")
	def flight(self):
		print("Sparrow can fly :)")

class Ostrich(Bird):
	def intro(self):
		print("This is ostrich")
	
	def flight(self):
		print("Ostrich cannot fly :( ")
		
		
		
def func(obj):
	obj.intro()
	obj.flight()
	



'''		
b=Bird()
b.intro()
b.flight()

s=Sparrow()
s.intro()
s.flight()
'''
o=Ostrich()
func(o)

#o.intro()
#o.flight()
		

		
