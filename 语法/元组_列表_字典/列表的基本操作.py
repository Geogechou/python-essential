# python中的列表，支持负数访问(当然也支持常规访问)，-1是最后一个元素，-2是倒数第二个元素
name=['John','James','Lee','David']
print(name[0]+" ,how are you today?")
print(name[-1]+" ,how are you?")

vehicle=['ofo','mobike','hello bike','foot']
print(vehicle)
# 列表中的元素的修改
vehicle[0]='Tiny Yellow Bike'
print(vehicle)
# 在列表尾部插入元素
vehicle.append('ducati')
print(vehicle)
# 在列表中插入元素，insert()接受两个参数，1.插入的位置 2.插入的元素
vehicle.insert(0,'suzuki')
print(vehicle)
# 使用del来删除元素，提供元素在列表中的位置
del vehicle[0]
print(vehicle)
# 使用pop()来删除元素，同时返回元素
# 可以使用pop()来删除列表中任何位置的元素，只需要在括号中指定哟啊删除的元素的索引即可
popped_vehicle=vehicle.pop()
print(vehicle)
print("pop的元素为 "+popped_vehicle)
first_own=vehicle.pop(0)
print(vehicle)
print(first_own)
# 使用romeve()来删除
too_slow='foot'
vehicle.remove(too_slow)
print(vehicle)
print(too_slow+" is to slow for me")









