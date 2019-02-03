alien_0={'speed':'fast','x_position':0,'y_position':25}
print("初始键值对 "+str(alien_0))
# 修改键值对
alien_0['x_position']=3+alien_0['x_position']
print("修改键值对 "+str(alien_0))
# 删除键值对
del alien_0['speed']
print("删除键值对 "+str(alien_0))
# 增添键值对
alien_0['color']='blue'
print("增添键值对 "+str(alien_0))

favorite_languages={
	'jen':'python',
	'sarach':'c',
	'edward':'ruby',
	'phil':'python'
}
print(favorite_languages)
