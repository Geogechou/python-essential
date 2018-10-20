
# 练习8.9------------------------------
"""
向函数传递一个列表，并修改列表中的每个值
"""
print('\n')
def show_magicians(magicians):
	for value in magicians:
		print(value)
def make_great(magicians):
	#遍历列表
	for index in range(0,len(magicians)):
		magicians[index]="The great "+magicians[index]
magicians=['A','B','C']
make_great(magicians)
show_magicians(magicians)		

