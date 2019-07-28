# 10-6加法运算
def plus():
	try:
		num1=int(input("enter a number:"))
		num2=int(input("enter  a number again:"))
	except ValueError:
		print("请输入数字")
	else:
		print("结果是"+str(num1+num2))		
# 10-8 猫和狗
def print_cat():
	try:
		with open("text_files/cat.txt",encoding="UTF-8") as file_object:
			content=file_object.read()
	except FileNotFoundError:
		#print("文件不存在")		
		pass
	else:
		print(content)	
# 10-10常见的单词
def count_words(word):
	try:
		with open("text_files/19520.txt",encoding="UTF-8") as file_object:
			content=file_object.read()
	except FileNotFoundError:
		print("文件找不到")
	else:
		message=word+" appear "+str(content.lower().count(word))+" times"
		print(message)
count_words('fuck')
