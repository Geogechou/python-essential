# 使用and来作为"&&"
# 使用or来作为"||"
# if-else后分别加分号(:)与缩进

age=19
if age>30 or age<10:
	print(True)
else:
	print(False)	
# in关键字的使用
request_toppings=['mushroom','onions','pineapple']
print('mushroom' in request_toppings )
# not in关键字的使用
banned_users=['andrew','carolina','david']
user='andrew'
if user not in banned_users:
	print(user.title()+" ,you can post a response if you wish")
else:
	print('you has been banned!')
