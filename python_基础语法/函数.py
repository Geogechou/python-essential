def describe_pet(pet_name,animal_type="dog",):
	"""显示宠物信息"""
	print("\nI have a "+animal_type+".")
	print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet("hamster","harry")	
# 关键字实参，顺序可以打乱
describe_pet("willie")
print("------------------------------------------\n")
# -----------------------------------------------
# 8-3 练习
def make_shirt(clothSize="big",clothWord="I love Python"):
	print("衣服的尺寸"+clothSize+" ,衣服上的字"+clothWord)
make_shirt()
make_shirt("medium","I love PHP")	
# 8-5城市
print("\n")
def describe_city(city_name,city_country):
	print(city_name+" is in "+city_country)

describe_city("Reyjavik","Iceland")
