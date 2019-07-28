print("Give me two numbers,and I'll divide them")
print("enter q to quit")
"""
try-except-else
只有可能引发异常的代码才需要放在try语句中
有一些仅在try代码块成功执行时才需要运行的代码；这些代码应放在else代码块中
"""
while True:
	first_number=input("\nFirst number: ")
	if first_number=='q':
		break
	second_number=input("second number: ")
	try:
		answer=int(first_number)/int(second_number)
			
	except ZeroDivisionError:
		print("You can't dovide by 0!")	
	else:
		print(answer)
	
