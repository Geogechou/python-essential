print("Give me two numbers,and I'll divide them")
print("enter q to quit")
"""
try-except-else
ֻ�п��������쳣�Ĵ������Ҫ����try�����
��һЩ����try�����ɹ�ִ��ʱ����Ҫ���еĴ��룻��Щ����Ӧ����else�������
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
	
