# 读取文件，with关键字，在程序处理完文件，py在合适的时候会关闭文件
import os
filename="text_files/movie.txt"

with open(filename) as file_object:
	# radlines()函数，将文件逐行读入到列表中
	movies=file_object.readlines()
total=0
temp_number=0
number_list=['1','2','3','4','5','6','7','8']
for movie in movies:
	for value in number_list:
		if value in movie:
			temp_number+=1
	if temp_number>1:
		total+=temp_number
		temp_number=0
	else:
		total+=1
	
print("total movie "+str(total))		
os.system("pause")
