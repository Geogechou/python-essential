file_name="text_files\learning_python.txt"
"""
用三种方法来打印文件
"""
# 打印整个文件
with open(file_name) as file_object:
	print(file_object.read())
# 遍历整个文件对象	
with open(file_name) as file_object:
	for line in file_object:
		print(line)
# 存储在列表中		
with open(file_name) as file_object:
	lines=file_object.readlines()
for line in lines:
	print(line)			

# ----------------------------------
"""
将文件中的python改为C
"""
with open(file_name) as file_object:
	lines=file_object.readlines()
for i in range(len(lines)):
	lines[i]=lines[i].replace("python","c")
for line in lines:
	print(line)
	
