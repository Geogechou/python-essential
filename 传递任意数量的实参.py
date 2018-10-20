# 使用任意数量实参(创建元祖)
def make_pizza(size,*toppings):
	"""打印顾客点的所有配料"""
	for topping in toppings:
		print(str(size)+'--'+topping)
make_pizza(10,'pepperoni')	
make_pizza(11,'pepperoni','mushroom','extra cheese')
# 使用任意数量的关键字实参(创建字典)
def build_profile(first,last,**user_info):
	"""创建一个字典"""
	profile={}
	profile['first_name']=first
	profile['last_name']=last
	for k,v in user_info.items():
		profile[k]=v
	return profile	

user_profile=build_profile("albert","einstein",location="princeton",
			field="physics")

print(user_profile)			
