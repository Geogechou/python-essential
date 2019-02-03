prompt="\nplease enter the name of a city you have visited: "
prompt+="\n(enter 'quit' when you are finished)  "
# while True:
	# city=input(prompt)
	# if city=="quit":
		# break
	# else:
		# print("I'd love to go to "+city)	

current_number=0
while current_number<10:
	current_number+=1
	if current_number%2==0:
		continue
	else:
		print(current_number)	

x=1
while 1:
	print(1)
# 如果程序陷入无限循环，可按crtl+C，也可以关闭显示程序输出的终端窗口
