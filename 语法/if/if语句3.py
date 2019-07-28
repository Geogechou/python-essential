users=['admin','user1','user2','user3','user4','user5']
for user in users:
	if user == 'admin':
		print('Hello admin,would you like to see a status repot?')
	else:
		print('Hello '+user+',thank you for logging in again')	
# 清空列表
for i in range(0,len(users)):
	del users[0]
if len(users) == 0:
	print('\nWe need to find some users')

# 检测两个列表是否有元素相同出现
current_users = ['john','snow','geoge','peter','mike']
new_users = ['patter','JOHN','michale','lee','Geoge']
for new_user in new_users:
	if new_user.lower() in new_users:
		print('You need input other name')
	else:
		print('This Nickname has not been used\n')	
# 列表的解析化
numbers=[value for value in range(1,10)]
for number in numbers:
	if number == 1:
		print('1st')
	elif number == 2:
		print('2nd')	
	elif number == 3:	
		print('3rd')
	else:	
		print(str(number)+'th')
