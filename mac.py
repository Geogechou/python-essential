import uuid
mac=uuid.uuid1()
mac=mac.hex
# 保存返回的数据的最后十二个十六进制数
mac=mac[-12:].upper()
# 每两个十六进制数之间插入一个 - 号
mac_temp=[]
index=0
for value in mac:
	if index==2:
		mac_temp.append('-')
		index=0
	index+=1	
	mac_temp.append(value)
		
mac_str=""
for value in mac_temp:
	mac_str+=value
# mac_str作为一个整洁的mac地址输出	
print(mac_str)
