"""
利用pygal绘制Bar直方图
"""
import pygal
from random import randint
class Die():
	def __init__(self,sides=6):
		self.sides=sides
	def roll(self):
		return randint(1,self.sides)
die1=Die(6)
die2=Die(6)
result=[]
for i in range(1000):
	result.append(die1.roll())
frequencies=[]	
for i in range(1,die1.sides+1):
		frequencies.append(result.count(i))
		
print(frequencies)

hist=pygal.Bar(width=600)
hist.title='The times of twice throw die'
hist.x_labels=map(str,range(1,7))
hist.add('Times',frequencies)
hist.render_to_file("dice_visual.svg")
#hist.render_to_png('dice_visual.png')
#生成图在浏览器中预览
hist.render_in_browser()
