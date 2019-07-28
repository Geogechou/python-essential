
def count_words(filename):
	"""计算一个文件大致包含多少个单词"""
	try:
		with open(filename,encoding="UTF_8") as file_object:
			content=file_object.read()
	except FileNotFoundError:
		#msg="sorry, the file "+filename+" does not exist."
		#print(msg)
		pass
	else:
		# 计算有多少个单词
		# 把字符串分成列表
		words=content.split()
		num_words=len(words)
		print("The file "+filename+" has about "+str(num_words)+" words.")
filenames=["text_files/19520.txt","text_files/pride and prijudice.txt",
			"text_files/movie.txt","aaaa.txt"]
for v in filenames:
	count_words(v)			
