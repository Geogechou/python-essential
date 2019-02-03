# 创建一个用于存储外星人的空列表
aliens=[]
# 创建30个绿色的外星人
for alien_number in range(30):
	new_alien={'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color']=='green':
		alien['color']='yellow'
		alien['points']=10
		alien['speed']='medium'
	elif alien['color']=='yellow':
		alien['color']='red'
		alien['speed']='fast'
		alien['points']=14	
for alien in aliens[:10]:
	print(alien)
print('.............')	

# 存储缩点披萨的信息
pizza={
	'crust':'thick',
	'toppings':['mushroom','extra cheese']
}
# 概述所点的比萨
print("You ordered a "+str(pizza['crust'])+" -crust pizza "+
		"with the folling toppings:")
for topping in pizza['toppings']:
	print("\t"+topping)

favorite_languages={
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell']
}
for name,languages in favorite_languages.items():
	print("\n"+name.title()+"'s favorite languages are: ")
	for language in languages:
		print("\t"+language.title())


