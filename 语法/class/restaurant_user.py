class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.name=restaurant_name
		self.type=cuisine_type
	def describe_restaurant(self):
		print("restaurant name: "+self.name)
		print("cuisine type: "+self.type+"\n")	
	def open_restaurant(self):
		print("this restaurant is opening")
			
# -------------------------------------------------------
class User():
	def __init__(self,f_n,l_n):
		self.first_name=f_n
		self.last_name=l_n
		self.login_attempts=0
	def describe_user(self):
		print("Name: "+self.first_name.title()+" "+self.last_name.title())	
	def greet_user(self):
		print("Hello "+self.first_name+" "+self.last_name+".")
	def increment_login_attempts(self):
	    self.login_attempts+=1
	def reset_login_attempts(self):
		self.login_attempts=0    
		


class IceCreamStand(Restaurant):
	"""冰激淋店铺，继承自restaurant类"""
	def __init__(self,name,kind):
		super().__init__(name,kind)
		self.flavors=["sweat","cold","hot","spicy"]
	def show_IceCream(self):
		print("all flavor are follwing:\n")
		print(self.flavors)

#---------------------------------------------------------

			
