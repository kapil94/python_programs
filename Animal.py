class Animal:
	def __init__(self,animal_type):
		self.animal_type=animal_type
		
	def type_of_animal(self):
		return self.animal_type
	
		


class Vertibrates(Animal):
	
	def __init__(self,animal,type_of_animal):
		self.animal=animal
		self.type_of_animal=type_of_animal
		
		Animal.__init__(self,"Vertibrate")
		
		
	def isVertibrate(self):
		
		return self.animal,"have a backbone and are",self.type_of_animal
		
		
		
class Invertibrate(Animal):
	def __init__(self,animal,type_of_animal):
	
		self.animal=animal
		self.type_of_animal=type_of_animal
		Animal.__init__(self,"Invertibrates")
		
	def isInvertibrate(self):
		return self.animal," doesn\'t have a backbone and are",self.type_of_animal
		
		



Vertibrates_list=["Fishes","Amphibians","Mammals","Reptiles","Birds"]

Invertibrates_list=["protozoans","annelids","echinoderms","mollusks","arthropods"]


animal=input("Enter animal type:")


if animal in Vertibrates_list:
	a=Animal("Vertibrate")
	
	b=Vertibrates(animal,a.type_of_animal())
	for element in b.isVertibrate():
		print(element,end=" ")	 
		
		
	print()
	
elif animal in Invertibrates_list:
	a=Animal("Invertibrate")
	
	b= Invertibrate(animal,a.type_of_animal())
	for element in b.isInvertibrate():
		print(element,end=" ")
	print()
	
else:
	print("Invalid input!!")



