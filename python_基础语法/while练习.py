# 7-4 比萨配料
prompt="输入一系列的比萨配料，按'quit'结束： "
message=""
active=True
while active:
	message=input(prompt)
	if message=='quit':
		break
	else:
		print("我们会添加"+message)	
		
		
# 7-5电影票(为了方便，检测三次即可)
for i in range(3):
	age=int(input("您的年龄？"))
	if age<3:
		ticket_price=0
	elif age<12:
		ticket_price=10
	else:
		ticket_price=15		
	print("票价为"+str(ticket_price)	)
# 7-6 三个出口
while True:
	print("无限循环")
