# 列表，使用切片
companies=['Apple','Samsung','Huawei','oppo','xiaomi','vivo','Sony','Ericsson','OnePlus']
print('The first three items in the list are:')
#切下来的元素分别是下标0,1,2
for company in companies[0:3]:
	print(company)
print('The items form the middle of the list are:')
for company in companies[3:6]:
	print(company)
print('The last three items in the list are:')
# 分割的元素分别是下标6到末尾
for company in companies[6:]:
	print(company)	
my_pizzas=['a','b','c','d']	
#执行拷贝，如果直接使用friends_pizzas=my_pizzas类似‘引用’的效果
friends_pizzas=my_pizzas[:]
my_pizzas.append("my_pizza")
friends_pizzas.append("friend_pizza")
for my_pizza in my_pizzas:
	print(my_pizza)
for friend_pizza in friends_pizzas:
	print(friend_pizza)	


