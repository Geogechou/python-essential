# 9-4就餐人数
class Restaurant():
	def __init__(self,name,food_type):
		self.name=name
		self.food_type=food_type
		self.number_served=0
	def set_number_served(self,number):
			self.number_served=number
	def increment_number_served(self,value):
		if self.number_served<value:
			self.number_served+=1		
		else:
			print("This room have full")	
r1=Restaurant("north rest","Chinese type")
r1.increment_number_served(100)
print(r1.number_served)
