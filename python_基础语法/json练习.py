import json

def like_number():
	filename="like_number.json"
	try:
		with open(filename) as f_obj:
			fav_num=json.load(f_obj)
	except FileNotFoundError:
		create_number()	
	else:
		print("you favorite number is "+fav_num)
		
def create_number():
	filename="like_number.json"
	with open(filename,'w') as f_obj:
		fav_num=input("which number is your favorite num?")
		# dump()函数传递文件对象，不能直接传递文件名
		json.dump(str(fav_num),f_obj)
like_number()
