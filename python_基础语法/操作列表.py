magicians=['alice','david','carolina']
# for循环后需要添加:(冒号)
for magician in magicians:
	print(magician.title()+" ,that was a great trick!")
	print("I can't wait to see you next trick, "+magician.title()+".\n")
print("Thank you,everyone. That was a great magic show!")

# 创建数字列表
for value in range(1,6):
	print(value)
# 使用range()和list()创建列表	
numbers=list(range(1,11,2))
print(numbers)

square=[]
for value in range(1,10):
	square.append(value**2)
print(square)	
# 对数字列表执行简单的统计计算
min(square)
max(square)
sum(square)

squares=[value**2 for value in range(1,10)]
print(squares)
