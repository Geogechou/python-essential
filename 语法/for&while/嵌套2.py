# 练习6-7
person1={
	'first':'albert',
	'last':'estention'
}
person2={
	'first':'john',
	'last':'snow'
}
person3={
	'first':'geoge',
	'last':'chow'
}
people=[person1,person2,person3]
for man in people:
	print(man)
# 练习6-8宠物
dog={
	'kind':'husky',
	'master':'kenn'
}
cat={
	'kind':'felis cats',
	'master':'john'
}
turtle={
	'kind':'chincmys reevesli',
	'master':'snow'
}
pets=[dog,cat,turtle]
for pet in pets:
	print(pet)
# 6-9 喜欢的地方
favorite_places={
	'Lee':['New York','Tokyo','HongKong'],
	'Bruise':['singapor','kyoto'],
	'Geoge':['Shanghai','peking','ulanqb']
}
for man,place in favorite_places.items():
	print(man+",favorite place is:")
	for place1 in place:
		print('\t'+place1)
# 6-10 喜欢的数字
favorite_number={
	'Lee':[1,2,3],
	'Bruise':[4,5,6],
	'Geoge':[7,8,9]
}

for per,number_list in favorite_number.items():
	print(per)
	for number1 in number_list:
		print('\t'+str(number1)) 
# 6-11 城市
cities={
	'BeiJing':{
		'population':'1300w',
		'country':'china',
		'fact':'china captical'	
	},
	'New York':{
		'population':'800w',
		'country':'USA',
		'fact':'the biggest city of USA'
	},
	'London':{
		'population':'1000w',
		'country':'British',
		'fact':'the captical of british'
	}
}
for city_name,city_info in cities.items():
	print('\n'+city_name.title()+'\n')
	for key,value in city_info.items():
		print(key.title()+': '+value.title())







	
	
	
	
	
	
	
	
	
	
	
