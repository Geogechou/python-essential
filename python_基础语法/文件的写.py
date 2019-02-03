filename="programing.txt"
"""
附加模式，不会重写整个文件，会在文件后加上新写的内容
"""
with open(filename,'a') as file_object:
	file_object.write("I also love finding meaning in large datasets\n")
	file_object.write("I love creating apps that can run in a browser.\n")
