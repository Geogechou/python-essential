# python将不能修改的值称为不可变的，而不可变的列表称为元祖
dimensions=(200,50)
for dimension in dimensions:
	print(dimension)
# 元组如果需要修改，直接重新赋值即可
dimensions=(400,100)
for dimension in dimensions:
	print(dimension)
# ********************
# 4-13练习
foods=('rice','noddle','instant noddle','chicken','fish')
for food in foods:
	print(food)
print('重新修改元组')	
foods=('rices','noddles')
for food in foods:
	print(food)
